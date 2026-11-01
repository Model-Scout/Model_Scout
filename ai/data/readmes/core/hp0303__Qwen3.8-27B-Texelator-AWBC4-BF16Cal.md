---
language:
- en
- ko
license: apache-2.0
library_name: transformers
base_model: Qwen/Qwen3.8-27B
tags:
- texelator
- bc4
- aw-bc4
- text-generation
---

# Qwen3.8-27B Texelator AW-BC4 (BF16 calibrated, SM120)

This is the standalone Texelator artifact for Qwen3.8-27B, encoded from the
original BF16 checkpoint with activation-aware, hardware-exact BC4 PTQ. It is
intended for the Texelator v0.3 runtime on NVIDIA RTX 50-series GPUs with compute
capability 12.0 and a matching measured BC4 palette hash.

Runtime: <https://github.com/hp0303/Texelator>

## Use

```bash
texelator pull qwen3.8:27b
texelator benchmark qwen3.8:27b
texelator run qwen3.8:27b
```

The one-time benchmark is mandatory. It selects correctness-checked decode
lookahead and BF16 prefill tiles for the actual GPU.

## Numerical and hardware scope

- Source and calibration dtype: BF16
- Runtime activation/output dtype: BF16
- Accumulation: FP32
- Weight payload: 8-byte BC4 per 16 weights plus one FP32 scale per output row
- Calibration: WikiText-2 train, 8,192 tokens
- Validated target: NVIDIA RTX 5080, compute capability 12.0
- Palette SHA256: `34670bd1c521c26b14ea88ed6f2d8f16c55720f20915909ac621dcabe0f3ed47`

Texelator verifies the local GPU's hardware reconstruction palette before loading
this artifact. It will fail rather than run on a mismatched palette or architecture.

## Prefill modes

BF16 CUTLASS Texture IteratorB prefill is the production default. Texelator v0.3
also includes an opt-in `--prefill-mode fp4` research path. FP4 is faster in the
reported 512-token experiment but is not quality-equivalent to BF16 and should not
be used when output fidelity is required.

## License

The upstream Qwen model license and acceptable-use terms continue to apply. The
Texelator runtime is MIT licensed.
