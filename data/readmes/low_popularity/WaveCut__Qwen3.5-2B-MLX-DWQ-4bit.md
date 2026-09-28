---
language: [en, ru, pl, uk, zh, ja, ko, ar, hi, bn, es, fr, de, pt, tr, vi]
library_name: mlx
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3.5-2B/blob/main/LICENSE
pipeline_tag: image-text-to-text
base_model: Qwen/Qwen3.5-2B
base_model_relation: quantized
datasets: [HuggingFaceFW/fineweb, HuggingFaceFW/fineweb-2, wikimedia/wikipedia]
tags: [mlx, mlx-vlm, qwen3.5, vision-language, dwq, 4-bit, mixed-precision, apple-silicon]
---

# Qwen3.5-2B — MLX DWQ 4-bit

[Qwen3.5-2B](https://huggingface.co/Qwen/Qwen3.5-2B) for Apple silicon in **MLX format**. The language backbone uses 4-bit affine DWQ with selected 8-bit matrices, group size 32. The vision tower retains the original BF16 weights. Weight file: **1.90 GB**.

Compatible with unmodified `mlx-lm==0.31.3` and `mlx-vlm==0.7.3`, tested on stable `mlx==0.32.2`.

## Quality

DWQ calibration uses multilingual natural text from FineWeb, FineWeb2 and Wikipedia, balanced across 16 languages. Source revision: `15852e8c16360a2fea060d615a32b45270f8a8fc`.

On 65,408 held-out tokens across 16 languages, teacher KL is **21.4% lower** than the 4-bit DWQ baseline without selective 8-bit matrices:

| Model | KL ↓ | Perplexity ↓ |
|---|---:|---:|
| DWQ 4-bit baseline | 0.08339 | 19.8703 |
| This model | **0.06554** | **19.6672** |

KL is measured against the BF16 source at temperature 1. These text metrics do not establish writing, instruction-following or vision quality. Image input passed a pipeline smoke test. [Evaluation details](eval/final-vlm-comparison.json).

## Use

```bash
python -m pip install "mlx-vlm==0.7.3"
mlx_vlm.generate --model WaveCut/Qwen3.5-2B-MLX-DWQ-4bit \
  --image /path/to/image.jpg --prompt "Describe this image." \
  --max-tokens 128 --temperature 0
```
