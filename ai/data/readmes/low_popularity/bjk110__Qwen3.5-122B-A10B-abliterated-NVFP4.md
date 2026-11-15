---
license: apache-2.0
license_name: apache-2.0
license_link: https://hf.co/Qwen/Qwen3.5-122B-A10B/blob/main/LICENSE
base_model:
- wangzhang/Qwen3.5-122B-A10B-abliterated
tags:
- qwen3.5
- moe
- nvfp4
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

# Qwen3.5-122B-A10B-abliterated-NVFP4

NVFP4 (4-bit floating point) quantized derivative of [wangzhang/Qwen3.5-122B-A10B-abliterated](https://huggingface.co/wangzhang/Qwen3.5-122B-A10B-abliterated), which itself is derived from [Qwen/Qwen3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B).

This repository provides a modified derivative checkpoint for local inference and serving. The primary changes in this repository are NVFP4 quantization, weight repacking / export formatting, and serving compatibility adjustments.

## Model Details

| Property | Value |
|----------|-------|
| Intermediate Base Model | [wangzhang/Qwen3.5-122B-A10B-abliterated](https://huggingface.co/wangzhang/Qwen3.5-122B-A10B-abliterated) |
| Original Base Model | [Qwen/Qwen3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B) |
| Architecture | Qwen3.5 MoE (256 routed experts, 10B active) |
| Quantization | NVFP4 (compressed-tensors, nvfp4-pack-quantized) |
| Original Size | 228 GB (BF16) |
| Quantized Size | **71.2 GB** (69% reduction) |
| Format | safetensors (2 shards) |

## Quantization Method

This model was quantized using a **template-based weight replacement** approach:

1. **Reference Template**: [RedHatAI/Qwen3.5-122B-A10B-NVFP4](https://huggingface.co/RedHatAI/Qwen3.5-122B-A10B-NVFP4) — a calibrated NVFP4 checkpoint of the original (non-abliterated) Qwen3.5-122B-A10B, produced by llm-compressor with proper calibration data.
2. **Weight Replacement**: Each quantized tensor (`weight_packed` and `weight_scale`) was regenerated from the abliterated BF16 weights using the reference checkpoint's `weight_global_scale` and `input_global_scale` values.
3. **Format Preservation**: The reference checkpoint's `config.json`, `quantization_config`, global scales, and all metadata were preserved unchanged, ensuring full compatibility with vLLM's CUTLASS NVFP4 MoE kernel.

### What is Quantized

| Component | Format | Notes |
|-----------|--------|-------|
| Routed experts (gate/up/down_proj) | **NVFP4** | 256 experts × 48 layers × 3 projections |
| Shared experts | **NVFP4** | 48 layers × 3 projections |
| Self-attention (q/k/v/o_proj) | **NVFP4** | 12 full-attention layers |
| Linear attention | **BF16** | 36 layers, kept at full precision |
| Embeddings, norms, gates | **BF16** | Kept at full precision |

## Serving with vLLM

This model requires a text-only compatibility patch for vLLM since Qwen3.5 MoE is a multimodal architecture but this checkpoint contains only text weights.

### Quick Start

```bash
# 1. Download the model
huggingface-cli download bjk110/Qwen3.5-122B-A10B-abliterated-NVFP4

# 2. Apply the text-only patch before starting vLLM
python vllm_patches/patch_qwen35_moe_text.py

# 3. Serve with vLLM
vllm serve /path/to/model \
    --served-model-name Qwen3.5-122B-A10B-abliterated-NVFP4 \
    --max-model-len 131072 \
    --max-num-seqs 4 \
    --gpu-memory-utilization 0.90 \
    --trust-remote-code \
    --enable-prefix-caching \
    --enable-chunked-prefill \
    --reasoning-parser qwen3

### Docker Compose (Recommended)

A complete Docker Compose setup is provided in the `serving/` directory:

```bash
# Copy serving files
cp -r serving/ /path/to/your/vllm-setup/

# Edit .env to set MODEL_PATH
vim serving/.env

# Start
cd serving && docker compose --profile head up -d
```

See `serving/` directory for:
- `docker-compose.yml` — Full vLLM serving configuration
- `.env.example` — Environment variables template
- `entrypoint.sh` — Entrypoint with automatic patch application

### Hardware Requirements

| Configuration | Memory | max_model_len | Notes |
|--------------|--------|---------------|-------|
| **1× NVIDIA DGX Spark (GB10)** | 121 GiB unified | 131,072 (128K) | **Tested and verified** |
| 1× GPU with 80+ GB VRAM | 80 GiB | ~65,536 | Estimated |

### Performance (DGX Spark, TP=1)

| Metric | Value |
|--------|-------|
| Throughput | 14.5 tok/s average, 16.8 tok/s peak |
| KV Cache | 222K tokens (20.4 GiB) |
| Max Concurrency | 6.16× at 128K context |
| Model Loading | ~13 min (2 shards) |

## Referenced Models

- **Base model**: [wangzhang/Qwen3.5-122B-A10B-abliterated](https://huggingface.co/wangzhang/Qwen3.5-122B-A10B-abliterated) — Abliterated (uncensored) version of Qwen3.5-122B-A10B
- **Original model**: [Qwen/Qwen3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B) — Official Qwen3.5 MoE model
- **Quantization template**: [RedHatAI/Qwen3.5-122B-A10B-NVFP4](https://huggingface.co/RedHatAI/Qwen3.5-122B-A10B-NVFP4) — Used as format reference for NVFP4 quantization structure
- **FP8 variant**: [bjk110/Qwen3.5-122B-A10B-abliterated-FP8](https://huggingface.co/bjk110/Qwen3.5-122B-A10B-abliterated-FP8) — FP8 block-wise quantized version (116 GB, requires TP=2)

