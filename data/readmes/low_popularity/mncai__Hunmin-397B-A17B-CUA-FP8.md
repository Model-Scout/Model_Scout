---
license: apache-2.0
base_model:
- mncai/Hunmin-397B-A17B-CUA
base_model_relation: quantized
language:
- en
- ko
pipeline_tag: image-text-to-text
---

# Hunmin-397B-A17B-CUA-FP8

Block-wise **FP8 (e4m3)** quantization of **[mncai/Hunmin-397B-A17B-CUA](https://huggingface.co/mncai/Hunmin-397B-A17B-CUA)**: 128×128 weight blocks in a mixed **FP8 + BF16** layout (following the official Qwen3.5-397B-A17B-FP8 scheme — precision-sensitive tensors kept in BF16). ~373 GB (about half the BF16 release), for cheaper multi-GPU serving.

For the model description, benchmarks, and evaluation methodology, see the **[main model card](https://huggingface.co/mncai/Hunmin-397B-A17B-CUA)**.

## Quickstart (vLLM)

```bash
vllm serve <path>/Hunmin-397B-A17B-CUA-FP8 \
  --tensor-parallel-size 8 \
  --max-model-len 131072 \
  --gpu-memory-utilization 0.90 \
  --enable-prefix-caching
```