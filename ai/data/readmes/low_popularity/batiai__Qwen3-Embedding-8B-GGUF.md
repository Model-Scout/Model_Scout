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
  - mteb
base_model: Qwen/Qwen3-Embedding-8B
pipeline_tag: sentence-similarity
library_name: llama.cpp
---

# Qwen3-Embedding-8B GGUF — Quantized by BatiAI

<p align="center">
  <a href="https://flow.bati.ai"><img src="https://img.shields.io/badge/BatiFlow-RAG%20on%20Mac-blue?style=for-the-badge&logo=apple" alt="BatiFlow"></a>
  <a href="https://ollama.com/batiai/qwen3-embedding"><img src="https://img.shields.io/badge/Ollama-batiai%2Fqwen3--embedding%3A8b-green?style=for-the-badge" alt="Ollama"></a>
  <a href="https://huggingface.co/Qwen/Qwen3-Embedding-8B"><img src="https://img.shields.io/badge/Upstream-Qwen3--Embedding--8B-orange?style=for-the-badge" alt="Upstream"></a>
</p>

> GGUF quantizations of **Qwen/Qwen3-Embedding-8B** — **MTEB #1 among open embeddings (70.58 avg)** at release. Top-tier retrieval quality for users with 24 GB+ Macs.
> Part of BatiAI's on-device RAG stack for [BatiFlow](https://flow.bati.ai).

## Why 8B?

- **MTEB Multilingual avg 70.58** — #1 among open-source embedding models at release
- **Strong Korean + multilingual retrieval** — single model covers 100+ languages
- **Matryoshka** — 2560 → 1024 → 512 → 256 dimensions at runtime, no re-embed

## Quick Start

### Ollama

```bash
ollama pull batiai/qwen3-embedding:8b        # Q6_K (6.2 GB, recommended default)
ollama pull batiai/qwen3-embedding:8b-q8     # Q8_0 (8.0 GB, max quality)

curl http://localhost:11434/api/embeddings -d '{
  "model": "batiai/qwen3-embedding:8b",
  "prompt": "semantic search query"
}'
```

### llama.cpp

```bash
./llama-server \
  -m Qwen3-Embedding-8B-Q8_0.gguf \
  --embeddings --pooling last -c 32768 \
  --host 127.0.0.1 --port 8080
```

## Available Quantizations

| File | Quant | Size | When to use |
|------|-------|------|-------------|
| **`Qwen3-Embedding-8B-Q6_K.gguf`** | **Q6_K** | **~6.2 GB** | **recommended default — Q8↔Q6 drift cos 0.999, indistinguishable on retrieval** |
| `Qwen3-Embedding-8B-Q8_0.gguf` | Q8_0 | ~8.1 GB | maximum quality, ~25 % bigger disk |

Why Q6 over Q8 as default? Drift 0.999 means the two files produce functionally identical embeddings. On a 24 GB Mac, saving ~1.8 GB keeps the window manager and browser comfortable alongside inference. If you want maximum conservatism, pull `:8b-q8`.

Why no IQ3 / IQ4 for embedding? Embedding quality cascades into cosine-similarity drift at low bit-widths. Q6_K / Q8_0 are the safe range.

## Quality Verification (measured)

