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
  - text-embedding
  - rag
  - quantized
  - batiai
  - on-device
  - apple-silicon
  - matryoshka
base_model: Qwen/Qwen3-Embedding-0.6B
pipeline_tag: sentence-similarity
library_name: llama.cpp
---

# Qwen3-Embedding-0.6B GGUF — Quantized by BatiAI

<p align="center">
  <a href="https://flow.bati.ai"><img src="https://img.shields.io/badge/BatiFlow-RAG%20on%20Mac-blue?style=for-the-badge&logo=apple" alt="BatiFlow"></a>
  <a href="https://ollama.com/batiai/qwen3-embedding"><img src="https://img.shields.io/badge/Ollama-batiai%2Fqwen3--embedding%3A0.6b-green?style=for-the-badge" alt="Ollama"></a>
  <a href="https://huggingface.co/Qwen/Qwen3-Embedding-0.6B"><img src="https://img.shields.io/badge/Upstream-Qwen3--Embedding--0.6B-orange?style=for-the-badge" alt="Upstream"></a>
</p>

> GGUF quantizations of **Qwen/Qwen3-Embedding-0.6B** — the lightweight tier of the Qwen3-Embedding family. Runs on every Mac (8 GB and up), 100 emb/sec on M-series.
> Part of BatiAI's on-device RAG stack for [BatiFlow](https://flow.bati.ai).

## TL;DR

- **100 % top-1 retrieval** on Korean business-doc test set (Q6_K), **95 % on English**
- Cross-lingual alignment **Δ = 0.52** (parallel vs unrelated) — semantic understanding across EN↔KO
- Quantization drift **avg cos 0.9967** (Q8↔Q6) — well above the 0.98 deploy threshold
- Tier goal: **light-weight default** for every Mac — if you don't know which size to pick, start here

## Quick Start

### Ollama (one command)

```bash
ollama pull batiai/qwen3-embedding:0.6b        # 472 MB (Q6_K default — recommended)
ollama pull batiai/qwen3-embedding:0.6b-q8     # 610 MB (Q8_0 — max quality)

# Use via Ollama embeddings API
curl http://localhost:11434/api/embeddings -d '{
  "model": "batiai/qwen3-embedding:0.6b",
  "prompt": "semantic search query"
}'
```

### llama.cpp (server)

```bash
./llama-server \
  -m Qwen3-Embedding-0.6B-Q8_0.gguf \
  --embeddings --pooling last -c 32768 \
  --host 127.0.0.1 --port 8080

# Native embedding endpoint
curl http://localhost:8080/embedding -d '{"content": "your text here"}'

# OpenAI-compatible endpoint
curl http://localhost:8080/v1/embeddings \
  -H 'Content-Type: application/json' \
  -d '{"input": "your text here", "model": "qwen3-embedding"}'
```

## Available Quantizations

| File | Quant | Size | When to use |
|------|-------|------|-------------|
| **`Qwen3-Embedding-0.6B-Q6_K.gguf`** | **Q6_K** | **472 MB** | **recommended default — we measured drift vs Q8 at cos 0.997 (indistinguishable on retrieval)** |
| `Qwen3-Embedding-0.6B-Q8_0.gguf` | Q8_0 | 610 MB | maximum quality, ~25 % bigger disk |

Why Q6 over Q8 as default? On our 4-stage harness the two are functionally equivalent — Q6 actually *edged out* Q8 by 2.5 pp on real-doc top-1 recall (measurement noise, but confirms Q6 is not inferior). 150 MB savings matters on 8 GB Macs. If you want maximum conservatism, pull `:0.6b-q8`.

Why no IQ3 / IQ4 for embedding? Unlike chat LLMs, embedding quality cascades into cosine-similarity drift at low bit-widths — every query is affected. Q6_K / Q8_0 are the safe range.

## Quality Verification (measured)

