---
language:
  - multilingual
  - en
  - id
  - fr
  - es
  - de
  - pt
  - it
  - nl
  - ja
  - zh
  - ko
  - ar
  - ru
  - vi
  - th
  - tr
  - pl
  - uk
  - sv
  - fa
  - he
  - hi
license: apache-2.0
library_name: sentence-transformers
tags:
  - sentence-transformers
  - feature-extraction
  - sentence-similarity
  - retrieval
  - multilingual
  - qwen3
  - pruned-model
---

# semantic-lite

Lightweight multilingual embedding model for retrieval and semantic similarity, built from **Qwen3-0.6B** via layer pruning (28 → 6 layers). 2.4× smaller than the base model while matching or beating dedicated embedding models on retrieval.

- **Dimensions:** 1024
- **Parameters:** 250M (pruned from 596M)
- **Languages:** inherits Qwen3's 100+ language coverage
- **Max sequence:** 8192 tokens

## Installation

```bash
pip install sentence-transformers
```

## Quick Start

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("ukung/semantic-lite")
embeddings = model.encode(["Hello world", "Halo dunia"])
# shape: (2, 1024)
```

---

## Use Cases

### 1. Semantic Similarity

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("ukung/semantic-lite")

sentences = [
    "A man is playing a guitar.",
    "A person is playing a musical instrument.",
    "The stock market crashed today.",
]
embeddings = model.encode(sentences, normalize_embeddings=True)
similarity = embeddings @ embeddings.T
print(similarity[0, 1])  # 0.96  (similar)
print(similarity[0, 2])  # 0.79  (different)
```

### 2. Semantic Search

```python
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("ukung/semantic-lite")

corpus = [
    "How to cook fried rice",
    "Guide to stock market investing",
    "Tips for caring for your cat",
    "Python programming tutorial for beginners",
    "How to grow chili peppers in pots",
]
corpus_embeddings = model.encode(corpus, normalize_embeddings=True)

query = "Easy home cooking recipes"
query_embedding = model.encode(query, normalize_embeddings=True)

scores = query_embedding @ corpus_embeddings.T
best = int(np.argmax(scores))
print(corpus[best])  # "How to cook fried rice"
```

**Tip:** for short, abstract queries (e.g. "I want to learn coding"), use an asymmetric prompt for better precision:

```python
query_emb = model.encode(query, prompt="query: ", normalize_embeddings=True)
doc_emb = model.encode(corpus, prompt="passage: ", normalize_embeddings=True)
```

### 3. Cross-Lingual Retrieval

```python
model = SentenceTransformer("ukung/semantic-lite")

documents = [
    "How to bake a chocolate cake",
    "Cara membuat kue cokelat",
    "Comment faire un gâteau au chocolat",
    "Cómo hacer un pastel de chocolate",
    "The weather forecast for tomorrow",
]
doc_embeddings = model.encode(documents, normalize_embeddings=True)

query = "Resep kue cokelat"  # Indonesian query
query_embedding = model.encode(query, normalize_embeddings=True)

scores = query_embedding @ doc_embeddings.T
print(documents[int(np.argmax(scores))])  # "Cara membuat kue cokelat"
```

### 4. Clustering

```python
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans

model = SentenceTransformer("ukung/semantic-lite")

texts = [
    "I love pizza and pasta",
    "Italian food is delicious",
    "Python is a great programming language",
    "I code in Python daily",
    "The cat is sleeping on the sofa",
    "My dog loves to play fetch",
]
embeddings = model.encode(texts, normalize_embeddings=True)
labels = KMeans(n_clusters=3, n_init=10, random_state=42).fit(embeddings).labels_
print(labels)  # [2 2 0 0 1 1]
```

### 5. Duplicate Detection

```python
model = SentenceTransformer("ukung/semantic-lite")

sentences = [
    "How do I reset my password?",
    "What is the process to reset a password?",
    "Where can I buy a new laptop?",
]
embeddings = model.encode(sentences, normalize_embeddings=True)
similarity = embeddings @ embeddings.T
print(similarity[0, 1])  # 0.91  (duplicate)
print(similarity[0, 2])  # 0.85  (not duplicate)
```

