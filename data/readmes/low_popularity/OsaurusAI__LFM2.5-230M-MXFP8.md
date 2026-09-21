---
license: other
license_name: lfm1.0
license_link: LICENSE
base_model: LiquidAI/LFM2.5-230M
pipeline_tag: text-generation
library_name: mlx
language: [en, ar, zh, fr, de, ja, ko, es]
tags: [lfm2, lfm2.5, liquid, hybrid, conv, mlx, mxfp8, osaurus]
---

![Osaurus](osaurus-x-banner.png)

# LFM2.5-230M · MXFP8

Official **OsaurusAI** MXFP8 build of [LiquidAI/LFM2.5-230M](https://huggingface.co/LiquidAI/LFM2.5-230M) (LFM Open License v1.0) — Liquid AI's **230M** tiny hybrid model. Near-lossless 8-bit microscaled FP; runs on Apple Silicon via [Osaurus](https://osaurus.ai) / mlx_lm.

- **~231 MB** bundle (down from ~459 MB bf16) — small enough for the most constrained on-device use.
- **MXFP8**: microscaled FP8 (group-size 32) on the linear weights; short-conv kernels and norms kept fp16.
- **Text-only**, multilingual (en, ar, zh, fr, de, ja, ko, es).

## Architecture

| | |
|---|---|
| Family | `lfm2` (hybrid) |
| Layers | 14 — **8 short-conv (LIV)** + **6 full-attention** |
| Hidden | 1024 · vocab 65536 · tied embeddings |
| Cache | hybrid (conv state + KV for attention layers) |
| Tools | Liquid Python-call format (`lfm2` tool parser) |

The short-conv (LIV) layers (`conv.conv` kernel + `conv.in_proj`/`conv.out_proj`) interleave with full-attention layers — verified coherent generation in mlx_lm after quantization.

## Usage
```bash
python -m mlx_lm generate --model OsaurusAI/LFM2.5-230M-MXFP8 --prompt "What is the capital of France?"
```
Or load in [Osaurus](https://osaurus.ai) for a local, no-setup agent loop.

## Provenance
- Base: [LiquidAI/LFM2.5-230M](https://huggingface.co/LiquidAI/LFM2.5-230M) © Liquid AI — LFM Open License v1.0 (see `LICENSE`)
- Quantization: Osaurus · MXFP8 (microscaled FP8, group-size 32) · eric@osaurus.ai