Four-stage harness run on both quants. Full testset + script reproducible via [`scripts/bench-embedding-quality.sh`](https://github.com/batiai/).

| Stage | Test | Q8_0 | Q6_K |
|-------|------|-----:|-----:|
| **A. Same-lang semantics** | 30 (EN+KO) triples, directional correctness | **30/30 (100 %)** | **30/30 (100 %)** |
|  | average margin | 0.278 | 0.281 |
| **B. Cross-lingual alignment** | 30 EN↔KO parallel pairs | **30/30 (100 %)** | **30/30 (100 %)** |
|  | parallel cos avg | 0.728 | 0.738 |
|  | unrelated cos avg | 0.206 | 0.218 |
|  | **separation Δ** | **0.522** | **0.521** |
| **C. Real-doc top-1 retrieval** | 20 EN chunks × 20 EN queries | 19/20 (**95 %**) | 19/20 (**95 %**) |
|  | 20 KO chunks × 20 KO queries | 19/20 (**95 %**) | 20/20 (**100 %**) |
|  | **combined recall** | **95.0 %** | **97.5 %** |
| **D. Quant drift** | Q8_0 ↔ Q6_K on 20 sample queries | avg cos **0.9967** (min 0.9943, max 0.9983) — PASS |

All stages PASS with healthy margin. **Q6_K actually edged out Q8_0 by 2.5 pp on combined top-1 recall** (quantization-as-regularization effect at this scale — within measurement noise but encouraging).

### Quality tier comparison (across BatiAI text-embedding lineup)

| Model | A margin | B separation Δ | C recall (EN / KO) | D drift avg |
|-------|---------:|---------------:|-------------------:|------------:|
| **Qwen3-Embedding-0.6B (Q6)** | **0.281** | **0.521** | **95 % / 100 %** | **0.9967** |
| Qwen3-Embedding-4B (Q6) | 0.289 | 0.540 | 95 % / 100 % | 0.9984 |
| Qwen3-Embedding-8B (Q6) | 0.308 | 0.569 | 100 % / 100 % | 0.9988 |

Monotonic improvement with size, but 0.6B already lands **95 %+ retrieval on real business docs** — strong default for anyone not sure which tier to pick.

## Why text-only?

The Qwen3-Embedding family is designed specifically for **text** (semantic retrieval, clustering, classification). For **multimodal** (image + text) RAG, see [Qwen3-VL-Embedding-2B / 8B on BatiAI](https://huggingface.co/batiai).

Use the right tool for the job:
- Document search / Q&A retrieval → **this repo (text-only)**
- Image / screenshot search → [`batiai/Qwen3-VL-Embedding-2B-GGUF`](https://huggingface.co/batiai/Qwen3-VL-Embedding-2B-GGUF)

## Matryoshka — runtime-configurable dimension

Qwen3-Embedding outputs **up to 1024 dimensions**. Use smaller dimensions for faster search by slicing at read time — no re-embed needed:

```python
# Full 1024-dim embedding
emb = get_embedding(text)  # shape: [1024]

# Truncate to 512 for 2× storage savings + faster ANN
emb_512 = emb[:512]
# → re-normalize if your distance metric expects unit vectors
import numpy as np
emb_512 = emb_512 / np.linalg.norm(emb_512)
```

BatiFlow RAG stack defaults to **1024 dimensions** (best quality / latency balance per our tests).

## RAG Stack Integration

This embedder is designed to pair with BatiAI's reranker + chat LLM:

```
user query
   ↓ [Qwen3-Embedding 0.6B]        ← YOU ARE HERE
1024-dim vector
   ↓ vector DB (sqlite-vec / LanceDB)
top-K candidates
   ↓ [Qwen3-Reranker 0.6B / 4B / 8B]
top-3
   ↓ [Qwen3.6-35B-A3B chat LLM]
answer
```

All on-device, all from `batiai/` on Hugging Face and Ollama.

## Why Qwen3-Embedding?

- **Multilingual** — trained on EN / KO / JA / ZH + 100+ languages
- **Instruction-aware** — supports query-side `Instruct: {task}` prefix for better retrieval
- **Matryoshka** — one model, multiple dimension budgets
- **Apache 2.0** — commercial-friendly
- **Small** — 596 M params, 472–610 MB as GGUF, fits in 8 GB RAM with room to spare

## Why BatiAI?

| | batiai/qwen3-embedding:0.6b | Official Ollama `qwen3-embedding:0.6b` |
|---|---|---|
| Source | Quantized direct from **Qwen's BF16 safetensors** | Likely re-quantized |
| Signing | `general.author: BatiAI` for provenance | — |
| Quality published | **4-stage harness + numbers above** | — |
| Korean verification | 95 – 100 % top-1 recall on real docs | — |
| Paired stack | Matched with [Qwen3-Reranker-0.6B-GGUF](https://huggingface.co/batiai/Qwen3-Reranker-0.6B-GGUF) + [Qwen3.6-35B-A3B-GGUF](https://huggingface.co/batiai/Qwen3.6-35B-A3B-GGUF) | — |
| BatiFlow integration | One-click Mac-native app | — |

## Recommended Usage — query vs document

Qwen3-Embedding performs best when queries carry an instruction prefix:

```python
# Query side
query = "Instruct: Given a document query, retrieve the most relevant chunk.\n" \
        "Query: " + user_input

# Document side — no instruction prefix, just raw text
document = chunk_text
```

BatiFlow handles this automatically. For custom integrations, see the [Qwen3-Embedding usage guide](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B).

## Technical Details

- **Original Model**: [Qwen/Qwen3-Embedding-0.6B](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B)
- **Architecture**: Qwen3 Causal LM → last-token pooling for sentence embedding
- **Parameters**: 596 M
- **Embedding dim**: up to 1024 (Matryoshka)
- **Context**: 32 K
- **License**: Apache 2.0
- **Quantized with**: [llama.cpp](https://github.com/ggml-org/llama.cpp) build `bafae2765`
- **Quantized by**: [BatiAI](https://bati.ai)
- **GGUF metadata**: `general.author: BatiAI`, `general.url: https://flow.bati.ai`

## BatiAI RAG Stack (all from `batiai/` org)

| Role | Model | Repo |
|------|-------|------|
| **Text embedder (entry)** | Qwen3-Embedding-0.6B | **this repo** |
| Text embedder (mid) | Qwen3-Embedding-4B | [batiai/Qwen3-Embedding-4B-GGUF](https://huggingface.co/batiai/Qwen3-Embedding-4B-GGUF) |
| Text embedder (top) | Qwen3-Embedding-8B | [batiai/Qwen3-Embedding-8B-GGUF](https://huggingface.co/batiai/Qwen3-Embedding-8B-GGUF) |
| VL embedder | Qwen3-VL-Embedding-2B / 8B | [batiai/Qwen3-VL-Embedding-2B-GGUF](https://huggingface.co/batiai/Qwen3-VL-Embedding-2B-GGUF) |
| Reranker | Qwen3-Reranker-0.6B / 4B / 8B | [batiai/Qwen3-Reranker-0.6B-GGUF](https://huggingface.co/batiai/Qwen3-Reranker-0.6B-GGUF) |
| Chat LLM | Qwen3.6-35B-A3B | [batiai/Qwen3.6-35B-A3B-GGUF](https://huggingface.co/batiai/Qwen3.6-35B-A3B-GGUF) |

## License

Mirrors upstream Qwen Apache 2.0 — commercial use permitted.
