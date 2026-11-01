---
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
language:
- en
- de
- es
- fr
- ja
- pt
- ar
- cs
- it
- ko
- nl
- zh
tags:
- granite
- granite-4.2
- reasoning
- thinking
- tool-calling
- ibm
- mlx
- mlx-my-repo
base_model: ibm-granite/granite-4.2-30b
---

# dr-robot/granite-4.2-30b-mlx-8Bit

The Model [dr-robot/granite-4.2-30b-mlx-8Bit](https://huggingface.co/dr-robot/granite-4.2-30b-mlx-8Bit) was converted to MLX format from [ibm-granite/granite-4.2-30b](https://huggingface.co/ibm-granite/granite-4.2-30b) using mlx-lm version **0.31.2**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("dr-robot/granite-4.2-30b-mlx-8Bit")

prompt="hello"

if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
