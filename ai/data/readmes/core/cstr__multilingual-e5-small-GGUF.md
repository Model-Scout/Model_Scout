---
license: mit
language: [en, de, fr, es, zh, ja, ko, ar, hi, pt, ru, it, nl, pl, tr, vi, th, id, sv, da, no, fi, cs, ro, hu, bg, uk, ca, el, hr, sk, sl, et, lt, lv, ms, tl, sw, af, cy, ga, sq, mk, bs, mt, gl, eu, is, ka, hy, kk, uz, az, be, mn, ne, si, km, my, lo, am, ps, sd, ku, ug, bo, dz, fy]
tags: [embeddings, gguf, ggml, text-embeddings, bert, crispembed, ollama]
pipeline_tag: feature-extraction
base_model: intfloat/multilingual-e5-small
---

# multilingual-e5-small GGUF

GGUF format of [intfloat/multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small) for use with [CrispEmbed](https://github.com/CrispStrobe/CrispEmbed) and [Ollama](https://ollama.com).

## Files

| File | Quantization | Size | cos vs HF |
|------|-------------|------|-----------|
| [multilingual-e5-small.gguf](https://huggingface.co/cstr/multilingual-e5-small-GGUF/resolve/main/multilingual-e5-small.gguf) | F32 | 455 MiB | 1.0000 (reference) |
| [multilingual-e5-small-q8_0.gguf](https://huggingface.co/cstr/multilingual-e5-small-GGUF/resolve/main/multilingual-e5-small-q8_0.gguf) | Q8_0 | 126 MiB | 0.9999 |
| [multilingual-e5-small-q4_k.gguf](https://huggingface.co/cstr/multilingual-e5-small-GGUF/resolve/main/multilingual-e5-small-q4_k.gguf) | Q4_K | 115 MiB | 0.990 |
| [multilingual-e5-small-q4_k-imatrix.gguf](https://huggingface.co/cstr/multilingual-e5-small-GGUF/resolve/main/multilingual-e5-small-q4_k-imatrix.gguf) | Q4_K + imatrix | 115 MiB | not measured |
| [multilingual-e5-small-iq4_xs.gguf](https://huggingface.co/cstr/multilingual-e5-small-GGUF/resolve/main/multilingual-e5-small-iq4_xs.gguf) | IQ4_XS | 115 MiB | not measured |

Sizes are MiB (what the file browser above reports). Auxiliary files:
[`multilingual-e5-small.imatrix`](https://huggingface.co/cstr/multilingual-e5-small-GGUF/resolve/main/multilingual-e5-small.imatrix)
(131 KiB, the importance matrix used for the imatrix/IQ quants) and
[`multilingual-e5-small-imatrix-ab.txt`](https://huggingface.co/cstr/multilingual-e5-small-GGUF/resolve/main/multilingual-e5-small-imatrix-ab.txt)
(the A/B notes from producing it).

**Recommended: Q8_0.** It is within 0.0001 cosine of the F32 reference while
being 3.6× smaller, so F32 buys nothing you can measure. Drop to a 4-bit quant
only when you are memory-bound: they save a further 11 MiB — about 9% — and
Q4_K gives up an order of magnitude more accuracy (0.990) to do it. At this
model size the 4-bit tier is rarely the right trade; it matters much more on
the larger models in this registry.

## Quick Start

### CrispEmbed
```bash
./crispembed -m multilingual-e5-small "Hello world"
./crispembed-server -m multilingual-e5-small --port 8080
```

### Ollama (with [CrispStrobe fork](https://github.com/CrispStrobe/ollama/tree/feat/xlmr-embedding))
```bash
# Create model
echo "FROM multilingual-e5-small-q8_0.gguf" > Modelfile
ollama create multilingual-e5-small -f Modelfile

# Embed
curl http://localhost:11434/api/embed -d '{"model":"multilingual-e5-small","input":["Hello world"]}'
```

### Python (CrispEmbed)
```python
from crispembed import CrispEmbed
model = CrispEmbed("multilingual-e5-small-q8_0.gguf")
vectors = model.encode(["Hello world", "Goodbye world"])
```

## Model Details

| Property | Value |
|----------|-------|
| Architecture | BERT |
| Parameters | 118M |
| Embedding Dimension | 384 |
| Layers | 12 |
| Pooling | mean |
| Tokenizer | SentencePiece |
| Language | multilingual |
| Q8_0 vs HuggingFace | 0.9999 |
| Q4_K vs HuggingFace | 0.990 |

## Server API

CrispEmbed server supports four API dialects:
- `POST /embed` — native
- `POST /v1/embeddings` — OpenAI-compatible
- `POST /api/embed` — Ollama-compatible
- `POST /api/embeddings` — Ollama legacy

## Credits

- Original model: [intfloat/multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small)
- Inference: [CrispEmbed](https://github.com/CrispStrobe/CrispEmbed) (MIT, ggml-based)

## Provenance and EU AI Act Art. 53 note

- **Upstream model:** [intfloat/multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small) — published by `intfloat`.
- **Upstream licence:** `mit`. This repository redistributes under the same terms; it grants no rights the upstream licence does not.
- **What was done here:** format conversion and/or quantisation only (GGUF/GGML). No training, no fine-tuning, no merging, no distillation, no change to architecture, vocabulary or capability. Only the numeric representation of the upstream weights differs.
- **Training data:** documented — where it is documented at all — by the upstream provider; see the upstream model card. No training data was used, added or selected by this repository.
- **Provider status:** under Regulation (EU) 2024/1689 the upstream authors remain the provider of this model. Converting the serialisation format does not make this repository the provider of a new general-purpose AI model, and no such claim is made. Questions about training content, copyright policy or model capability belong upstream.
