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

# me5s_compressed_v3_distilled (Distilled)

Compact multilingual sentence encoder compressed from `intfloat/multilingual-e5-small` (9x compression).

## Model Details

| Property | Value |
|---|---|
| Base model | `intfloat/multilingual-e5-small` |
| Architecture | bert (encoder) |
| Hidden dim | 384 (from 384) |
| Layers | 4 (from 12) |
| Intermediate | 1536 |
| Attention heads | 12 |
| Vocab size | 15,424 (from 250,037) |
| Parameters | ~13.2M |
| Model size (FP32) | 51.0MB |
| Compression | 9x |
| Distilled | Yes |

## Quick Start

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("me5s_compressed_v3_distilled", trust_remote_code=True)

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

**Overall Average: 54.35%**

| Task Group | Average |
|---|---|
| Classification | 58.21% |
| Clustering | 30.92% |
| STS | 70.01% |

### Classification

| Task | Average | Details |
|---|---|---|
| AmazonCounterfactualClassification | 68.96% | de: 72.24%, en-ext: 71.78%, en: 70.88%, ja: 60.94% |
| Banking77Classification | 67.0% | default: 67.0% |
| ImdbClassification | 60.0% | default: 60.0% |
| MTOPDomainClassification | 81.87% | en: 86.66%, es: 84.13%, hi: 81.63%, th: 80.64%, de: 79.96% |
| MassiveIntentClassification | 33.14% | en: 60.73%, ja: 56.7%, zh-CN: 55.96%, pt: 55.5%, it: 54.43% |
| MassiveScenarioClassification | 40.53% | en: 67.02%, zh-CN: 65.25%, ja: 64.48%, de: 62.75%, ko: 62.43% |
| ToxicConversationsClassification | 54.24% | default: 54.24% |
| TweetSentimentExtractionClassification | 59.93% | default: 59.93% |

### Clustering

| Task | Average | Details |
|---|---|---|
| ArXivHierarchicalClusteringP2P | 49.09% | default: 49.09% |
| ArXivHierarchicalClusteringS2S | 45.73% | default: 45.73% |
| BiorxivClusteringP2P.v2 | 19.77% | default: 19.77% |
| MedrxivClusteringP2P.v2 | 24.87% | default: 24.87% |
| MedrxivClusteringS2S.v2 | 21.53% | default: 21.53% |
| StackExchangeClustering.v2 | 39.58% | default: 39.58% |
| StackExchangeClusteringP2P.v2 | 31.91% | default: 31.91% |
| TwentyNewsgroupsClustering.v2 | 14.86% | default: 14.86% |

### STS

| Task | Average | Details |
|---|---|---|
| BIOSSES | 72.19% | default: 72.19% |
| SICK-R | 74.61% | default: 74.61% |
| STS12 | 73.56% | default: 73.56% |
| STS13 | 73.22% | default: 73.22% |
| STS14 | 73.27% | default: 73.27% |
| STS15 | 82.2% | default: 82.2% |
| STS17 | 58.93% | en-en: 84.37%, es-es: 79.99%, ko-ko: 71.8%, ar-ar: 67.21%, fr-en: 64.15% |
| STS22.v2 | 45.36% | fr: 67.64%, es: 64.13%, es-en: 61.91%, en: 60.63%, it: 60.07% |
| STSBenchmark | 77.67% | default: 77.67% |
| STSBenchmarkMultilingualSTS | 69.05% | en: 77.67%, es: 73.78%, fr: 73.75%, pt: 71.23%, it: 70.45% |



## Training

### Stage 1: Model Compression
- **Teacher**: `intfloat/multilingual-e5-small` (12L, 384d)
- **Compression**: Layer pruning + Vocab pruning
- **Result**: 4L / 384d / 15,424 vocab

### Stage 2: Knowledge Distillation
- **Method**: MSE + Cosine Similarity loss
- **Data**: 19.88M multilingual sentences (MTEB tasks + conversation corpus)
- **Optimizer**: AdamW (lr=2e-5, weight_decay=0.01)
- **Schedule**: Cosine annealing over 13 epochs
- **Batch size**: 512
- **Best loss**: 0.0093

### Key Feature: Byte Fallback Tokenizer
- Unigram tokenizer with `byte_fallback=true`
- 256 UTF-8 byte tokens (`<0x00>`~`<0xFF>`) added to vocab
- Guarantees zero `<unk>` tokens for any Unicode input
- Significantly improves multilingual STS performance (+15%p on STS17 vs non-byte-fallback version)

## UMAP Visualization

16 languages x 50 parallel sentences from MASSIVE dataset. Ideal: same-meaning sentences cluster together across languages.

![UMAP Visualization](umap_me5s_v3.png)

- **Top row** (colored by language): Colors are mixed = language-agnostic semantic space
- **Bottom row** (colored by sentence ID): Tight clusters = parallel sentences cluster across languages

## Supported Languages (16)

ko, en, ja, zh, es, fr, de, pt, it, ru, ar, hi, th, vi, id, pl
