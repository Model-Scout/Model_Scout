---
license: apache-2.0
base_model: Qwen/Qwen3.5-2B
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

# topk-embed-v1-small

**topk-embed-v1-small** is a 2B **multimodal late-interaction retriever**.
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
    "topk-io/topk-embed-v1-small",
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
Embeddings have 2048 dimensions. For smaller Matryoshka (MRL) embeddings, pass
`config_kwargs={"output_dim": 256}` when loading the model.

## Evaluation

Results on the eight public ViDoRe v3 test datasets, reported as percentages (higher is better).
Columns are Matryoshka (MRL) prefix dimensions; 2048 is the full embedding width.
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

| Dataset | 64 | 128 | 256 | 512 | 1024 | 2048 |
|---|---:|---:|---:|---:|---:|---:|
| Computer science | 77.91 | 78.89 | 79.58 | 79.62 | 79.93 | 80.27 |
| Energy | 69.77 | 70.65 | 70.55 | 70.57 | 71.06 | 71.13 |
| Finance (English) | 70.55 | 71.25 | 71.23 | 71.32 | 71.59 | 71.27 |
| Finance (French) | 50.65 | 51.40 | 51.93 | 52.30 | 52.47 | 52.47 |
| Human resources | 65.97 | 66.69 | 67.21 | 67.33 | 67.88 | 67.38 |
| Industrial | 56.57 | 57.78 | 57.77 | 57.69 | 58.16 | 58.05 |
| Pharmaceuticals | 68.76 | 69.65 | 70.11 | 69.95 | 70.03 | 69.99 |
| Physics | 49.71 | 50.83 | 50.88 | 51.08 | 51.34 | 51.20 |
| **Average** | **63.74** | **64.64** | **64.91** | **64.98** | **65.31** | **65.22** |

#### Recall@10

| Dataset | 64 | 128 | 256 | 512 | 1024 | 2048 |
|---|---:|---:|---:|---:|---:|---:|
| Computer science | 80.33 | 80.87 | 81.24 | 81.17 | 81.72 | 82.38 |
| Energy | 75.86 | 76.98 | 76.77 | 76.74 | 77.09 | 77.41 |
| Finance (English) | 73.68 | 74.40 | 74.84 | 75.00 | 75.68 | 74.88 |
| Finance (French) | 58.58 | 59.20 | 59.65 | 60.28 | 60.25 | 60.30 |
| Human resources | 70.15 | 70.29 | 71.27 | 71.38 | 71.83 | 71.27 |
| Industrial | 58.10 | 59.39 | 59.36 | 59.87 | 60.24 | 60.44 |
| Pharmaceuticals | 70.47 | 72.09 | 72.52 | 72.31 | 72.67 | 72.56 |
| Physics | 53.45 | 54.26 | 54.73 | 54.61 | 54.81 | 54.88 |
| **Average** | **67.58** | **68.44** | **68.80** | **68.92** | **69.29** | **69.26** |

### Vidore V3 (image, crosslingual)

#### nDCG@10

| Dataset | 64 | 128 | 256 | 512 | 1024 | 2048 |
|---|---:|---:|---:|---:|---:|---:|
| Computer science | 75.40 | 77.35 | 78.25 | 78.77 | 78.78 | 78.95 |
| Energy | 67.31 | 68.26 | 68.97 | 69.01 | 69.08 | 69.40 |
| Finance (English) | 63.42 | 65.96 | 66.95 | 67.14 | 67.44 | 67.40 |
| Finance (French) | 47.78 | 49.27 | 50.09 | 50.54 | 50.71 | 50.71 |
| Human resources | 62.12 | 63.91 | 64.54 | 64.83 | 64.92 | 64.86 |
| Industrial | 50.14 | 52.92 | 53.92 | 54.39 | 54.40 | 54.38 |
| Pharmaceuticals | 66.83 | 67.97 | 68.44 | 68.61 | 68.82 | 68.89 |
| Physics | 48.32 | 49.76 | 50.04 | 50.47 | 50.56 | 50.76 |
| **Average** | **60.16** | **61.92** | **62.65** | **62.97** | **63.09** | **63.17** |

#### Recall@10

| Dataset | 64 | 128 | 256 | 512 | 1024 | 2048 |
|---|---:|---:|---:|---:|---:|---:|
| Computer science | 77.87 | 79.95 | 80.27 | 80.85 | 80.86 | 81.25 |
| Energy | 74.31 | 75.39 | 76.03 | 76.09 | 76.17 | 76.60 |
| Finance (English) | 67.63 | 70.04 | 71.02 | 71.22 | 71.56 | 71.61 |
| Finance (French) | 56.34 | 57.64 | 58.35 | 59.08 | 59.10 | 59.07 |
| Human resources | 66.65 | 67.94 | 68.47 | 68.77 | 68.96 | 68.62 |
| Industrial | 52.98 | 55.55 | 56.66 | 57.24 | 57.41 | 57.28 |
| Pharmaceuticals | 68.81 | 70.04 | 70.49 | 70.88 | 71.19 | 71.10 |
| Physics | 52.29 | 53.51 | 53.95 | 54.08 | 54.12 | 54.14 |
| **Average** | **64.61** | **66.26** | **66.91** | **67.28** | **67.42** | **67.46** |

### Vidore V3 (markdown, native)

#### nDCG@10

