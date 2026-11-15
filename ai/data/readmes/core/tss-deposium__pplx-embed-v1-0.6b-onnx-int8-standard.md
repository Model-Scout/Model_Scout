---
base_model: perplexity-ai/pplx-embed-v1-0.6B
base_model_relation: quantized
library_name: transformers.js
license: mit
language:
  - en
  - fr
  - de
  - es
  - it
  - pt
  - zh
  - ja
  - ko
  - ar
  - ru
  - hi
  - bn
  - id
  - vi
  - tr
  - fa
  - cs
  - sv
  - ro
  - nb
  - hu
  - da
  - uk
  - th
  - el
  - fi
  - pl
  - nl
  - ms
  - sw
  - te
  - yo
tags:
  - feature-extraction
  - embeddings
  - onnx
  - int8
  - quantized
  - transformers.js
  - matryoshka
  - sentence-similarity
  - multilingual
pipeline_tag: feature-extraction
datasets:
  - mteb/results
---

# pplx-embed-v1-0.6B — ONNX standard-operator exports for Transformers.js

Re-exports of [perplexity-ai/pplx-embed-v1-0.6B](https://huggingface.co/perplexity-ai/pplx-embed-v1-0.6B) (revision `2c4d510d`) with **standard ONNX operators**, usable by Transformers.js / ONNX Runtime Web (WASM and WebGPU) and ONNX Runtime Node. The official ONNX files use `GatherBlockQuantized`, which ORT Web cannot load.

Pooling: masked mean over `last_hidden_state` (identical to the official `pooler_output`), then L2, then Matryoshka truncation to 256 dims and L2 again, as in the Deposium stack.

## Variants (2026-09-17)

| file | Transformers.js `dtype` | target | size | recipe | cos vs official FP32 (median / min) | cos vs Deposium server (INT8 official) |
|---|---|---|---|---|---|---|
| `onnx/model_int8.onnx` | `int8` | **WASM (CPU)** | 667 MB | MatMulNBits 8-bit, block 32, asymmetric, `accuracy_level=4`; embedding table int8 per row; fp32 activations; batch-dynamic graph | 0.99960 / 0.99808 (38 texts, ORT CPU) — 0.99974 / 0.99960 in Chrome WASM | 0.99981 / 0.99833 (ORT CPU) — 0.99999 / 0.99995 in Chrome WASM |
| `onnx/model_fp16.onnx` | `fp16` | **WebGPU** (needs `shader-f16`) | 1 194 MB | fp16 weights and activations; RMSNorms pre-fused as `SimplifiedLayerNormalization` kept in fp32; residual stream pre-scaled by 1/16 (exact, see below) | 0.99985 / 0.99971 (Chrome WebGPU, 8 texts up to 512 tokens) | 0.99958 / 0.99858 |
| `onnx/model_int8f16.onnx` | none (load with `model_file_name: 'model_int8f16'`, `dtype: 'fp32'`) | **WebGPU, light** | 639 MB | MatMulNBits 8-bit block 32 asymmetric `accuracy_level=1` + int8 embedding table, fp16 activations, residual pre-scaling 1/16 | 0.99966 / 0.99867 (Chrome WebGPU) | **0.99997 / 0.99986** |
| `onnx/model.onnx` = `onnx/model_quantized.onnx` | `fp32` / `q8` (legacy) | WASM | 602 MB | `quantize_dynamic` QInt8 (INT8 activations) — **deprecated**: 0.971 median, 0.79 minimum on 512-token inputs, and the graph has its batch size fixed to 1 (fails on batched inputs) | 0.97068 / 0.87992 | 0.96978 / 0.87849 |

Measurements: 38 texts in 6 languages (10 to 218 tokens) with ONNX Runtime 1.25 CPU, plus 8 texts (up to 512 tokens) in Chrome 152 with Transformers.js 4.3.0 / ORT Web 1.31-dev on an RTX 5060 (WebGPU) and on WASM. Full report, scripts and raw results: [deposium-turbov3 `docs/2026-09-17-browser-embedding-t1-weight-only-reexport.md`](https://github.com/theseedship/deposium-turbov3/blob/main/docs/2026-09-17-browser-embedding-t1-weight-only-reexport.md).

Why the residual pre-scaling: the residual stream of pplx-embed-v1 reaches 2.6e5 at 512 tokens, above the fp16 maximum (65 504), so a plain fp16 conversion returns NaN on WebGPU for many inputs. Dividing the embedding table, `o_proj` and `down_proj` weights by 16 and the residual RMSNorm epsilons by 256 leaves every RMSNorm output, hence `last_hidden_state`, mathematically unchanged (fused fp32 graph bit-identical to the original) while keeping the residual below ~2e4.

4-bit variants (MatMulNBits symmetric / asymmetric / HQQ, with fp32 or int8 activations) were all measured at 0.905-0.912 against FP32 and are not published.

## Usage — Transformers.js 4.x (browser)

```javascript
import { pipeline, mean_pooling } from '@huggingface/transformers'

const MODEL = 'tss-deposium/pplx-embed-v1-0.6b-onnx-int8-standard'
const REVISION = '<pin the commit sha you qualified>'

// WebGPU with fp16 support -> fp16 (or model_int8f16 for a lighter file); otherwise WASM + int8.
const adapter = await navigator.gpu?.requestAdapter()
const webgpuF16 = !!adapter?.features.has('shader-f16')
const opts = webgpuF16
  ? { device: 'webgpu', dtype: 'fp16' }                                   // onnx/model_fp16.onnx
  // ? { device: 'webgpu', dtype: 'fp32', model_file_name: 'model_int8f16' } // onnx/model_int8f16.onnx
  : { device: 'wasm', dtype: 'int8' }                                     // onnx/model_int8.onnx (never fp16 on WASM: 1.2 GB single file exhausts the WASM heap)

const ex = await pipeline('feature-extraction', MODEL, { revision: REVISION, ...opts })

// pipeline() does not truncate at 512 tokens (tokenizer.model_max_length is 131072): tokenize explicitly to match the server.
const enc = ex.tokenizer(['Your text here'], { padding: true, truncation: true, max_length: 512 })
const out = await ex.model(enc)
let hs = out.last_hidden_state
if (hs.type !== 'float32') hs = hs.to('float32')          // fp16 sessions return a float16 tensor
const pooled = mean_pooling(hs, enc.attention_mask)        // [batch, 1024]
const v = Array.from(pooled.data.slice(0, 256))            // MRL 256
const norm = Math.hypot(...v)
const embedding = v.map((x) => x / norm)                   // L2 normalized
```

Notes: the default `dtype` on WASM is `q8` and on WebGPU `fp32`, so always pass `dtype` explicitly; a misspelled `dtype` silently falls back to the default file. `int8` and `fp16` accept batched inputs; the legacy `q8` file does not. The browser cache key includes the revision.

## Usage — Python (ONNX Runtime)

```python
import onnxruntime as ort, numpy as np
from tokenizers import Tokenizer
tok = Tokenizer.from_file("tokenizer.json"); tok.enable_truncation(max_length=512); tok.no_padding()
sess = ort.InferenceSession("onnx/model_int8.onnx")
ids = np.array([tok.encode("Your text").ids], dtype=np.int64)
h = sess.run(["last_hidden_state"], {"input_ids": ids, "attention_mask": np.ones_like(ids)})[0][0]
e = h.mean(0); e = e / np.linalg.norm(e); e = e[:256]; e = e / np.linalg.norm(e)
```

## Files

```
onnx/model_int8.onnx        667 MB  WASM        (single file)
onnx/model_fp16.onnx      1 194 MB  WebGPU      (single file)
onnx/model_int8f16.onnx     639 MB  WebGPU light (single file, custom name)
onnx/model.onnx             602 MB  legacy q8   (deprecated, kept for backward compatibility)
onnx/model_quantized.onnx   602 MB  legacy q8   (same bytes as model.onnx)
config.json                          model config + transformers.js_config.model_file_name = "model"
tokenizer.json / tokenizer_config.json
```

`tokenizer.json` carries a fixed `padding` block (32, pad id 151643) inherited from the first export; token ids are identical to the official tokenizer for single inputs and Transformers.js applies its own padding.

## Revision history

- `a18fdffe` (2026-04): `quantize_dynamic` q8 export (`onnx/model.onnx`, `onnx/model_quantized.onnx`).
- `2d8b714b` (2026-09-17): + `onnx/model_int8.onnx` (WASM) and a first `onnx/model_fp16.onnx` that overflowed on WebGPU.
- next commit (2026-09-17): `onnx/model_fp16.onnx` replaced by the residual-pre-scaled version; + `onnx/model_int8f16.onnx`.

## Citation

Base model: [pplx-embed-v1](https://huggingface.co/perplexity-ai/pplx-embed-v1-0.6B) by Perplexity AI. Paper: [arxiv.org/abs/2602.11151](https://arxiv.org/abs/2602.11151).

Re-exports for Transformers.js compatibility by [Deposium](https://deposium.ai).
