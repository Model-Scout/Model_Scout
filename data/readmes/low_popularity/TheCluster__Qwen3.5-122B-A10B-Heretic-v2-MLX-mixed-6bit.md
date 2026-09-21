---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3.5-122B-A10B/blob/main/LICENSE
base_model:
- coder3101/Qwen3.5-122B-A10B-heretic-v2
library_name: mlx
pipeline_tag: image-text-to-text
tags:
- uncensored
- decensored
- unrestricted
- abliterated
- heretic
- mixed-precision
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
<div align="center"><img width="400px" src="https://qianwen-res.oss-accelerate.aliyuncs.com/logo_qwen3.5.png"></div>

# Qwen3.5-122B-A10B Heretic V2

**Quality**: quantized (***mixed quants per tensor**, group size: 32, **6.19 bpw***)

Quantization: 5 bit for experts, 8 bit for shared experts and attention layers, fp16 for embeddings & head. Average bits per weight: **6.19**.

This is an **uncensored** version of [Qwen/Qwen3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B), made using [Heretic](https://github.com/p-e-w/heretic) v1.2.0 with Multi-directional refusal supression

## Abliteration metrics

| Metric | This model | Original model ([Qwen/Qwen3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B)) |
| :----- | :--------: | :---------------------------: |
| **KL divergence** | 0.0646 | 0 *(by definition)* |
| **Refusals** | 16/100 | 84/100 |

#### Sampling Parameters:  
   - I suggest using the following sets of sampling parameters depending on the mode and task type:  
     - **Thinking mode for general tasks**:  
       `temperature=1.0`, `top_p=0.95`, `top_k=20`, `min_p=0.0`, `presence_penalty=1.5`, `repetition_penalty=1.0`  
     - **Thinking mode for precise coding tasks (e.g., WebDev)**:  
       `temperature=0.6`, `top_p=0.95`, `top_k=20`, `min_p=0.0`, `presence_penalty=0.0`, `repetition_penalty=1.0`  
     - **Instruct (or non-thinking) mode for general tasks**:  
       `temperature=0.7`, `top_p=0.8`, `top_k=20`, `min_p=0.0`, `presence_penalty=1.5`, `repetition_penalty=1.0`  
     - **Instruct (or non-thinking) mode for reasoning tasks**:  
       `temperature=1.0`, `top_p=1.0`, `top_k=40`, `min_p=0.0`, `presence_penalty=2.0`, `repetition_penalty=1.0`  
   - For supported frameworks, you can adjust the `presence_penalty` parameter between 0 and 2 to reduce endless repetitions. However, using a higher value may occasionally result in language mixing and a slight decrease in model performance.

-----
### Source
This model was converted to MLX format from [`coder3101/Qwen3.5-122B-A10B-heretic-v2`](https://huggingface.co/coder3101/Qwen3.5-122B-A10B-heretic-v2) using mlx-vlm version **0.4.0**.