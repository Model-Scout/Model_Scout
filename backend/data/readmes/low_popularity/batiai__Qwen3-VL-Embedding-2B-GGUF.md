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
base_model: Qwen/Qwen3-VL-Embedding-2B
pipeline_tag: sentence-similarity
library_name: llama.cpp
---

# Qwen3-VL-Embedding-2B GGUF — Quantized by BatiAI

<p align="center">
  <a href="https://flow.bati.ai"><img src="https://img.shields.io/badge/BatiFlow-RAG%20on%20Mac-blue?style=for-the-badge&logo=apple" alt="BatiFlow"></a>
  <a href="https://huggingface.co/Qwen/Qwen3-VL-Embedding-2B"><img src="https://img.shields.io/badge/Upstream-Qwen3--VL--Embedding--2B-orange?style=for-the-badge" alt="Upstream"></a>
</p>

> GGUF quantizations of **Qwen/Qwen3-VL-Embedding-2B** — the most-downloaded vision-language embedding model of 2026 (1.64 M downloads on HF).
> Part of BatiAI's on-device RAG stack for [BatiFlow](https://flow.bati.ai).

## What does it do?

**VL (Vision-Language) embedding** turns either text OR images into dense vectors. Same embedding space means:

- **Search photos by text** — "beach sunset" retrieves matching photos without manual tagging
- **Search text by image** — drop a screenshot, find similar notes
- **Cross-modal RAG** — index PDFs, notes, and images together in one vector DB

## Quick Start

### Text embedding (llama.cpp, via Ollama)

```bash
ollama pull batiai/qwen3-vl-embed-2b:q8

curl http://localhost:11434/api/embeddings -d '{
  "model": "batiai/qwen3-vl-embed-2b:q8",
  "prompt": "What is the capital of France?"
}'
```

### Image embedding

Image embedding requires llama.cpp's `mtmd` (multimodal) build. See [Qwen3-VL docs](https://huggingface.co/Qwen/Qwen3-VL-Embedding-2B) for batch image encoding.

## Available Quantizations

| File | Quant | Size | Recommended |
|------|-------|------|-------------|
| `Qwen3-VL-Embedding-2B-Q6_K.gguf` | Q6_K | ~**1.5 GB** | balanced (recommended default) |
| `Qwen3-VL-Embedding-2B-Q8_0.gguf` | Q8_0 | ~**1.8 GB** | near-lossless embeddings |

Embedding models are sensitive to low-bit quantization (vector quality drops). Q6_K minimum.

## Quality note

Direct embedding-quality eval (e.g. MTEB retrieval) is more involved than rerank pairwise testing and takes longer to run locally. Our sibling [reranker card](https://huggingface.co/batiai/Qwen3-Reranker-0.6B-GGUF) shows that **Q6_K ↔ Q8_0 drift is negligible (Pearson r = 0.998 on 40 pairs)** for the same model family — we expect the embedding model to behave similarly. MTEB/BEIR numbers will be added as measured.

## Why Qwen3-VL-Embedding?

- **SOTA on MTEB** — top multilingual embedding model across text + image
- **Multilingual** — en / ko / ja / zh
- **Multimodal** — text and image in the same embedding space
- **2048-dim vectors** — balance between expressiveness and storage

## Why BatiAI?

- Quantized **directly from Alibaba's BF16 safetensors**
- **BatiAI-signed** metadata
- Part of a **full on-device RAG stack**

## Technical Details

- **Original Model**: [Qwen/Qwen3-VL-Embedding-2B](https://huggingface.co/Qwen/Qwen3-VL-Embedding-2B)
- **Architecture**: Qwen3-VL with pooling head
- **Parameters**: 2 B (text tower) + vision tower
- **Embedding dim**: 2048
- **Max context**: 32 K (text)
- **License**: Apache 2.0
- **Quantized with**: [llama.cpp](https://github.com/ggml-org/llama.cpp)

## BatiAI's RAG Stack

| Role | Model | HF |
|------|-------|----|
| **VL Embedding (2 B)** | Qwen3-VL-Embedding-2B | **this repo** |
| Reranker (0.6 B) | Qwen3-Reranker-0.6B | [batiai/Qwen3-Reranker-0.6B-GGUF](https://huggingface.co/batiai/Qwen3-Reranker-0.6B-GGUF) |
| Reranker (4 B) | Qwen3-Reranker-4B | [batiai/Qwen3-Reranker-4B-GGUF](https://huggingface.co/batiai/Qwen3-Reranker-4B-GGUF) |
| Chat LLM (35 B-A3B) | Qwen3.6-35B-A3B | [batiai/Qwen3.6-35B-A3B-GGUF](https://huggingface.co/batiai/Qwen3.6-35B-A3B-GGUF) |

## License

Mirrors upstream Qwen Apache 2.0. Commercial use permitted.
