---
language:
- ko
- en
license: apache-2.0
tags:
- korean
- llm
- pretrained
- causal-lm
- qwen3-architecture
pipeline_tag: text-generation
---

# Yejin Korean 8B v3 Base

A Korean-English bilingual foundation language model with 8 billion parameters, pre-trained from scratch on a large-scale curated bilingual corpus.

## Model Details

- **Model Name**: Yejin-Korean-8B-v3-Base
- **Parameters**: ~7.52B (Tied Word Embeddings)
- **Architecture**: Transformer Decoder with QK-Norm, GQA, and SwiGLU
- **Hidden Size**: 4096
- **Layers**: 32
- **Attention Heads**: 32 (Query) / 8 (Key-Value) — Grouped Query Attention (4:1)
- **Head Dimension**: 128
- **Intermediate Size**: 14,336
- **Context Length**: 4096 tokens
- **RoPE Base (Theta)**: 500,000.0
- **Vocabulary Size**: 64,000 (Optimized Korean-English BPE)
- **Precision**: BF16 (bfloat16)

## Training

Pre-trained from scratch using PyTorch FSDP on an 8× NVIDIA H200 GPU cluster. The model was trained on a balanced, curated corpus consisting of extensive Korean web, encyclopedia, academic, news, and conversational datasets, alongside high-quality English educational and technical corpora.

## Usage

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "cooler8/yejin-korean-8b-v3-base"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

prompt = "대한민국의 수도는"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

outputs = model.generate(
    **inputs,
    max_new_tokens=64,
    do_sample=True,
    temperature=0.7,
    top_p=0.9,
    repetition_penalty=1.1
)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Notice

This is a pre-trained base model without instruction alignment. For interactive chat and assistant capabilities, please refer to the upcoming SFT / DPO aligned releases.

## License

Apache 2.0
