---
language: ["ko", "en", "ja", "zh", "es", "fr", "de", "pt", "it", "ru", "ar", "hi", "th", "vi", "id", "pl"]
tags:
- sentence-transformers
- multilingual
- model-compression
- layer-pruning
- vocab-pruning
- knowledge-distillation
- me5-small
library_name: sentence-transformers
pipeline_tag: sentence-similarity
license: apache-2.0
---

# me5s_compressed_v4_distilled (Distilled)

Compact multilingual sentence encoder compressed from `intfloat/multilingual-e5-small` (8x compression).

## Model Details

| Property | Value |
|---|---|
| Base model | `intfloat/multilingual-e5-small` |
| Architecture | bert (encoder) |
| Hidden dim | 384 (from 384) |
| Layers | 4 (from 12) |
| Intermediate | 1536 |
| Attention heads | 12 |
| Vocab size | 21,028 (from 250,037) |
| Parameters | ~15.4M |
| Model size (FP32) | 59.2MB |
| Compression | 8x |
| Distilled | Yes |

## Quick Start

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("me5s_compressed_v4_distilled", trust_remote_code=True)

sentences = [
    "Hello, how are you?",
    "안녕하세요, 잘 지내세요?",
    "こんにちは、元気ですか？",
    "你好，你好吗？",
]

embeddings = model.encode(sentences)
print(embeddings.shape)  # (4, 384)
```

## MTEB Evaluation Results

**Overall Average: 53.98%**

| Task Group | Average |
|---|---|
| Classification | 57.84% |
| Clustering | 30.54% |
| STS | 69.64% |

### Classification

| Task | Average | Details |
|---|---|---|
| AmazonCounterfactualClassification | 68.58% | de: 72.39%, en-ext: 71.31%, en: 70.72%, ja: 59.9% |
| Banking77Classification | 66.48% | default: 66.48% |
| ImdbClassification | 60.45% | default: 60.45% |
| MTOPDomainClassification | 81.11% | en: 86.31%, es: 83.43%, hi: 80.55%, th: 79.82%, de: 78.84% |
| MassiveIntentClassification | 32.44% | en: 60.21%, ja: 56.1%, zh-CN: 55.79%, pt: 54.51%, it: 53.26% |
| MassiveScenarioClassification | 39.97% | en: 66.62%, zh-CN: 64.52%, ja: 63.65%, ko: 61.75%, de: 61.51% |
| ToxicConversationsClassification | 54.38% | default: 54.38% |
| TweetSentimentExtractionClassification | 59.34% | default: 59.34% |

### Clustering

| Task | Average | Details |
|---|---|---|
| ArXivHierarchicalClusteringP2P | 46.97% | default: 46.97% |
| ArXivHierarchicalClusteringS2S | 45.12% | default: 45.12% |
| BiorxivClusteringP2P.v2 | 19.34% | default: 19.34% |
| MedrxivClusteringP2P.v2 | 24.71% | default: 24.71% |
| MedrxivClusteringS2S.v2 | 21.49% | default: 21.49% |
| StackExchangeClustering.v2 | 39.62% | default: 39.62% |
| StackExchangeClusteringP2P.v2 | 32.24% | default: 32.24% |
| TwentyNewsgroupsClustering.v2 | 14.83% | default: 14.83% |

### STS

| Task | Average | Details |
|---|---|---|
| BIOSSES | 71.48% | default: 71.48% |
| SICK-R | 74.06% | default: 74.06% |
| STS12 | 73.67% | default: 73.67% |
| STS13 | 72.82% | default: 72.82% |
| STS14 | 72.9% | default: 72.9% |
| STS15 | 81.85% | default: 81.85% |
| STS17 | 57.66% | en-en: 83.69%, es-es: 80.8%, ko-ko: 70.95%, ar-ar: 66.44%, es-en: 61.8% |
| STS22.v2 | 46.75% | fr: 68.67%, es: 64.85%, es-en: 62.91%, en: 62.07%, zh: 61.11% |
| STSBenchmark | 77.12% | default: 77.12% |
| STSBenchmarkMultilingualSTS | 68.06% | en: 77.12%, fr: 72.88%, es: 72.67%, pt: 69.94%, it: 68.6% |



## Training

### Stage 1: Model Compression
- **Teacher**: `intfloat/multilingual-e5-small` (12L, 384d)
- **Compression**: Layer pruning + Vocab pruning
- **Result**: 4L / 384d / 21,028 vocab

### Stage 2: Knowledge Distillation
- **Method**: MSE + Cosine Similarity loss
- **Data**: MTEB Classification/Clustering/STS task datasets
- **Optimizer**: AdamW (lr=2e-5, weight_decay=0.01)
- **Schedule**: Cosine annealing over 3 epochs


## Supported Languages (16)

ko, en, ja, zh, es, fr, de, pt, it, ru, ar, hi, th, vi, id, pl