| Dataset | 64 | 128 | 256 | 512 | 1024 | 2048 |
|---|---:|---:|---:|---:|---:|---:|
| Computer science | 74.75 | 76.06 | 76.22 | 77.06 | 77.16 | 77.41 |
| Energy | 66.19 | 67.06 | 67.53 | 67.89 | 68.27 | 68.24 |
| Finance (English) | 68.09 | 69.12 | 69.80 | 69.70 | 70.03 | 69.94 |
| Finance (French) | 48.39 | 49.63 | 50.28 | 50.92 | 50.78 | 50.66 |
| Human resources | 61.74 | 62.70 | 63.31 | 63.44 | 64.24 | 63.72 |
| Industrial | 53.27 | 54.32 | 54.53 | 55.21 | 55.18 | 54.98 |
| Pharmaceuticals | 66.79 | 67.76 | 67.82 | 68.16 | 68.40 | 68.29 |
| Physics | 47.19 | 48.05 | 49.38 | 49.17 | 49.20 | 49.13 |
| **Average** | **60.80** | **61.84** | **62.36** | **62.69** | **62.91** | **62.80** |

#### Recall@10

| Dataset | 64 | 128 | 256 | 512 | 1024 | 2048 |
|---|---:|---:|---:|---:|---:|---:|
| Computer science | 76.16 | 77.85 | 78.72 | 79.53 | 79.66 | 79.77 |
| Energy | 74.52 | 74.19 | 75.11 | 74.82 | 75.37 | 75.44 |
| Finance (English) | 72.32 | 73.30 | 73.17 | 73.37 | 73.50 | 73.79 |
| Finance (French) | 56.00 | 58.06 | 58.87 | 59.88 | 59.30 | 58.51 |
| Human resources | 66.62 | 67.19 | 67.83 | 68.01 | 68.98 | 68.05 |
| Industrial | 55.93 | 56.72 | 56.84 | 57.36 | 57.29 | 57.21 |
| Pharmaceuticals | 69.12 | 69.90 | 70.16 | 70.62 | 70.39 | 70.28 |
| Physics | 51.17 | 51.74 | 52.99 | 52.98 | 52.67 | 52.95 |
| **Average** | **65.23** | **66.12** | **66.71** | **67.07** | **67.15** | **67.00** |

### Vidore V3 (markdown, crosslingual)

#### nDCG@10

| Dataset | 64 | 128 | 256 | 512 | 1024 | 2048 |
|---|---:|---:|---:|---:|---:|---:|
| Computer science | 72.70 | 74.57 | 75.49 | 76.14 | 76.21 | 76.29 |
| Energy | 64.48 | 65.89 | 66.40 | 66.94 | 67.11 | 67.31 |
| Finance (English) | 61.21 | 63.56 | 64.68 | 64.64 | 64.98 | 65.04 |
| Finance (French) | 45.42 | 47.40 | 47.99 | 48.58 | 48.90 | 48.82 |
| Human resources | 57.30 | 58.97 | 60.04 | 59.86 | 60.28 | 60.17 |
| Industrial | 45.21 | 48.19 | 49.80 | 50.58 | 50.56 | 50.52 |
| Pharmaceuticals | 64.67 | 66.43 | 66.80 | 66.77 | 67.13 | 67.07 |
| Physics | 46.88 | 48.33 | 48.63 | 48.68 | 48.65 | 48.68 |
| **Average** | **57.23** | **59.17** | **59.98** | **60.27** | **60.48** | **60.49** |

#### Recall@10

| Dataset | 64 | 128 | 256 | 512 | 1024 | 2048 |
|---|---:|---:|---:|---:|---:|---:|
| Computer science | 74.71 | 76.95 | 78.16 | 78.99 | 79.03 | 79.01 |
| Energy | 73.19 | 74.06 | 74.41 | 74.69 | 74.91 | 75.17 |
| Finance (English) | 66.05 | 68.23 | 69.57 | 69.46 | 69.64 | 69.98 |
| Finance (French) | 53.39 | 56.04 | 56.30 | 56.95 | 57.09 | 56.96 |
| Human resources | 61.53 | 62.85 | 63.82 | 63.83 | 64.26 | 63.99 |
| Industrial | 48.55 | 51.84 | 53.26 | 54.43 | 54.25 | 54.05 |
| Pharmaceuticals | 66.85 | 68.40 | 68.94 | 69.30 | 69.43 | 69.28 |
| Physics | 50.36 | 51.26 | 51.78 | 52.08 | 52.00 | 52.16 |
| **Average** | **61.83** | **63.70** | **64.53** | **64.97** | **65.08** | **65.08** |

### Pooling performance

Each figure shows image and Markdown retrieval side by side at the full MRL width
of 2048 dimensions. Scores are percentages, averaged equally across the eight datasets
for each task. Solid blue lines with circles show native queries; dashed amber lines
with squares show crosslingual queries. Pooling factors use a base-2 logarithmic axis;
1× is the unpooled baseline. Both panels share the same score scale.

Document vectors are pooled at full width using Ward linkage on cosine distances, then
L2-normalized without prefix truncation. Pooling factors 2×, 4×, and 8× reduce each
document to approximately one-half, one-quarter, and one-eighth as many vectors.
Queries are not pooled. Vector storage remains FP16; scoring and the pre-export
evaluation settings are the same as above.

#### nDCG@10

![Average nDCG@10 versus pooling factor at the full 2048-dimensional width, with image and Markdown panels for native and crosslingual queries.](pooling-ndcg.png)

#### Recall@10

![Average Recall@10 versus pooling factor at the full 2048-dimensional width, with image and Markdown panels for native and crosslingual queries.](pooling-recall.png)