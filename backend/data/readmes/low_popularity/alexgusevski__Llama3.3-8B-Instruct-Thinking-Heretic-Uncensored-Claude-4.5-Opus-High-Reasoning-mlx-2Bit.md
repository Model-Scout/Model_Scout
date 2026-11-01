---
license: apache-2.0
datasets:
- TeichAI/claude-4.5-opus-high-reasoning-250x
base_model: DavidAU/Llama3.3-8B-Instruct-Thinking-Heretic-Uncensored-Claude-4.5-Opus-High-Reasoning
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
- heretic
- uncensored
- abliterated
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
- mlx-my-repo
pipeline_tag: text-generation
library_name: transformers
---

# alexgusevski/Llama3.3-8B-Instruct-Thinking-Heretic-Uncensored-Claude-4.5-Opus-High-Reasoning-mlx-2Bit

The Model [alexgusevski/Llama3.3-8B-Instruct-Thinking-Heretic-Uncensored-Claude-4.5-Opus-High-Reasoning-mlx-2Bit](https://huggingface.co/alexgusevski/Llama3.3-8B-Instruct-Thinking-Heretic-Uncensored-Claude-4.5-Opus-High-Reasoning-mlx-2Bit) was converted to MLX format from [DavidAU/Llama3.3-8B-Instruct-Thinking-Heretic-Uncensored-Claude-4.5-Opus-High-Reasoning](https://huggingface.co/DavidAU/Llama3.3-8B-Instruct-Thinking-Heretic-Uncensored-Claude-4.5-Opus-High-Reasoning) using mlx-lm version **0.29.1**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("alexgusevski/Llama3.3-8B-Instruct-Thinking-Heretic-Uncensored-Claude-4.5-Opus-High-Reasoning-mlx-2Bit")

prompt="hello"

if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
