---
language:
  - multilingual
  - fr
  - en
  - de
  - es
  - it
  - pt
  - zh
  - ja
  - ko
tags:
  - sentence-transformers
  - onnx
  - int8
  - matryoshka
  - embedding
  - bge-m3
  - multilingual
  - cross-lingual
  - rag
license: mit
base_model: tss-deposium/bge-m3-matryoshka-1024d
pipeline_tag: sentence-similarity
library_name: onnxruntime
---

# BGE-M3 Matryoshka — ONNX INT8

ONNX INT8 dynamically-quantized version of [tss-deposium/bge-m3-matryoshka-1024d](https://huggingface.co/tss-deposium/bge-m3-matryoshka-1024d) for **CPU-optimized inference**.

Fine-tuned from [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3) with **MatryoshkaLoss** — supports dynamic dimension truncation at query time (1024 -> 768 -> 512 -> 256) via simple array slicing, with a single model loaded in memory (~571 MB).

## Key Features

- **Dynamic dimensions**: Truncate embeddings to 1024/768/512/256D at inference time — zero overhead
- **ONNX INT8**: CPU-optimized, no GPU required (~571 MB RAM)
- **Matryoshka-trained**: Quality degrades gracefully at lower dimensions (not random truncation)
- **Cross-lingual**: FR/EN/DE/ES/IT/PT/ZH/JA/KO — inherited from BGE-M3
- **Drop-in replacement**: Same 1024D output as `gpahal/bge-m3-onnx-int8`, with better discrimination (+6.6%)

## Benchmark Results

Tested on 4 semantic pairs (FR/EN cross-lingual) + 2 negative pairs.
**Discrimination** = avg_positive_similarity - avg_negative_similarity (higher = better separation).

| Model | Dim | AvgPair | AvgNeg | Discrim | Throughput | Notes |
|-------|-----|---------|--------|---------|------------|-------|
| m2v-bge-m3-1024d | 1024 | 0.470 | 0.159 | 0.312 | **581 t/s** | GPU, 20x faster but weaker cross-lingual |
| gpahal/bge-m3-onnx-int8 | 1024 | 0.695 | 0.317 | 0.377 | 28 t/s | CPU baseline |
| **This model** | **1024** | **0.698** | **0.295** | **0.403** | 29 t/s | **Best discrimination (+6.6% vs baseline)** |
| This model @768D | 768 | 0.711 | 0.315 | 0.397 | 29 t/s | -1.4% discrim, -25% storage |
| This model @512D | 512 | 0.729 | 0.348 | 0.381 | 29 t/s | -5.4% discrim, -50% storage |
| This model @256D | 256 | 0.658 | 0.200 | 0.458* | 25 t/s | *Anomalous — loses cross-lingual |

### Per-Pair Breakdown (Cosine Similarity)

| Pair | m2v-1024 | onnx-1024 | matr-1024 | matr-768 | matr-512 | matr-256 |
|------|----------|-----------|-----------|----------|----------|----------|
| couple_serrage (FR/EN) | 0.056 | 0.351 | 0.284 | 0.321 | 0.371 | 0.197 |
| fogg_depart (FR/FR) | 0.634 | 0.837 | 0.866 | 0.873 | 0.878 | 0.825 |
| revenue_q2 (EN/FR) | 0.391 | 0.645 | 0.686 | 0.697 | 0.711 | 0.658 |
| moteur_spec (FR/EN) | 0.801 | 0.946 | 0.954 | 0.954 | 0.955 | 0.950 |

### Dimension Recommendations

| Dimension | vs M2V baseline | vs bge-m3-onnx-1024D | Storage (1M vectors) | Recommendation |
|-----------|----------------|----------------------|---------------------|----------------|
| 1024D | +29.2% | +6.6% | 4 GB | Maximum quality |
| 768D | +27.2% | +5.3% | 3 GB | Safe, -25% storage |
| **512D** | **+22.1%** | **+1.1%** | **2 GB** | **Best for cloud CPU scaling** |
| 256D | anomalous | anomalous | 1 GB | Not recommended (loses cross-lingual) |

**512D Matryoshka is BETTER than full-resolution bge-m3-onnx-int8 at 1024D** (+1.1% discrimination) with **half the storage and 2x faster cosine similarity**.

## Usage

### With ONNX Runtime (Python)

```python
from onnxruntime import InferenceSession
from transformers import AutoTokenizer
import numpy as np

tokenizer = AutoTokenizer.from_pretrained("tss-deposium/bge-m3-matryoshka-1024d-onnx-int8")
session = InferenceSession("model_quantized.onnx")

inputs = tokenizer("Bonjour le monde", return_tensors="np", padding=True, truncation=True)
outputs = session.run(None, dict(inputs))
embedding_1024d = outputs[0][0]  # [1024] float32

# Matryoshka truncation — just slice!
embedding_768d = embedding_1024d[:768]
embedding_512d = embedding_1024d[:512]
embedding_256d = embedding_1024d[:256]
```

### With Deposium TurboV2 API

```bash
# Full 1024D (default)
curl -X POST http://localhost:11435/api/embed \
  -d '{"model": "bge-m3-matryoshka", "input": "Bonjour le monde"}'

# Truncated to 512D (50% less storage, ~95% quality)
curl -X POST http://localhost:11435/api/embed \
  -d '{"model": "bge-m3-matryoshka", "input": "Bonjour", "dimensions": 512}'
```

## Training Details

- **Base model**: [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3) (XLM-RoBERTa, 0.6B params)
- **Fine-tuning**: MatryoshkaLoss + MultipleNegativesRankingLoss
- **Matryoshka dims**: [1024, 768, 512, 256]
- **Dataset**: 672,676 training samples / 35,405 eval samples
- **Epochs**: 3, batch size 32, lr 2e-5, bf16
- **ONNX export**: Dynamic INT8 quantization (avx512_vnni)
- **Size**: ~571 MB (vs ~2.2 GB FP32)

## Files

| File | Description |
|------|-------------|
| `model_quantized.onnx` | ONNX INT8 quantized model |
| `config.json` | Model configuration |
| `ort_config.json` | ONNX Runtime configuration |
| `tokenizer.json` | Fast tokenizer |
| `tokenizer_config.json` | Tokenizer configuration |
| `sentencepiece.bpe.model` | SentencePiece BPE model |
| `special_tokens_map.json` | Special tokens mapping |

## License

MIT — commercial use allowed.