Four-stage harness run on both quants. Full testset + script reproducible via [`scripts/bench-embedding-quality.sh`](https://github.com/batiai/).

| Stage | Test | Q8_0 | Q6_K |
|-------|------|-----:|-----:|
| **A. Same-lang semantics** | 30 (EN+KO) triples, directional correctness | **30/30 (100 %)** | **30/30 (100 %)** |
|  | average margin | 0.310 | 0.308 |
| **B. Cross-lingual alignment** | 30 EN↔KO parallel pairs | **30/30 (100 %)** | **30/30 (100 %)** |
|  | parallel cos avg | 0.835 | 0.833 |
|  | unrelated cos avg | 0.268 | 0.264 |
|  | **separation Δ** | **0.567** | **0.569** |
| **C. Real-doc top-1 retrieval** | 20 EN chunks × 20 EN queries | **20/20 (100 %)** | **20/20 (100 %)** |
|  | 20 KO chunks × 20 KO queries | **20/20 (100 %)** | **20/20 (100 %)** |
|  | **combined recall** | **100 %** | **100 %** |
| **D. Quant drift** | Q8_0 ↔ Q6_K on 20 sample queries | avg cos **0.9988** (min 0.9983, max 0.9991) — PASS |

**Perfect retrieval across 40 queries on both languages** — the full value of MTEB #1 shows up cleanly on this harness. Q8_0 and Q6_K produce essentially identical quality; pick Q6_K if disk is tight.

## Quality tier comparison (across BatiAI text-embedding lineup)

| Model | A margin | B separation Δ | C recall (EN / KO) | D drift avg |
|-------|---------:|---------------:|-------------------:|------------:|
| Qwen3-Embedding-0.6B (Q6) | 0.281 | 0.521 | 95 % / 100 % | 0.9967 |
| Qwen3-Embedding-4B (Q6) | 0.289 | 0.540 | 95 % / 100 % | 0.9984 |
| **Qwen3-Embedding-8B (Q6)** | **0.308** | **0.569** | **100 % / 100 %** | **0.9988** |

Cleanly monotonic: every metric improves with size. If retrieval accuracy is critical and you have the RAM, 8B is the pick.

## Matryoshka — runtime-configurable dimension

Qwen3-Embedding-8B outputs **up to 2560 dimensions**. BatiFlow RAG stack defaults to **1024** (quality / latency sweet spot). Truncate at read time:

```python
emb = get_embedding(text)     # [2560]
emb_1024 = emb[:1024]
import numpy as np
emb_1024 = emb_1024 / np.linalg.norm(emb_1024)
```

## Why text-only?

For **image + text** retrieval, see [Qwen3-VL-Embedding-8B on BatiAI](https://huggingface.co/batiai/Qwen3-VL-Embedding-8B-GGUF).

## RAG Stack Integration

```
user query
   ↓ [Qwen3-Embedding 8B]            ← YOU ARE HERE (top tier, MTEB #1)
1024-dim vector
   ↓ vector DB (sqlite-vec / LanceDB)
top-K candidates
   ↓ [Qwen3-Reranker 8B]
top-3
   ↓ [Qwen3.6-35B-A3B chat LLM]
answer
```

## Recommended Usage — query vs document

```python
# Query side
query = "Instruct: Given a document query, retrieve the most relevant chunk.\n" \
        "Query: " + user_input

# Document side — no instruction prefix
document = chunk_text
```

BatiFlow handles this automatically. For custom integrations, see [Qwen3-Embedding usage](https://huggingface.co/Qwen/Qwen3-Embedding-8B).

## Why BatiAI?

- Quantized **directly from Qwen's BF16 safetensors** — no intermediate GGUF
- `general.author: BatiAI` for provenance
- **4-stage quality harness** — full EN + KO retrieval numbers published
- Matched with [Qwen3-Reranker-8B](https://huggingface.co/batiai/Qwen3-Reranker-8B-GGUF) and [Qwen3.6-35B-A3B](https://huggingface.co/batiai/Qwen3.6-35B-A3B-GGUF) — complete Mac-first RAG stack

## Technical Details

- **Original Model**: [Qwen/Qwen3-Embedding-8B](https://huggingface.co/Qwen/Qwen3-Embedding-8B)
- **Architecture**: Qwen3 Causal LM → last-token pooling
- **Parameters**: 8.19 B
- **Embedding dim**: up to 2560 (Matryoshka)
- **Context**: 32 K
- **License**: Apache 2.0
- **Quantized with**: [llama.cpp](https://github.com/ggml-org/llama.cpp) build `bafae2765`
- **Quantized by**: [BatiAI](https://bati.ai)

## BatiAI RAG Stack

| Role | Model | Repo |
|------|-------|------|
| Text embedder (entry) | Qwen3-Embedding-0.6B | [batiai/Qwen3-Embedding-0.6B-GGUF](https://huggingface.co/batiai/Qwen3-Embedding-0.6B-GGUF) |
| Text embedder (mid) | Qwen3-Embedding-4B | [batiai/Qwen3-Embedding-4B-GGUF](https://huggingface.co/batiai/Qwen3-Embedding-4B-GGUF) |
| **Text embedder (top)** | Qwen3-Embedding-8B | **this repo** |
| VL embedder | Qwen3-VL-Embedding-2B / 8B | [batiai/Qwen3-VL-Embedding-8B-GGUF](https://huggingface.co/batiai/Qwen3-VL-Embedding-8B-GGUF) |
| Reranker | Qwen3-Reranker-8B | [batiai/Qwen3-Reranker-8B-GGUF](https://huggingface.co/batiai/Qwen3-Reranker-8B-GGUF) |
| Chat LLM | Qwen3.6-35B-A3B | [batiai/Qwen3.6-35B-A3B-GGUF](https://huggingface.co/batiai/Qwen3.6-35B-A3B-GGUF) |

## License

Mirrors upstream Qwen Apache 2.0 — commercial use permitted.
