---
language:
- multilingual
- ar
- zh
- cs
- da
- nl
- en
- fi
- fr
- de
- he
- hu
- it
- ja
- ko
- 'no'
- pl
- pt
- ru
- es
- sv
- th
- tr
- uk
library_name: transformers
license: mit
license_link: https://huggingface.co/microsoft/Phi-4-mini-instruct/resolve/main/LICENSE
pipeline_tag: text-generation
tags:
- nlp
- code
- mlx
- mlx-my-repo
widget:
- messages:
  - role: user
    content: Can you provide ways to eat combinations of bananas and dragonfruits?
base_model: microsoft/Phi-4-mini-instruct
---

# SkyStar-tech/Phi-4-mini-instruct-mlx-4Bit

The Model [SkyStar-tech/Phi-4-mini-instruct-mlx-4Bit](https://huggingface.co/SkyStar-tech/Phi-4-mini-instruct-mlx-4Bit) was converted to MLX format from [microsoft/Phi-4-mini-instruct](https://huggingface.co/microsoft/Phi-4-mini-instruct) using mlx-lm version **0.31.2**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("SkyStar-tech/Phi-4-mini-instruct-mlx-4Bit")

prompt="hello"

if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
