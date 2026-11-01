---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3.6-35B-A3B/blob/main/LICENSE
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
base_model:
- tvall43/Qwen3.6-35B-A3B-heretic
library_name: mlx
tags:
- heretic
- uncensored
- unrestricted
- decensored
- abliterated
- 3bit
- 4bit
- mixed-precision
pipeline_tag: image-text-to-text
---
<div align="center"><img width="400px" src="https://qianwen-res.oss-accelerate.aliyuncs.com/Qwen3.6/logo.png"></div>
<div style="text-align:center; margin-bottom:12pt">If you like my work, you can <a href="https://donatr.ee/thecluster/">support me</a><br/></div>

# Qwen3.6-35B-A3B Heretic

**Quality**: quantized (***mixed quants per tensor**, group size: 32, **3.891 bpw***)

Quantization: 3 bit for experts, 4 bit for head, shared experts and attention tensors, 6 for embeddings and fp16/bf16 for some linear attention tensors.

This is an **uncensored** version of [Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B), made using [Heretic](https://github.com/p-e-w/heretic) v1.2.0 (mpoa+soma).


### Abliteration metrics
| Metric | This model | Original model ([unsloth/Qwen3.6-35B-A3B](https://huggingface.co/unsloth/Qwen3.6-35B-A3B)) |
| :----- | :--------: | :---------------------------: |
| **KL divergence** | 0.0097 | 0 *(by definition)* |
| **Refusals** | 5/100 | 86/100 |

### Abliteration parameters

| Parameter | Value |
| :-------- | :---: |
| **direction_index** | per layer |
| **attn.o_proj.max_weights.0** | 0: 0.93 |
| **attn.o_proj.max_weights.1** | 1: 1.38 |
| **attn.o_proj.max_weights.2** | 2: 1.37 |
| **attn.o_proj.max_weights.3** | 3: 1.08 |
| **attn.o_proj.max_weight_position** | 24.08 |
| **attn.o_proj.min_weights.0** | 0: 0.34 |
| **attn.o_proj.min_weights.1** | 1: 0.95 |
| **attn.o_proj.min_weights.2** | 2: 1.35 |
| **attn.o_proj.min_weights.3** | 3: 0.54 |
| **attn.o_proj.min_weight_distance** | 9.81 |

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
This model was converted to MLX format from [`tvall43/Qwen3.6-35B-A3B-heretic`](https://huggingface.co/tvall43/Qwen3.6-35B-A3B-heretic) using mlx-vlm version **0.4.4**.