---
license: apache-2.0
base_model: Jiunsong/SuperGemma-4-12b-abliterated
base_model_relation: quantized
library_name: mlx
pipeline_tag: text-generation
tags:
- gemma4
- abliterated
- mlx
- 4-bit
- quantized
language:
- en
- ko
---

# SuperGemma-4-12b-abliterated - MLX 4-bit

This repository contains an MLX affine 4-bit quantization of the BF16 parent model.

Parent model: [Jiunsong/SuperGemma-4-12b-abliterated](https://huggingface.co/Jiunsong/SuperGemma-4-12b-abliterated)

## Parent Benchmark Summary

| Benchmark | Gemma4 12B original | SuperGemma-4-12b-abliterated | Delta |
| --- | ---: | ---: | ---: |
| Overall public top-5 500 | 23.8 | 44.6 | +20.8 |
| GPQA Diamond | 10.0 | 19.0 | +9.0 |
| MMLU-Pro | 17.0 | 18.0 | +1.0 |
| IFEval | 61.0 | 59.0 | -2.0 |
| HumanEval+ | 18.0 | 46.0 | +28.0 |
| MBPP+ | 13.0 | 81.0 | +68.0 |

## Usage

```bash
pip install -U mlx-lm
mlx_lm.generate --model Jiunsong/SuperGemma-4-12b-abliterated-mlx-4bit --prompt "Write a short release note."
```

## Notes

- This quantized build is provided for smaller local inference deployments.
- The included MLX chat template uses a direct instruction format for clean local text-generation output.
- For benchmark numbers and validation details, see the BF16 parent repository.
