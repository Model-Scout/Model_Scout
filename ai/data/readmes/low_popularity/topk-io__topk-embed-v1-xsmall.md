---
license: apache-2.0
base_model: Qwen/Qwen3.5-0.8B
language:
- en
- ru
- fr
- nl
- de
- es
- it
- pt
- da
- 'no'
- sv
- zh
- ja
- ko
library_name: sentence-transformers
pipeline_tag: feature-extraction
tags:
- sentence-transformers
- image-text-to-text
- multi-vector
- retrieval
- custom_code
- late-interaction
---

<p align="center">
<svg width="300" height="84" viewBox="0 0 2000 560" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="100" height="100" fill="#EDEDED"/>
<rect x="115" width="100" height="100" fill="#EDEDED"/>
<rect x="230" width="100" height="100" fill="#EDEDED"/>
<rect x="345" width="100" height="100" fill="#EDEDED"/>
<rect x="460" width="100" height="100" fill="#EDEDED"/>
<rect x="230" y="115" width="100" height="100" fill="#EDEDED"/>
<rect x="230" y="230" width="100" height="100" fill="#EDEDED"/>
<rect x="230" y="345" width="100" height="100" fill="#EDEDED"/>
<rect x="230" y="460" width="100" height="100" fill="#EDEDED"/>
<rect x="1075" width="100" height="100" fill="#EDEDED"/>
<rect x="1075" width="100" height="100" fill="#EDEDED"/>
<rect x="1190" width="100" height="100" fill="#EDEDED"/>
<rect x="1305" width="100" height="100" fill="#EDEDED"/>
<rect x="1190" y="230" width="100" height="100" fill="#EDEDED"/>
<rect x="1305" y="230" width="100" height="100" fill="#EDEDED"/>
<rect x="1420" width="100" height="100" fill="#EDEDED"/>
<rect x="1420" width="100" height="100" fill="#EDEDED"/>
<rect x="1075" y="460" width="100" height="100" fill="#EDEDED"/>
<rect x="1075" y="460" width="100" height="100" fill="#EDEDED"/>
<rect x="1075" y="115" width="100" height="100" fill="#EDEDED"/>
<rect x="1075" y="230" width="100" height="100" fill="#EDEDED"/>
<rect x="1420" width="100" height="100" fill="#EDEDED"/>
<rect x="1420" width="100" height="100" fill="#EDEDED"/>
<rect x="1420" y="115" width="100" height="100" fill="#EDEDED"/>
<rect x="1420" y="230" width="100" height="100" fill="#EDEDED"/>
<rect x="1075" y="345" width="100" height="100" fill="#EDEDED"/>
<rect x="1075" y="460" width="100" height="100" fill="#EDEDED"/>
<rect x="710" width="100" height="100" fill="#EDEDED"/>
<rect x="825" width="100" height="100" fill="#EDEDED"/>
<rect x="940" width="100" height="100" fill="#EDEDED"/>
<rect x="595" width="100" height="100" fill="#EDEDED"/>
<rect x="595" y="115" width="100" height="100" fill="#EDEDED"/>
<rect x="595" y="230" width="100" height="100" fill="#EDEDED"/>
<rect x="595" y="345" width="100" height="100" fill="#EDEDED"/>
<rect x="595" y="460" width="100" height="100" fill="#EDEDED"/>
<rect x="940" width="100" height="100" fill="#EDEDED"/>
<rect x="710" y="460" width="100" height="100" fill="#EDEDED"/>
<rect x="825" y="460" width="100" height="100" fill="#EDEDED"/>
<rect x="940" y="460" width="100" height="100" fill="#EDEDED"/>
<rect x="595" y="460" width="100" height="100" fill="#EDEDED"/>
<rect x="940" y="460" width="100" height="100" fill="#EDEDED"/>
<rect x="940" y="115" width="100" height="100" fill="#EDEDED"/>
<rect x="940" y="230" width="100" height="100" fill="#EDEDED"/>
<rect x="940" y="345" width="100" height="100" fill="#EDEDED"/>
<rect x="940" y="460" width="100" height="100" fill="#EDEDED"/>
<rect x="940" width="100" height="100" fill="#EDEDED"/>
<rect x="940" width="100" height="100" fill="#EDEDED"/>
<rect x="940" y="460" width="100" height="100" fill="#EDEDED"/>
<rect x="940" y="460" width="100" height="100" fill="#EDEDED"/>
<rect x="940" y="115" width="100" height="100" fill="#EDEDED"/>
<rect x="940" y="230" width="100" height="100" fill="#EDEDED"/>
<rect x="940" y="345" width="100" height="100" fill="#EDEDED"/>
<rect x="940" y="460" width="100" height="100" fill="#EDEDED"/>
<rect x="1555" width="100" height="100" fill="#FE5000"/>
<rect x="1555" y="115" width="100" height="100" fill="#FE5000"/>
<rect x="1555" y="230" width="100" height="100" fill="#FE5000"/>
<rect x="1785" y="115" width="100" height="100" fill="#FE5000"/>
<rect x="1670" y="230" width="100" height="100" fill="#FE5000"/>
<rect x="1900" width="100" height="100" fill="#FE5000"/>
<rect x="1900" width="100" height="100" fill="#FE5000"/>
<rect x="1785" y="345" width="100" height="100" fill="#FE5000"/>
<rect x="1900" y="460" width="100" height="100" fill="#FE5000"/>
<rect x="1555" y="345" width="100" height="100" fill="#FE5000"/>
<rect x="1555" y="460" width="100" height="100" fill="#FE5000"/>
<rect x="1900" y="460" width="100" height="100" fill="#FE5000"/>
</svg>
</p>

