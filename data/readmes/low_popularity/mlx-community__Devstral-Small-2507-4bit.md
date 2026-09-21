---
language:
- en
- fr
- de
- es
- pt
- it
- ja
- ko
- ru
- zh
- ar
- fa
- id
- ms
- ne
- pl
- ro
- sr
- sv
- tr
- uk
- vi
- hi
- bn
license: apache-2.0
library_name: mlx
inference: false
base_model: mlx-community/Devstral-Samll-2507-bf16
extra_gated_description: If you want to learn more about how we process your personal
  data, please read our <a href="https://mistral.ai/terms/">Privacy Policy</a>.
pipeline_tag: text-generation
tags:
- mlx
---

# mlx-community/Devstral-Small-2507-4bit

This model [mlx-community/Devstral-Small-2507-4bit](https://huggingface.co/mlx-community/Devstral-Small-2507-4bit) was
converted to MLX format from [mlx-community/Devstral-Samll-2507-bf16](https://huggingface.co/mlx-community/Devstral-Samll-2507-bf16)
using mlx-lm version **0.26.0**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/Devstral-Small-2507-4bit")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
