---
base_model: tiiuae/Falcon-H1-1.5B-Instruct
language:
- ar
- cs
- de
- en
- es
- fr
- hi
- it
- ja
- ko
- nl
- pl
- pt
- ro
- ru
- sv
- ur
- zh
library_name: mlx
license: other
license_name: falcon-llm-license
license_link: https://falconllm.tii.ae/falcon-terms-and-conditions.html
tags:
- falcon-h1
- mlx
inference: true
pipeline_tag: text-generation
paper: tiiuae/falcon-h1
---

# mlx-community/Falcon-H1-1.5B-Instruct-4bit

This model [mlx-community/Falcon-H1-1.5B-Instruct-4bit](https://huggingface.co/mlx-community/Falcon-H1-1.5B-Instruct-4bit) was
converted to MLX format from [tiiuae/Falcon-H1-1.5B-Instruct](https://huggingface.co/tiiuae/Falcon-H1-1.5B-Instruct)
using mlx-lm version **0.28.0**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/Falcon-H1-1.5B-Instruct-4bit")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