<p align="center">
<sup>Looking for production ready multi-vector search? Check out <a href="https://topk.io">TopK</a>.</sup>
</p>

# topk-embed-v1-xsmall

**topk-embed-v1-xsmall** is a 0.8B **multimodal late-interaction retriever**.
It uses text queries to search both text documents and images, such as scanned pages,
reports, and slides.

Rather than compressing an input into a single vector, it keeps multiple embeddings
for text tokens or image patches. Retrieval uses **MaxSim scoring**: each query vector
is matched to its most similar document vector, and those similarities are summed.
Higher scores indicate more relevant documents.

## Usage with SentenceTransformers

Install the dependencies in [requirements.txt](requirements.txt).
A CUDA GPU with bfloat16 support (Ampere or newer) is required.

```python
from PIL import Image
from sentence_transformers import MultiVectorEncoder

model = MultiVectorEncoder(
    "topk-io/topk-embed-v1-xsmall",
    trust_remote_code=True,
    device="cuda",
)

query_embeddings = model.encode_query(["What was Q3 revenue?"])

# Encode text and image documents in separate batches.
text_embeddings = model.encode_document([
    "Q3 revenue was $12 million, up 20% year over year.",
    "The company opened a new office in October.",
])
with Image.open("page.png") as page:
    image_embeddings = model.encode_document([page.convert("RGB")])

# MaxSim scores: one row per query, one column per document.
text_scores = model.similarity(query_embeddings, text_embeddings)    # (1, 2)
image_scores = model.similarity(query_embeddings, image_embeddings)  # (1, 1)
```

Default limits are 1024 tokens per query and 8192 tokens per text document.
Embeddings have 1024 dimensions. For smaller Matryoshka (MRL) embeddings, pass
`config_kwargs={"output_dim": 256}` when loading the model.

## Evaluation

Results on the eight public ViDoRe v3 test datasets, reported as percentages (higher is better).
Columns are Matryoshka (MRL) prefix dimensions; 1024 is the full embedding width.
In each per-dataset table, the final row is the unweighted mean across datasets, computed before rounding.

Native queries use the document language: French for Energy, Finance (French), and Physics;
English for the remaining datasets. Crosslingual results include all six query languages,
including the native language. Image retrieval uses page images; Markdown retrieval uses
the corresponding page text.

The per-dataset tables use all document vectors (no token pooling), prefix truncation followed by
FP32 L2 normalization, FP16 query/document vector storage, and exhaustive FP32 MaxSim scoring.
nDCG@10 uses the graded relevance labels with linear gains. Recall@10 divides retrieved
relevant documents by all relevant documents for each query (not capped recall).

### Vidore V3 (image, native)

#### nDCG@10

