---
license: apache-2.0
language:
- ko
- en
pipeline_tag: text-generation
tags:
- korean
- dpo
- rlhf
- reasoning
base_model: cooler8/yejin-korean-3b-v2-sft
---

# Yejin Korean 3B v2 - DPO (Direct Preference Optimization)

**Yejin Korean 3B v2 DPO** is an advanced 3-billion-parameter Korean language model aligned using Direct Preference Optimization (DPO) on top of `cooler8/yejin-korean-3b-v2-sft`.

## Model Highlights
- **Parameters**: ~3.0B
- **Alignment**: Direct Preference Optimization (DPO) with enterprise curated Korean preference pairs
- **Context Window**: 4,096 tokens
- **Tokenizer**: Custom 64,000 Korean-optimized vocabulary (high Hangul compression efficiency)
- **Target Use Cases**: Complex Korean instruction following, chit-chat, reasoning, and multi-turn dialogue

## Prompt Template

```
<|user|>
{prompt}<|end|>
<|assistant|>
{response}<|end|>
```

## Quick Start

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "cooler8/yejin-korean-3b-v2-dpo"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

messages = [
    {"role": "user", "content": "인공지능의 윤리적 문제점에 대해 3가지로 설명해줘."}
]
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

outputs = model.generate(**inputs, max_new_tokens=512, temperature=0.7, top_p=0.9)
print(tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))
```

## Training Details
- **Alignment Algorithm**: DPO (beta=0.1)
- **Hardware**: 8× NVIDIA H200 (141GB) SXM Tensor Core GPUs
- **Training Loss**: 0.265 | **Reward Accuracy**: 92.3%

## License
Apache 2.0
