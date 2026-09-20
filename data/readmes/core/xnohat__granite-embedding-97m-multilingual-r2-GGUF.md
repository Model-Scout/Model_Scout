---
language:
  - ar
  - az
  - bg
  - bn
  - ca
  - cs
  - da
  - de
  - el
  - en
  - es
  - et
  - fa
  - fi
  - fr
  - he
  - hi
  - hr
  - hu
  - id
  - is
  - it
  - ja
  - ka
  - kk
  - km
  - ko
  - lt
  - lv
  - mr
  - ms
  - nl
  - "no"
  - pl
  - pt
  - ro
  - ru
  - sk
  - sl
  - sq
  - sr
  - sv
  - sw
  - te
  - th
  - tl
  - tr
  - uk
  - ur
  - uz
  - vi
  - zh
library_name: GGUF
license: apache-2.0
pipeline_tag: feature-extraction
tags:
  - granite
  - embeddings
  - multilingual
  - mteb
  - feature-extraction
  - sentence-similarity
  - llama-cpp
base_model: ibm-granite/granite-embedding-97m-multilingual-r2
---

# Granite-Embedding-97M-Multilingual-R2-GGUF

GGUF builds of [`ibm-granite/granite-embedding-97m-multilingual-r2`](https://huggingface.co/ibm-granite/granite-embedding-97m-multilingual-r2).

This repository is a **mirror**, published so that AICoworker (OpenClaw gateway)
can ship Granite R2 as its default local embedding model without depending on a
third-party repository remaining available. The files are byte-identical to the
conversion credited below.

| | |
|---|---|
| Parameters | 97M |
| Architecture | ModernBERT (`general.architecture = modern-bert`) |
| Embedding dimensions | 384 |
| Context length | 32768 |
| Pooling | **CLS** (`modern-bert.pooling_type = 2`) |
| License | Apache-2.0 |

## Files

| File | Size |
|---|---|
| `granite-embedding-97M-multilingual-r2-BF16.gguf` | 206 MB |
| `granite-embedding-97M-multilingual-r2-Q8_0.gguf` | 115 MB |
| `granite-embedding-97M-multilingual-r2-Q6_K.gguf` | 113 MB |
| `granite-embedding-97M-multilingual-r2-Q5_K_M.gguf` | 107 MB |
| `granite-embedding-97M-multilingual-r2-Q4_K_M.gguf` | 105 MB |
| `granite-embedding-97M-multilingual-r2-Q3_K_L.gguf` | 103 MB |

**Q8_0 is the recommended default**: the retrieval-quality gap to BF16 is
negligible while the download is roughly half the size.

## Pooling is baked into the file

llama.cpp pools token vectors according to the GGUF's own `pooling_type` — the
caller does not get to choose it at load time. These files declare **CLS**
pooling, which is what Granite R2 was trained for. A mean-pooled re-quant still
loads and still returns vectors, but retrieval quality degrades measurably with
no other symptom, so keep CLS if you re-quantize.

## Usage (node-llama-cpp)

```js
import { getLlama, resolveModelFile } from 'node-llama-cpp';

const file = await resolveModelFile(
  'hf:xnohat/granite-embedding-97m-multilingual-r2-GGUF/granite-embedding-97M-multilingual-r2-Q8_0.gguf',
);
const llama = await getLlama();
const model = await llama.loadModel({ modelPath: file });
const context = await model.createEmbeddingContext();

const { vector } = await context.getEmbeddingFor('Mật khẩu wifi nhà là gì?'); // 384 dims
```

Granite takes **raw text** — no `query:` / `passage:` prefixes (those are E5 and
EmbeddingGemma conventions, and applying them here measurably hurts).

## Credits

- Original model: [`ibm-granite/granite-embedding-97m-multilingual-r2`](https://huggingface.co/ibm-granite/granite-embedding-97m-multilingual-r2) — IBM Granite, Apache-2.0.
- GGUF conversion: [`mykor/granite-embedding-97m-multilingual-r2-GGUF`](https://huggingface.co/mykor/granite-embedding-97m-multilingual-r2-GGUF).

All credit for the model and for the GGUF conversion belongs to the authors
above. This repo only pins availability.
