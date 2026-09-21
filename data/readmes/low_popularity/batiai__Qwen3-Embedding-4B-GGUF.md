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
base_model: Qwen/Qwen3-Embedding-4B
pipeline_tag: sentence-similarity
library_name: llama.cpp
---

# Qwen3-Embedding-4B GGUF — Quantized by BatiAI

<p align="center">
  <a href="https://flow.bati.ai"><img src="https://img.shields.io/badge/BatiFlow-RAG%20on%20Mac-blue?style=for-the-badge&logo=apple" alt="BatiFlow"></a>
  <a href="https://ollama.com/batiai/qwen3-embedding"><img src="https://img.shields.io/badge/Ollama-batiai%2Fqwen3--embedding%3A4b-green?style=for-the-badge" alt="Ollama"></a>
  <a href="https://huggingface.co/Qwen/Qwen3-Embedding-4B"><img src="https://img.shields.io/badge/Upstream-Qwen3--Embedding--4B-orange?style=for-the-badge" alt="Upstream"></a>
</p>

> GGUF quantizations of **Qwen/Qwen3-Embedding-4B** — the mid-tier sweet spot for 16 GB+ Macs. Higher retrieval quality than 0.6B; leaner RAM than 8B.
> Part of BatiAI's on-device RAG stack for [BatiFlow](https://flow.bati.ai).

## Quick Start

### Ollama

```bash
ollama pull batiai/qwen3-embedding:4b        # Q6_K (3.3 GB, recommended default)
ollama pull batiai/qwen3-embedding:4b-q8     # Q8_0 (4.3 GB, max quality)

curl http://localhost:11434/api/embeddings -d '{
  "model": "batiai/qwen3-embedding:4b",
  "prompt": "semantic search query"
}'
```

### llama.cpp

```bash
./llama-server \
  -m Qwen3-Embedding-4B-Q8_0.gguf \
  --embeddings --pooling last -c 32768 \
  --host 127.0.0.1 --port 8080
```

## Available Quantizations

| File | Quant | Size | When to use |
|------|-------|------|-------------|
| **`Qwen3-Embedding-4B-Q6_K.gguf`** | **Q6_K** | **~3.3 GB** | **recommended default — Q8↔Q6 drift cos 0.998, indistinguishable on retrieval** |
| `Qwen3-Embedding-4B-Q8_0.gguf` | Q8_0 | ~4.3 GB | maximum quality, ~25 % bigger disk |

Why Q6 over Q8 as default? Measured drift 0.998 = cosine distance well below any retrieval noise floor. Saving ~1 GB matters on 16 GB Macs where every GB of free RAM helps. If you want maximum conservatism, pull `:4b-q8`.

Why no IQ3 / IQ4 for embedding? Unlike chat LLMs, embedding quality cascades into cosine-similarity drift at low bit-widths. Q6_K / Q8_0 are the safe range.

## Quality Verification (measured)

