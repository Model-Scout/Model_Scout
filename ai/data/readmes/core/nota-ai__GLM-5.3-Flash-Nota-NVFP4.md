---
language:
- en
- zh
- ko
base_model:
- zai-org/GLM-5.3-Flash-BF16
tags:
- nota
- nvfp4
- moe
- quantization
license: mit
library_name: transformers
pipeline_tag: text-generation
---

# Nota GLM-5.3-Flash · NVFP4 (W4A4)

A 4-bit (NVFP4) quantized release of
[Z.ai](https://z.ai/)'s [GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash-BF16) — a
**320B-parameter** natively multimodal Mixture-of-Experts model with ~18B active per token.

<div align="center">

**4 × B300  →  1 × B300**

**598.5 GiB → 191.0 GiB (31.9%)**

Full 1,048,576-token context · MTP speculative decoding preserved

</div>

## Highlights

- **NVFP4 (4-bit float, W4A4)** — `group_size=16`, packed in the compressed-tensors
  `nvfp4-pack-quantized` format for direct serving in
  [vLLM](https://github.com/vllm-project/vllm). Both weights and activations are quantized to
  4-bit floating point.
  - > **Requires NVIDIA Blackwell.** NVFP4 relies on the FP4 tensor cores introduced in the
    > Blackwell architecture (e.g. B200 / B300 / GB200), so inference must run on a
    > Blackwell-class GPU. Earlier architectures (Hopper, Ada, Ampere) do not support NVFP4
    > execution.
- **Only the routed experts are quantized.** They hold 94.8% of the parameters, so the memory
  saving is captured almost in full while every precision-critical path stays in BF16 — the same
  split the reference GLM-5.3 NVFP4 release uses.
- **No architecture change.** Tensor names, layer count and expert count are identical to the
  base checkpoint, so stock vLLM serves it as-is — no patched modeling file.
- **MTP and multimodal preserved.** The multi-token-prediction block and the vision tower stay
  BF16, so speculative decoding and image/video inputs work as in the base model.

## Quantization scope

| | Modules | Parameters |
|---|---:|---:|
| NVFP4 — routed experts, layers 3–44 | 36,288 | 304.41 B (94.8%) |
| BF16 — everything else | 1,574 | 16.85 B (5.2%) |

Kept in BF16:

| Group | Tensors |
|---|---|
| KDA linear attention | `self_attn.{q,k,v,b,f_a,f_b,g_a,g_b,o}_proj`, `conv1d`, `A_log`, `dt_bias` |
| DSA sparse attention (MLA) | `self_attn.{q_a,q_b,kv_a_proj_with_mqa,kv_b,o}_proj` |
| DSA indexer | `self_attn.indexer.*` |
| MoE routers | `mlp.gate.weight`, `mlp.gate.e_score_correction_bias` |
| Shared experts | `mlp.shared_experts.*` |
| Leading dense MLPs | `layers.{0,1,2}.mlp.*` |
| MTP block | `layers.45.*` |
| Embeddings / head / vision | `embed_tokens`, `lm_head`, `model.visual.*` |

## Calibration

512 conversations of exactly 4,096 tokens, rendered through the GLM chat template and drawn from
the workloads this model is built for rather than generic web text: agentic tool use (20.5%), SWE
agent trajectories (14.3%), instruction following (8.2%), terminal agents (7.8%), code (7.0%),
STEM (5.9%), reasoning (4.7%), knowledge MCQ (2.3%), and **29.3% Korean** sources. 71.7% of the
samples carry reasoning traces inside `<think>` blocks.

## Requirements

```
vllm >= 0.29.0
flashinfer >= 0.6.17     # sparse MLA
```

## Quick Start

**B300 × 1**

```bash
CUDA_VISIBLE_DEVICES=0 \
vllm serve nota-ai/GLM-5.3-Flash-Nota-NVFP4 \
  --served-model-name nota-ai/GLM-5.3-Flash-Nota-NVFP4 \
  --tensor-parallel-size 1 \
  --gpu-memory-utilization 0.96 \
  --compilation-config '{"cudagraph_mode":"PIECEWISE"}' \
  --kv-cache-dtype fp8 \
  --speculative-config '{"method":"mtp","num_speculative_tokens":5}' \
  --tool-call-parser glm47 \
  --reasoning-parser glm45 \
  --enable-auto-tool-choice
```

**B200 × 2**

```bash
CUDA_VISIBLE_DEVICES=0,1 \
vllm serve nota-ai/GLM-5.3-Flash-Nota-NVFP4 \
  --served-model-name nota-ai/GLM-5.3-Flash-Nota-NVFP4 \
  --tensor-parallel-size 2 \
  --gpu-memory-utilization 0.90 \
  --compilation-config '{"cudagraph_mode":"PIECEWISE"}' \
  --kv-cache-dtype fp8 \
  --speculative-config '{"method":"mtp","num_speculative_tokens":5}' \
  --tool-call-parser glm47 \
  --reasoning-parser glm45 \
  --enable-auto-tool-choice
```
