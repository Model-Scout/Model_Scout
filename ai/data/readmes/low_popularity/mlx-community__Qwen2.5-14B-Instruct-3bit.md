---
base_model: Qwen/Qwen2.5-14B
language:
- zho
- eng
- fra
- spa
- por
- deu
- ita
- rus
- jpn
- kor
- vie
- tha
- ara
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen2.5-14B-Instruct/blob/main/LICENSE
pipeline_tag: text-generation
tags:
- chat
- mlx
---

# mlx-community/Qwen2.5-14B-Instruct-3bit

The Model [mlx-community/Qwen2.5-14B-Instruct-3bit](https://huggingface.co/mlx-community/Qwen2.5-14B-Instruct-3bit) was converted to MLX format from [Qwen/Qwen2.5-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct) using mlx-lm version **0.21.1**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/Qwen2.5-14B-Instruct-3bit")
response = generate(model, tokenizer, prompt="hello", verbose=True)
```
