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
- pt
pipeline_tag: text-generation
tags:
- liquid
- lfm2.5
- edge
- mlx
- mlx-my-repo
base_model: LiquidAI/LFM2.5-350M
---

# Oscilla/LFM2.5-350M-mlx-4Bit

The Model [Oscilla/LFM2.5-350M-mlx-4Bit](https://huggingface.co/Oscilla/LFM2.5-350M-mlx-4Bit) was converted to MLX format from [LiquidAI/LFM2.5-350M](https://huggingface.co/LiquidAI/LFM2.5-350M) using mlx-lm version **0.31.2**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("Oscilla/LFM2.5-350M-mlx-4Bit")

prompt="hello"

if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
