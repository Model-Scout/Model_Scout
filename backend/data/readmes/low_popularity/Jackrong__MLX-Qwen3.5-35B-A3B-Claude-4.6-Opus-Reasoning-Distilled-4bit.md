---
base_model: Jackrong/Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled
tags:
- text-generation-inference
- transformers
- unsloth
- qwen3_5_moe
- qwen
- qwen3.5
- reasoning
- chain-of-thought
- mlx
license: apache-2.0
language:
- zh
- en
- ko
pipeline_tag: text-generation
datasets:
- nohurry/Opus-4.6-Reasoning-3000x-filtered
- Jackrong/Qwen3.5-reasoning-700x
library_name: mlx
---

# Jackrong/MLX-Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled-4bit

This model [Jackrong/MLX-Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled-4bit](https://huggingface.co/Jackrong/MLX-Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled-4bit) was
converted to MLX format from [Jackrong/Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled)
using mlx-lm version **0.30.7**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("Jackrong/MLX-Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled-4bit")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True, return_dict=False,
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
