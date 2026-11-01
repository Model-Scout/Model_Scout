---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3.5-9B/blob/main/LICENSE
base_model:
- DavidAU/Qwen3.5-9B-Claude-4.6-HighIQ-INSTRUCT-HERETIC-UNCENSORED
library_name: mlx
tags:
- heretic
- uncensored
- unrestricted
- decensored
- abliterated
- 8bit
- 10bit
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

# Qwen3.5-9B-Claude-4.6-HighIQ-INSTRUCT-HERETIC-UNCENSORED

**Quality**: quantized (***mixed quants per tensor**, group size: 32, **10.101 bpw***).
*Most layers use 8-bit affine quantization with a group size 32; some layers are saved in bf16.*

Fully **uncensored** and fine-tuned (by DavidAU) using Claude 4.6 large distill dataset.

This version is **INSTRUCT**, with modified jinja template which put this model into "instruct only" mode.

The model weights were updated on April 14.

### Abliteration metrics

| Metric | This model | Original model ([Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)) |
| :----- | :--------: | :---------------------------: |
| **KL divergence** | 0.0793 | 0 *(by definition)* |
| **Refusals** | 6/100 | 100/100 |


### Benchmarks:

```
         arc   arc/e boolq hswag obkqa piqa  wino

HERETIC verison (this model):
mxfp8    0.574,0.755,0.869,0.714,0.410,0.780,0.691

Qwen3.5-9B-Claude-4.6-HighIQ-INSTRUCT
mxfp8    0.574,0.729,0.882,0.711,0.422,0.775,0.691

Qwen3.5-9B
mxfp8    0.417,0.458,0.623,0.634,0.338,0.737,0.639
```

-----
### Source
This model was converted to MLX format from [`DavidAU/Qwen3.5-9B-Claude-4.6-HighIQ-INSTRUCT-HERETIC-UNCENSORED`](https://huggingface.co/DavidAU/Qwen3.5-9B-Claude-4.6-HighIQ-INSTRUCT-HERETIC-UNCENSORED) using mlx-vlm version **0.4.4**.
