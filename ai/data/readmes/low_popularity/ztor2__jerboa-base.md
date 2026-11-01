---
language:
- en
- ko
license: apache-2.0
tags:
- jerboa
- pytorch
- causal-lm
- edge-ai
- apple-silicon
pipeline_tag: text-generation
---

# Jerboa

**Lightweight Language & Multimodal Model** (in active development)

Jerboa is an ultra-lightweight language and multimodal model (~221M parameters) featuring a 28-layer Deep & Thin architecture optimized for Apple Silicon (MPS / Metal) and edge deployments.

---

## Model Specifications

| Attribute | Specification |
| :--- | :--- |
| **Language Backbone** | `JerboaForCausalLM` (~221M parameters) |
| **Multimodal Model** | `JerboaVLForConditionalGeneration` |
| **Layers & Hidden Dim** | 28 Layers, $d_{model}=768$, $d_{ffn}=2048$ (SwiGLU) |
| **Attention** | GQA (12 Query : 4 KV heads), QK-Norm, Interleaved SWA (window 2048, global every 4 layers) |
| **Vocabulary & RoPE** | 49,152 BPE Vocab, RoPE $	heta=500,000$ |
| **Pre-training Volume** | > 1.23 Billion tokens (75% FineWeb-Edu, 25% Python Code) |
| **Hardware Target** | Apple Silicon (MPS / Metal) & Edge Devices |

---

## Quickstart

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "ztor2/jerboa-base"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True)

prompt = "Hello, what are you?"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=128)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```
