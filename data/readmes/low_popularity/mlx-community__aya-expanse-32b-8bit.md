---
base_model: CohereForAI/aya-expanse-32b
language:
- en
- fr
- de
- es
- it
- pt
- ja
- ko
- zh
- ar
- el
- fa
- pl
- id
- cs
- he
- hi
- nl
- ro
- ru
- tr
- uk
- vi
library_name: transformers
license: cc-by-nc-4.0
tags:
- mlx
inference: false
extra_gated_prompt: By submitting this form, you agree to the [License Agreement](https://cohere.com/c4ai-cc-by-nc-license)  and
  acknowledge that the information you provide will be collected, used, and shared
  in accordance with Cohere’s [Privacy Policy]( https://cohere.com/privacy). You’ll
  receive email updates about C4AI and Cohere research, events, products and services.
  You can unsubscribe at any time.
extra_gated_fields:
  Name: text
  Affiliation: text
  Country: country
  I agree to use this model for non-commercial use ONLY: checkbox
---

# mlx-community/aya-expanse-32b-8bit

The Model [mlx-community/aya-expanse-32b-8bit](https://huggingface.co/mlx-community/aya-expanse-32b-8bit) was converted to MLX format from [CohereForAI/aya-expanse-32b](https://huggingface.co/CohereForAI/aya-expanse-32b) using mlx-lm version **0.19.1**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/aya-expanse-32b-8bit")

prompt="hello"

if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
