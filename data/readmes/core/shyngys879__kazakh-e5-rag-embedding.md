---
language:
- kk
- ru
- en
license: other
library_name: sentence-transformers
pipeline_tag: feature-extraction
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- embeddings
- semantic-search
- retrieval
- rag
- kazakh
- kk
- nlp
- e5
- text-embeddings-inference
base_model:
- Nurlykhan/kazembed-v5
- intfloat/multilingual-e5-base
datasets:
- shyngys879/Kazakh-Wiki-RAG-Dataset
- issai/kazqad
- issai/kazqad-retrieval
---

# Kazakh-E5-RAG-Embedding: Kazakh Embedding Model for RAG

  **Kazakh-E5-RAG-Embedding** is an E5-style text embedding model for **Kazakh RAG, semantic search, FAQ search, question-answer retrieval, and document search**.

🏆 **Best evaluated BASE-size embedding model on our Kazakh hard-negative retrieval benchmark.**

The model is built on the **multilingual-e5-base** architecture and further optimized for Kazakh question-passage matching, hard-negative retrieval, and Kazakh Wikipedia-style document search.

## Why use this model?

- **Kazakh-focused retrieval:** optimized for Kazakh questions, passages, and document search
- 🔍 **Hard-negative ranking:** designed to distinguish correct passages from very similar incorrect passages
- ⚡ **Efficient BASE-size model:** 278M parameters
- 🧠 **E5-style format:** uses `query:` and `passage:` prefixes
- 🔧 **RAG-ready:** works with `sentence-transformers`, vector databases, and retrieval pipelines
- 📊 **Evaluated on 3 Kazakh retrieval benchmarks**

---

## Usage

### Installation

```bash
pip install sentence-transformers numpy
```

### Convert Text to Embeddings

This model converts Kazakh text into **768-dimensional embedding vectors** that can be used for semantic search, retrieval, and RAG.

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("shyngys879/kazakh-e5-rag-embedding")

text = "passage: Астана — Қазақстан Республикасының астанасы."

embedding = model.encode(text, normalize_embeddings=True)

print(embedding.shape)
# (768,)

print(embedding[:5])
# Example output: [0.021, -0.034, 0.056, ...]
```

### Basic Usage

```python
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("shyngys879/kazakh-e5-rag-embedding")

query = "query: Қазақстанның астанасы қай қала?"
passage = "passage: Астана — Қазақстан Республикасының астанасы."

query_embedding = model.encode(query, normalize_embeddings=True)
passage_embedding = model.encode(passage, normalize_embeddings=True)

# Since embeddings are normalized, dot product = cosine similarity
similarity = np.dot(query_embedding, passage_embedding)

print(f"Similarity: {similarity:.4f}")
```

### FAQ / Document Search

```python
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("shyngys879/kazakh-e5-rag-embedding")

documents = [
    "Астана — Қазақстан Республикасының астанасы.",
    "Алматы — Қазақстанның ең үлкен қаласы.",
    "Қазақстан — Орталық Азиядағы мемлекет.",
    "Абай Құнанбайұлы — қазақтың ұлы ақыны және ағартушысы.",
]

query = "Қазақстанның астанасы қай қала?"

doc_embeddings = model.encode(
    ["passage: " + doc for doc in documents],
    normalize_embeddings=True
)

query_embedding = model.encode(
    "query: " + query,
    normalize_embeddings=True
)

scores = np.dot(doc_embeddings, query_embedding)
best_idx = np.argmax(scores)

