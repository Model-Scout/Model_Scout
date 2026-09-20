---
license: mit
base_model: deepreinforce-ai/Ornith-1.0-35B
base_model_relation: quantized
pipeline_tag: image-text-to-text
library_name: transformers
tags:
- nvfp4
- compressed-tensors
- vllm
- agentic-coding
- mixture-of-experts
- qwen3_5_moe
language:
- en
- zh
- ja
- fr
---

# Ornith-1.0-35B-NVFP4

NVFP4 (W4A4) quantization of [**deepreinforce-ai/Ornith-1.0-35B**](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B) — DeepReinforce's self-scaffolding agentic-coding model (`qwen3_5_moe`, 35B MoE with a Qwen3-VL vision tower). Quantized with [llm-compressor](https://github.com/vllm-project/llm-compressor) to `compressed-tensors` `nvfp4-pack-quantized`.

**21.9 GB** (from 70.3 GB bf16). Serves on a pair of 16 GB GPUs. Loads in vLLM with **no `--quantization` flag** (auto-detected).

## What was quantized

All linear layers → NVFP4 (W4A4, group size 16). Kept in bf16: the **vision tower** (`re:.*visual.*`), the **MoE routers** (`mlp.gate`, `mlp.shared_expert_gate`), and `lm_head`. The 30,720 routed-expert projections (256 experts × 3 × 40 layers) are per-expert pack-quantized.

```yaml
# recipe.yaml
QuantizationModifier:
  targets: [Linear]
  ignore: [lm_head, 're:.*visual.*', 're:.*mlp.gate$', 're:.*mlp.shared_expert_gate$']
  scheme: NVFP4
```

## Benchmarks

pass@1 on HumanEval+ / MBPP+, scored with an identical local harness. Quantized (this model) vs. a panel of same-class open baselines:

| Benchmark | no-think | **think** |
|---|---|---|
| HumanEval+ (N=163) | 87.1% | **93.9%** |
| MBPP+ (N=160) | 78.1% | **80.6%** |

With reasoning enabled, the W4A4 quant matches or tops the strongest same-class open coders we benchmarked against, on both suites. Quality of the W4A4 quantization is intact.

> **Reasoning-model eval tip:** Ornith reasons at length. For one-shot code benchmarks (a) give it room (`max_tokens ≥ 6500`), and (b) extract the answer from **after** `</think>` — a naive code extractor that scans the whole message will grab draft code from inside the reasoning block and badly under-score the model.

### Throughput (vLLM, NVFP4, on RTX PRO 2000 Blackwell 16 GB)

| Config | single-stream | aggregate @ C=8 | aggregate (peak) |
|---|---|---|---|
| TP=2 | 114 tok/s | 466 tok/s | ~986 tok/s (saturates @ C=32) |
| TP=4 | 166 tok/s | 699 tok/s | ~2280 tok/s (still scaling @ C=64) |

(`--enforce-eager` costs ~5× single-stream; the numbers above are with CUDA graphs on.)

## Serving (vLLM)

This box has no NVLink/P2P, hence the NCCL flags. Drop them on a P2P-capable host.

```bash
vllm serve sakamakismile/Ornith-1.0-35B-NVFP4 \
  --tensor-parallel-size 2 \
  --max-model-len 8192 \
  --disable-custom-all-reduce \
  --trust-remote-code
# env: NCCL_P2P_DISABLE=1   (no-NVLink hosts only)
```

Toggle reasoning per request with `chat_template_kwargs: {"enable_thinking": true|false}`.

## Attribution & License

Base model © DeepReinforce, released under **MIT**. This quantized derivative is redistributed under the same MIT license. All credit for the model itself goes to the original authors — see their [model card](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B) and [technical write-up](https://deep-reinforce.com/ornith_1_0.html). This repository only adds the NVFP4 weights and serving metadata.
