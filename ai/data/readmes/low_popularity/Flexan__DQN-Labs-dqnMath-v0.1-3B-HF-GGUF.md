---
base_model: DQN-Labs/dqnMath-v0.1-3B-HF
library_name: mlx
language:
- en
- fr
- es
- de
- it
- pt
- nl
- zh
- ja
- ko
- ar
license: apache-2.0
inference: true
pipeline_tag: text-generation
tags:
- mlx
---

# GGUF Files for dqnMath-v0.1-3B-HF

These are the GGUF files for [DQN-Labs/dqnMath-v0.1-3B-HF](https://huggingface.co/DQN-Labs/dqnMath-v0.1-3B-HF).

## Downloads

| GGUF Link | Quantization | Description |
| ---- | ----- | ----------- |
| [Download](https://huggingface.co/Flexan/DQN-Labs-dqnMath-v0.1-3B-HF-GGUF/resolve/main/dqnMath-v0.1-3B-HF.Q2_K.gguf) | Q2_K | Lowest quality |
| [Download](https://huggingface.co/Flexan/DQN-Labs-dqnMath-v0.1-3B-HF-GGUF/resolve/main/dqnMath-v0.1-3B-HF.Q3_K_S.gguf) | Q3_K_S |  |
| [Download](https://huggingface.co/Flexan/DQN-Labs-dqnMath-v0.1-3B-HF-GGUF/resolve/main/dqnMath-v0.1-3B-HF.IQ3_S.gguf) | IQ3_S | Integer quant, preferable over Q3_K_S |
| [Download](https://huggingface.co/Flexan/DQN-Labs-dqnMath-v0.1-3B-HF-GGUF/resolve/main/dqnMath-v0.1-3B-HF.IQ3_M.gguf) | IQ3_M | Integer quant |
| [Download](https://huggingface.co/Flexan/DQN-Labs-dqnMath-v0.1-3B-HF-GGUF/resolve/main/dqnMath-v0.1-3B-HF.Q3_K_M.gguf) | Q3_K_M |  |
| [Download](https://huggingface.co/Flexan/DQN-Labs-dqnMath-v0.1-3B-HF-GGUF/resolve/main/dqnMath-v0.1-3B-HF.Q3_K_L.gguf) | Q3_K_L |  |
| [Download](https://huggingface.co/Flexan/DQN-Labs-dqnMath-v0.1-3B-HF-GGUF/resolve/main/dqnMath-v0.1-3B-HF.IQ4_XS.gguf) | IQ4_XS | Integer quant |
| [Download](https://huggingface.co/Flexan/DQN-Labs-dqnMath-v0.1-3B-HF-GGUF/resolve/main/dqnMath-v0.1-3B-HF.Q4_K_S.gguf) | Q4_K_S | Fast with good performance |
| [Download](https://huggingface.co/Flexan/DQN-Labs-dqnMath-v0.1-3B-HF-GGUF/resolve/main/dqnMath-v0.1-3B-HF.Q4_K_M.gguf) | Q4_K_M | **Recommended:** Perfect mix of speed and performance |
| [Download](https://huggingface.co/Flexan/DQN-Labs-dqnMath-v0.1-3B-HF-GGUF/resolve/main/dqnMath-v0.1-3B-HF.Q5_K_S.gguf) | Q5_K_S |  |
| [Download](https://huggingface.co/Flexan/DQN-Labs-dqnMath-v0.1-3B-HF-GGUF/resolve/main/dqnMath-v0.1-3B-HF.Q5_K_M.gguf) | Q5_K_M |  |
| [Download](https://huggingface.co/Flexan/DQN-Labs-dqnMath-v0.1-3B-HF-GGUF/resolve/main/dqnMath-v0.1-3B-HF.Q6_K.gguf) | Q6_K | Very good quality |
| [Download](https://huggingface.co/Flexan/DQN-Labs-dqnMath-v0.1-3B-HF-GGUF/resolve/main/dqnMath-v0.1-3B-HF.Q8_0.gguf) | Q8_0 | Best quality |
| [Download](https://huggingface.co/Flexan/DQN-Labs-dqnMath-v0.1-3B-HF-GGUF/resolve/main/dqnMath-v0.1-3B-HF.f16.gguf) | f16 | Full precision, don't bother; use a quant |

## Note from Flexan

I provide GGUFs and quantizations of publicly available models that do not have a GGUF equivalent available yet,
usually for models **I deem interesting and wish to try out**.

If there are some quants missing that you'd like me to add, you may request one in the community tab.
If you want to request a public model to be converted, you can also request that in the community tab.
If you have questions regarding this model, please refer to [the original model repo](https://huggingface.co/DQN-Labs/dqnMath-v0.1-3B-HF).

You can find more info about me and what I do [here](https://huggingface.co/Flexan/Flexan).

# DQN-Labs/dqnMath-v0.1-3B-HF

This model [DQN-Labs/dqnMath-v0.1-3B-HF](https://huggingface.co/DQN-Labs/dqnMath-v0.1-3B-HF) was
converted to MLX format from [LakoMoor/Ministral-3-3B-Text-Only](https://huggingface.co/LakoMoor/Ministral-3-3B-Text-Only)
using mlx-lm version **0.29.1**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("DQN-Labs/dqnMath-v0.1-3B-HF")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```