---
language:
  - en
  - ko
  - ja
  - zh
license: apache-2.0
tags:
  - gguf
  - qwen
  - qwen3
  - embedding
  - sentence-similarity
  - multimodal
  - vl
  - rag
  - quantized
  - batiai
  - on-device
base_model: Qwen/Qwen3-VL-Embedding-8B
pipeline_tag: sentence-similarity
library_name: llama.cpp
---

# Qwen3-VL-Embedding-8B GGUF — Quantized by BatiAI

<p align="center">
  <a href="https://flow.bati.ai"><img src="https://img.shields.io/badge/BatiFlow-RAG%20on%20Mac-blue?style=for-the-badge&logo=apple" alt="BatiFlow"></a>
  <a href="https://huggingface.co/Qwen/Qwen3-VL-Embedding-8B"><img src="https://img.shields.io/badge/Upstream-Qwen3--VL--Embedding--8B-orange?style=for-the-badge" alt="Upstream"></a>
</p>

> GGUF quantizations of **Qwen/Qwen3-VL-Embedding-8B** — the quality tier of Qwen3's vision-language embedding family.
> Part of BatiAI's on-device RAG stack for [BatiFlow](https://flow.bati.ai).

## When to pick 8B over 2B?

| Use case | Pick |
|----------|------|
| Workstation / desktop Mac, retrieval quality matters | **8B** — richer embeddings, better semantic separation |
| Laptop / Mac mini / latency matters | 2B — 4× smaller, sufficient for most tasks |

## What does it do?

**VL (Vision-Language) embedding** turns either text OR images into dense vectors in the same embedding space. This enables:

- **Search photos by text** — "beach sunset" retrieves matching photos without manual tagging
- **Search text by image** — drop a screenshot, find similar notes
- **Cross-modal RAG** — index PDFs, notes, and images together in one vector DB

## Quick Start

### Text embedding (Ollama)

```bash
ollama pull batiai/qwen3-vl-embed-8b:q8

curl http://localhost:11434/api/embeddings -d '{
  "model": "batiai/qwen3-vl-embed-8b:q8",
  "prompt": "What is the capital of France?"
}'
```

Returns a 3584-dim float vector (8B model uses wider embedding than 2B's 2048).

### Image embedding

Image support requires llama.cpp's `mtmd` multimodal build. See upstream docs.

## Available Quantizations

| File | Quant | Size | Recommended |
|------|-------|------|-------------|
| `Qwen3-VL-Embedding-8B-Q6_K.gguf` | Q6_K | **5.8 GB** | balanced |
| `Qwen3-VL-Embedding-8B-Q8_0.gguf` | Q8_0 | **7.5 GB** | near-lossless, best for retrieval quality |

Embedding models are sensitive to low-bit quantization (vector quality drops). Q6_K minimum.

## Quality note

Direct embedding-quality evaluation (e.g. MTEB retrieval) is more involved than pairwise reranker testing and takes longer to run locally — it will be added as measured. In the meantime, our sibling [Qwen3-Reranker-8B](https://huggingface.co/batiai/Qwen3-Reranker-8B-GGUF) card shows **Q6_K ↔ Q8_0 Pearson correlation r = 0.9986** on 40 hard-negative triples. Same architecture family, same quantization approach — we expect this embedding model to behave similarly (quantization drift under noise floor).

## Why Qwen3-VL-Embedding?

- **SOTA on MTEB** — top multilingual embedding model
- **Multilingual** — en / ko / ja / zh
- **Multimodal** — text and image in the same embedding space

## Why BatiAI?

- Quantized **directly from Alibaba's BF16 safetensors**
- **BatiAI-signed** metadata
- Part of a **full on-device RAG stack**

## Technical Details

- **Original Model**: [Qwen/Qwen3-VL-Embedding-8B](https://huggingface.co/Qwen/Qwen3-VL-Embedding-8B)
- **Architecture**: Qwen3-VL with pooling head
- **Parameters**: 8 B (text tower) + vision tower
- **License**: Apache 2.0

## BatiAI's RAG Stack

| Role | Model | HF |
|------|-------|----|
| VL Embedding (2 B) | Qwen3-VL-Embedding-2B | [batiai/Qwen3-VL-Embedding-2B-GGUF](https://huggingface.co/batiai/Qwen3-VL-Embedding-2B-GGUF) |
| **VL Embedding (8 B)** | **Qwen3-VL-Embedding-8B** | **this repo** |
| Reranker (0.6 B) | Qwen3-Reranker-0.6B | [batiai/Qwen3-Reranker-0.6B-GGUF](https://huggingface.co/batiai/Qwen3-Reranker-0.6B-GGUF) |
| Reranker (4 B) | Qwen3-Reranker-4B | [batiai/Qwen3-Reranker-4B-GGUF](https://huggingface.co/batiai/Qwen3-Reranker-4B-GGUF) |
| Reranker (8 B) | Qwen3-Reranker-8B | [batiai/Qwen3-Reranker-8B-GGUF](https://huggingface.co/batiai/Qwen3-Reranker-8B-GGUF) |
| Chat LLM (35 B-A3B) | Qwen3.6-35B-A3B | [batiai/Qwen3.6-35B-A3B-GGUF](https://huggingface.co/batiai/Qwen3.6-35B-A3B-GGUF) |

## License

Mirrors upstream Qwen Apache 2.0. Commercial use permitted.
