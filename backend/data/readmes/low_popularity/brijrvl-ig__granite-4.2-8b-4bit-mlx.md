---
license: apache-2.0
library_name: mlx
pipeline_tag: text-generation
language:
- en
- de
- es
- fr
- ja
- pt
- ar
- cs
- it
- ko
- nl
- zh
tags:
- granite
- granite-4.2
- reasoning
- thinking
- tool-calling
- ibm
- mlx
---

# granite-4.2-8b-4bit-mlx

4-bit quantized MLX format of [ibm-granite/granite-4.2-8b](https://huggingface.co/ibm-granite/granite-4.2-8b) optimized for Apple Silicon inference.

## Features
- **4-bit Quantization**: Low memory footprint (~4.9 GB), fast prefill and generation on Apple Silicon.
- **Thinking / Chain-of-Thought**: Native reasoning support via `<think> ... </think>` tags.
- **Tool Calling**: Tool use and function calling capabilities.
- **Languages**: Multilingual support across 12+ languages.

## Usage with mlx-lm

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("brijrvl-ig/granite-4.2-8b-4bit-mlx")

prompt = "What is the capital of France?"
messages = [{"role": "user", "content": prompt}]
prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True)

response = generate(model, tokenizer, prompt=prompt, max_tokens=256)
print(response)
```

