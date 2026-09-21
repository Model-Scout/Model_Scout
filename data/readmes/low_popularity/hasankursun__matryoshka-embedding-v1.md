---
library_name: sentence-transformers
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- matryoshka
- multilingual
- embeddings
- xlm-roberta
language:
- multilingual
- en
- ar
- de
- es
- fr
- zh
- ru
- tr
- ko
- ja
- it
- pt
- nl
license: cc-by-nc-4.0
base_model: xlm-roberta-base
metrics:
- cosine_accuracy
- cosine_precision
- cosine_recall
- cosine_f1
- cosine_ap
- dot_accuracy
- dot_precision
- dot_recall
- dot_f1
- dot_ap
- manhattan_accuracy
- manhattan_precision
- manhattan_recall
- manhattan_f1
- manhattan_ap
- euclidean_accuracy
- euclidean_precision
- euclidean_recall
- euclidean_f1
- euclidean_ap
model-index:
- name: Matryoshka Text Embedding v1
  results:
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: SciFact
      type: scifact
      config: default
      split: test
      revision: d56462d0e63a25450459c4f213e49ffdb866f7f9
    metrics:
    - type: ndcg_at_10
      value: 0.63084
      name: NDCG@10
    - type: ndcg_at_1
      value: 0.51
      name: NDCG@1
    - type: ndcg_at_3
      value: 0.578
      name: NDCG@3
    - type: ndcg_at_5
      value: 0.60648
      name: NDCG@5
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: STSBenchmark
      type: stsbenchmark
      config: default
      split: test
      revision: b0fddb56ed78048fa8b90373c8a3cfc37b684831
    metrics:
    - type: spearman
      value: 0.850616
      name: Spearman
    - type: pearson
      value: 0.838067
      name: Pearson
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: STS17
      type: sts17-crosslingual-sts
      config: en-en
      split: test
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
    metrics:
    - type: spearman
      value: 0.873981
      name: Spearman (en-en)
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: STS17
      type: sts17-crosslingual-sts
      config: es-es
      split: test
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
    metrics:
    - type: spearman
      value: 0.88079
      name: Spearman (es-es)
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: STS17
      type: sts17-crosslingual-sts
      config: ko-ko
      split: test
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
    metrics:
    - type: spearman
      value: 0.821019
      name: Spearman (ko-ko)
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: STS17
      type: sts17-crosslingual-sts
      config: ar-ar
      split: test
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
    metrics:
    - type: spearman
      value: 0.805643
      name: Spearman (ar-ar)
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: STS17
      type: sts17-crosslingual-sts
      config: en-de
      split: test
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
    metrics:
    - type: spearman
      value: 0.824516
      name: Spearman (en-de)
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: STS17
      type: sts17-crosslingual-sts
      config: nl-en
      split: test
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
    metrics:
    - type: spearman
      value: 0.819011
      name: Spearman (nl-en)
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: STS17
      type: sts17-crosslingual-sts
      config: it-en
      split: test
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
    metrics:
    - type: spearman
      value: 0.815176
      name: Spearman (it-en)
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: STS17
      type: sts17-crosslingual-sts
      config: fr-en
      split: test
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
    metrics:
    - type: spearman
      value: 0.815679
      name: Spearman (fr-en)
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: STS17
      type: sts17-crosslingual-sts
      config: en-tr
      split: test
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
    metrics:
    - type: spearman
      value: 0.748444
      name: Spearman (en-tr)
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: STS17
      type: sts17-crosslingual-sts
      config: es-en
      split: test
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
    metrics:
    - type: spearman
      value: 0.766019
      name: Spearman (es-en)
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: STS17
      type: sts17-crosslingual-sts
      config: en-ar
      split: test
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
    metrics:
    - type: spearman
      value: 0.71912
      name: Spearman (en-ar)
---

# Matryoshka Text Embedding v1

A multilingual text embedding model with Matryoshka Representation Learning, allowing flexible embedding dimensions from 64D to 1024D.

## Model Overview

This model implements Matryoshka Representation Learning, enabling you to truncate embeddings to different dimensions while maintaining good performance. This allows you to balance accuracy, speed, and storage based on your specific needs.

### Key Features

- **Flexible Dimensions**: Choose from 7 different embedding sizes (64D, 128D, 256D, 384D, 512D, 768D, 1024D)
- **Multilingual Support**: Trained on 100+ languages
- **Base Architecture**: XLM-RoBERTa
- **Max Sequence Length**: 8192 tokens

## Quick Start

### Installation

```python
pip install sentence-transformers

```

### Basic Usage

```python
from sentence_transformers import SentenceTransformer

# Load model
model = SentenceTransformer('hasankursun/matryoshka-text-embedding-v1')

# Full precision (1024D)
embeddings = model.encode(["Your text here"])

# Balanced mode (512D) - Recommended for most use cases
embeddings = model.encode(["Your text here"], truncate_dim=512)

# Fast mode (256D) - For high-throughput applications
embeddings = model.encode(["Your text here"], truncate_dim=256)

# Ultra-fast mode (128D) - For real-time applications
embeddings = model.encode(["Your text here"], truncate_dim=128)

```

