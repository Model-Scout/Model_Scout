---
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
language:
- en
- ko
tags:
- code
- code-generation
- function-calling
- darwin
- mlx
- mlx-my-repo
base_model: FINAL-Bench/Darwin-28B-Coder
datasets:
- m-a-p/CodeFeedback-Filtered-Instruction
---

# usermma/Darwin-28B-Coder-mlx-fp16

The Model [usermma/Darwin-28B-Coder-mlx-fp16](https://huggingface.co/usermma/Darwin-28B-Coder-mlx-fp16) was converted to MLX format from [FINAL-Bench/Darwin-28B-Coder](https://huggingface.co/FINAL-Bench/Darwin-28B-Coder) using mlx-lm version **0.31.2**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("usermma/Darwin-28B-Coder-mlx-fp16")

prompt="hello"

if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
