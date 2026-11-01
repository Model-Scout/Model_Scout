---
license: apache-2.0
license_name: apache-2.0
license_link: https://hf.co/Qwen/Qwen3.5-122B-A10B/blob/main/LICENSE
base_model:
- wangzhang/Qwen3.5-122B-A10B-abliterated
tags:
- qwen3.5
- moe
- fp8
- quantized
- abliterated
- compressed-tensors
- vllm
language:
- en
- ko
- zh
- ja
library_name: transformers
pipeline_tag: text-generation
---

# Qwen3.5-122B-A10B-abliterated-FP8

FP8 quantized derivative of [wangzhang/Qwen3.5-122B-A10B-abliterated](https://huggingface.co/wangzhang/Qwen3.5-122B-A10B-abliterated), which itself is derived from [Qwen/Qwen3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B).

This repository provides a modified derivative checkpoint for local inference and serving. The primary changes in this repository are FP8 quantization, weight repacking / export formatting, and serving compatibility adjustments.

## Model Details

| Property | Value |
|----------|-------|
| Intermediate Base Model | [wangzhang/Qwen3.5-122B-A10B-abliterated](https://huggingface.co/wangzhang/Qwen3.5-122B-A10B-abliterated) |
| Original Base Model | [Qwen/Qwen3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B) |
| Architecture | Qwen3.5 MoE (256 routed experts, 10B active) |
| Quantization | FP8 |
| Original Size | 228 GB (BF16) |
| Quantized Size | **116 GB** |
| Format | safetensors |

## Quantization Method

This model was quantized from the abliterated BF16 checkpoint into FP8 format for more practical deployment while preserving compatibility with modern inference stacks.

### What is Quantized

| Component | Format | Notes |
|-----------|--------|-------|
| Expert weights | **FP8** | Quantized for reduced memory footprint |
| Attention projections | **FP8** | Quantized where supported |
| Selected sensitive components | **BF16** | Kept at higher precision where needed for stability |
| Embeddings / norms / control tensors | **BF16** | Preserved at full precision |

## Serving with vLLM

This model is intended for vLLM-based inference and may require tensor parallelism depending on available memory.

### Quick Start

```bash
# 1. Download the model
huggingface-cli download bjk110/Qwen3.5-122B-A10B-abliterated-FP8

# 2. Serve with vLLM
vllm serve /path/to/model \
    --served-model-name Qwen3.5-122B-A10B-abliterated-FP8 \
    --tensor-parallel-size 2 \
    --max-model-len 131072 \
    --max-num-seqs 4 \
    --gpu-memory-utilization 0.90 \
    --trust-remote-code \
    --enable-prefix-caching \
    --enable-chunked-prefill \
    --reasoning-parser qwen3
```

### Docker Entrypoint Auto-Patch

Add to the beginning of your entrypoint.sh:
```bash
if [ -f /patches/patch_qwen35_moe_text.py ]; then
    python3 /patches/patch_qwen35_moe_text.py || true
fi
```

Mount the patches volume in docker-compose.yml:
```yaml
volumes:
  - ./vllm_patches:/patches:ro
```

## What the Patch Does

| Issue | Cause | Fix |
|-------|-------|-----|
| `Qwen3_5MoeForCausalLM` not recognized | Not in vLLM registry | Registers TextOnlyShim class |
| Hybrid cache page-size error | Bug in text-only CausalLM path | Reuses multimodal wrapper's cache-spec |
| Vision encoder init failure | Wrapper forces vision init | Skips vision encoder |
| TP2 block_k=128 error | vision_config.hidden_size=1152 | Injects dummy vision config |

The patch will become unnecessary once vLLM adds native support for `qwen3_5_moe_text`.

## Hardware Requirements

| Config | GPU Memory | Notes |
|--------|-----------|-------|
| TP=1 | ~115 GB | Requires GB200 or similar |
| **TP=2** | **~58 GB/GPU** | DGX Spark, H100×2, A100 80GB×2 |
| TP=4 | ~29 GB/GPU | A100 40GB×4 |

## Base Model

[wangzhang/Qwen3.5-122B-A10B-abliterated](https://huggingface.co/wangzhang/Qwen3.5-122B-A10B-abliterated) — uncensored via [Prometheus](https://github.com/wuwangzhang1216/prometheus) abliteration. Refusal rate 0.5% (1/200), KL divergence 0.0115.

## License

Follows the license of the base model.
