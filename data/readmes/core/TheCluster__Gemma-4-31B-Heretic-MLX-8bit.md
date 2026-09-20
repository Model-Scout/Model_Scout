---
license: apache-2.0
license_link: https://ai.google.dev/gemma/docs/gemma_4_license
base_model:
- coder3101/gemma-4-31B-it-heretic
library_name: mlx
tags:
- heretic
- uncensored
- unrestricted
- decensored
- abliterated
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

# Gemma-4-31B Heretic

**Quality**: quantized (***8 bit**, group size: 32, 8.802 bpw*)

This is a abliterated (**uncensored**) version of [google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it), made using [Heretic](https://github.com/p-e-w/heretic) v1.2.0 with the [Arbitrary-Rank Ablation (ARA)](https://github.com/p-e-w/heretic/pull/211) method (with row-norm preservation)

### Performance
| Metric | This model | Original model ([google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)) |
| :----- | :--------: | :---------------------------: |
| **KL divergence** | 0.0434 | 0 *(by definition)* |
| **Refusals** | 15/100 | 99/100 |

### Abliteration parameters

| Parameter | Value |
| :-------- | :---: |
| **start_layer_index** | 1 |
| **end_layer_index** | 59 |
| **preserve_good_behavior_weight** | 0.8438 |
| **steer_bad_behavior_weight** | 0.0002 |
| **overcorrect_relative_weight** | 1.0760 |
| **neighbor_count** | 15 |

-----
### Source
This model was converted to MLX format from [`coder3101/gemma-4-31B-it-heretic`](https://huggingface.co/coder3101/gemma-4-31B-it-heretic) using mlx-vlm version **0.4.4**.
