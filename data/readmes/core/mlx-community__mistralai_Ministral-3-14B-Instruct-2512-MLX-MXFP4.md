---
library_name: mlx
language:
- en
- fr
- es
- de
- it
- pt
- nl
- zh
- ja
- ko
- ar
license: apache-2.0
inference: false
base_model: mistralai/Ministral-3-14B-Instruct-2512
extra_gated_description: If you want to learn more about how we process your personal
  data, please read our <a href="https://mistral.ai/terms/">Privacy Policy</a>.
tags:
- mistral-common
- mlx
pipeline_tag: text-generation
---

# mlx-community/mistralai_Ministral-3-14B-Instruct-2512-MLX-MXFP4

This model [mlx-community/mistralai_Ministral-3-14B-Instruct-2512-MLX-MXFP4](https://huggingface.co/mlx-community/mistralai_Ministral-3-14B-Instruct-2512-MLX-MXFP4) was
converted to MLX format from [mistralai/Ministral-3-14B-Instruct-2512](https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512)
using mlx-lm version **0.29.1**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/mistralai_Ministral-3-14B-Instruct-2512-MLX-MXFP4")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
