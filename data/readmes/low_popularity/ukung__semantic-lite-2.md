---
license: apache-2.0
language:
  - id
  - en
  - ar
  - zh
  - ja
  - ko
  - ru
  - th
  - hi
  - vi
  - am
  - sw
library_name: transformers
pipeline_tag: sentence-similarity
tags:
  - sentence-transformers
  - feature-extraction
  - sentence-similarity
  - embedding
  - multilingual
  - indonesian
  - quantization
  - semantic-search
  - retrieval
  - rag
base_model: XHToken/Spark-X2.5-1.7B
---

# Semantic-Lite-2

Semantic-Lite-2 is a lightweight multilingual sentence embedding model that produces 256-dimensional semantic vectors. It is designed for semantic search, sentence similarity, clustering, retrieval, and retrieval-augmented generation (RAG) tasks. The model is built on top of the [Spark-X2.5-1.7B](https://huggingface.co/XHToken/Spark-X2.5-1.7B) backbone using a frozen-backbone plus trainable-projection-head approach.

The 256-dimensional output keeps vector storage compact while preserving strong retrieval quality. Vectors are L2-normalized, so cosine similarity is computed as a simple dot product.

## Model Architecture

```
input -> embedding (frozen)
      -> 2 backbone layers (frozen)       # pretrained knowledge
      -> 2 attention-head layers (trained) # projection head
      -> mean pooling
      -> Linear(2048 -> 256)
      -> L2 normalization
      -> 256-dimensional semantic vector
```

| Component | Parameters | Status |
|---|---|---|
| Embedding table (131072 x 2048) | 268.4M | frozen |
| 2 backbone layers | 102.8M | frozen |
| 2 attention-head layers | 88.1M | trainable |
| Linear projection (2048 -> 256) | 0.52M | trainable |

## Performance

Evaluated on 500 Indonesian NLI evaluation pairs (retrieval task, chance level 0.2%):

| Metric | Semantic-Lite-2 | all-MiniLM-L6-v2 |
|---|---|---|
| top-1 accuracy | 82.4% | 64.0% |
| top-5 accuracy | 91.0% | 75.8% |
| MRR | 0.863 | 0.696 |

Cross-lingual evaluation (10 languages, 20 pairs per language): 64.5% versus MiniLM 44.5%.

## Quantized Versions

The model is available in three precision levels. Quality is measured on the same 500 Indonesian NLI evaluation pairs.

| Version | File | Size | top-1 | top-5 | MRR |
|---|---|---|---|---|---|
| fp16 | model.safetensors | 919 MB | 82.8% | 91.2% | 0.864 |
| q8 | model_q8.safetensors | 471 MB | 82.6% | 91.0% | 0.863 |
| q4 | model_q4.safetensors | 241 MB | 80.0% | 89.6% | 0.847 |

Quantization uses per-group quantization (group size 128) applied to the 2D weight tensors. Small tensors (biases and layer norms) remain in fp16. The q8 variant is practically lossless, while the q4 variant reduces top-1 accuracy by roughly 3% in exchange for a roughly 75% reduction in size.

## Quick Start

```python
from transformers import AutoTokenizer, AutoModel
import torch

model = AutoModel.from_pretrained("ukung/semantic-lite-2", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("ukung/semantic-lite-2")

def embed(texts):
    enc = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        v = model(input_ids=enc["input_ids"], attention_mask=enc["attention_mask"])
    return v  # already L2-normalized, shape (n, 256)

v1 = embed(["a cat sleeps on the sofa"])
v2 = embed(["a cat is sleeping on top of the sofa"])
similarity = (v1 * v2).sum(-1)  # cosine similarity
print(similarity.item())
```

For the quantized variants, use the `quant_loader.py` helper:

```python
from quant_loader import load_quantized_model, encode
from transformers import AutoTokenizer

model = load_quantized_model("ukung/semantic-lite-2", bits=8)  # or bits=4
tokenizer = AutoTokenizer.from_pretrained("ukung/semantic-lite-2")
v = encode(model, tokenizer, ["an example sentence in English"])
print(v.shape)  # (1, 256)
```

## Use Cases

This section provides ready-to-use recipes for the most common semantic tasks developers implement with sentence embeddings.

### 1. Semantic Search

Find the most relevant documents for a query by comparing cosine similarity against a precomputed index.

```python
import torch

def embed(texts):
    enc = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        return model(input_ids=enc["input_ids"], attention_mask=enc["attention_mask"])

# index your corpus once
corpus = [
    "how to apply for an online loan",
    "traditional beef rendang recipe",
    "train schedule from Jakarta to Bandung",
    "requirements for making a new passport",
]
corpus_vectors = embed(corpus)  # (4, 256)

# search at query time
query = embed(["how do I borrow money through an app"])
scores = (query @ corpus_vectors.T).squeeze(0)  # cosine similarity
rank = torch.argsort(scores, descending=True)
for i in rank:
    print(f"{scores[i].item():.3f}  {corpus[i]}")
```

### 2. Sentence Similarity and Paraphrase Detection

Measure how similar two sentences are, or detect whether two sentences express the same meaning.

```python
def similarity(a, b):
    va = embed([a])
    vb = embed([b])
    return (va * vb).sum(-1).item()

print(similarity("cheap flight ticket prices", "affordable airfare"))  # high
print(similarity("cheap flight ticket prices", "how to grow rice"))     # low

# threshold-based paraphrase detection
THRESHOLD = 0.75
is_paraphrase = similarity(text_a, text_b) > THRESHOLD
```

### 3. Clustering and Topic Grouping

Group related texts into clusters without labels using KMeans on the embedding space.

```python
from sklearn.cluster import KMeans

texts = [...]  # your documents
X = embed(texts).numpy()

kmeans = KMeans(n_clusters=5, n_init=10, random_state=42)
labels = kmeans.fit_predict(X)

for text, label in zip(texts, labels):
    print(label, text)
```

### 4. Duplicate and Near-Duplicate Detection

Identify duplicate or near-duplicate records in a dataset using pairwise similarity.

```python
import torch

X = embed(texts)
sim = X @ X.T  # (n, n) cosine similarity matrix

# find pairs above a high threshold (excluding self-comparison)
n = X.shape[0]
mask = torch.triu(torch.ones(n, n), diagonal=1).bool()
high = (sim > 0.92) & mask
idx = high.nonzero(as_tuple=False)
for i, j in idx.tolist():
    print(f"duplicate: {texts[i]}  <->  {texts[j]}")
```

### 5. Retrieval-Augmented Generation (RAG)

Retrieve relevant context for a language model from a vector store.

```python
# build an index (here using a simple in-memory list)
chunks = [...]      # your knowledge-base chunks
chunk_vectors = embed(chunks)

query_vector = embed([user_question])
scores = (query_vector @ chunk_vectors.T).squeeze(0)
top_k = torch.topk(scores, k=3)

context = "
".join(chunks[i] for i in top_k.indices.tolist())
prompt = f"Context:
{context}

Question: {user_question}
Answer:"
# pass `prompt` to your generative LLM
```

For production RAG, pair the model with a vector database such as FAISS, Qdrant, Chroma, or Pinecone.

### 6. Zero-Shot Classification

Classify text into predefined categories without training a classifier, by comparing the text against label descriptions.

```python
labels = [
    "a question about payment",
    "a question about shipping",
    "a question about returns and refunds",
]
label_vectors = embed(labels)

text_vector = embed(["how long will my package take to arrive"])
scores = (text_vector @ label_vectors.T).squeeze(0)
predicted = labels[torch.argmax(scores).item()]
print(predicted)
```

### 7. Cross-Lingual Matching

Match queries and documents written in different languages. The backbone is multilingual, so Indonesian, English, Arabic, Chinese, Japanese, Korean, Russian, Thai, Hindi, Vietnamese, Amharic, and Swahili share the same vector space.

```python
q = embed(["how to brew coffee"])
docs = embed([
    "how to brew coffee",
    "how to grow rice",
])
scores = (q @ docs.T).squeeze(0)
print(scores)  # the coffee sentence should score highest
```

### 8. Recommendation by Content Similarity

Recommend items that are semantically similar to an item the user already likes.

```python
items = [...]  # item descriptions
item_vectors = embed(items)

liked = embed(["a smartphone with a great camera"])
scores = (liked @ item_vectors.T).squeeze(0)
top_k = torch.topk(scores, k=5)
for i in top_k.indices.tolist():
    print(items[i])
```

### 9. Semantic Deduplication for Training Data

Clean a training corpus by removing semantically redundant examples, which improves downstream model quality.

```python
seen = []
keep = []
for text in texts:
    v = embed([text])
    if seen and max((v @ torch.stack(seen).T).squeeze(0)).item() > 0.95:
        continue  # near-duplicate, skip
    seen.append(v)
    keep.append(text)
```

### 10. FAQ and Chatbot Intent Matching

Route a user message to the most relevant FAQ entry or intent.

```python
faq = [
    ("how do I reset my password", "reset_password"),
    ("how to track my order", "track_order"),
    ("what is the refund policy", "refund_policy"),
]
faq_questions = [q for q, _ in faq]
faq_vectors = embed(faq_questions)

user_vector = embed(["I forgot my account password"])
scores = (user_vector @ faq_vectors.T).squeeze(0)
best = torch.argmax(scores).item()
print(faq[best][1])  # intent
```

## Tips

- The output vectors are already L2-normalized. Use a dot product for cosine similarity.
- For large corpora, precompute and cache the corpus vectors once, then only embed new queries.
- For production vector storage, any vector database that accepts 256-dimensional float vectors works.
- The q8 variant is recommended for most deployments: it halves the model size with negligible quality loss.

## Credits and License

The backbone originates from [XHToken/Spark-X2.5-1.7B](https://huggingface.co/XHToken/Spark-X2.5-1.7B) (Apache-2.0). This model is licensed under Apache-2.0.