Four-stage harness run on both quants. Full testset + script reproducible via [`scripts/bench-embedding-quality.sh`](https://github.com/batiai/).

| Stage | Test | Q8_0 | Q6_K |
|-------|------|-----:|-----:|
| **A. Same-lang semantics** | 30 (EN+KO) triples, directional correctness | **30/30 (100 %)** | **30/30 (100 %)** |
|  | average margin | 0.289 | 0.289 |
| **B. Cross-lingual alignment** | 30 EN↔KO parallel pairs | **30/30 (100 %)** | **30/30 (100 %)** |
|  | parallel cos avg | 0.762 | 0.761 |
|  | unrelated cos avg | 0.220 | 0.221 |
|  | **separation Δ** | **0.542** | **0.540** |
| **C. Real-doc top-1 retrieval** | 20 EN chunks × 20 EN queries | 19/20 (**95 %**) | 19/20 (**95 %**) |
|  | 20 KO chunks × 20 KO queries | 20/20 (**100 %**) | 20/20 (**100 %**) |
|  | **combined recall** | **97.5 %** | **97.5 %** |
| **D. Quant drift** | Q8_0 ↔ Q6_K on 20 sample queries | avg cos **0.9984** (min 0.9979, max 0.9990) — PASS |

All stages PASS with comfortable margin. Q8_0 and Q6_K produce essentially identical retrieval quality on this testset, with Q6_K saving ~25 % on disk.

### Quality tier comparison (across BatiAI text-embedding lineup)

| Model | A margin | B separation Δ | C recall (EN / KO) | D drift avg |
|-------|---------:|---------------:|-------------------:|------------:|
| Qwen3-Embedding-0.6B (Q6) | 0.281 | 0.521 | 95 % / 100 % | 0.9967 |
| **Qwen3-Embedding-4B (Q6)** | **0.289** | **0.540** | **95 % / 100 %** | **0.9984** |
| Qwen3-Embedding-8B (Q6) | 0.308 | 0.569 | 100 % / 100 % | 0.9988 |

4B sits in the middle — meaningfully better separation than 0.6B, within striking distance of 8B, at roughly half the disk footprint of 8B. Recommended default for 16 GB+ Macs.

## Matryoshka — runtime-configurable dimension

Qwen3-Embedding-4B outputs **up to 2560 dimensions**. BatiFlow RAG stack defaults to **1024** (quality / latency sweet spot per our tests). Truncate at read time — no re-embed needed:

```python
emb = get_embedding(text)     # [2560]
emb_1024 = emb[:1024]         # truncate for storage savings
import numpy as np
emb_1024 = emb_1024 / np.linalg.norm(emb_1024)   # re-normalize
```

## Why text-only?

Qwen3-Embedding-4B is designed specifically for **text**. For **multimodal** (image + text), see [Qwen3-VL-Embedding-8B on BatiAI](https://huggingface.co/batiai/Qwen3-VL-Embedding-8B-GGUF).

| Task | Use |
|------|-----|
| Document search / Q&A retrieval | **this repo (text-only)** |
| Image / screenshot search | [`batiai/Qwen3-VL-Embedding-2B-GGUF`](https://huggingface.co/batiai/Qwen3-VL-Embedding-2B-GGUF) |

## RAG Stack Integration

```
user query
   ↓ [Qwen3-Embedding 4B]            ← YOU ARE HERE (mid tier)
1024-dim vector
   ↓ vector DB (sqlite-vec / LanceDB)
top-K candidates
   ↓ [Qwen3-Reranker 4B or 8B]
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

BatiFlow handles this automatically. For custom integrations, see [Qwen3-Embedding usage](https://huggingface.co/Qwen/Qwen3-Embedding-4B).

## Why BatiAI?

- Quantized **directly from Qwen's BF16 safetensors**
- `general.author: BatiAI` for provenance
- **4-stage quality harness** (same-lang, cross-lingual, real-doc top-1, quant drift) — numbers published
- Paired with [Qwen3-Reranker-4B](https://huggingface.co/batiai/Qwen3-Reranker-4B-GGUF) and [Qwen3.6-35B-A3B](https://huggingface.co/batiai/Qwen3.6-35B-A3B-GGUF) on the same org

## Technical Details

- **Original Model**: [Qwen/Qwen3-Embedding-4B](https://huggingface.co/Qwen/Qwen3-Embedding-4B)
- **Architecture**: Qwen3 Causal LM → last-token pooling
- **Parameters**: 4.02 B
- **Embedding dim**: up to 2560 (Matryoshka)
- **Context**: 32 K
- **License**: Apache 2.0
- **Quantized with**: [llama.cpp](https://github.com/ggml-org/llama.cpp) build `bafae2765`
- **Quantized by**: [BatiAI](https://bati.ai)

## BatiAI RAG Stack

| Role | Model | Repo |
|------|-------|------|
| Text embedder (entry) | Qwen3-Embedding-0.6B | [batiai/Qwen3-Embedding-0.6B-GGUF](https://huggingface.co/batiai/Qwen3-Embedding-0.6B-GGUF) |
| **Text embedder (mid)** | Qwen3-Embedding-4B | **this repo** |
| Text embedder (top) | Qwen3-Embedding-8B | [batiai/Qwen3-Embedding-8B-GGUF](https://huggingface.co/batiai/Qwen3-Embedding-8B-GGUF) |
| VL embedder | Qwen3-VL-Embedding-2B / 8B | [batiai/Qwen3-VL-Embedding-2B-GGUF](https://huggingface.co/batiai/Qwen3-VL-Embedding-2B-GGUF) |
| Reranker | Qwen3-Reranker-4B / 8B | [batiai/Qwen3-Reranker-4B-GGUF](https://huggingface.co/batiai/Qwen3-Reranker-4B-GGUF) |
| Chat LLM | Qwen3.6-35B-A3B | [batiai/Qwen3.6-35B-A3B-GGUF](https://huggingface.co/batiai/Qwen3.6-35B-A3B-GGUF) |

## License

Mirrors upstream Qwen Apache 2.0 — commercial use permitted.
