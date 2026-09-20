---
language:
- en
- zh
- ko
license: apache-2.0
base_model: Jackrong/Qwopus3.5-9B-v3
tags:
- unsloth
- qwen
- qwen3.5
- reasoning
- chain-of-thought
- lora
- competitive-programming
- mlx
pipeline_tag: text-generation
library_name: mlx
---

# Jackrong/MLX-Qwopus3.5-9B-v3-4bit

This model [Jackrong/MLX-Qwopus3.5-9B-v3-4bit](https://huggingface.co/Jackrong/MLX-Qwopus3.5-9B-v3-4bit) was
converted to MLX format from [Jackrong/Qwopus3.5-9B-v3](https://huggingface.co/Jackrong/Qwopus3.5-9B-v3)
using mlx-lm version **0.30.7**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("Jackrong/MLX-Qwopus3.5-9B-v3-4bit")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True, return_dict=False,
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
