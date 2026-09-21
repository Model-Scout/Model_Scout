---
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
library_name: mlx
pipeline_tag: text-generation
license: apache-2.0
base_model: tencent/Hy-MT2-1.8B
tags:
- mlx
- translation
---

# Hy-MT2-1.8B, 4-bit MLX build

A 4-bit quantization of [tencent/Hy-MT2-1.8B](https://huggingface.co/tencent/Hy-MT2-1.8B),
Tencent's translation model for 33 languages, converted for Apple silicon with
[mlx-lm](https://github.com/ml-explore/mlx-lm):

    mlx_lm convert --hf-path tencent/Hy-MT2-1.8B -q --q-bits 4

Weights are unchanged apart from the quantization (4.5 bits per weight, group size 64).
Built for [Awnsy](https://awnsy.com), a macOS menu bar translator, where it runs on-device.

Licensed under Apache 2.0, as the original.