## Performance Benchmarks

### SciFact (Scientific Document Retrieval)

| Dimension | NDCG@10 | Relative Performance |
| --- | --- | --- |
| **1024D** | 0.6308 | 100.0% |
| **768D** | 0.6277 | 99.5% |
| **512D** | 0.6114 | 96.9% |
| **384D** | 0.6035 | 95.7% |
| **256D** | 0.5614 | 89.0% |
| **128D** | 0.4732 | 75.0% |
| **64D** | 0.3317 | 52.6% |

### STSBenchmark (English Semantic Similarity)

* **Spearman**: 0.8506 (1024D)
* **Pearson**: 0.8381 (1024D)

### STS17 (Multilingual Semantic Similarity)

**Average Spearman Correlation across languages: 0.8096**

Performance by language pair (1024D):

* Spanish (es-es): 0.8808
* English (en-en): 0.8740
* German (en-de): 0.8245
* Korean (ko-ko): 0.8210
* French (fr-en): 0.8157
* Italian (it-en): 0.8152
* Dutch (nl-en): 0.8190
* Arabic (ar-ar): 0.8056
* Turkish (en-tr): 0.7484
* Spanish-English (es-en): 0.7660
* English-Arabic (en-ar): 0.7191

## Use Cases

### High Accuracy Applications (768D-1024D)

* Scientific literature search
* Legal document retrieval
* Medical information systems

### Balanced Production (512D) - Recommended

* General web search
* E-commerce product search
* Content recommendation engines
* Knowledge base retrieval

### High-Throughput Systems (256D-384D)

* Real-time search APIs
* Large-scale document indexing
* Social media search

### Mobile & Edge Devices (64D-128D)

* Mobile applications
* IoT devices
* Browser-based search
* Resource-constrained environments

## Advanced Usage

### Semantic Search

```python
import numpy as np
from sentence_transformers import util

# Index documents with 512D (optimal balance)
documents = [
    "Artificial intelligence is transforming healthcare.",
    "Machine learning models require large datasets.",
    "Quantum computing promises exponential speedups."
]

doc_embeddings = model.encode(documents, truncate_dim=512)

# Search with same dimension
query = "How is AI used in medicine?"
query_embedding = model.encode(query, truncate_dim=512)

# Compute similarities
similarities = util.cos_sim(query_embedding, doc_embeddings)
top_result = np.argmax(similarities)

print(f"Most relevant: {documents[top_result]}")

```

### Integration with FAISS

```python
import faiss
import numpy as np

# Create embeddings with 512D
embeddings = model.encode(documents, truncate_dim=512)
embeddings = embeddings.astype('float32')

# Build FAISS index
dimension = 512
index = faiss.IndexFlatIP(dimension)
faiss.normalize_L2(embeddings)
index.add(embeddings)

# Search
query_embedding = model.encode(query, truncate_dim=512).astype('float32')
faiss.normalize_L2(query_embedding.reshape(1, -1))
distances, indices = index.search(query_embedding.reshape(1, -1), k=10)

```

## Technical Details

### Architecture

* **Base**: XLM-RoBERTa transformer encoder
* **Embedding Dimensions**: 1024 (full) with 7 supported truncation levels
* **Max Sequence Length**: 8192 tokens
* **Vocabulary Size**: 250,002 tokens
* **Parameters**: ~568M

### Training

* **Technique**: Matryoshka Representation Learning
* **Languages**: 100+ languages
* **Max Input Length**: 8192 tokens

## Model Files

* `pytorch_model.bin` - Model weights
* `config.json` - Model configuration
* `tokenizer.json` - Tokenizer configuration
* `matryoshka_config.json` - Matryoshka-specific configuration

## License

This model is released under the **CC-BY-NC-4.0** (Creative Commons Attribution-NonCommercial 4.0 International) license.

See the [LICENSE](https://www.google.com/search?q=LICENSE) file for full details and acknowledgments.

## Acknowledgments

This model builds upon important foundational work:

* **XLM-RoBERTa**: Base architecture for multilingual representations
* **BAAI**: For their contributions through RetroMAE and BGE-M3 papers
* **Matryoshka Representation Learning**: Training methodology (Kusupati et al., 2022)

## Citation

If you use this model in your research or application, please cite:

```bibtex
@misc{matryoshka-text-embedding-v1,
  title={Matryoshka Text Embedding v1},
  author={Hasan Kurşun},
  year={2025},
  url={[https://huggingface.co/hasankursun/matryoshka-text-embedding-v1](https://huggingface.co/hasankursun/matryoshka-text-embedding-v1)}
}

```

```

```