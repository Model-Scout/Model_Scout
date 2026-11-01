---
license: apache-2.0
base_model: tencent/Hy-MT2-1.8B
base_model_relation: quantized
pipeline_tag: translation
library_name: mlx
tags:
  - mlx
  - apple-silicon
  - quantized
  - ternary
  - sherry
  - stq1_0
  - hunyuan
  - machine-translation
language:
  - zh
  - en
  - ko
  - ja
  - fr
  - es
  - pt
  - de
  - it
  - ru
  - ar
  - th
  - vi
  - id
  - ms
  - tr
  - pl
  - cs
  - nl
  - uk
  - hi
---

# Hy-MT2-1.8B · 1.25-bit · MLX

The same weights as
[`AngelSlim/Hy-MT2-1.8B-1.25Bit-GGUF`](https://huggingface.co/AngelSlim/Hy-MT2-1.8B-1.25Bit-GGUF),
converted **losslessly** for [MLX](https://github.com/ml-explore/mlx):
[Hy-MT2-1.8B](https://huggingface.co/tencent/Hy-MT2-1.8B) — Tencent's
33-language translation model, in its official 1.25-bit QAT checkpoint
(*Sherry*, ggml type `STQ1_0`) — running on the Apple-Silicon GPU. The runtime
is [**hy-mt2-mlx**](https://github.com/kuotient/hy-mt2-mlx): the model ships
its own decoder (`sherry_model.py`, loaded via mlx-lm's `model_file` hook), so
vanilla `mlx-lm` runs it with zero extra code.

The upstream checkpoint exists only as a GGUF with CPU-only (NEON) kernels in
an unmerged llama.cpp PR. This artifact is that checkpoint on the GPU:

| path (M2 Pro) | decode | prefill @207 tok | peak mem | weights |
|---|---|---|---:|---:|
| llama.cpp CPU, 8 threads (NEON) | 98 tok/s | 313 tok/s | — | 462 MB GGUF |
| **this artifact — MLX 1.31-bit native** | **136** | **1020** | **0.59 GB** | **455 MB** |
| MLX 2-bit transcode (same weights, via converter) | 150 | 1220 | 1.09 GB | 745 MB |

Methodology and full conditions: [hy-mt2-mlx `docs/benchmarks.md`](https://github.com/kuotient/hy-mt2-mlx/blob/main/docs/benchmarks.md).

## Use

```bash
pip install mlx-lm

mlx_lm.generate --model kuotient/Hy-MT2-1.8B-1.25Bit-MLX \
  --prompt "Translate the following segment into Korean, without additional explanation.

The quarterly results exceeded expectations, but the team remains cautious."
```

The chat template (bundled) wraps the prompt in Hy-MT's expected markers.
Decode runs a custom Metal GEMV over the packed 1.31-bpw stream; multi-token
prefill dequantizes one layer at a time into the stock matmul. Weights stay
1.31 bpw resident. If you prefer maximum speed over the memory savings,
convert the source GGUF with hy-mt2-mlx's `convert.py` instead — the same
weights transcode losslessly into MLX's stock affine 2-bit kernels.

## What "lossless" means here

Sherry is quantization-aware-trained: the released GGUF *is* the trained
weight grid, so no re-quantization is involved —

- all **224 STQ1_0 linear tensors are preserved bit-exact** (the sparse-ternary
  grid travels verbatim and is decoded by the bundled kernel);
- the tied **embedding** (Q6_K in the GGUF) is re-quantized to 6-bit affine —
  the only approximation, Q6_K-class fidelity;
- norms are fp16.

Greedy outputs matched llama.cpp's reference CPU implementation
token-for-token (5/5) in the parity suite
([`scripts/parity.py`](https://github.com/kuotient/hy-mt2-mlx/blob/main/scripts/parity.py)).

## Provenance

- Source: [`AngelSlim/Hy-MT2-1.8B-1.25Bit-GGUF`](https://huggingface.co/AngelSlim/Hy-MT2-1.8B-1.25Bit-GGUF)
  · `Hy-MT2-1.8B-1.25Bit.gguf` ·
  sha256 `cc497fe8f033b52b3b8b00a7669e9661435432f9d4cd43f7ed24400c01507a93`
- Converter: [hy-mt2-mlx](https://github.com/kuotient/hy-mt2-mlx)
  `python -m sherry_mlx.convert_native --gguf Hy-MT2-1.8B-1.25Bit.gguf --ref <tencent/Hy-MT2-1.8B json files> --out <dir> --embed-bits 6`
- Config/tokenizer files come from the original
  [`tencent/Hy-MT2-1.8B`](https://huggingface.co/tencent/Hy-MT2-1.8B) repo.

## License & attribution

Apache-2.0, matching both upstream repos. The model, the Sherry quantization
scheme (arXiv 2601.07892) and the Hy-MT2 weights (arXiv 2605.22064) are
Tencent's ([Hunyuan](https://github.com/Tencent-Hunyuan) /
[AngelSlim](https://github.com/Tencent/AngelSlim)); the STQ1_0 format
reference is [llama.cpp PR #22836](https://github.com/ggml-org/llama.cpp/pull/22836).
This repo only moves those weights to a new backend — see the
[hy-mt2-mlx](https://github.com/kuotient/hy-mt2-mlx) NOTICE for full
attribution.
