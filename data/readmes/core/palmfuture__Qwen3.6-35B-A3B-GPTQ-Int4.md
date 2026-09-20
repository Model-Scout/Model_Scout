---
base_model: Qwen/Qwen3.6-35B-A3B
license: apache-2.0
language:
- en
- th
- zh
- multilingual
tags:
- quantized
- gptq
- int4
- moe
- qwen3.6
- qwen3_5_moe
- mtp
- speculative-decoding
library_name: transformers
pipeline_tag: image-text-to-text
---

# Qwen3.6-35B-A3B-GPTQ-Int4

GPTQ Int4 quantization of [Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B), produced on **consumer multi-GPU hardware** (4× RTX 3060 12GB) using Python 3.13t free-threading.

This v2 release ships **MTP (Multi-Token Prediction) speculative decoding weights** verified working on both vLLM 0.19.1 and SGLang 0.5.10.

## Quality

| Metric | Value |
|--------|-------|
| GPTQ success rate | **97.42%** |
| RTN fallback rate | 2.58% |
| Loss mean | 1.38e-04 |
| Loss median | 9.29e-05 |
| Loss max | 2.14e-03 |
| Total modules | 30,720 |
| Perplexity (wikitext-2-raw-v1) | 6.1846 (~97.9% BF16 retention) |

## Model specs

| Property | Value |
|----------|-------|
| Base model | Qwen3.6-35B-A3B (MoE, 35B total / 3B active) |
| Architecture | `Qwen3_5MoeForConditionalGeneration` (vision + text) |
| Experts | 256 (top-8 routing per token) |
| Hidden layers | 40 |
| Context length | 262,144 tokens |
| Quantization | GPTQ v2, 4-bit, group_size=128, symmetric |
| Quantized size | 24.4 GB (incl. MTP weights) |
| KV cache support | fp16, bf16, fp8_e4m3 (storage-only on Ampere) |
| MTP head | Included (BF16, 785 keys, split per-expert format) |

### What's quantized vs kept bf16

**Quantized (int4):** All MoE expert weights (`mlp.experts.*`) across layers 0–39