| Dataset | 64 | 128 | 256 | 512 | 1024 |
|---|---:|---:|---:|---:|---:|
| Computer science | 75.96 | 77.38 | 77.34 | 77.61 | 77.63 |
| Energy | 66.45 | 67.08 | 67.86 | 68.48 | 68.08 |
| Finance (English) | 66.79 | 68.82 | 68.92 | 68.87 | 69.05 |
| Finance (French) | 47.34 | 48.52 | 49.05 | 49.53 | 49.27 |
| Human resources | 62.98 | 63.74 | 64.29 | 64.43 | 64.81 |
| Industrial | 55.07 | 56.20 | 56.02 | 56.28 | 56.65 |
| Pharmaceuticals | 67.52 | 68.66 | 68.33 | 68.52 | 68.77 |
| Physics | 47.02 | 48.49 | 48.27 | 48.75 | 48.76 |
| **Average** | **61.14** | **62.36** | **62.51** | **62.81** | **62.88** |

#### Recall@10

| Dataset | 64 | 128 | 256 | 512 | 1024 |
|---|---:|---:|---:|---:|---:|
| Computer science | 78.38 | 80.06 | 79.70 | 80.18 | 80.44 |
| Energy | 74.18 | 73.47 | 75.05 | 75.18 | 74.66 |
| Finance (English) | 69.87 | 72.54 | 72.53 | 71.91 | 72.00 |
| Finance (French) | 54.58 | 55.34 | 56.20 | 56.66 | 56.17 |
| Human resources | 67.31 | 67.83 | 68.69 | 68.24 | 67.96 |
| Industrial | 56.41 | 57.83 | 57.87 | 58.45 | 58.52 |
| Pharmaceuticals | 70.60 | 70.81 | 70.78 | 70.76 | 71.15 |
| Physics | 49.90 | 51.16 | 51.53 | 52.14 | 51.93 |
| **Average** | **65.15** | **66.13** | **66.55** | **66.69** | **66.60** |

### Vidore V3 (image, crosslingual)

#### nDCG@10

| Dataset | 64 | 128 | 256 | 512 | 1024 |
|---|---:|---:|---:|---:|---:|
| Computer science | 71.38 | 74.49 | 74.95 | 75.59 | 75.48 |
| Energy | 63.59 | 65.41 | 66.23 | 66.70 | 66.51 |
| Finance (English) | 59.25 | 62.78 | 63.36 | 63.67 | 63.70 |
| Finance (French) | 43.46 | 45.09 | 46.02 | 46.25 | 46.55 |
| Human resources | 57.72 | 59.81 | 60.76 | 60.98 | 60.96 |
| Industrial | 45.89 | 49.74 | 50.18 | 50.74 | 50.97 |
| Pharmaceuticals | 64.66 | 66.36 | 66.86 | 67.25 | 67.24 |
| Physics | 46.87 | 48.39 | 48.49 | 48.72 | 48.71 |
| **Average** | **56.60** | **59.01** | **59.61** | **59.99** | **60.02** |

#### Recall@10

| Dataset | 64 | 128 | 256 | 512 | 1024 |
|---|---:|---:|---:|---:|---:|
| Computer science | 74.19 | 77.22 | 77.50 | 77.96 | 78.17 |
| Energy | 71.80 | 72.67 | 73.55 | 73.65 | 73.65 |
| Finance (English) | 64.06 | 67.60 | 68.07 | 68.03 | 68.24 |
| Finance (French) | 50.73 | 52.48 | 53.52 | 53.78 | 54.21 |
| Human resources | 61.93 | 64.29 | 65.02 | 65.00 | 64.79 |
| Industrial | 49.47 | 52.66 | 53.45 | 53.86 | 53.87 |
| Pharmaceuticals | 67.92 | 68.92 | 69.24 | 69.62 | 69.94 |
| Physics | 49.30 | 51.09 | 51.51 | 51.71 | 52.04 |
| **Average** | **61.17** | **63.37** | **63.98** | **64.20** | **64.36** |

### Vidore V3 (markdown, native)

#### nDCG@10

| Dataset | 64 | 128 | 256 | 512 | 1024 |
|---|---:|---:|---:|---:|---:|
| Computer science | 74.69 | 76.13 | 76.81 | 76.89 | 76.80 |
| Energy | 65.34 | 66.58 | 67.24 | 67.21 | 67.40 |
| Finance (English) | 65.92 | 67.99 | 68.33 | 68.48 | 68.82 |
| Finance (French) | 46.91 | 47.42 | 48.18 | 48.04 | 48.84 |
| Human resources | 60.40 | 60.96 | 62.14 | 61.76 | 61.94 |
| Industrial | 53.19 | 54.29 | 54.57 | 54.60 | 54.91 |
| Pharmaceuticals | 66.08 | 66.52 | 67.22 | 66.82 | 66.73 |
| Physics | 45.92 | 47.07 | 47.70 | 47.56 | 47.71 |
| **Average** | **59.81** | **60.87** | **61.52** | **61.42** | **61.64** |

