---
language:
- en
- ko
license: other
license_name: solar-apache-2.0
tags:
- upstage
- solar
- moe
- 100b
- llm
- mlx
library_name: mlx
base_model: upstage/Solar-Open-100B
pipeline_tag: text-generation
---

# mlx-community/Solar-Open-100B-8bit

This model [mlx-community/Solar-Open-100B-8bit](https://huggingface.co/mlx-community/Solar-Open-100B-8bit) was
converted to MLX format from [upstage/Solar-Open-100B](https://huggingface.co/upstage/Solar-Open-100B)
using mlx-lm version **0.30.0**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/Solar-Open-100B-8bit")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True, return_dict=False,
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
