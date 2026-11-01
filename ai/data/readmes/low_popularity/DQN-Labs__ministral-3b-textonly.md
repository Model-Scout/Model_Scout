---
base_model: LakoMoor/Ministral-3-3B-Text-Only
library_name: mlx
language:
- en
- fr
- es
- de
- it
- pt
- nl
- zh
- ja
- ko
- ar
license: apache-2.0
inference: true
tags:
- mlx
pipeline_tag: text-generation
---

# DQN-Labs/ministral-3b-textonly

This model [DQN-Labs/ministral-3b-textonly](https://huggingface.co/DQN-Labs/ministral-3b-textonly) was
converted to MLX format from [LakoMoor/Ministral-3-3B-Text-Only](https://huggingface.co/LakoMoor/Ministral-3-3B-Text-Only)
using mlx-lm version **0.29.1**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("DQN-Labs/ministral-3b-textonly")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
