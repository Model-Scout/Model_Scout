---
license: other
license_name: exaone
license_link: LICENSE
language:
- en
- ko
- es
tags:
- lg-ai
- exaone
- exaone-4.0
- mlx
pipeline_tag: text-generation
library_name: mlx
base_model: LGAI-EXAONE/EXAONE-4.0-32B
---

# mlx-community/EXAONE-4.0-32B-4bit

This model [mlx-community/EXAONE-4.0-32B-4bit](https://huggingface.co/mlx-community/EXAONE-4.0-32B-4bit) was
converted to MLX format from [LGAI-EXAONE/EXAONE-4.0-32B](https://huggingface.co/LGAI-EXAONE/EXAONE-4.0-32B)
using mlx-lm version **0.26.0**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/EXAONE-4.0-32B-4bit")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
