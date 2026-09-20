---
license: apache-2.0
language:
- en
- de
- es
- fr
- it
- pt
- pl
- nl
- tr
- sv
- cs
- el
- hu
- ro
- fi
- uk
- sl
- sk
- da
- lt
- lv
- et
- bg
- 'no'
- ca
- hr
- ga
- mt
- gl
- zh
- ru
- ko
- ja
- ar
- hi
base_model: utter-project/EuroLLM-1.7B-Instruct
library_name: transformers
tags:
- mlx
---

# jevoma4362/EuroLLM-1.7B-Instruct-mlx-4Bit

The Model [jevoma4362/EuroLLM-1.7B-Instruct-mlx-4Bit](https://huggingface.co/jevoma4362/EuroLLM-1.7B-Instruct-mlx-4Bit) was converted to MLX format from [utter-project/EuroLLM-1.7B-Instruct](https://huggingface.co/utter-project/EuroLLM-1.7B-Instruct) using mlx-lm version **0.31.2**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("jevoma4362/EuroLLM-1.7B-Instruct-mlx-4Bit")

prompt="hello"

if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
