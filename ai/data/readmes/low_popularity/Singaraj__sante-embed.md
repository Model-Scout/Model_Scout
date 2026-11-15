---
license: apache-2.0
language:
- en
- zh
- ar
- es
- fr
- ko
- pl
- ru
- vi
base_model:
- Alibaba-NLP/gte-Qwen2-1.5B-instruct
pipeline_tag: feature-extraction
library_name: sentence-transformers
tags:
- sentence-transformers
- feature-extraction
- medical
---

# sante-embed

- Model Type: Text Embedding
- Number of Parameters: 1.5B
- Embedding Dimension: 1536
- Max Input Tokens: 512
- Adapted from: [Alibaba-NLP/gte-Qwen2-1.5B-instruct](https://huggingface.co/Alibaba-NLP/gte-Qwen2-1.5B-instruct)
- Pooling: Last token
- Similarity: Cosine

A text embedding model for medical retrieval in nine languages. Embeddings are L2
normalised. Queries take an instruction prefix, documents do not. Input longer than 512
tokens is truncated.

## Usage

### Sentence Transformers

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("Singaraj/sante-embed", trust_remote_code=True)

queries = [
    "what are the first signs of diabetic retinopathy",
    "is metformin safe during pregnancy",
]
documents = [
    "Early diabetic retinopathy is often asymptomatic. The first detectable changes on fundus examination are microaneurysms, dot and blot haemorrhages, and hard exudates. Patients may later report blurred vision, floaters, or difficulty with night vision as macular oedema develops.",
    "Metformin crosses the placenta but has not been associated with an increased risk of congenital malformations. It is used in gestational diabetes and in women with type 2 diabetes who conceive, though insulin remains the preferred agent in many guidelines.",
]

query_embeddings = model.encode(queries, prompt_name="query")
document_embeddings = model.encode(documents)

scores = (query_embeddings @ document_embeddings.T) * 100
print(scores.tolist())
# [[63.21099853515625, 8.87006950378418], [20.293703079223633, 53.954315185546875]]
```

### Transformers

```python
import torch
import torch.nn.functional as F
from torch import Tensor
from transformers import AutoTokenizer, AutoModel


def last_token_pool(last_hidden_states: Tensor, attention_mask: Tensor) -> Tensor:
    left_padding = (attention_mask[:, -1].sum() == attention_mask.shape[0])
    if left_padding:
        return last_hidden_states[:, -1]
    sequence_lengths = attention_mask.sum(dim=1) - 1
    batch_size = last_hidden_states.shape[0]
    return last_hidden_states[torch.arange(batch_size, device=last_hidden_states.device), sequence_lengths]


def get_detailed_instruct(task_description: str, query: str) -> str:
    return f"Instruct: {task_description}\nQuery: {query}"


task = "Given a web search query, retrieve relevant passages that answer the query"
queries = [
    get_detailed_instruct(task, "what are the first signs of diabetic retinopathy"),
    get_detailed_instruct(task, "is metformin safe during pregnancy"),
]
documents = [
    "Early diabetic retinopathy is often asymptomatic. The first detectable changes on fundus examination are microaneurysms, dot and blot haemorrhages, and hard exudates. Patients may later report blurred vision, floaters, or difficulty with night vision as macular oedema develops.",
    "Metformin crosses the placenta but has not been associated with an increased risk of congenital malformations. It is used in gestational diabetes and in women with type 2 diabetes who conceive, though insulin remains the preferred agent in many guidelines.",
]
input_texts = queries + documents

model_id = "Singaraj/sante-embed"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModel.from_pretrained(model_id, trust_remote_code=True)

batch_dict = tokenizer(input_texts, max_length=512, padding=True, truncation=True, return_tensors="pt")
outputs = model(**batch_dict)
embeddings = last_token_pool(outputs.last_hidden_state, batch_dict["attention_mask"])
embeddings = F.normalize(embeddings, p=2, dim=1)

scores = (embeddings[:2] @ embeddings[2:].T) * 100
print(scores.tolist())
# [[63.211082458496094, 8.870075225830078], [20.29365348815918, 53.95436096191406]]
```

## Prompts

Queries take an instruction in the following format:

```text
Instruct: {task_description}
Query: {query}
```

The default query prompt is stored in `config_sentence_transformers.json` and is applied by
`prompt_name="query"`. Pass `model.encode(queries, prompt="Instruct: ...\nQuery: ")` to use
a different one. Documents are encoded without a prompt.

## Training data

- [codefuse-ai/F2LLM-v2](https://huggingface.co/datasets/codefuse-ai/F2LLM-v2), medical and multilingual retrieval subsets
- [clips/mqa](https://huggingface.co/datasets/clips/mqa), FAQ pairs in Arabic, Chinese, French, Korean, Polish, Russian, Spanish and Vietnamese
- [mteb/nfcorpus](https://huggingface.co/datasets/mteb/nfcorpus), train split
- [mteb/scifact](https://huggingface.co/datasets/mteb/scifact), train split

## Intended use

Retrieval, semantic search and clustering over medical text. This is a retrieval model,
not a clinical decision support tool, and its output should not be used to guide patient
care.

## Citation

```
@misc{b2026santeembed,
  title={sante-embed: a multilingual text embedding model for medical retrieval},
  author={B, Singaraj},
  year={2026},
  url={https://huggingface.co/Singaraj/sante-embed},
}
```

The base model:

```
@article{li2023towards,
  title={Towards general text embeddings with multi-stage contrastive learning},
  author={Li, Zehan and Zhang, Xin and Zhang, Yanzhao and Long, Dingkun and Xie, Pengjun and Zhang, Meishan},
  journal={arXiv preprint arXiv:2308.03281},
  year={2023}
}
```
