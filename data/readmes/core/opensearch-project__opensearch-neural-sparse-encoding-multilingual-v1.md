---
language:
- en
- zh
- fr
- bn
- te
- es
- id
- hi
- ru
- ar
- fa
- ja
- fi
- sw
- ko
license: apache-2.0
tags:
- learned sparse
- opensearch
- transformers
- retrieval
- passage-retrieval
- document-expansion
- bag-of-words
- sentence-transformers
- sparse-encoder
- sparse
- asymmetric
- inference-free
- splade
pipeline_tag: feature-extraction
library_name: sentence-transformers
datasets:
- miracl/miracl
---

# opensearch-neural-sparse-encoding-multilingual-v1

## Select the model
The model should be selected considering search relevance, model inference and retrieval efficiency(FLOPS). We benchmark models' performance on **MIRACL** benchmark (we exclude th since the uncased backbone can not encode it).
**We recommend to use it with max_ratio pruning.**

| Model | Inference-free for Retrieval | Model Parameters | AVG NDCG@10 | AVG FLOPS | AVG EMB SIZE |
|-------|------------------------------|------------------|-------------|-----------| -----------|
| [opensearch-neural-sparse-encoding-multilingual-v1](https://huggingface.co/opensearch-project/opensearch-neural-sparse-encoding-multilingual-v1) | ✔️ | 160M | 0.629 | 1.3 | 138 |
| [opensearch-neural-sparse-encoding-multilingual-v1](https://huggingface.co/opensearch-project/opensearch-neural-sparse-encoding-multilingual-v1); prune_ratio 0.1 | ✔️ | 160M | 0.626 | 0.8 | 75 |

## Overview

- **Paper**: [Towards Competitive Search Relevance For Inference-Free Learned Sparse Retrievers](https://arxiv.org/abs/2411.04403)
- **Fine-tuning sample**: [opensearch-sparse-model-tuning-sample](https://github.com/zhichao-aws/opensearch-sparse-model-tuning-sample)

This is a learned sparse retrieval model. It encodes the documents to 105879 dimensional **sparse vectors**. For queries, it just use a tokenizer and a weight look-up table to generate sparse vectors. The non-zero dimension index means the corresponding token in the vocabulary, and the weight means the importance of the token. And the similarity score is the inner product of query/document sparse vectors.

OpenSearch neural sparse feature supports learned sparse retrieval with lucene inverted index. Link: https://opensearch.org/docs/latest/query-dsl/specialized/neural-sparse/. The indexing and search can be performed with OpenSearch high-level API.

## Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.

```python
from sentence_transformers.sparse_encoder import SparseEncoder

# Download from the 🤗 Hub
model = SparseEncoder("opensearch-project/opensearch-neural-sparse-encoding-multilingual-v1")

query = "What's the weather in ny now?"
document = "Currently New York is rainy."

query_embed = model.encode_query(query)
document_embed = model.encode_document(document)

sim = model.similarity(query_embed, document_embed)
print(f"Similarity: {sim}")
# Similarity: tensor([[7.7400]])

decoded_query = model.decode(query_embed)
decoded_document = model.decode(document_embed)

for i in range(len(decoded_query)):
    query_token, query_score = decoded_query[i]
    doc_score = next((score for token, score in decoded_document if token == query_token), 0)
    if doc_score != 0:
        print(f"Token: {query_token}, Query score: {query_score:.4f}, Document score: {doc_score:.4f}")

# Token: weather, Query score: 3.0699, Document score: 1.2821
# Token: now, Query score: 1.6406, Document score: 0.9018
# Token: ?, Query score: 1.6108, Document score: 0.3141
# Token: ny, Query score: 1.2721, Document score: 1.3446
# Token: in, Query score: 0.6005, Document score: 0.1804
```

## Usage (HuggingFace)
This model is supposed to run inside OpenSearch cluster. But you can also use it outside the cluster, with HuggingFace models API. 

```python
import json
import itertools
import torch

from transformers import AutoModelForMaskedLM, AutoTokenizer


# get sparse vector from dense vectors with shape batch_size * seq_len * vocab_size
def get_sparse_vector(feature, output, prune_ratio=0.1):
    values, _ = torch.max(output*feature["attention_mask"].unsqueeze(-1), dim=1)
    values = torch.log(1 + torch.relu(values))
    values[:,special_token_ids] = 0
    max_values = values.max(dim=-1)[0].unsqueeze(1) * prune_ratio
    return values * (values > max_values)
    
# transform the sparse vector to a dict of (token, weight)
def transform_sparse_vector_to_dict(sparse_vector):
    sample_indices,token_indices=torch.nonzero(sparse_vector,as_tuple=True)
    non_zero_values = sparse_vector[(sample_indices,token_indices)].tolist()
    number_of_tokens_for_each_sample = torch.bincount(sample_indices).cpu().tolist()
    tokens = [transform_sparse_vector_to_dict.id_to_token[_id] for _id in token_indices.tolist()]

    output = []
    end_idxs = list(itertools.accumulate([0]+number_of_tokens_for_each_sample))
    for i in range(len(end_idxs)-1):
        token_strings = tokens[end_idxs[i]:end_idxs[i+1]]
        weights = non_zero_values[end_idxs[i]:end_idxs[i+1]]
        output.append(dict(zip(token_strings, weights)))
    return output
    
# download the idf file from model hub. idf is used to give weights for query tokens
def get_tokenizer_idf(tokenizer):
    from huggingface_hub import hf_hub_download
    local_cached_path = hf_hub_download(repo_id="opensearch-project/opensearch-neural-sparse-encoding-multilingual-v1", filename="idf.json")
    with open(local_cached_path) as f:
        idf = json.load(f)
    idf_vector = [0]*tokenizer.vocab_size
    for token,weight in idf.items():
        _id = tokenizer._convert_token_to_id_with_added_voc(token)
        idf_vector[_id]=weight
    return torch.tensor(idf_vector)

# load the model
model = AutoModelForMaskedLM.from_pretrained("opensearch-project/opensearch-neural-sparse-encoding-multilingual-v1")
tokenizer = AutoTokenizer.from_pretrained("opensearch-project/opensearch-neural-sparse-encoding-multilingual-v1")
idf = get_tokenizer_idf(tokenizer)

# set the special tokens and id_to_token transform for post-process
special_token_ids = [tokenizer.vocab[token] for token in tokenizer.special_tokens_map.values()]
get_sparse_vector.special_token_ids = special_token_ids
id_to_token = ["" for i in range(tokenizer.vocab_size)]
for token, _id in tokenizer.vocab.items():
    id_to_token[_id] = token
transform_sparse_vector_to_dict.id_to_token = id_to_token



query = "What's the weather in ny now?"
document = "Currently New York is rainy."

# encode the query
feature_query = tokenizer([query], padding=True, truncation=True, return_tensors='pt', return_token_type_ids=False)
input_ids = feature_query["input_ids"]
batch_size = input_ids.shape[0]
query_vector = torch.zeros(batch_size, tokenizer.vocab_size)
query_vector[torch.arange(batch_size).unsqueeze(-1), input_ids] = 1
query_sparse_vector = query_vector*idf

# encode the document
feature_document = tokenizer([document], padding=True, truncation=True, return_tensors='pt', return_token_type_ids=False)
output = model(**feature_document)[0]
document_sparse_vector = get_sparse_vector(feature_document, output)


# get similarity score
sim_score = torch.matmul(query_sparse_vector[0],document_sparse_vector[0])
print(sim_score)   # tensor(7.6317, grad_fn=<DotBackward0>)


query_token_weight = transform_sparse_vector_to_dict(query_sparse_vector)[0]
document_query_token_weight = transform_sparse_vector_to_dict(document_sparse_vector)[0]
for token in sorted(query_token_weight, key=lambda x:query_token_weight[x], reverse=True):
    if token in document_query_token_weight:
        print("score in query: %.4f, score in document: %.4f, token: %s"%(query_token_weight[token],document_query_token_weight[token],token))
        

        
# result:
# score in query: 3.0699, score in document: 1.2821, token: weather
# score in query: 1.6406, score in document: 0.9018, token: now
# score in query: 1.6108, score in document: 0.3141, token: ?
# score in query: 1.2721, score in document: 1.3446, token: ny
```

The above code sample shows an example of neural sparse search. Although there is no overlap token in original query and document, but this model performs a good match. 

## Detailed Search Relevance

<div style="overflow-x: auto;">
    
| Model | Average | bn | te | es | fr | id | hi | ru | ar | zh | fa | ja | fi | sw | ko | en |
|-------|---------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| BM25 | 0.305 | 0.482 | 0.383 | 0.077 | 0.115 | 0.297 | 0.350 | 0.256 | 0.395 | 0.175 | 0.287 | 0.312 | 0.458 | 0.351 | 0.371 | 0.267 |
| [opensearch-neural-sparse-encoding-multilingual-v1](https://huggingface.co/opensearch-project/opensearch-neural-sparse-encoding-multilingual-v1) | 0.629 | 0.670 | 0.740 | 0.542 | 0.558 | 0.582 | 0.486 | 0.658 | 0.740 | 0.562 | 0.514 | 0.669 | 0.767 | 0.768 | 0.607 | 0.575 |
| [opensearch-neural-sparse-encoding-multilingual-v1](https://huggingface.co/opensearch-project/opensearch-neural-sparse-encoding-multilingual-v1); prune_ratio 0.1 | 0.626 | 0.667 | 0.740 | 0.537 | 0.555 | 0.576 | 0.481 | 0.655 | 0.737 | 0.558 | 0.511 | 0.664 | 0.761 | 0.766 | 0.604 | 0.572 |

</div>

## License

This project is licensed under the [Apache v2.0 License](https://github.com/opensearch-project/neural-search/blob/main/LICENSE).

## Copyright

Copyright OpenSearch Contributors. See [NOTICE](https://github.com/opensearch-project/neural-search/blob/main/NOTICE) for details.