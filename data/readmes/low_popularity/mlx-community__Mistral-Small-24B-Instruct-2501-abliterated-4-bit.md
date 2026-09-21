---
language:
- en
- fr
- de
- es
- it
- pt
- zh
- ja
- ru
- ko
license: apache-2.0
library_name: vllm
inference: false
base_model: huihui-ai/Mistral-Small-24B-Instruct-2501-abliterated
extra_gated_description: If you want to learn more about how we process your personal
  data, please read our <a href="https://mistral.ai/terms/">Privacy Policy</a>.
tags:
- abliterated
- uncensored
- transformers
- mlx
---

# mlx-community/Mistral-Small-24B-Instruct-2501-abliterated-4-bit

The Model [mlx-community/Mistral-Small-24B-Instruct-2501-abliterated-4-bit](https://huggingface.co/mlx-community/Mistral-Small-24B-Instruct-2501-abliterated-4-bit) was
converted to MLX format from [huihui-ai/Mistral-Small-24B-Instruct-2501-abliterated](https://huggingface.co/huihui-ai/Mistral-Small-24B-Instruct-2501-abliterated)
using mlx-lm version **0.21.1**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/Mistral-Small-24B-Instruct-2501-abliterated-4-bit")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
