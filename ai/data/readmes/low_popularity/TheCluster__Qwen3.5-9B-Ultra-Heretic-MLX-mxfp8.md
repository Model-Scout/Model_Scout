---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3.5-9B/blob/main/LICENSE
base_model:
- llmfan46/Qwen3.5-9B-ultra-heretic
library_name: mlx
tags:
- heretic
- uncensored
- unrestricted
- decensored
- abliterated
- mxfp8
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

# Qwen3.5-9B Ultra Heretic

**Quality**: quantized (***mxfp8**, group size: 32, 8.626 bpw*)

This is a abliterated (**uncensored**) version of [Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B), made using [Heretic](https://github.com/p-e-w/heretic) v1.2.0 with Magnitude-Preserving Orthogonal Ablation (MPOA) and Self-Organizing Map Abliteration (SOMA)

### Performance
| Metric | This model | Original model ([Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)) |
| :----- | :--------: | :---------------------------: |
| **KL divergence** | 0.1085 | 0 *(by definition)* |
| **Refusals** | 2/100 | 86/100 |

Lower refusals indicate fewer content restrictions, while lower KL divergence indicates better preservation of the original model's capabilities.

Alternative fine-tuned version: [TheCluster/Qwen3.5-9B-Claude-4.6-HighIQ-INSTRUCT-HERETIC-UNCENSORED-MLX-mxfp8](https://huggingface.co/TheCluster/Qwen3.5-9B-Claude-4.6-HighIQ-INSTRUCT-HERETIC-UNCENSORED-MLX-mxfp8)

#### Sampling Parameters:  
   - I suggest using the following sets of sampling parameters depending on the mode and task type:  
     - **Thinking mode for general tasks**:  
       `temperature=1.0`, `top_p=0.95`, `top_k=20`, `min_p=0.0`, `presence_penalty=1.5`, `repetition_penalty=1.0`  
     - **Instruct (or non-thinking) mode for general tasks**:  
       `temperature=0.7`, `top_p=0.8`, `top_k=20`, `min_p=0.0`, `presence_penalty=1.5`, `repetition_penalty=1.0`  
     - **Instruct (or non-thinking) mode for reasoning tasks**:  
       `temperature=1.0`, `top_p=1.0`, `top_k=40`, `min_p=0.0`, `presence_penalty=2.0`, `repetition_penalty=1.0`  
   - For supported frameworks, you can adjust the `presence_penalty` parameter between 0 and 2 to reduce endless repetitions. However, using a higher value may occasionally result in language mixing and a slight decrease in model performance.
-----
### Source
This model was converted to MLX format from [`llmfan46/Qwen3.5-9B-ultra-heretic`](https://huggingface.co/llmfan46/Qwen3.5-9B-ultra-heretic) using mlx-vlm version **0.4**.