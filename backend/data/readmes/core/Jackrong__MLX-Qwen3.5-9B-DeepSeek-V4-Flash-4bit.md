---
base_model: Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash
tags:
- text-generation-inference
- transformers
- unsloth
- qwen3_5
- reasoning
- distillation
- deepseek
- deepseek-v4
- sft
- long-cot
- chain-of-thought
- efficient-inference
- agent
- multilingual
- mlx
license: apache-2.0
language:
- en
- zh
- ko
- ja
- es
- ru
pipeline_tag: text-generation
datasets:
- Jackrong/DeepSeek-V4-Distill-8000x
library_name: mlx
---

# Jackrong/MLX-Qwen3.5-9B-DeepSeek-V4-Flash-4bit

This model [Jackrong/MLX-Qwen3.5-9B-DeepSeek-V4-Flash-4bit](https://huggingface.co/Jackrong/MLX-Qwen3.5-9B-DeepSeek-V4-Flash-4bit) was
converted to MLX format from [Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash](https://huggingface.co/Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash)
using mlx-lm version **0.30.7**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("Jackrong/MLX-Qwen3.5-9B-DeepSeek-V4-Flash-4bit")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True, return_dict=False,
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