print("Question:", query)
print("Best match:", documents[best_idx])
print("Score:", float(scores[best_idx]))
```

This same pattern can be used for FAQ search, document retrieval, and RAG pipelines: encode your documents, retrieve the most relevant passages, then pass them to an LLM as context.

### Important Prefix Format

For best results, use E5-style prefixes:

| Input type | Prefix |
|---|---|
| Query / question | `query: ...` |
| Passage / document | `passage: ...` |

---

## Benchmark Results

The model was evaluated on three Kazakh retrieval settings:

1. **OfficialKazQAD-HardTFIDF99** — hard-negative question-passage retrieval.
2. **WikiFullCorpus** — Kazakh Wikipedia-style full-corpus retrieval.
3. **KazQAD-100 local** — KazQAD-style retrieval with 100 candidates per query.

**MRR** means *Mean Reciprocal Rank*: higher is better, and it rewards models that rank the correct passage closer to the top.

---

### OfficialKazQAD-HardTFIDF99

This benchmark uses **1,929 KazQAD test queries**.  
For each query, the model must rank the correct passage among **100 candidate passages**.

The candidate set contains:

- 1 correct passage
- 99 TF-IDF hard negatives

A **hard negative** is an incorrect passage that is textually or topically similar to the query. This makes the task harder than retrieval with random negative passages, because the model must identify which similar passage actually answers the question.

| Model | Hits@1 | Hits@5 | MRR | Params |
|---|---:|---:|---:|---:|
| **Kazakh-E5-RAG-Embedding** | **35.98%** | **72.47%** | **0.5189** | 278M |
| KazEmbed-V5 original | 30.07% | 65.68% | 0.4619 | 278M |
| multilingual-e5-large | 30.17% | 62.99% | 0.4490 | 560M |
| multilingual-e5-base | 25.87% | 56.71% | 0.4048 | 278M |
| paraphrase-multilingual-mpnet-base-v2 | 10.01% | 29.91% | 0.2082 | 278M |
| LaBSE | 7.47% | 26.75% | 0.1821 | 471M |

---

### Additional Benchmarks

| Benchmark | Model | Hits@1 | Hits@5 | MRR | Params |
|---|---|---:|---:|---:|---:|
| WikiFullCorpus | multilingual-e5-large | 69.13% | 85.79% | 0.7656 | 560M |
| WikiFullCorpus | multilingual-e5-base | 65.85% | 80.87% | 0.7290 | 278M |
| WikiFullCorpus | **Kazakh-E5-RAG-Embedding** | **60.38%** | **74.32%** | **0.6689** | 278M |
| WikiFullCorpus | KazEmbed-V5 original | 56.83% | 70.49% | 0.6276 | 278M |
| KazQAD-100 local | **Kazakh-E5-RAG-Embedding** | **91.55%** | **100.00%** | **0.9554** | 278M |
| KazQAD-100 local | KazEmbed-V5 original | 87.32% | 100.00% | 0.9334 | 278M |
| KazQAD-100 local | multilingual-e5-large | 86.27% | 98.24% | 0.9189 | 560M |
| KazQAD-100 local | multilingual-e5-base | 85.56% | 97.54% | 0.9105 | 278M |

**Benchmark notes:**

- **WikiFullCorpus** evaluates full-corpus retrieval over Kazakh Wikipedia-style passages. The model must find the correct passage from a larger document corpus, which makes this closer to practical semantic search and RAG.
- **KazQAD-100 local** evaluates Kazakh question-passage retrieval with 100 candidates per query. It is a supporting benchmark for checking whether the model ranks the correct answer passage near the top.

---

## Model Details

| Field | Value |
|---|---|
| Model name | `shyngys879/kazakh-e5-rag-embedding` |
| Model type | Text embedding / bi-encoder retrieval model |
| Architecture family | multilingual-e5-base / XLM-RoBERTa |
| Continued fine-tuning from | `Nurlykhan/kazembed-v5` |
| Model lineage | `intfloat/multilingual-e5-base` → `Nurlykhan/kazembed-v5` → this model |
| Parameters | 278M |
| Embedding dimension | 768 |
| Main language | Kazakh |
| Task | Retrieval, semantic search, RAG, question-passage matching |
| Training objective | Kazakh retrieval / question-passage matching |
| Training data | KazQAD-style retrieval data, TF-IDF hard negatives, Kazakh Wikipedia-style retrieval examples |

---

## Recommended Use Cases

- Kazakh RAG systems
- Kazakh semantic search
- FAQ search
- document retrieval
- question-answer retrieval
- educational search
- Kazakh Wikipedia / encyclopedic search
- multilingual projects involving Kazakh

---

## Limitations

- The model is optimized mainly for Kazakh retrieval and RAG.
- On WikiFullCorpus, multilingual-e5-base and multilingual-e5-large perform better.

---

## Citation

```bibtex
@misc{kazakh-e5-rag-embedding-2026,
  title={Kazakh-E5-RAG-Embedding: A Kazakh Retrieval Embedding Model for RAG},
  author={Shyngys Sovetkhan},
  year={2026},
  howpublished={Hugging Face Model Hub},
  url={https://huggingface.co/shyngys879/kazakh-e5-rag-embedding}
}
```

---

## Acknowledgements

This model builds on:

- `Nurlykhan/kazembed-v5`
- `intfloat/multilingual-e5-base`
- KazQAD / KazQAD-style retrieval data
- Kazakh Wikipedia-style retrieval examples

---

## Contact, Custom Fine-Tuning, and Model Use

For commercial deployment, RAG or semantic-search integration, model evaluation, or custom fine-tuning on your organization's documents and domain-specific data, please contact:

**Shyngys Sovetkhan**  
**Email:** [shyngyssovetkhan0@gmail.com](mailto:shyngyssovetkhan0@gmail.com)

If your company or organization uses this model, has evaluated it, or has found it useful, I would greatly appreciate a brief official confirmation letter describing the use case or evaluation results. Such documentation helps demonstrate the model's real-world impact in my university applications. The letter can be sent to the email address above.

