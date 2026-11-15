---
license: other
license_name: exaone
license_link: LICENSE
language:
- en
- ko
tags:
- lg-ai
- exaone
- exaone-3.5
- mlx
pipeline_tag: text-generation
library_name: transformers
base_model: LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct
---

# mlx-community/EXAONE-3.5-7.8B-Instruct-3bit

The Model [mlx-community/EXAONE-3.5-7.8B-Instruct-3bit](https://huggingface.co/mlx-community/EXAONE-3.5-7.8B-Instruct-3bit) was
converted to MLX format from [LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct](https://huggingface.co/LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct)
using mlx-lm version **0.20.4**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/EXAONE-3.5-7.8B-Instruct-3bit")

prompt="hello"

if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
