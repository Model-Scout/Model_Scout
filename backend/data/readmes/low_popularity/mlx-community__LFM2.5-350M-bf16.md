---
library_name: mlx
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
- pt
pipeline_tag: text-generation
tags:
- liquid
- lfm2.5
- edge
- mlx
base_model: LiquidAI/LFM2.5-350M
---

# mlx-community/LFM2.5-350M-bf16

This model [mlx-community/LFM2.5-350M-bf16](https://huggingface.co/mlx-community/LFM2.5-350M-bf16) was
converted to MLX format from [LiquidAI/LFM2.5-350M](https://huggingface.co/LiquidAI/LFM2.5-350M)
using mlx-lm version **0.31.1**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/LFM2.5-350M-bf16")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True, return_dict=False,
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
