---
license: apache-2.0
datasets:
- TeichAI/claude-4.5-opus-high-reasoning-250x
base_model: DavidAU/Llama3.3-8B-Instruct-Thinking-Claude-4.5-Opus-High-Reasoning
language:
- en
- fr
- de
- es
- it
- pt
- zh
- ja
- ru
- ko
tags:
- thinking
- reasoning
- instruct
- Claude4.5-Opus
- creative
- creative writing
- fiction writing
- plot generation
- sub-plot generation
- story generation
- scene continue
- storytelling
- fiction story
- science fiction
- romance
- all genres
- story
- writing
- vivid prosing
- vivid writing
- fiction
- roleplaying
- bfloat16
- role play
- 128k context
- llama3.3
- llama-3
- llama-3.3
- unsloth
- finetune
- mlx
pipeline_tag: text-generation
library_name: mlx
---

# genai-archive/DavidAU__Llama3.3-8B-Instruct-Thinking-Claude-4.5-Opus-High-Reasoning-mlx-mxfp4

This model [genai-archive/DavidAU__Llama3.3-8B-Instruct-Thinking-Claude-4.5-Opus-High-Reasoning-mlx-mxfp4](https://huggingface.co/genai-archive/DavidAU__Llama3.3-8B-Instruct-Thinking-Claude-4.5-Opus-High-Reasoning-mlx-mxfp4) was
converted to MLX format from [DavidAU/Llama3.3-8B-Instruct-Thinking-Claude-4.5-Opus-High-Reasoning](https://huggingface.co/DavidAU/Llama3.3-8B-Instruct-Thinking-Claude-4.5-Opus-High-Reasoning)
using mlx-lm version **0.31.1**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("genai-archive/DavidAU__Llama3.3-8B-Instruct-Thinking-Claude-4.5-Opus-High-Reasoning-mlx-mxfp4")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True, return_dict=False,
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
