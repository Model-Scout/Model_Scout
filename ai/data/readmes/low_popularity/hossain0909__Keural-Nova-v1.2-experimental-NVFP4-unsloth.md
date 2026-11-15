---
license: apache-2.0
base_model: mkd-hossain/Keural-Nova-v1.2-experimental
language: [ko, en]
pipeline_tag: text-generation
library_name: transformers
tags: [keural, keural-nova, mkd, nvfp4, fp4, fp8, mixed-precision, quantized, compressed-tensors, vllm, blackwell, moe, qwen3]
---

# Keural Nova v1.2 — NVFP4 (unsloth mixed-precision recipe)

**Mixed-precision NVFP4 quantization of [Keural Nova v1.2](https://huggingface.co/mkd-hossain/Keural-Nova-v1.2-experimental)**,
by **[MKD](https://mkd.kr)**, for high-throughput serving on **NVIDIA Blackwell** via **vLLM**.

Replicates the **`unsloth/Qwen3.6-35B-A3B-NVFP4`** recipe — a *dynamic* mixed FP8/FP4 scheme that
keeps accuracy-sensitive layers at higher precision. This is the **most accuracy-preserving** of
our NVFP4 builds. (A pure-NVFP4 variant is at
[`Keural-Nova-v1.2-experimental-NVFP4`](https://huggingface.co/mkd-hossain/Keural-Nova-v1.2-experimental-NVFP4).)

- **67 GB (bf16) → 24.8 GB** — slightly larger than pure NVFP4 because sensitive layers stay FP8.
- Format: **`compressed-tensors` / mixed-precision** → served natively by vLLM.

## The recipe (exactly unsloth's)
| Precision | Layers |
|---|---|
| **FP8** (8-bit) | attention (q/k/v/o), linear-attn projections (in_proj_qkv/z, out_proj), lm_head, **last 8 layers' experts (32–39)** |
| **FP4** (NVFP4, 4-bit) | the first 32 layers' experts + shared experts (the bulk) |
| **High-precision (bf16)** | linear-attn in_proj_a/b/norm, router gates (`mlp.gate`, `shared_expert_gate`), **vision tower**, **MTP** |

Verified coverage: layer-0 experts FP4, layer-32 experts FP8, all listed sensitive layers bf16.

## ⚠️ Hardware
FP4 tensor cores exist only on **Blackwell (B200 / GB200 / RTX 50xx)** — serve there for the
speed/memory benefit (Hopper lacks FP4 kernels).

## Serving (vLLM on Blackwell)
```bash
vllm serve mkd-hossain/Keural-Nova-v1.2-experimental-NVFP4-unsloth \
  --served-model-name Keural-Nova-v1.2 \
  --tensor-parallel-size 2 --max-model-len 262144 \
  --tool-call-parser qwen3_xml --enable-auto-tool-choice
```
Non-thinking default; Qwen XML tool calls; native 256K for agents (YaRN only for >256K). Multimodal works.

## Quantization details
- **Tool:** `llm-compressor` (compressed-tensors), using unsloth's exact `config_groups` + `ignore`.
- **Calibration:** 512 samples from the Keural Nova v1.2 SFT mix, seq-len 2048.

## Accuracy
Mixed FP8/FP4 keeps the most sensitive layers (linear-attn, gates, attention, final-layer experts)
in higher precision, so this typically loses **less** than pure NVFP4 — the same design as unsloth's
public checkpoint. **Validate on Blackwell** with `scripts/nvfp4_verify_vllm.py` against the
[bf16 base](https://huggingface.co/mkd-hossain/Keural-Nova-v1.2-experimental).

## License & attribution
Apache-2.0, inheriting the base **Qwen/Qwen3.6-35B-A3B** license. Recipe after
`unsloth/Qwen3.6-35B-A3B-NVFP4`. "Keural Nova" is a model by MKD.
