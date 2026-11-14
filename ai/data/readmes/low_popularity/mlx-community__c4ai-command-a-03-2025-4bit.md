---
inference: false
library_name: transformers
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
license: cc-by-nc-4.0
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
base_model: CohereForAI/c4ai-command-a-03-2025
tags:
- mlx
---

# mlx-community/c4ai-command-a-03-2025-4bit

The Model [mlx-community/c4ai-command-a-03-2025-4bit](https://huggingface.co/mlx-community/c4ai-command-a-03-2025-4bit) was
converted to MLX format from [CohereForAI/c4ai-command-a-03-2025](https://huggingface.co/CohereForAI/c4ai-command-a-03-2025)
using mlx-lm version **0.22.0**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/c4ai-command-a-03-2025-4bit")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
