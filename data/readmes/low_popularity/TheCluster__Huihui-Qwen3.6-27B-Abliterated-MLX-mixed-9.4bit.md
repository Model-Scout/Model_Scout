---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3.6-27B/blob/main/LICENSE
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
- huihui-ai/Huihui-Qwen3.6-27B-abliterated
library_name: mlx
tags:
- abliterated
- uncensored
- decensored
- 9bit
- mixed-precision
pipeline_tag: image-text-to-text
---
<div align="center"><img width="400px" src="https://qianwen-res.oss-accelerate.aliyuncs.com/Qwen3.6/logo.png"></div>
<div style="text-align:center; margin-bottom:12pt">If you like my work, you can <a href="https://donatr.ee/thecluster/">support me</a><br/></div>

# Qwen3.6-27B Abliterated (by huihui.ai)

This is another **uncensored** version of [Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B), made by [huihui.ai](https://huggingface.co/huihui-ai).

**Quality**: quantized (***mixed quants per tensor**, group size: 32, **9.450 bpw***)

*Most tensors use 8-bit affine quantization with a group size 32; some important tensors are saved in bf16*.

Alternative version (*from other source*): [`TheCluster/Qwen3.6-27B-Heretic-MLX-mixed-9.4bit`](https://huggingface.co/TheCluster/Qwen3.6-27B-Heretic-MLX-mixed-9.4bit)

### Recommended settings

1. **Sampling Parameters**:  
   - The developers suggest using the following sets of sampling parameters depending on the mode and task type:  
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
This model was converted to MLX format from [`huihui-ai/Huihui-Qwen3.6-27B-abliterated`](https://huggingface.co/huihui-ai/Huihui-Qwen3.6-27B-abliterated) using mlx-vlm version **0.4.4**.