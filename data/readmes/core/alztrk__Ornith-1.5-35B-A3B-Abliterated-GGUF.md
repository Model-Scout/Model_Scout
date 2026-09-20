---
base_model: alztrk/Ornith-1.5-35B-A3B-Abliterated
library_name: gguf
tags:
- gguf
- llama-cpp
- quantized
- abliterated
- uncensored
- moe
- dynamic-quant
pipeline_tag: text-generation
license: apache-2.0
language:
- en
- tr
- zh
quantized_by: alztrk
---

# Ornith-1.5-35B-A3B-Abliterated-GGUF

Official Dynamic GGUF quantization suite of [`alztrk/Ornith-1.5-35B-A3B-Abliterated`](https://huggingface.co/alztrk/Ornith-1.5-35B-A3B-Abliterated) (derived from [`ornith-ai/Ornith-1.5-35B-A3B`](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)).

## Overview

**Ornith-1.5-35B-A3B-Abliterated** is created through directional ablation surgery across all 40 hybrid layers, orthogonally projecting refusal directions out from attention and MLP down-projection matrices.

This dedicated repository provides optimized Dynamic GGUF quantizations for local inference in Ollama, LM Studio, and Llama.cpp.

---

## Quantization Details

| File Name | Format | Size | Description |
| :--- | :--- | :--- | :--- |
| `Ornith-1.5-35B-Abliterated-Dynamic-Q4_K_M.gguf` | Q4_K_M (Dynamic) | ~19.71 GB | Balanced performance for 12GB - 16GB VRAM GPUs. |
| `Ornith-1.5-35B-Abliterated-Dynamic-Q5_K_M.gguf` | Q5_K_M (Dynamic) | ~23.03 GB | Higher precision retention. |
| `Ornith-1.5-35B-Abliterated-Dynamic-Q3_K_M.gguf` | Q3_K_M (Dynamic) | ~15.61 GB | Lower memory footprint. |
| `Ornith-1.5-35B-Abliterated-Q8_0.gguf` | Q8_0 | ~34.37 GB | High precision reference quantization. |

---

## How to Run

### 1. Using Ollama

```bash
ollama run hf.co/alztrk/Ornith-1.5-35B-A3B-Abliterated-GGUF:Ornith-1.5-35B-Abliterated-Dynamic-Q4_K_M.gguf
```

### 2. Using LM Studio / Llama.cpp

```bash
llama-cli.exe -hf alztrk/Ornith-1.5-35B-A3B-Abliterated-GGUF -hff Ornith-1.5-35B-Abliterated-Dynamic-Q4_K_M.gguf -p "<|im_start|>user\nHello!<|im_end|>\n<|im_start|>assistant\n" -ngl 24 -c 8192
```

---

## License & Attribution

Derived from [`ornith-ai/Ornith-1.5-35B-A3B`](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B), licensed under the Apache 2.0 / MIT License.