**Kept bf16 (per Qwen3.6 recipe):**
- Attention layers (`*.attn.*`)
- MoE routers (`*.mlp.gate`)
- Shared experts (`*.shared_expert.*`)
- Multi-token prediction heads (`*.mtp.*`) — see [Speculative decoding](#speculative-decoding-mtp) below
- Vision encoder (`*.visual.*`)
- Embeddings and `lm_head`

## Calibration recipe

Domain-mixed calibration set to ensure all 256 experts receive meaningful activation signal:

| Source | Samples | Purpose |
|--------|---------|---------|
| [allenai/c4](https://huggingface.co/datasets/allenai/c4) | 102 | General English text |
| [allenai/tulu-3-sft-mixture](https://huggingface.co/datasets/allenai/tulu-3-sft-mixture) | 77 | Instruction-following |
| [codeparrot/codeparrot-clean-valid](https://huggingface.co/datasets/codeparrot/codeparrot-clean-valid) | 51 | Code generation |
| [HuggingFaceH4/MATH-500](https://huggingface.co/datasets/HuggingFaceH4/MATH-500) | 26 | Mathematical reasoning |
| **Total** | **256** (seq_len=1024) | |

## Hardware used for quantization

- **GPUs**: 4× NVIDIA RTX 3060 12GB
- **Motherboard**: SuperMicro C9X299-RPGF (LGA 2066)
- **CPU**: Intel i9-7900X (10c/20t, Skylake-X)
- **RAM**: 32 GB DDR4-2666
- **Runtime**: ~4h 20m wall-clock

## Toolchain

| Component | Version |
|-----------|---------|
| GPTQModel | 6.0.3 |
| Flash Linear Attention (FLA) | 0.4.2 |
| PyTorch | 2.11.0+cu128 |
| Triton | 3.6.0 (cp313t wheel) |
| Python | **3.13.13t** (free-threading, no-GIL) |
| CUDA | 12.8 |

Python 3.13t was the enabler for multi-GPU quantization on consumer cards — the no-GIL runtime let GPTQModel's data-parallel quantizer actually use all 4 GPUs without serializing through the interpreter lock.

## Usage

### SGLang (recommended for production)

```bash
python -m sglang.launch_server \
  --model-path palmfuture/Qwen3.6-35B-A3B-GPTQ-Int4 \
  --quantization moe_wna16 \
  --tp-size 4 \
  --mem-fraction-static 0.89 \
  --kv-cache-dtype fp8_e4m3 \
  --context-length 262144 \
  --port 30000
```

Verified on 4× RTX 3060 12GB with SGLang 0.5.10 (`max_total_num_tokens=415184`, `context_len=262144`, `max_running_requests=39`).

### vLLM

```bash
vllm serve palmfuture/Qwen3.6-35B-A3B-GPTQ-Int4 \
  --tensor-parallel-size 4 \
  --max-model-len 200000 \
  --gpu-memory-utilization 0.85 \
  --kv-cache-dtype fp8 \
  --dtype bfloat16 \
  --reasoning-parser qwen3 \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder \
  --trust-remote-code
```

> **Important:** Do **not** pass `--quantization moe_wna16` to vLLM. Let vLLM auto-detect quantization from `config.json`. Forcing the flag triggers a `KeyError: 'experts.w2_weight'` in the `Qwen3_5MoeMTP` loader path even when MTP is disabled.

### Transformers (single-GPU, for testing)

Requires `trust_remote_code=True` for the Qwen3.5-MoE architecture.

## Recommended sampling

Follow the [official Qwen3.6 sampling guidance](https://huggingface.co/Qwen/Qwen3.6-35B-A3B). For workloads where you want to cap reasoning length (agents, coding tasks), see [vllm-default-thinking-budget](https://github.com/palmfuture/vllm-default-thinking-budget) — a vLLM plugin I built for setting default `thinking_token_budget` and `presence_penalty`:

```bash
git clone https://github.com/palmfuture/vllm-default-thinking-budget
./vllm-default-thinking-budget/install.sh /path/to/your/vllm/venv

export VLLM_DEFAULT_THINKING_BUDGET=8192
export VLLM_DEFAULT_PRESENCE_PENALTY=1.0
vllm serve palmfuture/Qwen3.6-35B-A3B-GPTQ-Int4 ...
```

## Speculative decoding (MTP)

This release ships **MTP (Multi-Token Prediction) weights** in the per-expert split format expected by vLLM and SGLang loaders (785 MTP keys total, all BF16). Speculative decoding is verified working on both engines.

### vLLM with MTP

```bash
vllm serve palmfuture/Qwen3.6-35B-A3B-GPTQ-Int4 \
  --tensor-parallel-size 4 \
  --max-model-len 200000 \
  --gpu-memory-utilization 0.85 \
  --kv-cache-dtype fp8 \
  --dtype bfloat16 \
  --reasoning-parser qwen3 \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder \
  --speculative-config '{"method": "mtp", "num_speculative_tokens": 2}' \
  --trust-remote-code
```

Verified on vLLM 0.19.1 + 4× RTX 3060 12GB:

| Metric | Value |
|--------|-------|
| Steady-state decode | 56–82 t/s |
| Avg draft acceptance rate | 70–89% (peak 88.9%) |
| Per-position acceptance | token 1: ~0.93, token 2: ~0.85 |
| Mean acceptance length | 2.4–2.8 / 2 draft tokens |
| KV pool | 160,800 tokens (262K max-model-len, 2.34× concurrency) |

### SGLang with MTP (EAGLE)

```bash
SGLANG_ENABLE_SPEC_V2=1 \
SGLANG_MAMBA_CONV_DTYPE=float16 \
python -m sglang.launch_server \
  --model-path palmfuture/Qwen3.6-35B-A3B-GPTQ-Int4 \
  --tp-size 4 \
  --dtype float16 \
  --quantization moe_wna16 \
  --context-length 200000 \
  --mem-fraction-static 0.80 \
  --mamba-scheduler-strategy extra_buffer \
  --speculative-algorithm EAGLE \
  --speculative-eagle-topk 1 \
  --speculative-num-steps 3 \
  --speculative-num-draft-tokens 4 \
  --reasoning-parser qwen3 \
  --tool-call-parser qwen3_coder \
  --port 30000
```

Verified on SGLang 0.5.10 + 4× RTX 3060 12GB: 52–141 t/s decode (peak with batching), 34–70% acceptance rate, 1.4–2.8 mean acceptance length.

### Notes on MTP weight layout

This release stores MTP experts in **per-expert split format** (`mtp.layers.0.mlp.experts.{i}.{gate,up,down}_proj.weight`, 256 experts × 3 projections = 768 expert keys), matching the layout that the upstream vLLM/SGLang MTP loaders expect.

The Qwen3.6 BF16 base model stores these as **fused 3D tensors** (`gate_up_proj` shape `[E, 2I, H]`, `down_proj` shape `[E, H, I]`). They are split bit-for-bit during release packaging — there is no quantization or numerical transformation of the MTP head, only a tensor reshape.

## Reproducibility

The full per-module quantization log is published as [`quant_log.csv`](./quant_log.csv) (1.8 MB). Each row records the layer, module, GPTQ loss (or RTN fallback marker), sample count, damping value, and wall-clock time — making the run fully auditable.

## Known characteristics

- **Per-layer RTN distribution.** Layers 32–39 show ~7–10% RTN rate vs ~1–3% for early layers. Consistent with MoE routing concentration in deeper layers and memory pressure late in the run.
- **Cold experts.** 157 of 256 expert IDs fell back to RTN in at least one layer; 99 always got GPTQ. Top cold experts: 235, 249, 234, 197, 237. These rarely route at inference.
- **Ampere-only limitations.** On RTX 3060 (SM86), fp8 KV cache is storage-only (dequantized for attention). No FP8 compute path.
- **vLLM `--quantization` flag.** Do not pass `--quantization moe_wna16` to vLLM — it triggers a `KeyError` in the MTP loader path. SGLang requires the flag; vLLM must auto-detect.

## Credits

- [Qwen Team](https://huggingface.co/Qwen) — base model
- [ModelCloud / GPTQModel](https://github.com/ModelCloud/GPTQModel) — quantization framework
- [sustcsonglin / flash-linear-attention](https://github.com/sustcsonglin/flash-linear-attention) — GDN hybrid attention support
- Python 3.13 free-threading working group — no-GIL runtime

---

Quantized by [@palmfuture](https://huggingface.co/palmfuture).