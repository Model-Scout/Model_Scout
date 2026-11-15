---
license: apache-2.0
base_model: Jiunsong/SuperQwen-AgentWorld-35B-A3B-abliterated
library_name: transformers
pipeline_tag: text-generation
tags:
- qwen
- qwen-agentworld
- world-model
- agent
- environment-simulation
- supertune
- abliterated
- false-refusal-reduction
- post-training
- mlx
- mlx-my-repo
language:
- en
- ko
---

# McG-221/SuperQwen-AgentWorld-35B-A3B-abliterated-mlx-8Bit

The Model [McG-221/SuperQwen-AgentWorld-35B-A3B-abliterated-mlx-8Bit](https://huggingface.co/McG-221/SuperQwen-AgentWorld-35B-A3B-abliterated-mlx-8Bit) was converted to MLX format from [Jiunsong/SuperQwen-AgentWorld-35B-A3B-abliterated](https://huggingface.co/Jiunsong/SuperQwen-AgentWorld-35B-A3B-abliterated) using mlx-lm version **0.31.2**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("McG-221/SuperQwen-AgentWorld-35B-A3B-abliterated-mlx-8Bit")

prompt="hello"

if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
