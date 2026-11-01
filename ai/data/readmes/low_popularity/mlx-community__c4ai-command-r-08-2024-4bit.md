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
library_name: transformers
license: cc-by-nc-4.0
tags:
- mlx

---

# mlx-community/c4ai-command-r-08-2024-4bit

The Model [mlx-community/c4ai-command-r-08-2024-4bit](https://huggingface.co/mlx-community/c4ai-command-r-08-2024-4bit) was converted to MLX format from [CohereForAI/c4ai-command-r-08-2024](https://huggingface.co/CohereForAI/c4ai-command-r-08-2024) using mlx-lm version **0.18.1**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/c4ai-command-r-08-2024-4bit")
response = generate(model, tokenizer, prompt="hello", verbose=True)
```
