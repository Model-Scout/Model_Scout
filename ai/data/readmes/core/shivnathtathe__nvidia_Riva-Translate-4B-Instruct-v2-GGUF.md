---
base_model: nvidia/Riva-Translate-4B-Instruct-v2
base_model_relation: quantized
language:
- en
- de
- fr
- es
- zh
- ja
- hi
- ar
- ru
- ko
tags:
- translation
- gguf
- llama-cpp
- mistral
- nvidia
- quantized
license: apache-2.0
library_name: gguf
pipeline_tag: translation
quantized_by: shivnathtathe
---

# Riva-Translate-4B-Instruct-v2 GGUF

GGUF quantization of [nvidia/Riva-Translate-4B-Instruct-v2](https://huggingface.co/nvidia/Riva-Translate-4B-Instruct-v2).

Supports translation across **36 languages**. Trained Nov 2025 – May 2026.

## Provided Quants

| Quant | Size | Description |
|---|---|---|
| [Q4_K_M](https://huggingface.co/shivnathtathe/nvidia_Riva-Translate-4B-Instruct-v2-GGUF/blob/main/Riva-Translate-4B-Instruct-v2-Q4_K_M.gguf) | 2.76GB | Recommended |

## Usage with llama.cpp

```bash
llama-cli -m Riva-Translate-4B-Instruct-v2-Q4_K_M.gguf -p "Translate to French: Hello"
```

Quantized by [@shivnathtathe](https://huggingface.co/shivnathtathe)