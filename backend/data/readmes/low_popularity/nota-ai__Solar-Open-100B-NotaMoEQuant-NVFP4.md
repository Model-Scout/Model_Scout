---
language:
- en
- ko
library_name: transformers
license: other
license_name: upstage-solar-license
pipeline_tag: text-generation
tags:
- upstage
- solar
- moe
- 100b
- llm
- nvfp4
- nota
- moequantization
---

# **Solar-Open-100B-NotaMoeQuant-NVFP4**

This repository provides **Upstage’s flagship model, [Solar-Open-100B](https://huggingface.co/upstage/Solar-Open-100B)**, packaged with [**Nota AI**](https://www.nota.ai/)’s proprietary quantization technique specifically developed for Mixture-of-Experts (MoE)-based LLMs. Unlike conventional quantization methods, this approach incorporates a novel method designed to mitigate representation distortion that can occur when experts are mixed under quantization in MoE architectures.

## Overview

- **Base model:** [Solar-Open-100B](https://huggingface.co/upstage/Solar-Open-100B) 
- **Quantization:** NVFP4
- **Packing format:** `compressed-tensors` (ensuring backend compatibility with HF and vLLM)
- **Hardware Requirements:** 
    * **Minimum:** 1 x NVIDIA B100 
    * We have tested on B100, B200, and B300.   

## License
This repository contains both model weights and code,
which are licensed under different terms:

1. MODEL WEIGHTS (*.safetensors)
   Licensed under **Upstage Solar License**
   See: https://huggingface.co/upstage/Solar-Open-100B/blob/main/LICENSE

2. CODE (*.py, *.json, *.jinja files)
   Licensed under **Apache License 2.0**
   See: https://www.apache.org/licenses/LICENSE-2.0


## Performance

- English

|                 |**Solar-Open-100B**|**Nota MoE Quantization (Ours)**|**AutoRound**|
|---              | ---               | ---                            | ---         |
|PPL (WikiText-2)↓|6.06               |**6.90**                        |7.22         |
|MMLU-Pro↑        |73.91              |**62.53**                       |61.56        |
|GPQA-Diamond↑    |58.08              |**45.96**                       |42.42        |
|General Evaluation Benchmarks |75.77 |**73.94**                       |73.74        |

- Model weigth memory footprint

|**Solar-Open-100B**|**Nota MoE Quantization (Ours)**|
| ---               | ---                            |
|191.2 GB           |58.7 GB                         |


* Note 
  - General evaluation benchmarks: relatively low-difficulty tasks that typically require short responses (ARC-C, ARC-E, BoolQ, HellaSwag, MMLU, PIQA, TruthfulQA, WinoGrande, GSM8K). The score is calculated by averaging across all tasks.
  - ↑ / ↓ denote the direction of improvement: higher is better (↑), lower is better (↓).
  - Because we used a smaller thinking budget (8,192 tokens), the results for MMLU-Pro and GPQA-Diamond are slightly lower than the numbers reported in the original Solar-Open-100B repository.
  - Memory refers to the pure VRAM footprint occupied only by the model weights.


## Inference

### vLLM
Step 1: Create and activate a Python virtual environment
```bash
uv venv --python 3.12 --seed
source .venv/bin/activate
```

Step 2: Install Solar Open's optimized vLLM
```bash
pip install vllm==0.17.0
```

Step 3: Overwrite the two files (solar_open.py and registry.py) in the `patches` folder of the repository containing the model weights into the `vllm/model_executor/models` directory inside the folder where vLLM is installed (typically lib/python3.xx/site-packages).

Step 4: Start the vLLM server (For 1GPUs)
```bash
vllm serve nota-ai/Solar-Open-100B-NotaMoEQuant-NVFP4 \
    --served-model-name Solar-Open \
    --trust-remote-code \
    --tensor-parallel-size 1 
```

Step 5: Generate the response
```bash
from openai import OpenAI

client = OpenAI(
    base_url="http://0.0.0.0:8000/v1",
    api_key="EMPTY"
)

response = client.chat.completions.create(
    model="Solar-Open",
    messages=[
        {"role": "user", "content": "who are you?"}
    ],
    temperature=0.8,
    top_p=0.95,
)

print(response.choices[0].message.content)
```