---
license: apache-2.0
library_name: mlx
pipeline_tag: text-generation
language:
- en
- de
- es
- fr
- ja
- pt
- ar
- cs
- it
- ko
- nl
- zh
tags:
- granite
- granite-4.2
- reasoning
- thinking
- tool-calling
- ibm
- mlx
base_model: ibm-granite/granite-4.2-3b
---

# granite-4.2-3b-q8-hi-mlx

Brainwaves
```brainwaves
         arc   arc/e boolq hswag obkqa piqa  wino
q8-hi    0.426,0.570,0.838,0.527,0.410,0.708,0.579
mxfp8    0.393,0.486,0.739,0.492,0.394,0.724,0.603
Thinking
mxfp8    0.344,0.380,0.622
```

# Previous model

granite-4.1-3b
```
         arc   arc/e boolq hswag obkqa piqa  wino
mxfp8    0.406,0.581,0.821,0.484,0.434,0.712,0.559
```

The performance in mxfp8 dips significantly below the old base. It looks like this model does better with int quants.

More metrics coming soon. 

-G

---

This model [granite-4.2-3b-q8-hi-mlx](https://huggingface.co/granite-4.2-3b-q8-hi-mlx) was
converted to MLX format from [ibm-granite/granite-4.2-3b](https://huggingface.co/ibm-granite/granite-4.2-3b)
using mlx-lm version **0.31.3**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("granite-4.2-3b-q8-hi-mlx")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True, return_dict=False,
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
