---
library_name: mlx
pipeline_tag: text-generation
language:
- zh
- en
- fr
- pt
- es
- ja
- tr
- ru
- ar
- ko
- th
- it
- de
- vi
- ms
- id
- tl
- hi
- pl
- cs
- nl
- km
- my
- fa
- gu
- ur
- te
- mr
- he
- bn
- ta
- uk
- bo
- kk
- mn
- ug
tags:
- transformers
- mlx
- translation
base_model:
- tencent/HY-MT1.5-1.8B
---

# mlx-community/HY-MT1.5-1.8B-8bit

The Model [mlx-community/HY-MT1.5-1.8B-8bit](https://huggingface.co/mlx-community/HY-MT1.5-1.8B-8bit) was converted to MLX format from [tencent/HY-MT1.5-1.8B](https://huggingface.co/tencent/HY-MT1.5-1.8B) using mlx-lm version **0.29.1**.

You can find other similar translation-related MLX model quants for an Apple Mac at https://huggingface.co/bibproj

The following parameters values are recommended for inference:
* top_k: 20
* top_p: 0.6
* repetition_penalty: 1.05
* temperature: 0.7

36 Supported Languages: Chinese, English, French, Portuguese, Spanish, Japanese, Turkish, Russian, Korean, Thai, Italian, German, Vietnamese, Malay, Indonesian, Filipino, Hindi, Traditional Chinese, Polish, Czech, Dutch, Khmer, Burmese, Persian, Gujarati, Urdu, Telugu, Marathi, Hebrew, Bengali, Tamil, Ukrainian, Tibetan, Kazakh, Mongolian, Uyghur, and Cantonese.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/HY-MT1.5-1.8B-8bit")

prompt="Translate from English to French: Hi there!"

if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```