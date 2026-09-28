---
license: gemma
base_model: Jiunsong/supergemma4-26b-abliterated-multimodal
tags:
- gemma4
- transformers
- bf16
- multimodal
- instruction-following
- tool-use
- mlx
- mlx-my-repo
language:
- en
- ko
pipeline_tag: text-generation
library_name: transformers
---

# andosen/supergemma4-26b-abliterated-multimodal-mlx-6Bit

The Model [andosen/supergemma4-26b-abliterated-multimodal-mlx-6Bit](https://huggingface.co/andosen/supergemma4-26b-abliterated-multimodal-mlx-6Bit) was converted to MLX format from [Jiunsong/supergemma4-26b-abliterated-multimodal](https://huggingface.co/Jiunsong/supergemma4-26b-abliterated-multimodal) using mlx-lm version **0.31.2**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("andosen/supergemma4-26b-abliterated-multimodal-mlx-6Bit")

prompt="hello"

if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
