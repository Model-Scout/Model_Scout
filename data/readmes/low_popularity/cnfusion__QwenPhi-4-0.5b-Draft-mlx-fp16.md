---
license: apache-2.0
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
base_model: rdsm/QwenPhi-4-0.5b-Draft
pipeline_tag: text-generation
library_name: transformers
tags:
- qwen
- qwen2.5
- phi-4
- phi
- mlx
- mlx-my-repo
---

# cnfusion/QwenPhi-4-0.5b-Draft-mlx-fp16

The Model [cnfusion/QwenPhi-4-0.5b-Draft-mlx-fp16](https://huggingface.co/cnfusion/QwenPhi-4-0.5b-Draft-mlx-fp16) was converted to MLX format from [rdsm/QwenPhi-4-0.5b-Draft](https://huggingface.co/rdsm/QwenPhi-4-0.5b-Draft) using mlx-lm version **0.22.3**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("cnfusion/QwenPhi-4-0.5b-Draft-mlx-fp16")

prompt="hello"

if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
