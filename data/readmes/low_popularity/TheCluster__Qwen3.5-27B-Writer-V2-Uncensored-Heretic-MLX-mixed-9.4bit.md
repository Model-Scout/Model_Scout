---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3.5-27B/blob/main/LICENSE
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
- llmfan46/Qwen3.5-27B-Writer-V2-uncensored-heretic
library_name: mlx
tags:
- 9bit
- roleplay
- conversational
- mixed-precision
- uncensored
- heretic
- decensored
- abliterated
pipeline_tag: image-text-to-text
---
<div align="center"><img width="400px" src="https://qianwen-res.oss-accelerate.aliyuncs.com/logo_qwen3.5.png"></div>

# Qwen3.5-27B Writer V2 Uncensored Heretic

**Quality**: quantized (***mixed quants per tensor**, group size: 32, **9.450 bpw***)

Most layers use 8-bit affine quantization with a group size 32; some layers are saved in bf16.

A writing & roleplay finetune of uncensored Qwen3.5 27B. The primary emphasis is on writing quality as it strongly generalizes across both domains.

#### Recommended Settings:  
* Chatml template with `<think>\n\n</think>` or `{{char}}:` prefill. Only non-thinking was trained, but thinking probably still works.
* temperature = `0.7`
* top_p = `0.95`
* I do not recommend using high rep pen values like Qwen suggests for the base model. rep_pen = `1.05` or a moderate dry setting should suffice.
-----
### Source
This model was converted to MLX format from [`llmfan46/Qwen3.5-27B-Writer-V2-uncensored-heretic`](https://huggingface.co/llmfan46/Qwen3.5-27B-Writer-V2-uncensored-heretic) using mlx-vlm version **0.4.4**.