### 6. Paraphrase Mining

```python
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("ukung/semantic-lite")

corpus = [
    "What is the capital of France?",
    "Paris is the capital of France.",
    "How do I learn Python?",
    "Python is a programming language.",
    "The capital city of France is Paris.",
]
pairs = util.paraphrase_mining(model, corpus, top_k=3)
for score, i, j in pairs:
    print(f"{score:.3f}: {corpus[i]} <-> {corpus[j]}")
```

### 7. Retrieval-Augmented Generation (RAG)

```python
model = SentenceTransformer("ukung/semantic-lite")

knowledge_base = [
    "Qwen3 is a family of large language models by Alibaba.",
    "Sentence-transformers is a Python library for embeddings.",
    "The Eiffel Tower is located in Paris, France.",
]
kb_embeddings = model.encode(knowledge_base, normalize_embeddings=True)

query = "What is Qwen3?"
query_embedding = model.encode(query, normalize_embeddings=True)

scores = query_embedding @ kb_embeddings.T
context = knowledge_base[int(np.argmax(scores))]
print(context)  # "Qwen3 is a family of large language models by Alibaba."
```

### 8. Recommendation

```python
model = SentenceTransformer("ukung/semantic-lite")

items = [
    "Action movie with explosions",
    "Romantic comedy film",
    "Sci-fi space adventure",
    "Horror ghost story",
]
item_embeddings = model.encode(items, normalize_embeddings=True)

user_preference = "I enjoy science fiction and space"
user_embedding = model.encode(user_preference, normalize_embeddings=True)

scores = user_embedding @ item_embeddings.T
print(items[int(np.argmax(scores))])  # "Sci-fi space adventure"
```

### 9. Batch Encoding

```python
model = SentenceTransformer("ukung/semantic-lite")

documents = [f"Document {i} about topic {i % 5}" for i in range(1000)]
embeddings = model.encode(
    documents,
    batch_size=32,
    normalize_embeddings=True,
    show_progress_bar=True,
)
print(embeddings.shape)  # (1000, 1024)
```

---

## Multilingual Support

Inherits Qwen3's 100+ language coverage. Mean cosine similarity to English across 22 tested languages: **0.786** (21/22 above 0.6).

| Language | cos | Language | cos |
|---|---|---|---|
| es | 0.858 | ru | 0.775 |
| pt | 0.858 | ja | 0.771 |
| id | 0.857 | th | 0.765 |
| fr | 0.847 | ar | 0.756 |
| vi | 0.842 | ko | 0.753 |
| de | 0.837 | he | 0.732 |
| nl | 0.827 | tr | 0.723 |
| it | 0.804 | uk | 0.722 |
| zh | 0.790 | pl | 0.721 |
| sv | 0.787 | fa | 0.671 |
| | | hi | 0.598 |

---

## Specifications

| Property | Value |
|---|---|
| Base model | Qwen3-0.6B |
| Parameters | 250M (pruned from 596M) |
| Layers | 6 (pruned from 28) |
| Embedding dimension | 1024 |
| Max sequence length | 8192 |
| Normalization | L2 (cosine) |

## Evaluation

Retrieval benchmark on an internal Indonesian corpus (20 documents, 8 queries):

| Metric | semantic-lite | all-MiniLM-L6-v2 |
|---|---|---|
| nDCG@5 | **0.923** | 0.812 |
| Recall@5 | **1.000** | 0.875 |
| MRR | **0.900** | 0.807 |

## Limitations

- **Zero-shot classification is not supported.** The model's embeddings are not calibrated for label-matching tasks. Use a dedicated zero-shot classifier instead.
- **Short, abstract queries** may require an asymmetric prompt (`query:` / `passage:`) for optimal retrieval precision.
- **Evaluation is on a small internal corpus.** Results on large public benchmarks (MTEB, BEIR) are not yet validated.

## License

Apache 2.0 (inherited from Qwen3).
