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
- abliterated
- uncensored
- mlx
- mlx-my-repo
base_model: huihui-ai/Huihui-LFM2.5-8B-A1B-abliterated
---

# usermma/Huihui-LFM2.5-8B-A1B-abliterated-mlx-2Bit

The Model [usermma/Huihui-LFM2.5-8B-A1B-abliterated-mlx-2Bit](https://huggingface.co/usermma/Huihui-LFM2.5-8B-A1B-abliterated-mlx-2Bit) was converted to MLX format from [huihui-ai/Huihui-LFM2.5-8B-A1B-abliterated](https://huggingface.co/huihui-ai/Huihui-LFM2.5-8B-A1B-abliterated) using mlx-lm version **0.31.2**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("usermma/Huihui-LFM2.5-8B-A1B-abliterated-mlx-2Bit")

prompt="hello"

if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
