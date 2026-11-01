---
library_name: transformers
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
pipeline_tag: text-generation
tags:
- liquid
- lfm2
- edge
- mlx
- mlx-my-repo
new_version: LiquidAI/LFM2.5-1.2B-Instruct
base_model: LiquidAI/LFM2-1.2B
---

# Oscilla/LFM2-1.2B-mlx-8Bit

The Model [Oscilla/LFM2-1.2B-mlx-8Bit](https://huggingface.co/Oscilla/LFM2-1.2B-mlx-8Bit) was converted to MLX format from [LiquidAI/LFM2-1.2B](https://huggingface.co/LiquidAI/LFM2-1.2B) using mlx-lm version **0.31.2**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("Oscilla/LFM2-1.2B-mlx-8Bit")

prompt="hello"

if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
