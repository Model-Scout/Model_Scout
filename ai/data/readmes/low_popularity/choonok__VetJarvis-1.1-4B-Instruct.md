---
license: other
license_name: vetjarvis-model-license-1.0-nc
license_link: LICENSE
language:
- ko
- en
base_model:
- choonok/VetJarvis-4B-Base
- Qwen/Qwen3.5-4B
base_model_relation: finetune
pipeline_tag: text-generation
library_name: transformers
tags:
- veterinary
- companion-animal
- canine
- feline
- medical
- domain-specific
- qwen3.5
- not-a-medical-device
---

# Introducing VetJarvis 1.1-4B

**언어 / Language**: [🇰🇷 한국어](README_ko.md) · [🇺🇸 English](README.md)

![VetJarvis 1.1 Benchmark](media/VetJarvis_1.1.png)

We are pleased to release **VetJarvis 1.1**, an upgraded version featuring enhanced **reasoning capabilities** powered by an improved post-training process over the 1.0 release.

## Quickstart

### Serving VetJarvis-1.1-4B-Instruct

VetJarvis-1.1-4B-Instruct is a text-only LLM based on Qwen3.5-4B, and can be served in BF16 using a variety of frameworks including Hugging Face Transformers and vLLM.

### Hugging Face Transformers

Qwen3.5 architecture is natively supported from `transformers>=5.5`.

```bash
pip install -U "transformers>=5.5" accelerate torch flash-attn
```

```python
import torch
from transformers import AutoTokenizer, Qwen3_5ForConditionalGeneration

MODEL = "choonok/VetJarvis-1.1-4B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = Qwen3_5ForConditionalGeneration.from_pretrained(
    MODEL,
    dtype=torch.bfloat16,
    device_map="auto",
    attn_implementation="flash_attention_2",
)
model.eval()

messages = [
    {
        "role": "system",
        "content": "You are 'VetJarvis', a clinical-support AI assistant for veterinarians.",
    },
    {"role": "user", "content": "Please tell me the metronidazole protocol."},
]

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=True,
)

inputs = tokenizer(text, return_tensors="pt").to(model.device)

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=32768,
        temperature=0.8,
        top_p=0.9,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id,
    )

print(tokenizer.decode(
    outputs[0][inputs.input_ids.shape[-1]:],
    skip_special_tokens=True,
))
```

On Blackwell GPUs (RTX 5090 / B200), a compatible build of flash-attn ≥ 2.7 is required. If you encounter build or compatibility issues, fall back to `attn_implementation="sdpa"`.

### vLLM

Recommended for production or high-throughput use cases. `vllm>=0.18` supports the Qwen3.5 architecture, and the jointly trained MTP layer can be used for speculative decoding to improve throughput.

```bash
pip install "vllm>=0.18"
```

Launch an OpenAI-compatible server:

```bash
vllm serve choonok/VetJarvis-1.1-4B-Instruct \
    --served-model-name VetJarvis-1.1-4B-Instruct \
    --port 8000 \
    --max-model-len 65535 \
    --dtype bfloat16 \
    --gpu-memory-utilization 0.85 \
    --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens":2}'
```

Example:

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="EMPTY",
)

response = client.chat.completions.create(
    model="VetJarvis-1.1-4B-Instruct",
    messages=[
        {
            "role": "system",
            "content": "You are 'VetJarvis', a clinical-support AI assistant for veterinarians.",
        },
        {
            "role": "user",
            "content": "Please tell me the metronidazole protocol.",
        },
    ],
    max_tokens=32768,
    temperature=0.8,
    top_p=0.9,
    extra_body={
        "chat_template_kwargs": {"enable_thinking": True},
    },
)

print(response.choices[0].message.content)
```

### Recommended Parameters

| Parameter | Value |
|---|---|
| **Temperature** | 0.8 |
| **Top-p** | 0.9 |
| **max_new_tokens** | 32,768 |
| **enable_thinking** | `True` (recommended) |
| **Context length** | ≤ 262,144 tokens |

## Key Improvements

- **Enhanced Reasoning Performance**: While VetJarvis 1.0 showed minimal performance differences with or without the `think` option enabled, version 1.1 addresses this limitation and delivers meaningful performance gains in `think` mode.
- **GPT-5.4-mini Class Reasoning**: Through a refined post-training pipeline, VetJarvis 1.1 provides logical reasoning performance on par with **GPT-5.4-mini**.

## Usage

For usage instructions and detailed model documentation, please refer to the [VetJarvis 1.0 repository](https://huggingface.co/choonok/VetJarvis-4B-Instruct).
