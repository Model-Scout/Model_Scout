---
license: apache-2.0
language:
- en
- es
- fr
- de
- it
- pt
- ru
- ar
- hi
- ko
- zh
library_name: mlx
base_model: arcee-ai/Trinity-Mini
pipeline_tag: text-generation
tags:
- mlx
---

# mlx-community/Trinity-Mini-4bit

This model [mlx-community/Trinity-Mini-4bit](https://huggingface.co/mlx-community/Trinity-Mini-4bit) was
converted to MLX format from [arcee-ai/Trinity-Mini](https://huggingface.co/arcee-ai/Trinity-Mini)
using mlx-lm version **0.28.4**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/Trinity-Mini-4bit")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
