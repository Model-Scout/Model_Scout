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
license: wtfpl
tags:
- heretic
- uncensored
- decensored
- abliterated
- transformers
- mlx
- mlx-my-repo
base_model: darkc0de/XORTRON.CriminalComputing.LARGE.2026.3
pipeline_tag: text-generation
library_name: transformers
---

# otherwhere1/XORTRON.CriminalComputing.LARGE.2026.3-mlx-3Bit

The Model [otherwhere1/XORTRON.CriminalComputing.LARGE.2026.3-mlx-3Bit](https://huggingface.co/otherwhere1/XORTRON.CriminalComputing.LARGE.2026.3-mlx-3Bit) was converted to MLX format from [darkc0de/XORTRON.CriminalComputing.LARGE.2026.3](https://huggingface.co/darkc0de/XORTRON.CriminalComputing.LARGE.2026.3) using mlx-lm version **0.31.2**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("otherwhere1/XORTRON.CriminalComputing.LARGE.2026.3-mlx-3Bit")

prompt="hello"

if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
