---
license: apache-2.0
base_model: Qwen/Qwen3.6-27B
base_model_relation: quantized
library_name: transformers
tags:
  - qwen3_5
  - qwen3.6
  - nvfp4
  - quantized
  - modelopt
  - mtp
  - speculative-decoding
  - blackwell
  - text-only
pipeline_tag: text-generation
language:
  - en
  - zh
  - ja
  - ko
  - fr
  - de
  - es
  - it
  - pt
  - ru
  - ar
---

# Qwen3.6-27B-Text-NVFP4-MTP

NVFP4-quantized text-only sibling of [`Qwen/Qwen3.6-27B`](https://huggingface.co/Qwen/Qwen3.6-27B), with the **MTP (Multi-Token Prediction) head restored in bf16** so speculative decoding actually works.

## What's different from `sakamakismile/Qwen3.6-27B-NVFP4`

| | This repo (`-Text-NVFP4-MTP`) | `Qwen3.6-27B-NVFP4` |
|---|---|---|
| Quantization format | **`modelopt`** (vLLM SM120 native path) | `compressed-tensors` |
| MTP head | **Restored in bf16, working** | Dropped during export → 0% draft acceptance |
| Vision tower | **Stripped (text-only)** | Present (kept for VLM use) |
| Suggested launch | with `--speculative-config` | without speculation |

The original `Qwen3.6-27B-NVFP4` is left untouched so existing users (~15K downloads) are not disrupted. This is a focused text-only sibling for users who want maximum speed and don't need vision input.

## Why this exists

Two HF Discussion threads on the original repo prompted this:

- [#5 — slower than official FP8 on Blackwell](https://huggingface.co/sakamakismile/Qwen3.6-27B-NVFP4/discussions/5) — root cause is the `compressed-tensors` NVFP4 path being slower than `modelopt` on Blackwell SM120; this repo uses `modelopt` natively.
- [#7 — MTP not responding](https://huggingface.co/sakamakismile/Qwen3.6-27B-NVFP4/discussions/7) — `AutoModelForCausalLM.from_pretrained` does not load the MTP head, so it gets dropped during quantization, leading to 0% draft acceptance. This repo grafts the 15 `mtp.*` tensors (bf16) back into the quantized checkpoint and adds them to the quantization ignore list.

Recipe is adapted from [`osoleve/Qwen3.5-27B-Text-NVFP4-MTP`](https://huggingface.co/osoleve/Qwen3.5-27B-Text-NVFP4-MTP) — credit and thanks.

## Reproduce this quantization

This model was produced by the open-source [`lna-lab/GGUF-to-NVFP4-SM120`](https://github.com/lna-lab/GGUF-to-NVFP4-SM120) pipeline — Lna-Lab's production line for converting Qwen3.5 / 3.6 / Gemma 4 checkpoints into modelopt-format NVFP4 + working MTP, ready for vLLM on Blackwell SM120. The exact script is [`src/quantize/qwen36_27b_text_mtp.py`](https://github.com/lna-lab/GGUF-to-NVFP4-SM120/blob/main/src/quantize/qwen36_27b_text_mtp.py); the 5-step MTP graft recipe is documented in [`docs/MTP_GRAFT_RECIPE.md`](https://github.com/lna-lab/GGUF-to-NVFP4-SM120/blob/main/docs/MTP_GRAFT_RECIPE.md).

## Quantization details

- **Base**: `Qwen/Qwen3.6-27B` (bf16, 27.78B params, hybrid linear-attn + full-attn, 64 layers, 1 MTP layer)
- **Quantizer**: `nvidia-modelopt` 0.43.0 with `NVFP4_DEFAULT_CFG`
- **Calibration**: 20 samples from `neuralmagic/calibration` (LLM split), max_seq_len 8192
- **Ignored from quantization** (kept in bf16):
  - `lm_head`
  - All `model.visual.*` (vision tower) — then **physically deleted** in the text-only build
  - All `*linear_attn.conv1d*` (Mamba-style SSM convolutions, 48 of the 64 layers)
  - All `mtp.*` modules (the 1-layer MTP head: 15 tensors total, ~850 MB bf16)
  - Other defaults from `NVFP4_DEFAULT_CFG`: `*router*`, `*mlp.gate.*`, `*block_sparse_moe.gate*`, `*output_layer*`

## Usage with vLLM (Blackwell, SM120)

### Recommended production launch — 256K context · KV FP8 · MTP n=3 · max-num-seqs 2

```bash
vllm serve sakamakismile/Qwen3.6-27B-Text-NVFP4-MTP \
    --trust-remote-code \
    --quantization modelopt \
    --language-model-only \
    --max-model-len 262144 \
    --max-num-seqs 2 \
    --kv-cache-dtype fp8 \
    --gpu-memory-utilization 0.9 \
    --reasoning-parser qwen3 \
    --speculative-config '{"method":"qwen3_5_mtp","num_speculative_tokens":3}'
```

This is the production launch on a single RTX PRO 6000 Blackwell — full 256K context, two concurrent slots, KV FP8 for concurrency headroom. The four flags that are easy to skip but matter:

- **`--max-model-len 262144`** — full 256K context (Qwen3.6 trained max).
- **`--kv-cache-dtype fp8`** — halves KV memory; lifts max concurrency at 256K from ~4× (BF16, won't fit) to **7.0×** with the same VRAM. ~5–10 % per-token decode overhead, more than paid back by capacity.
- **`--max-num-seqs 2`** — load-bearing. `--max-num-seqs 4` plus `--kv-cache-dtype fp8` plus `--speculative-config n=3` plus `--max-model-len 262144` will silently OOM during cuda-graph capture on this build of vLLM (0.19.1rc1).
- **`num_speculative_tokens: 3`** — vLLM applies the single MTP layer (`mtp_num_hidden_layers=1`) recursively three times per draft pass. Per-position acceptance ~87 / 72 / 61 %, mean accepted-length ≈ 3.0 / 4.0. The `qwen3_5_mtp` handler is internally normalized to `mtp` (deprecated-name warning is harmless).

The `mtp.fc` weight is kept in **bf16** in the safetensors (not NVFP4) — equivalent to the Lorbus-style "dequantize the fusion layer in the file" trick applied to NVFP4 instead of AutoRound. Side effect of the `*mtp*` ignore entry in the modelopt config, but load-bearing for the n=3 throughput.

### Smaller-context launch (16K, no fp8) — fastest single-request decode

```bash
vllm serve sakamakismile/Qwen3.6-27B-Text-NVFP4-MTP \
    --trust-remote-code \
    --gpu-memory-utilization 0.85 \
    --max-model-len 8192 \
    --language-model-only \
    --quantization modelopt \
    --reasoning-parser qwen3 \
    --speculative-config '{"method":"qwen3_5_mtp","num_speculative_tokens":3}'
```

## Verified throughput vs the family baseline (RTX PRO 6000 Blackwell, vLLM 0.19.1rc1)

Same 256K + KV FP8 + max-num-seqs 2 production launch, T = 0:

| Repo | Format | MTP | Single (S/M/L) | 2-parallel agg (M/L) | vs baseline |
|---|---|---|---|---|---|
| [`Qwen3.6-27B-NVFP4`](https://huggingface.co/sakamakismile/Qwen3.6-27B-NVFP4) (the family baseline) | `compressed-tensors` | ❌ | 56 / 59 / 59 | 119 / 119 | 1.0× |
| **`Qwen3.6-27B-Text-NVFP4-MTP`** (this repo) | `modelopt` | ✅ n=3 | **104 / 98 / 100** | **189 / 207** | **1.67× / 1.74×** |
| [`Carnice-V2-27b-NVFP4-TEXT-MTP`](https://huggingface.co/sakamakismile/Carnice-V2-27b-NVFP4-TEXT-MTP) | `modelopt` | ✅ n=3 | 107 / 98 / 102 | 193 / 194 | 1.68× / 1.63× |
| [`Huihui-Qwen3.6-27B-abliterated-NVFP4-TEXT-MTP`](https://huggingface.co/sakamakismile/Huihui-Qwen3.6-27B-abliterated-NVFP4-TEXT-MTP) | `modelopt` | ✅ n=3 | 117 / 96 / 101 | 203 / 183 | 1.65× / 1.54× |
| [`Huihui-Qwen3.6-27B-abliterated-NVFP4-MTP`](https://huggingface.co/sakamakismile/Huihui-Qwen3.6-27B-abliterated-NVFP4-MTP) (VLM) | `modelopt` | ✅ n=3 | 118 / 97 / 100 | 183 / 198 | 1.66× / 1.66× |

(S = 50-token, M = 350-token, L = 700-token decodes.)

This repo lands at **1.74× the baseline's 2-parallel aggregate throughput** on long-form decodes (207 tok/s vs 119) — the gain comes from two compounding fixes:

- **`modelopt` NVFP4 export** — vLLM's native fast path on Blackwell SM120, vs the `compressed-tensors` slow fallback the baseline lands on.
- **bf16-restored MTP head + `num_speculative_tokens=3`** — single MTP layer applied recursively for ~1.9× decode multiplier via speculative decoding.

KV cache size at 256K + fp8: **491,200 tokens** → max concurrency 6.98× per request at full 256K. Mean acceptance length 1.93 / 2.0 at n=1, ~3.0 / 4.0 at n=3.

### Smaller-context single-request bench (16K, no fp8)

| Prompt | Tokens | n=1 tok/s | **n=3 tok/s** |
|---|---|---|---|
| Short (50 tok) | 50 | ~71 | **132.5** |
| Medium (350 tok) | 350 | ~85 | **105.5** |
| Long-form (700 tok) | 700 | ~85 | **106.5** |

GPU memory at load: ~15 GB.

## Hardware target

Built and tested on **NVIDIA RTX PRO 6000 Blackwell (SM120)**. Should also work on **RTX 5090** and other Blackwell consumer/workstation cards with sufficient VRAM (the model is roughly 14 GB after NVFP4 + ~850 MB of bf16 MTP/conv1d/lm_head).

## Acknowledgements

- [`osoleve`](https://huggingface.co/osoleve) — for the MTP-restoration recipe on Qwen3.5
- [`Qwen`](https://huggingface.co/Qwen) — for the base model
- [`nvidia-modelopt`](https://github.com/NVIDIA/TensorRT-Model-Optimizer) team
- The reporters of Discussions #5 and #7 — for catching this cleanly

## Support the Base Model Authors

If you find this model useful, please consider supporting:

- **Qwen Team** (original model): [Star the Qwen repo](https://huggingface.co/Qwen/Qwen3.6-27B)

## License

This model inherits the Apache 2.0 license.
