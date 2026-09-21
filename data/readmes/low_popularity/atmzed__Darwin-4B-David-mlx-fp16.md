---
license: apache-2.0
base_model: FINAL-Bench/Darwin-4B-David
tags:
- darwin-v6
- generation-2
- evolutionary-merge
- mri-guided
- dare-ties
- gemma4
- reasoning
- thinking
- proto-agi
- vidraft
- mlx
- mlx-my-repo
language:
- en
- ko
- ja
- zh
- multilingual
pipeline_tag: text-generation
library_name: transformers
---

# atmzed/Darwin-4B-David-mlx-fp16

The Model [atmzed/Darwin-4B-David-mlx-fp16](https://huggingface.co/atmzed/Darwin-4B-David-mlx-fp16) was converted to MLX format from [FINAL-Bench/Darwin-4B-David](https://huggingface.co/FINAL-Bench/Darwin-4B-David) using mlx-lm version **0.31.2**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("atmzed/Darwin-4B-David-mlx-fp16")

prompt="hello"

if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
