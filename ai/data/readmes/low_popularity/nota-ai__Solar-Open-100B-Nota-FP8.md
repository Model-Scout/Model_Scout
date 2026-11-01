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
- nota
- quantization
---

# **Solar-Open-100B-Nota-FP8**

This repository provides an FP8-quantized version of **Upstage’s flagship model, [Solar-Open-100B](https://huggingface.co/upstage/Solar-Open-100B)**.

## Overview

- **Base model:** [Solar-Open-100B](https://huggingface.co/upstage/Solar-Open-100B) 
- **Quantization:** FP8 (weight: per-channel/static, activation: per-token/dynamic)
- **Hardware Requirements:** 
    * **Minimum:** 2 x NVIDIA A100 (80GB)    

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

|                 |**Solar-Open-100B**|**Nota FP8 (Ours)**|
|---              | ---               | ---               |
|PPL (WikiText-2)↓|6.06               |6.06               |
|PPL (C4)↓        |20.37              |20.62              |
|PIQA↑            |82.37              |81.94              |
|BoolQ↑           |84.89              |85.14              |
|ARC-E↑           |87.25              |87.08              |
|ARC-C↑           |61.43              |61.60              |
|TruthfulQA↑      |59.25              |59.29              |
|WinoGrande↑      |76.09              |76.01              |

- Korean

|                 |**Solar-Open-100B**|**Nota FP8 (Ours)**|
|---              | ---               | ---               |
|HRM8K↑           |81.52              |81.54              |
|MMLU-ProX-Lite↑  |55.44              |54.86              |
|KoBEST↑          |62.00              |62.00              |
|CLiCK↑           |71.33              |71.28              |

- Model weigth memory footprint

|**Solar-Open-100B**|**Nota MoE Quantization (Ours)**|
| ---               | ---                            |
|191.2 GB           |97.2 GB                         |


* Note 
  - ↑ / ↓ denote the direction of improvement: higher is better (↑), lower is better (↓).
  - Because we used a smaller thinking budget, the results for HRM8K and CLiCK are slightly lower than the numbers reported in the original Solar-Open-100B repository.
  - Memory refers to the pure VRAM footprint occupied only by the model weights.

## Inference
### Transformers

Install the required dependencies:

```bash
pip install -U transformers kernels torch accelerate
```

Run inference with the following code:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = "nota-ai/Solar-Open-100B-Nota-FP8"

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

model = AutoModelForCausalLM.from_pretrained(
    pretrained_model_name_or_path=MODEL_ID,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)

# Prepare input
messages = [{"role": "user", "content": "who are you?"}]
inputs = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_dict=True,
    return_tensors="pt",
)
inputs = inputs.to(model.device)

# Generate response
generated_ids = model.generate(
    **inputs,
    max_new_tokens=4096,
    temperature=0.8,
    top_p=0.95,
    top_k=50,
    do_sample=True,
)
generated_text = tokenizer.decode(generated_ids[0][inputs.input_ids.shape[1] :])
print(generated_text)
```

### vLLM
Create and activate a Python virtual environment
```bash
uv venv --python 3.12 --seed
source .venv/bin/activate
```

Install Solar Open's optimized vLLM
```bash
VLLM_PRECOMPILED_WHEEL_LOCATION="https://github.com/vllm-project/vllm/releases/download/v0.12.0/vllm-0.12.0-cp38-abi3-manylinux_2_31_x86_64.whl" \
VLLM_USE_PRECOMPILED=1 \
uv pip install git+https://github.com/UpstageAI/vllm.git@v0.12.0-solar-open
```

Start the vLLM server (For 2 GPUs)
```bash
PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
vllm serve nota-ai/Solar-Open-100B-Nota-FP8 \
    --trust-remote-code \
    --enable-auto-tool-choice \
    --tool-call-parser solar_open \
    --reasoning-parser solar_open \
    --logits-processors vllm.model_executor.models.parallel_tool_call_logits_processor:ParallelToolCallLogitsProcessor \
    --logits-processors vllm.model_executor.models.solar_open_logits_processor:SolarOpenTemplateLogitsProcessor \
    --tensor-parallel-size 2 \
    --max-num-seqs 64 \
    --gpu-memory-utilization 0.8
```
