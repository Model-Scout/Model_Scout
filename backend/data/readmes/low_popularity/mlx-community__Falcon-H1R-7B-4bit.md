---
library_name: mlx
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
tags:
- falcon-h1r
- mlx
license: other
license_name: falcon-llm-license
license_link: https://falconllm.tii.ae/falcon-terms-and-conditions.html
base_model: tiiuae/Falcon-H1R-7B
pipeline_tag: text-generation
---

# mlx-community/Falcon-H1R-7B-4bit

This model [mlx-community/Falcon-H1R-7B-4bit](https://huggingface.co/mlx-community/Falcon-H1R-7B-4bit) was
converted to MLX format from [tiiuae/Falcon-H1R-7B](https://huggingface.co/tiiuae/Falcon-H1R-7B)
using mlx-lm version **0.29.1**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/Falcon-H1R-7B-4bit")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
