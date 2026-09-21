---
tags:
- chat
- mlx
base_model: Goekdeniz-Guelmez/JOSIE-1.1-4B-Instruct
pipeline_tag: text-generation
language:
- multilingual
- en
- es
- fr
- pt
- it
- ar
- ko
- id
- ru
- vi
- de
- th
- ja
- zh
library_name: mlx
license: mit
---

# mlx-community/JOSIE-1.1-4B-Instruct-4bit

This model [mlx-community/JOSIE-1.1-4B-Instruct-4bit](https://huggingface.co/mlx-community/JOSIE-1.1-4B-Instruct-4bit) was
converted to MLX format from [Goekdeniz-Guelmez/JOSIE-1.1-4B-Instruct](https://huggingface.co/Goekdeniz-Guelmez/JOSIE-1.1-4B-Instruct)
using mlx-lm version **0.31.0**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/JOSIE-1.1-4B-Instruct-4bit")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True, return_dict=False,
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
