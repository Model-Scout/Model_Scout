---
library_name: mlx
license: apache-2.0
pipeline_tag: text-generation
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
tags:
- transformers
- mlx
- translation
base_model:
- utter-project/EuroLLM-22B-Instruct-2512
---

# mlx-community/EuroLLM-22B-Instruct-2512-mlx-8bit

The Model [mlx-community/EuroLLM-22B-Instruct-2512-mlx-8bit](https://huggingface.co/mlx-community/EuroLLM-22B-Instruct-2512-mlx-8bit) was converted to MLX format from [utter-project/EuroLLM-22B-Instruct-2512](https://huggingface.co/utter-project/EuroLLM-22B-Instruct-2512) using mlx-lm version **0.28.4**.

You can find other similar translation-related MLX model quants for an Apple Mac at https://huggingface.co/bibproj

35 Languages: Bulgarian, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, German, Greek, Hungarian, Irish, Italian, Latvian, Lithuanian, Maltese, Polish, Portuguese, Romanian, Slovak, Slovenian, Spanish, Swedish, Arabic, Catalan, Chinese, Galician, Hindi, Japanese, Korean, Norwegian, Russian, Turkish, and Ukrainian. 

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/EuroLLM-22B-Instruct-2512-mlx-8bit")

prompt="Translate from English to French: Hi there!"

if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```