---
license: apache-2.0
language:
- en
- ko
- zh
- ja
- de
- fr
- es
- ru
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
- embedding
- qwen
- qwen3
- text-embedding
- retrieval
- matryoshka
- academic-search
- scientific-search
- multilingual
library_name: transformers
base_model: Qwen/Qwen3-Embedding-0.6B
datasets:
- ms_marco
---

# LinerAI/Qwen3-Embedding-0.6B-academic for Academic Search

This is a fine-tuned version of [Qwen/Qwen3-Embedding-0.6B](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B) optimized for **academic and scientific literature search**. The model has been trained using contrastive learning with hard negative mining, specifically curated for academic search scenarios.

## Highlights

- **Optimized for Academic Search**: Fine-tuned on datasets specifically designed for academic literature retrieval
- **Hard Negative Mining**: Trained with carefully mined hard negatives to improve discrimination between similar academic papers
- **Matryoshka Representation Learning (MRL)**: Supports flexible embedding dimensions (1024, 768, 512, 256, 128) for efficiency
- **Multilingual**: Inherits strong multilingual capabilities from Qwen3, supporting English, Chinese, Korean, Japanese, and more
- **Long Context**: Supports up to 4096 tokens

## Model Description

| Attribute | Value |
|-----------|-------|
| Base Model | Qwen/Qwen3-Embedding-0.6B |
| Architecture | Qwen3 |
| Embedding Dimension | 1024 |
| MRL Dimensions | 1024, 768, 512, 256, 128 |
| Max Sequence Length | 4096 |
| Pooling | Last token |
| Precision | float16 |

## Evaluation Results

| **Model** | Avg. | SciFact: Recall@10 | TRECCOVID: Recall@10 | NFCorpus: Recall@10 | SCIDOCS: Recall@10 | LitSearch: Recall@10 | QASA: Recall@10 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Qwen3-Embedding-0.6B-academic | 0.3881 | 0.8482 | 0.0227 | 0.1739 | 0.2323 | 0.6944 | 0.357 |
| Qwen3-Embedding-0.6B | 0.362 | 0.8277 | 0.0213 | 0.1604 | 0.2311 | 0.6489 | 0.2828 |

## Training Details

### Training Configuration

| Parameter | Value |
|-----------|-------|
| Learning Rate | 1e-6 |
| Batch Size | 8192 (effective) |
| Per-Device Batch Size | 32 |
| Warmup Steps | 100 |
| Weight Decay | 0.1 |
| Precision | fp16 |
| Max Length | 4096 |
| Loss Function | InfoNCE (Contrastive) |
| Temperature (τ) | 0.02 |

### Training Data

The model was trained on [LEAD (Liner Embedding Academic Dataset)](https://huggingface.co/datasets/LinerAI/LEAD), a combination of ~55,560 samples tailored for academic search:
- **MS MARCO** (49%): General passage retrieval dataset with hard negatives
- **Academic Search Dataset** (51%): Custom dataset built specifically for academic literature search, with two-stage hard negative mining

### Matryoshka Representation Learning (MRL)

This model supports [Matryoshka Representation Learning](https://arxiv.org/abs/2205.13147). You can truncate embeddings to smaller dimensions (768, 512, 256, 128) for faster computation and reduced storage.

```python
# Full dimension (1024)
full_embedding = embeddings[:, :1024]

# MRL dimensions
embedding_768 = embeddings[:, :768]
embedding_512 = embeddings[:, :512]
embedding_256 = embeddings[:, :256]
embedding_128 = embeddings[:, :128]
```

## Usage

### Using Transformers

```python
import torch
from transformers import AutoModel, AutoTokenizer

model_path = "LinerAI/Qwen3-Embedding-0.6B-academic"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModel.from_pretrained(model_path, torch_dtype=torch.float16)
model.eval()

general_instruction = "Given a query, retrieve relevant passages that answer the query"

# For queries
def encode_query(text):
    input_text = f"Instruct: {general_instruction}\nQuery: {text}"
    inputs = tokenizer(input_text, return_tensors="pt", max_length=4096, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
        embeddings = outputs.last_hidden_state[:, -1]  # Last token pooling
        embeddings = torch.nn.functional.normalize(embeddings, p=2, dim=1)
    return embeddings

# For passages
def encode_passage(text):
    inputs = tokenizer(text, return_tensors="pt", max_length=4096, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
        embeddings = outputs.last_hidden_state[:, -1]  # Last token pooling
        embeddings = torch.nn.functional.normalize(embeddings, p=2, dim=1)
    return embeddings

# Example: Academic search
query = "transformer models for protein structure prediction"
abstract = "We introduce AlphaFold, a deep learning system that predicts protein structures..."

query_emb = encode_query(query)
passage_emb = encode_passage(abstract)

similarity = torch.nn.functional.cosine_similarity(query_emb, passage_emb)
print(f"Similarity: {similarity.item():.4f}")
```

## Input Format

### Query Format
```
Instruct: Given a query, retrieve relevant passages that answer the query
Query: {your_query_text}
```

### Passage Format
```
{your_passage_text}
```

## Intended Use

- **Academic Paper Search**: Finding relevant research papers given a research query
- **Literature Review**: Discovering related work in academic literature
- **Scientific Document Retrieval**: Retrieving scientific documents, abstracts, and articles
- **Research Question Answering**: Finding papers that address specific research questions

## Limitations

- Maximum sequence length is 4096 tokens
- Best performance achieved when using the specific input formats described above
- The model uses asymmetric encoding (instruction prefix for queries, no prefix for passages)

## License

This model is released under the Apache 2.0 license.
