---
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
library_name: transformers
tags:
- mlx
---

# mlx-community/aya-23-8B-4bit

The Model [mlx-community/aya-23-8B-4bit](https://huggingface.co/mlx-community/aya-23-8B-4bit) was converted to MLX format from [CohereForAI/aya-23-8B](https://huggingface.co/CohereForAI/aya-23-8B) using mlx-lm version **0.13.1**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/aya-23-8B-4bit")
response = generate(model, tokenizer, prompt="hello", verbose=True)
```
