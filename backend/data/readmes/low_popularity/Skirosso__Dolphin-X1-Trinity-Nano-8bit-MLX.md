---
license: apache-2.0
base_model: dphn/Dolphin-X1-Trinity-Nano
pipeline_tag: text-generation
library_name: mlx
language:
- en
- es
- fr
- de
- it
- pt
- ru
- ar
- hi
- ko
- zh
tags:
- mlx
---

# drewocarr/Dolphin-X1-Trinity-Nano-8bit-MLX

This model [drewocarr/Dolphin-X1-Trinity-Nano-8bit-MLX](https://huggingface.co/drewocarr/Dolphin-X1-Trinity-Nano-8bit-MLX) was
converted to MLX format from [dphn/Dolphin-X1-Trinity-Nano](https://huggingface.co/dphn/Dolphin-X1-Trinity-Nano)
using mlx-lm version **0.31.3**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("drewocarr/Dolphin-X1-Trinity-Nano-8bit-MLX")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True, return_dict=False,
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
