---
inference: false
library_name: mlx
language:
- en
- nl
- fr
- it
- pt
- ro
- es
- cs
- pl
- uk
- ru
- el
- de
- da
- sv
- 'no'
- ca
- gl
- cy
- ga
- eu
- hr
- lv
- lt
- sk
- sl
- et
- fi
- hu
- sr
- bg
- ar
- fa
- ur
- tr
- mt
- he
- hi
- mr
- bn
- gu
- pa
- ta
- te
- ne
- tl
- ms
- id
- vi
- jv
- km
- th
- lo
- zh
- my
- ja
- ko
- am
- ha
- ig
- mg
- sn
- sw
- wo
- xh
- yo
- zu
license: cc-by-nc-4.0
extra_gated_prompt: By submitting this form, you agree to the [License Agreement](https://cohere.com/c4ai-cc-by-nc-license)  and
  acknowledge that the information you provide will be collected, used, and shared
  in accordance with Cohere's [Privacy Policy]( https://cohere.com/privacy). You'll
  receive email updates about Cohere Labs and Cohere research, events, products and
  services. You can unsubscribe at any time.
extra_gated_fields:
  Name: text
  Affiliation: text
  Country: country
  I agree to use this model for non-commercial use ONLY: checkbox
base_model: CohereLabs/tiny-aya-global
pipeline_tag: text-generation
tags:
- mlx
---

# mlx-community/tiny-aya-global-8bit-mlx

This model [mlx-community/tiny-aya-global-8bit-mlx](https://huggingface.co/mlx-community/tiny-aya-global-8bit-mlx) was
converted to MLX format from [CohereLabs/tiny-aya-global](https://huggingface.co/CohereLabs/tiny-aya-global)
using mlx-lm version **0.28.3**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/tiny-aya-global-8bit-mlx")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