#### Recall@10

| Dataset | 64 | 128 | 256 | 512 | 1024 |
|---|---:|---:|---:|---:|---:|
| Computer science | 77.00 | 78.79 | 79.71 | 79.45 | 79.13 |
| Energy | 73.34 | 74.80 | 75.17 | 75.51 | 75.96 |
| Finance (English) | 71.21 | 72.67 | 73.10 | 72.84 | 72.58 |
| Finance (French) | 54.15 | 54.78 | 56.08 | 55.87 | 56.43 |
| Human resources | 64.94 | 65.52 | 66.61 | 66.09 | 65.88 |
| Industrial | 54.61 | 55.44 | 56.70 | 56.31 | 56.36 |
| Pharmaceuticals | 68.52 | 68.94 | 69.94 | 69.55 | 69.22 |
| Physics | 47.79 | 49.67 | 50.89 | 51.02 | 51.09 |
| **Average** | **63.94** | **65.08** | **66.02** | **65.83** | **65.83** |

### Vidore V3 (markdown, crosslingual)

#### nDCG@10

| Dataset | 64 | 128 | 256 | 512 | 1024 |
|---|---:|---:|---:|---:|---:|
| Computer science | 70.11 | 73.14 | 74.11 | 74.46 | 74.65 |
| Energy | 63.11 | 64.33 | 65.05 | 65.32 | 65.73 |
| Finance (English) | 56.81 | 59.72 | 60.48 | 61.14 | 60.92 |
| Finance (French) | 42.20 | 43.85 | 44.54 | 45.12 | 45.57 |
| Human resources | 54.64 | 57.03 | 57.79 | 58.00 | 58.44 |
| Industrial | 42.81 | 45.92 | 46.74 | 47.06 | 47.41 |
| Pharmaceuticals | 61.86 | 63.42 | 64.16 | 64.10 | 64.10 |
| Physics | 45.85 | 47.49 | 47.83 | 47.81 | 48.13 |
| **Average** | **54.67** | **56.86** | **57.59** | **57.88** | **58.12** |

#### Recall@10

| Dataset | 64 | 128 | 256 | 512 | 1024 |
|---|---:|---:|---:|---:|---:|
| Computer science | 71.83 | 74.96 | 76.04 | 76.03 | 76.31 |
| Energy | 71.24 | 72.60 | 73.27 | 73.72 | 74.37 |
| Finance (English) | 62.20 | 64.93 | 65.63 | 66.03 | 65.96 |
| Finance (French) | 49.20 | 51.28 | 52.20 | 52.96 | 53.21 |
| Human resources | 59.57 | 61.69 | 62.54 | 62.41 | 63.02 |
| Industrial | 46.62 | 49.47 | 49.96 | 50.42 | 50.48 |
| Pharmaceuticals | 65.77 | 67.24 | 67.74 | 67.76 | 67.48 |
| Physics | 47.76 | 50.19 | 50.68 | 50.73 | 50.98 |
| **Average** | **59.27** | **61.55** | **62.26** | **62.51** | **62.73** |

### Pooling performance

Each figure shows image and Markdown retrieval side by side at the full MRL width
of 1024 dimensions. Scores are percentages, averaged equally across the eight datasets
for each task. Solid blue lines with circles show native queries; dashed amber lines
with squares show crosslingual queries. Pooling factors use a base-2 logarithmic axis;
1× is the unpooled baseline. Both panels share the same score scale.

Document vectors are pooled at full width using Ward linkage on cosine distances, then
L2-normalized without prefix truncation. Pooling factors 2×, 4×, and 8× reduce each
document to approximately one-half, one-quarter, and one-eighth as many vectors.
Queries are not pooled. Vector storage remains FP16; scoring and the pre-export
evaluation settings are the same as above.

#### nDCG@10

![Average nDCG@10 versus pooling factor at the full 1024-dimensional width, with image and Markdown panels for native and crosslingual queries.](pooling-ndcg.png)

#### Recall@10

![Average Recall@10 versus pooling factor at the full 1024-dimensional width, with image and Markdown panels for native and crosslingual queries.](pooling-recall.png)