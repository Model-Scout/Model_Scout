---
library_name: mlx
license: apache-2.0
language:
- af
- am
- ar
- as
- az
- be
- bg
- bn
- br
- bs
- ca
- cs
- cy
- da
- de
- el
- en
- eo
- es
- et
- eu
- fa
- ff
- fi
- fr
- fy
- ga
- gd
- gl
- gn
- gu
- ha
- he
- hi
- hr
- ht
- hu
- hy
- id
- ig
- is
- it
- ja
- jv
- ka
- kk
- km
- kn
- ko
- ku
- ky
- la
- lg
- li
- ln
- lo
- lt
- lv
- mg
- mk
- ml
- mn
- mr
- ms
- my
- ne
- nl
- 'no'
- ns
- om
- or
- pa
- pl
- ps
- pt
- qu
- rm
- ro
- ru
- sa
- sc
- sd
- si
- sk
- sl
- so
- sq
- sr
- ss
- su
- sv
- sw
- ta
- te
- th
- tl
- tn
- tr
- ug
- uk
- ur
- uz
- vi
- wo
- xh
- yi
- yo
- zh
- zu
language_bcp47:
- bn-Latn
- hi-Latn
- my-x-zawgyi
- ta-Latn
- te-Latn
- ur-Latn
- zh-Hans
- zh-Hant
pipeline_tag: text-generation
tags:
- mlx
base_model: mixedbread-ai/mxbai-rerank-large-v2
---

# mlx-community/mxbai-rerank-large-v2

This model [mlx-community/mxbai-rerank-large-v2](https://huggingface.co/mlx-community/mxbai-rerank-large-v2) was
converted to MLX format from [mixedbread-ai/mxbai-rerank-large-v2](https://huggingface.co/mixedbread-ai/mxbai-rerank-large-v2)
using mlx-lm version **0.26.0**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/mxbai-rerank-large-v2")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
