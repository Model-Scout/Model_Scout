---
license: other
license_name: qwen
license_link: https://huggingface.co/Qwen/Qwen2.5-72B-Instruct/blob/main/LICENSE
language:
- zho
- eng
- fra
- spa
- por
- deu
- ita
- rus
- jpn
- kor
- vie
- tha
- ara
pipeline_tag: text-generation
base_model: Qwen/Qwen2.5-72B-Instruct
tags:
- chat
- mlx
library_name: transformers
---

# GGorman/Qwen2.5-72B-Instruct-Q8-mlx

The Model [GGorman/Qwen2.5-72B-Instruct-Q8-mlx](https://huggingface.co/GGorman/Qwen2.5-72B-Instruct-Q8-mlx) was converted to MLX format from [Qwen/Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) using mlx-lm version **0.19.1**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("GGorman/Qwen2.5-72B-Instruct-Q8-mlx")

prompt="hello"

if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
