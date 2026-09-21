---
library_name: mlx
tags:
- translation
- mlx
language:
- zh
- en
- fr
- pt
- es
- ja
- tr
- ru
- ar
- ko
- th
- it
- de
- vi
- ms
- id
- tl
- hi
- pl
- cs
- nl
- km
- my
- fa
- gu
- ur
- te
- mr
- he
- bn
- ta
- uk
- bo
- kk
- mn
- ug
license: apache-2.0
base_model: tencent/Hy-MT2-1.8B
pipeline_tag: text-generation
---

# Hy-MT2-1.8B-mlx-4bit

4-bit [MLX](https://github.com/ml-explore/mlx-lm) quantization of Tencent's
[**tencent/Hy-MT2-1.8B**](https://huggingface.co/tencent/Hy-MT2-1.8B) multilingual
translation model, for fast on-device inference on Apple Silicon (native Metal).

- **Base model:** [tencent/Hy-MT2-1.8B](https://huggingface.co/tencent/Hy-MT2-1.8B) (Apache-2.0)
- **Quantization:** 4-bit (≈4.5 bits/weight), via `mlx_lm.convert`
- **Size:** ~974 MB on disk, ~1.1 GB resident
- **Languages:** 33 (Mandarin, Cantonese, English, French, Japanese, Korean, Arabic, Russian, …)
- Converted with `mlx-lm` 0.31.3.

This is a derivative redistribution permitted under the base model's Apache-2.0
license. All credit for the model goes to Tencent Hunyuan.

## Use with mlx-lm

```bash
pip install mlx-lm

# one-shot
python -m mlx_lm generate --model jizhiovo/Hy-MT2-1.8B-mlx-4bit \
  --prompt "Translate into Chinese.\n\nThe quick brown fox jumps over the lazy dog."

# OpenAI-compatible server
python -m mlx_lm server --model jizhiovo/Hy-MT2-1.8B-mlx-4bit --host 127.0.0.1 --port 8110
```

## Reproduce the conversion

```bash
python -m mlx_lm convert --hf-path tencent/Hy-MT2-1.8B -q --q-bits 4 \
  --mlx-path Hy-MT2-1.8B-mlx-4bit
```
