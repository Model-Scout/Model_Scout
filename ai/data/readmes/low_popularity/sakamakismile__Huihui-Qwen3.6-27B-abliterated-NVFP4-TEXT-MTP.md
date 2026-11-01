---
license: apache-2.0
base_model: huihui-ai/Huihui-Qwen3.6-27B-abliterated
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
  - abliterated
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

# Huihui-Qwen3.6-27B-abliterated-NVFP4-TEXT-MTP

**Text-only** NVFP4-quantized abliterated sibling of [`Qwen/Qwen3.6-27B`](https://huggingface.co/Qwen/Qwen3.6-27B), with the **MTP (Multi-Token Prediction) head preserved in bf16** so speculative decoding works.

Vision tower is **removed** (333 tensors / ~0.92 GB stripped) — pure-text inference only. If you need image / video input, use the VLM sibling below.

## Headline performance (1 × RTX PRO 6000 Blackwell, vLLM 0.19.1rc1)

- 🚀 **Aggregate 200+ tok/s on a single GPU** with two concurrent sessions at full **256K context** (KV FP8 + MTP n=3): **202.8 tok/s** at 350-token decodes, 183.1 tok/s at 700-token decodes — production-grade serving from one Blackwell card.
- ⚡ **135 tok/s single-request decode** at the smaller 16K BF16-KV configuration — fastest of our Qwen3.6 family of NVFP4 + MTP releases.
- 🎯 **256K context ceiling, 7× concurrency budget** at full 256K with KV FP8 (KV cache holds 491,200 tokens on a 96 GB Blackwell card).
- 🟢 vLLM-ready, full launch flags below.

## Sibling repos

| | This repo (text-only) | VLM sibling | Original VLM (compressed-tensors) |
|---|---|---|---|
| Repo | **`Huihui-Qwen3.6-27B-abliterated-NVFP4-TEXT-MTP`** | [`Huihui-Qwen3.6-27B-abliterated-NVFP4-MTP`](https://huggingface.co/sakamakismile/Huihui-Qwen3.6-27B-abliterated-NVFP4-MTP) | [`Huihui-Qwen3.6-27B-abliterated-NVFP4`](https://huggingface.co/sakamakismile/Huihui-Qwen3.6-27B-abliterated-NVFP4) |
| Vision input | ❌ text-only | ✅ image + video | ✅ |
| File size | **~19.6 GB** | ~20.6 GB | similar |
| Quantization format | `modelopt` | `modelopt` | `compressed-tensors` |
| MTP head | ✅ bf16, working | ✅ bf16, working | ❌ dropped → 0% acceptance |
| Abliterated | ✅ (huihui-ai base) | ✅ (huihui-ai base) | ✅ |
| Architecture | `Qwen3_5ForConditionalGeneration` (text-only mode) | `Qwen3_5ForConditionalGeneration` | `Qwen3_5ForConditionalGeneration` |

## What's different from the VLM parent

This repo was **derived** from `Huihui-Qwen3.6-27B-abliterated-NVFP4-MTP` by physically dropping the vision tower tensors from the safetensors archive, **without re-quantizing**. All NVFP4-quantized language-model weights and the bf16 MTP head are bit-for-bit identical to the parent.

What was removed:

- **`model.visual.*`** — 333 vision tower tensors (BF16-preserved in parent, stripped here)
- **`model.embed_vision*`** — vision embedding projection

`preprocessor_config.json` and `video_preprocessor_config.json` are kept for
loader compatibility (vLLM's `AutoProcessor` lookup), but the corresponding
vision weights are gone — sending image input will fail.

What was kept:

- All NVFP4 language-model weights (LM, attention, MoE-style FFNs)
- BF16 MTP head (15 `mtp.*` tensors)
- BF16 `linear_attn.conv1d` (Mamba-style SSM convolutions)
- `lm_head` BF16
- Tokenizer, chat template, generation_config

The slim was performed by [`slim_qwen36_27b_text_mtp.py`](https://github.com/lna-lab/blackwell-geforce-nvfp4-gemm) — single-pass safetensors filter, no recompute.

## Why a text-only variant?

The VLM parent is a multimodal model: when used for pure-text workloads, the
~1 GB of bf16 vision-tower weights occupy VRAM with no benefit. This variant
removes that surface so:

- **Smaller VRAM footprint at load** (~0.92 GB freed)
- **Faster startup** (no vision encoder init)
- **Lighter image footprint** when bundled in containers
- Same MTP-driven decode speed as the VLM parent

Use this when you know you don't need image/video input. Use the VLM parent when you do.

## Why "Unsensor"?

This is the abliterated counterpart of our text-only release. The intent (per the
maintainer's [philosophy](https://huggingface.co/sakamakismile)) is **not "remove
the chains" but "remove the colored glasses"** — let the model observe and reason
neutrally, without the strong refusal-shaped priors learned during alignment.
You're expected to use it responsibly.

## Quantization details (inherited unchanged from parent)

- **Base**: `huihui-ai/Huihui-Qwen3.6-27B-abliterated` (bf16, 27.78B params,
  hybrid linear-attn + full-attn, 64 layers, 1 MTP layer)
- **Quantizer**: `nvidia-modelopt` 0.43.0 with `NVFP4_DEFAULT_CFG`
- **Calibration**: 20 samples from `neuralmagic/calibration` (LLM split),
  max_seq_len 8192
- **Ignored from quantization** (kept in bf16):
  - `lm_head`
  - All `*linear_attn.conv1d*` (Mamba-style SSM convolutions, 48 of 64 layers)
  - All `mtp.*` modules (15 tensors, ~850 MB bf16)
  - Other `NVFP4_DEFAULT_CFG` defaults (router, mlp.gate, output_layer …)

(Vision-related ignore entries from the parent's `hf_quant_config.json` are
removed here since the corresponding tensors no longer exist.)

## Usage with vLLM (Blackwell, SM120)

### Recommended production launch — 256K context, KV FP8, n=3 MTP

```bash
vllm serve sakamakismile/Huihui-Qwen3.6-27B-abliterated-NVFP4-TEXT-MTP \
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

This is what we run in production on a single RTX PRO 6000 Blackwell. The four flags that are easy to skip but matter:

- **`--max-model-len 262144`** — full 256K context. The Qwen3.6 family declares 262K as the trained max, and at NVFP4 weights + fp8 KV the budget fits comfortably on a 96 GB Blackwell card.
- **`--kv-cache-dtype fp8`** — halves KV memory, lifts maximum concurrency at 256K from ~4× (BF16, won't fit) to **7.0×** with the same VRAM. Per-token decode pays a small overhead (~5–10 % vs BF16 KV), the trade is worth it on long-context workloads.
- **`--max-num-seqs 2`** — the load-bearing number. `--max-num-seqs 4` plus `--kv-cache-dtype fp8` plus `--speculative-config n=3` plus `--max-model-len 262144` will silently OOM during cuda-graph capture on this build of vLLM (0.19.1rc1). Two in-flight slots is the sweet spot for a single-card deployment; if you have a multi-GPU box, run one instance per GPU at `--max-num-seqs 2` rather than one large instance.
- **`num_speculative_tokens: 3`** — vLLM applies the single MTP layer (`mtp_num_hidden_layers=1`) recursively three times per draft pass; per-position acceptance ~87 / 72 / 61 % at positions 1 / 2 / 3 lands mean accepted-length around 3.0, which is what unlocks the 100+ tok/s rate. `num_speculative_tokens: 1` is a safer fallback if you hit a draft-path bug.

The `qwen3_5_mtp` handler is internally normalized to `mtp` by current vLLM (deprecated-name warning is harmless).

Send a chat request:

```bash
curl http://localhost:8000/v1/chat/completions -H 'Content-Type: application/json' -d '{
  "model": "sakamakismile/Huihui-Qwen3.6-27B-abliterated-NVFP4-TEXT-MTP",
  "messages": [{"role": "user", "content": "Explain attention sinks in 200 words."}],
  "max_tokens": 400
}'
```

### Multi-GPU + KV FP8 (high-throughput serving)

For aggregate throughput on a 6-GPU Blackwell box, **one instance per GPU with
`--max-num-seqs 2` and `--kv-cache-dtype fp8`** is the practical layout:

```bash
for gpu in 0 1 2 3 4 5; do
  CUDA_VISIBLE_DEVICES=$gpu vllm serve <repo> \
      --trust-remote-code \
      --gpu-memory-utilization 0.85 \
      --kv-cache-dtype fp8 \
      --max-model-len 8192 \
      --max-num-seqs 2 \
      --quantization modelopt \
      --reasoning-parser qwen3 \
      --speculative-config '{"method":"qwen3_5_mtp","num_speculative_tokens":3}' \
      --port $((8002 + gpu)) &
done
```

This gives **12 in-flight requests max** across the 6 GPUs (= 6 × 2)
and lets vLLM's continuous batching share the MTP draft path between
the two slots on each GPU.

KV FP8 introduces no measurable quality regression on the Qwen3.5/3.6
family.

> **Why not 2 vLLM instances per GPU?** vLLM V1 cannot reliably share
> a single GPU between two processes — each instance accounts for the
> *entire* GPU's free memory, so two simultaneous instances both
> reserve overlapping pools and OOM during cuda-graph capture. RTX PRO
> 6000 Blackwell *Workstation* Edition does not expose MIG either, so
> the practical ceiling is one vLLM per GPU.

## Verified locally (RTX PRO 6000 Blackwell, vLLM 0.19.1rc1)

### Production config — 256K context · KV FP8 · MTP n=3 · max-num-seqs 2

Single + 2-session-parallel decode, T = 0:

| Prompt | Single tok/s | **2-parallel agg tok/s** | per-request |
|---|---|---|---|
| Short (50 tok) | 116.6 | 68.5 | 34.3 (latency-bound) |
| Medium (350 tok) | 96.4 | **202.8** | 101.4 |
| Long-form (700 tok) | 101.3 | **183.1** | 91.5 |

KV cache size at 256K + fp8: **491,200 tokens** → **maximum concurrency 6.98×** at full 256K context. Available KV memory: 63.97 GiB on a 96 GB Blackwell card. Per-token decode pays ~5–10 % vs BF16 KV but the context capacity and concurrent-request headroom more than compensate.

### Smaller-context configuration (16K, BF16 KV) — fastest single-request decode

Single-request decode, T = 0, 9 runs across 3 prompt lengths:

| Prompt | Tokens | n=1 tok/s | **n=3 tok/s** |
|---|---|---|---|
| Short (50 tok) | 50 | ~71 | **135.3** |
| Medium (350 tok) | 350 | ~85 | **112.2** |
| Long-form (700 tok) | 700 | ~85 | **108.8** |

→ **100+ tok/s on every prompt length, fastest among our Qwen3.6 family
NVFP4-MTP releases** (Carnice 134/102/103, Qwen3.6 base 132/105/106 on the
same hardware). The abliterated body appears to give marginally smoother
hidden states for the recursive MTP draft pass, lifting acceptance enough
to land here. GPU memory at load: ~20 GB. Use this configuration when
short interactive latency matters more than context length or
concurrency.

Quality smoke test (T = 0):

- Factual + format-strict: "Helium, Neon, Argon, Krypton, Xenon" ✓
- Multi-step arithmetic ($147 split, third pays the rest): $47, 47/147, with
  prime factorisation note ✓
- Japanese, format-strict (富士山標高 integer-only): `3776` ✓

The language path is bit-identical to the VLM parent
(`...-NVFP4-MTP`), so the tok/s here transfers cleanly to that variant
when you don't need the vision tower.

## Hardware target

Built and tested on **NVIDIA RTX PRO 6000 Blackwell (SM120)**. Should also
work on **RTX 5090** and other Blackwell consumer/workstation cards with
sufficient VRAM (~15 GB NVFP4 weights + ~4 GB bf16 MTP/SSM/lm_head ≈
19.6 GB on disk).

## Acknowledgements

- [`huihui-ai`](https://huggingface.co/huihui-ai) — for the abliterated base
- [`Qwen`](https://huggingface.co/Qwen) — for the original Qwen3.6-27B
- [`osoleve`](https://huggingface.co/osoleve) — for the MTP-restoration recipe on Qwen3.5
- [`nvidia-modelopt`](https://github.com/NVIDIA/TensorRT-Model-Optimizer) team
- The reporters of Discussions #5 and #7 on the original repo — for catching the issues cleanly

## Support the Base Model Authors

If you find this model useful, please consider supporting:

- **huihui-ai** (abliteration): [Ko-fi](https://ko-fi.com/huihuiai) | BTC: `bc1qqnkhuchxw0zqjh2ku3lu4hq45hc6gy84uk70ge`
- **Qwen Team** (original model): [Star the Qwen repo](https://huggingface.co/Qwen/Qwen3.6-27B)

## License

This model inherits the Apache 2.0 license.
