---
license: openmdw-1.1
base_model: nvidia/Nemotron-3-Embed-1B-BF16
base_model_relation: quantized
library_name: gguf
pipeline_tag: sentence-similarity
tags:
  - gguf
  - text-embeddings
  - feature-extraction
  - retrieval
  - semantic-search
  - rag
  - llama-cpp
  - ollama
language:
  - multilingual
  - en
  - ar
  - as
  - bn
  - bg
  - zh
  - da
  - nl
  - fi
  - fr
  - de
  - hi
  - id
  - it
  - ja
  - ko
  - ms
  - mr
  - ne
  - "no"
  - fa
  - pt
  - ro
  - ru
  - es
  - sw
  - sv
  - ta
  - te
  - th
  - uk
  - ur
  - vi
---

# Nemotron-3-Embed-1B GGUF

GGUF conversions of NVIDIA [Nemotron-3-Embed-1B-BF16](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16), a multilingual text embedding model optimized for retrieval and semantic similarity, prepared for local inference with llama.cpp-compatible runtimes and Ollama.

The model produces 2,048-dimensional, L2-normalized embeddings via mean pooling. It is a Ministral-3-based pruned encoder (16 layers, 1.14B parameters) trained by NVIDIA and evaluated across 34 languages.

## Quantizations

| File | Quantization | Size | SHA-256 |
|---|---:|---:|---|
| `nemotron-3-embed-1b-f16.gguf` | F16 | 2,289,841,280 bytes | `b808437186a493f6c89af374cc7094e64275e4559746e8dbe7d64f8c974c0d85` |
| `nemotron-3-embed-1b-q8_0.gguf` | Q8_0 | 1,220,293,760 bytes | `58e41095862c50bc084bb8afa9b00e586733faaef2627d88c3e04da80d8d8e92` |
| `nemotron-3-embed-1b-q4_k_m.gguf` | Q4_K_M | 749,352,064 bytes | `3d112b61858b5671bde9dfc190f9577fa7ad1818a8a0c201bc74ed10b4f238a4` |

All quantizations share the same embedding space as the BF16 original. Q8_0 is the recommended default for retrieval quality with a small memory footprint; F16 is the highest-fidelity GGUF option; Q4_K_M is the smallest option for memory-constrained hosts.

## Usage with Ollama

Create a model from the GGUF file of your choice:

```bash
ollama create nemotron-3-embed-1b -f Modelfile
```

With a `Modelfile` such as:

```
FROM ./nemotron-3-embed-1b-q8_0.gguf
PARAMETER NUM_CTX 4096
```

Then embed text:

```bash
curl http://localhost:11434/api/embed \
  -d '{"model": "nemotron-3-embed-1b", "input": ["query: What is retrieval-augmented generation?", "passage: Retrieval-augmented generation adds retrieved documents to a model prompt."]}'
```

## Usage with llama.cpp

```bash
llama-server -m nemotron-3-embed-1b-q8_0.gguf --pooling mean --ctx-size 4096
curl http://localhost:8080/v1/embeddings \
  -H 'Content-Type: application/json' \
  -d '{"model": "nemotron-3-embed-1b", "input": ["text to embed"]}'
```

## Conversion details

- Source: `nvidia/Nemotron-3-Embed-1B-BF16` (revision `0677b2025cbc37daf92d7b9c7a225de8cfbc5b0b`)
- Toolchain: llama.cpp (see `CONVERSION_REPORT.md` for the exact build and commands)
- Path: BF16 Safetensors -> F16 GGUF -> Q8_0 / Q4_K_M
- Embedding dimension: 2048, L2-normalized, mean pooling
- Context length: 262,144 declared; validated at 4,096 tokens

## License

The model weights are derived from NVIDIA Nemotron-3-Embed-1B-BF16 and are licensed under the [OpenMDW License Agreement, version 1.1](https://openmdw.ai/license/1-1/). See `LICENSE`, `NOTICE`, and `THIRD_PARTY_NOTICES.md` in this repository. This conversion is not an official NVIDIA release and is not affiliated with or endorsed by NVIDIA.
