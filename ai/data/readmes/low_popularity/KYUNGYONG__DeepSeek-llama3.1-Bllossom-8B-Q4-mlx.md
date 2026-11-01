---
license: mit
language:
- ko
- en
base_model: UNIVA-Bllossom/DeepSeek-llama3.1-Bllossom-8B
library_name: transformers
tags:
- mlx
---

# KYUNGYONG/DeepSeek-llama3.1-Bllossom-8B-Q4-mlx

The Model [KYUNGYONG/DeepSeek-llama3.1-Bllossom-8B-Q4-mlx](https://huggingface.co/KYUNGYONG/DeepSeek-llama3.1-Bllossom-8B-Q4-mlx) was converted to MLX format from [UNIVA-Bllossom/DeepSeek-llama3.1-Bllossom-8B](https://huggingface.co/UNIVA-Bllossom/DeepSeek-llama3.1-Bllossom-8B) using mlx-lm version **0.21.5**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("KYUNGYONG/DeepSeek-llama3.1-Bllossom-8B-Q4-mlx")

prompt="hello"

if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
