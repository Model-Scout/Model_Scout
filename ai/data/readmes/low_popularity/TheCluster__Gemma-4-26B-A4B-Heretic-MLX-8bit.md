---
license: apache-2.0
license_link: https://ai.google.dev/gemma/docs/gemma_4_license
base_model:
- coder3101/gemma-4-26B-A4B-it-heretic
library_name: mlx
tags:
- heretic
- uncensored
- unrestricted
- decensored
- abliterated
- 8bit
pipeline_tag: image-text-to-text
language:
- en
- zh
- ru
- es
- fr
- it
- ja
- ko
- af
- de
- ar
- tr
- is
- pl
- sw
- sv
- nl
- he
- id
- uk
- fa
- pa
- pt
- ms
- fi
- el
---
<div align="center">
  <img src=https://ai.google.dev/gemma/images/gemma4_banner.png>
</div>

# Gemma-4-26B-A4B Heretic

**Quality**: quantized (***8 bit**, group size: 32, 9.153 bpw*)

This is a abliterated (**uncensored**) version of [google/gemma-4-26B-A4B-it](https://huggingface.co/google/gemma-4-26B-A4B-it), made using [Heretic](https://github.com/p-e-w/heretic) v1.2.0 with the [Arbitrary-Rank Ablation (ARA)](https://github.com/p-e-w/heretic/pull/211) method (with row-norm preservation)

Alternative version: [TheCluster/Gemma-4-26B-A4B-Heretic-MLX-9bit](https://huggingface.co/TheCluster/Gemma-4-26B-A4B-Heretic-MLX-9bit)

### Performance
| Metric | This model | Original model ([google/gemma-4-26B-A4B-it](https://huggingface.co/google/gemma-4-26B-A4B-it)) |
| :----- | :--------: | :---------------------------: |
| **KL divergence** | 0.0499 | 0 *(by definition)* |
| **Refusals** | 11/100 | 100/100 |

### Abliteration parameters

| Parameter | Value |
| :-------- | :---: |
| **start_layer_index** | 10 |
| **end_layer_index** | 30 |
| **preserve_good_behavior_weight** | 0.5480 |
| **steer_bad_behavior_weight** | 0.0009 |
| **overcorrect_relative_weight** | 0.5868 |
| **neighbor_count** | 14 |

-----
### Source
This model was converted to MLX format from [`coder3101/gemma-4-26B-A4B-it-heretic`](https://huggingface.co/coder3101/gemma-4-26B-A4B-it-heretic) using mlx-vlm version **0.4.4**.
