---
license: other
license_name: tongyi-qianwen
license_link: https://hf.co/Qwen/Qwen3.5-122B-A10B/blob/main/LICENSE
base_model:
  - wangzhang/Qwen3.5-122B-A10B-abliterated
tags:
  - qwen3.5
  - moe
  - awq
  - int4
  - quantized
  - abliterated
  - compressed-tensors
language:
  - en
  - ko
  - zh
  - ja
library_name: transformers
pipeline_tag: text-generation
---

# Qwen3.5-122B-A10B-abliterated-AWQ

AWQ INT4 (W4A16) quantized version of [wangzhang/Qwen3.5-122B-A10B-abliterated](https://huggingface.co/wangzhang/Qwen3.5-122B-A10B-abliterated), a Mixture-of-Experts model with 122B total parameters and 10B active parameters per token.

## Model Details

| Property | Value |
|----------|-------|
| Base Model | [wangzhang/Qwen3.5-122B-A10B-abliterated](https://huggingface.co/wangzhang/Qwen3.5-122B-A10B-abliterated) |
| Architecture | Qwen3.5 MoE (256 routed experts, 10B active) |
| Quantization | AWQ INT4 (W4A16, symmetric, group_size=128) |
| Quantization Tool | [llm-compressor](https://github.com/vllm-project/llm-compressor) 0.10.1.dev (main branch) |
| Quantization Format | compressed-tensors, pack-quantized |
| Original Size | 228 GB (BF16) |
| Quantized Size | **66 GB** (71% reduction) |
| Format | safetensors (2 shards) |
| Calibration | WikiText-103, 8 samples, seq_len=256 |

## Quantization Details

### What is Quantized

| Component | Format | Notes |
|-----------|--------|-------|
| Routed experts (gate/up/down_proj) | **INT4 packed** | 256 experts x 48 layers x 3 projections = 36,864 quantized tensors |
| Self-attention (q/k/v/o_proj) | **INT4 packed** | 12 full-attention layers |
| Shared experts | BF16 | Kept at full precision for quality |
| Linear attention | BF16 | Kept at full precision (36 layers) |
| Embeddings, norms, gates | BF16 | Kept at full precision |

### Quantization Method

This model was quantized using **llm-compressor** (main branch, commit `e48353f8`) with `AWQModifier`:

1. **Fused Expert Unfusing**: llm-compressor's `CalibrationQwen3_5MoeSparseMoeBlock` unfuses the 3D fused expert parameters (`Qwen3_5MoeExperts`) into individual `nn.Linear` modules, enabling standard AWQ quantization
2. **AWQ Smoothing**: Activation-aware weight quantization with grid search (n_grid=10) for optimal scale factors
3. **INT4 Packing**: Weights packed into int32 tensors (8 INT4 values per int32) with per-group scales (group_size=128)

## Compatibility

### Serving Requirements

> **Important**: This model uses `compressed-tensors` format with `WNA16` (Weight N-bit Activation 16-bit) quantization. The required inference kernels have specific GPU architecture requirements.

| GPU Architecture | Compute Capability | Compatible? | Notes |
|-----------------|-------------------|-------------|-------|
| NVIDIA Hopper (H100, H200) | SM90 | **Yes** | CutlassW4A8 + MacheteLinearKernel |
| NVIDIA Ada (L40S, RTX 4090) | SM89 | **Yes** | Marlin kernel |
| NVIDIA Blackwell (B200) | SM100 | **Yes** | Full support |
| NVIDIA DGX Spark (GB10) | SM121 | **No** | WNA16 kernels require SM90+ |
| NVIDIA Ampere (A100) | SM80 | Untested | May work with Marlin fallback |

### vLLM Serving Example

```bash
vllm serve bjk110/Qwen3.5-122B-A10B-abliterated-AWQ \
    --served-model-name Qwen3.5-122B-A10B-abliterated-AWQ \
    --quantization compressed-tensors \
    --max-model-len 32768 \
    --trust-remote-code \
    --enable-chunked-prefill \
    --reasoning-parser qwen3
```

**Note**: This model requires the TextOnlyShim patch for vLLM since the base architecture is multimodal (Qwen3.5 MoE) but this checkpoint contains only text weights. The patch is included in the `vllm_patches/` directory.

## Referenced Models

- **Base model**: [wangzhang/Qwen3.5-122B-A10B-abliterated](https://huggingface.co/wangzhang/Qwen3.5-122B-A10B-abliterated) — Abliterated (uncensored) version
- **Original model**: [Qwen/Qwen3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B) — Official Qwen3.5 MoE
- **NVFP4 variant**: [bjk110/Qwen3.5-122B-A10B-abliterated-NVFP4](https://huggingface.co/bjk110/Qwen3.5-122B-A10B-abliterated-NVFP4) — NVFP4 quantized (71 GB, compatible with DGX Spark)
- **FP8 variant**: [bjk110/Qwen3.5-122B-A10B-abliterated-FP8](https://huggingface.co/bjk110/Qwen3.5-122B-A10B-abliterated-FP8) — FP8 block-wise (116 GB)

## License

This model inherits the license from the base model: [Tongyi Qianwen License](https://hf.co/Qwen/Qwen3.5-122B-A10B/blob/main/LICENSE).
