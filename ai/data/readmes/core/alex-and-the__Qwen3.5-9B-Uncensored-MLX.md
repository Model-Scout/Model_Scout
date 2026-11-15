---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3.5-9B/blob/main/LICENSE
base_model:
- darkc0de/Qwen3.5-9B-heretic
library_name: mlx
tags:
- heretic
- uncensored
- unrestricted
- decensored
- abliterated
- mxfp4
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
<div align="center"><img width="400px" src="https://qianwen-res.oss-accelerate.aliyuncs.com/logo_qwen3.5.png"></div>
<div style="text-align:center; margin-bottom:12pt">If you like my work, you can <a href="https://donatr.ee/thecluster/">support me</a><br/></div>

# Qwen3.5-9B Heretic

**Quality**: quantized (**mxfp4**)

This is a **decensored** version of [Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B), made using [Heretic](https://github.com/p-e-w/heretic) v1.2.0 with Magnitude-Preserving Orthogonal Ablation (MPOA).

#### Sampling Parameters:  
   - We suggest using the following sets of sampling parameters depending on the mode and task type:  
     - **Thinking mode for general tasks**:  
       `temperature=1.0`, `top_p=0.95`, `top_k=20`, `min_p=0.0`, `presence_penalty=1.5`, `repetition_penalty=1.0`  
     - **Instruct (or non-thinking) mode for general tasks**:  
       `temperature=0.7`, `top_p=0.8`, `top_k=20`, `min_p=0.0`, `presence_penalty=1.5`, `repetition_penalty=1.0`  
     - **Instruct (or non-thinking) mode for reasoning tasks**:  
       `temperature=1.0`, `top_p=1.0`, `top_k=40`, `min_p=0.0`, `presence_penalty=2.0`, `repetition_penalty=1.0`  
   - For supported frameworks, you can adjust the `presence_penalty` parameter between 0 and 2 to reduce endless repetitions. However, using a higher value may occasionally result in language mixing and a slight decrease in model performance.
-----
### Source
This model was converted to MLX format from [`darkc0de/Qwen3.5-9B-heretic`](https://huggingface.co/darkc0de/Qwen3.5-9B-heretic) using mlx-vlm version **0.3.12**.