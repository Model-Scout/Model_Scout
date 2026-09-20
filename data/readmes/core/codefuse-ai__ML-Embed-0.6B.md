---
license: apache-2.0
language:
- en
- zh
- ru
- es
- fr
- de
- ar
- nl
- vi
- hi
- ko
- ja
- it
- id
- pt
- pl
- tr
- da
- th
- sv
- fa
- uk
- cs
- 'no'
- el
- ca
- ro
- fi
- bg
- tl
- gl
- my
- hy
- km
- ne
- hu
- eu
- he
- lo
- sw
- az
- lv
- si
- sk
- tg
- et
- lt
- ms
- hr
- is
- sl
- sr
- ur
- bn
- af
- ta
- ka
- te
- ml
- mn
- nn
- kk
- cy
- mr
- sq
- nb
- mk
- jv
- kn
- eo
- la
- gu
- uz
- am
- oc
- be
- mg
- vo
- pa
- lb
- ht
- br
- ga
- xh
- tt
- bs
- yo
base_model:
- codefuse-ai/F2LLM-v2-0.6B-Preview
pipeline_tag: feature-extraction
library_name: transformers
tags:
- sentence-transformers
datasets:
- codefuse-ai/F2LLM-v2
---

# ML-Embed-0.6B

**ML-Embed-0.6B** is a multilingual text embedding model developed by CodeFuse AI and trained from Qwen3-0.6B. It is part of the ML-Embed family introduced in the ICML 2026 paper [**ML-Embed: Inclusive and Efficient Embeddings for a Multilingual World**](https://arxiv.org/abs/2605.15081).

This model is designed to be:

- strong multilingual embedding model
- fully compatible with standard Qwen3 loading/inference
- efficient to deploy, thanks to:
  - **Matryoshka Layer Learning (MLL)** for layer truncation
  - **Matryoshka Embedding Learning (MEL)** for factorized embedding deployment
  - **Matryoshka Representation Learning (MRL)** for flexible embedding dimension truncation

The default released checkpoint is in **compatibility mode**, meaning it behaves like a standard Transformer embedding model and can be used directly with `sentence-transformers` or `transformers`.


## Model Highlights

- Base architecture: Qwen3-0.6B
- Embedding dimension: 1024
- Sequence embedding: EOS token representation
- Attention type: causal attention
- Trained in two stages (first-stage checkpiont: [codefuse-ai/F2LLM-v2-0.6B-Preview](https://huggingface.co/codefuse-ai/F2LLM-v2-0.6B-Preview))
- Supports multilingual retrieval and semantic similarity
- Supports efficient deployment with:
  - fewer transformer layers
  - factorized embedding matrices (`U.pth`, `V.pth`)


## Quick Start

### With Sentence Transformers

To encode text with the [Sentence Transformers](https://www.sbert.net/) library:

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "codefuse-ai/ML-Embed-0.6B",
    device="cuda:0",
    model_kwargs={"torch_dtype": "bfloat16"}
)

# Some sample query and documents
query = "What is ML-Embed used for?"
documents = [
    "ML-Embed is a family of multilingual embedding models for retrieval, semantic search, and other NLP tasks.",
    "ML-Embed is trained to produce text embeddings that work well across many languages.",
    "ML-Embed 是 CodeFuse AI 开源的多语言嵌入模型。",
    "ML-Embed — это многоязычная модель эмбеддингов для поиска и семантического сопоставления."
]

# Encode the query and documents separately. The encode_query method uses the query prompt
query_embedding = model.encode_query(query)
document_embeddings = model.encode_document(documents)

print(query_embedding.shape, document_embeddings.shape)
# (1024,) (4, 1024)

# Compute cosine similarity between the query and documents
similarity = model.similarity(query_embedding, document_embeddings)
print(similarity)
```

### With Transformers

Or directly with the [Transformers](https://huggingface.co/docs/transformers/index) library:

```python
from transformers import AutoModel, AutoTokenizer
import torch
import torch.nn.functional as F

model_path = "codefuse-ai/ML-Embed-0.6B"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModel.from_pretrained(
    model_path,
    torch_dtype=torch.bfloat16,
    device_map={"": 0}
)

query = "What is ML-Embed used for?"
query_prompt = "Instruct: Given a question, retrieve passages that can help answer the question.\nQuery: "

documents = [
    "ML-Embed is a family of multilingual embedding models for retrieval, semantic search, and other NLP tasks.",
    "ML-Embed is trained to produce text embeddings that work well across many languages.",
    "ML-Embed 是 CodeFuse AI 开源的多语言嵌入模型。",
    "ML-Embed — это многоязычная модель эмбеддингов для поиска и семантического сопоставления."
]

def encode(sentences):
    batch_size = len(sentences)
    tokenized_inputs = tokenizer(sentences, padding=True, return_tensors="pt").to(model.device)
    last_hidden_state = model(**tokenized_inputs).last_hidden_state
    eos_positions = tokenized_inputs.attention_mask.sum(dim=1) - 1
    embeddings = last_hidden_state[torch.arange(batch_size, device=model.device), eos_positions]
    embeddings = F.normalize(embeddings, p=2, dim=1)
    return embeddings

# Encode the query and documents
query_embedding = encode([query_prompt + query])
document_embeddings = encode(documents)

print(query_embedding.shape, document_embeddings.shape)
# torch.Size([1, 1024]) torch.Size([4, 1024])

# Compute cosine similarity between the query and documents
similarity = query_embedding @ document_embeddings.T
print(similarity)
```


## Prompts

The model supports custom instructions in the following format:

```text
Instruct: your_instruction
Query:
```

In general, for retrieval and reranking tasks:

- use the prompt for **queries**
- do **not** prepend the prompt to **documents/passages**

For symmetric tasks such as STS, clustering, and bitext mining, you can encode the documents either with or without prompts. The model is trained to support both scenarios.


## Efficient Deployment

ML-Embed-0.6B was trained with **3D Matryoshka Learning**, including:

- **MLL**: Matryoshka Layer Learning
- **MEL**: Matryoshka Embedding Learning
- **MRL**: Matryoshka Representation Learning

This enables multiple deployment modes.

### 1. Compatibility Mode

The default released checkpoint is a standard Qwen3-compatible model. You can load it normally with `AutoModel` or `SentenceTransformer` without any code changes (refer to the examples above).

This is the recommended option if you want the simplest integration.

### 2. Fewer-Layer Deployment with MLL

This model was trained so that **shallower versions remain useful**.  
If you want to save memory or compute, you can deploy a smaller model by editing:

- `num_hidden_layers`
- `max_window_layers`

in `config.json` to a value smaller than the current one.

For example, changing both values from `28` to `16` will make `transformers` load only the first 16 layers and ignore the remaining weights.

This works automatically with the Hugging Face `transformers` library.

> Note: make sure `num_hidden_layers` and `max_window_layers` stay consistent. If you are using transformers v5, you will also need to trucate `layer_types` in the config file according to the new layer count.

### 3. Factorized Embedding Deployment with MEL

This repository also provides two additional weight files:

- `U.pth`
- `V.pth`

These correspond to the factorized embedding layer.

Instead of using the full embedding matrix, you can reconstruct token embeddings from:

$$
E \approx U V
$$

This can reduce storage and memory usage for the embedding layer, and it also allows more aggressive low-rank deployment if desired.

Below is a simple inference example adapted from the training code.

#### Inference demo using `U.pth` and `V.pth`

```python
import torch
import torch.nn.functional as F
from transformers import AutoModel, AutoTokenizer
from huggingface_hub import hf_hub_download

model_path = "codefuse-ai/ML-Embed-0.6B"
dtype = torch.bfloat16
device = "cuda"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModel.from_pretrained(
    model_path,
    torch_dtype=dtype,
    device_map={"": 0}
)
model.eval()

# Load factorized embedding weights
u_path = hf_hub_download(repo_id=model_path, filename="U.pth")
v_path = hf_hub_download(repo_id=model_path, filename="V.pth")

U = torch.load(u_path, map_location="cpu").to(dtype).to(device)
V = torch.load(v_path, map_location="cpu").to(dtype).to(device)

# Optional: choose a smaller rank for more compression
# If rank is None, use the full factorized rank
rank = None

def encode_with_factorized_embedding(sentences, rank=None):
    tokenized = tokenizer(sentences, padding=True, return_tensors="pt").to(device)
    input_ids = tokenized["input_ids"]
    attention_mask = tokenized["attention_mask"]

    if rank is None:
        inputs_embeds = (U @ V)[input_ids]
    else:
        inputs_embeds = (U[:, :rank] @ V[:rank, :])[input_ids]

    outputs = model(
        inputs_embeds=inputs_embeds,
        attention_mask=attention_mask
    )

    last_hidden_state = outputs.last_hidden_state
    eos_positions = attention_mask.sum(dim=1) - 1
    embeddings = last_hidden_state[torch.arange(len(sentences), device=device), eos_positions]
    embeddings = F.normalize(embeddings, p=2, dim=1)
    return embeddings

query = "What is ML-Embed used for?"
query_prompt = "Instruct: Given a question, retrieve passages that can help answer the question.\nQuery: "

documents = [
    "ML-Embed is a family of multilingual embedding models for retrieval, semantic search, and other NLP tasks.",
    "ML-Embed is trained to produce text embeddings that work well across many languages.",
    "ML-Embed 是 CodeFuse AI 开源的多语言嵌入模型。",
    "ML-Embed — это многоязычная модель эмбеддингов для поиска и семантического сопоставления."
]

query_embedding = encode_with_factorized_embedding([query_prompt + query], rank=rank)
document_embeddings = encode_with_factorized_embedding(documents, rank=rank)

similarity = query_embedding @ document_embeddings.T
print(similarity)
```


## Matryoshka Representation Learning

This model was also trained with MRL, which means the embedding is trained to support prefix truncation.

The full embedding size is 1024, but users may also experiment with keeping only the first `d` dimensions. This can reduce storage and speed up vector search in downstream systems. The model is trained with a smallest Matryoshka dimension of 8.

Example:

```python
embedding = embedding[..., :512]
embedding = torch.nn.functional.normalize(embedding, p=2, dim=-1)
```

> Note: you need to apply normalization **after** trucation, not the other way around.

If you are using sentence transformer, you can also simply pass `truncate_dim=512` to the encode interface.

## Training

ML-Embed-0.6B is trained in two stages from Qwen3-0.6B.
- Stage 1 includes large-scale retrieval-focused data to build strong semantic embedding capability.
- Stage 2 uses instruction-aware fine-tuning on a diverse multilingual mixture of tasks.

The model is fully open:
- Training data is available at: [`codefuse-ai/F2LLM-v2`](https://huggingface.co/datasets/codefuse-ai/F2LLM-v2)
- Training code is available at: https://github.com/codefuse-ai/CodeFuse-Embeddings/tree/main/ML-Embed

## Intended Uses

ML-Embed-0.6B can be used for:

- semantic search
- dense retrieval
- RAG pipelines
- clustering
- classification
- duplicate detection
- cross-lingual retrieval
- multilingual similarity search


## Limitations

- Performance may vary across languages, domains, and task formats.
- Benchmark performance does not guarantee optimal behavior in all production retrieval or RAG systems.
- For best embedding quality, use appropriate prompts for queries.
- Efficient modes such as fewer-layer deployment and low-rank factorized embeddings involve trade-offs between quality and efficiency.

### Citation (to be updated after the conference)

```bibtex
@misc{zhang2026mlembedinclusiveefficientembeddings,
      title={ML-Embed: Inclusive and Efficient Embeddings for a Multilingual World}, 
      author={Ziyin Zhang and Zihan Liao and Hang Yu and Peng Di and Rui Wang},
      year={2026},
      eprint={2605.15081},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2605.15081}, 
}
```

## Related models

The baseline models are released and submitted to the MTEB leaderboard under the name [`F2LLM-v2`](https://huggingface.co/collections/codefuse-ai/f2llm):

| Model | Base                                                                                | Instruct                                                            |
| ----- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| 80M   |                                                                                     | [🤗F2LLM-v2-80M](https://huggingface.co/codefuse-ai/F2LLM-v2-80M)   |
| 160M  |                                                                                     | [🤗F2LLM-v2-160M](https://huggingface.co/codefuse-ai/F2LLM-v2-160M) |
| 330M  |                                                                                     | [🤗F2LLM-v2-330M](https://huggingface.co/codefuse-ai/F2LLM-v2-330M) |
| 0.6B  | [🤗F2LLM-v2-0.6B-Preview](https://huggingface.co/codefuse-ai/F2LLM-v2-0.6B-Preview) | [🤗F2LLM-v2-0.6B](https://huggingface.co/codefuse-ai/F2LLM-v2-0.6B) |
| 1.7B  | [🤗F2LLM-v2-1.7B-Preview](https://huggingface.co/codefuse-ai/F2LLM-v2-1.7B-Preview) | [🤗F2LLM-v2-1.7B](https://huggingface.co/codefuse-ai/F2LLM-v2-1.7B) |
| 4B    | [🤗F2LLM-v2-4B-Preview](https://huggingface.co/codefuse-ai/F2LLM-v2-4B-Preview)     | [🤗F2LLM-v2-4B](https://huggingface.co/codefuse-ai/F2LLM-v2-4B)     |
| 8B    | [🤗F2LLM-v2-8B-Preview](https://huggingface.co/codefuse-ai/F2LLM-v2-8B-Preview)     | [🤗F2LLM-v2-8B](https://huggingface.co/codefuse-ai/F2LLM-v2-8B)     |
| 14B   | [🤗F2LLM-v2-14B-Preview](https://huggingface.co/codefuse-ai/F2LLM-v2-14B-Preview)   | [🤗F2LLM-v2-14B](https://huggingface.co/codefuse-ai/F2LLM-v2-14B)   |