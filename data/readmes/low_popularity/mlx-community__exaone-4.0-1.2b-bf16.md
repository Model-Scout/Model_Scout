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
base_model: LGAI-EXAONE/EXAONE-4.0-1.2B
---

# mlx-community/exaone-4.0-1.2b-bf16

This model [mlx-community/exaone-4.0-1.2b-bf16](https://huggingface.co/mlx-community/exaone-4.0-1.2b-bf16) was
converted to MLX format from [LGAI-EXAONE/EXAONE-4.0-1.2B](https://huggingface.co/LGAI-EXAONE/EXAONE-4.0-1.2B)
using mlx-lm version **0.26.0**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/exaone-4.0-1.2b-bf16")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
