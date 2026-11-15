---
license: llama3.2
base_model: torchtorchkimtorch/Llama-3.2-Korean-GGACHI-1B-Instruct-v1
base_model_relation: quantized
library_name: gguf
pipeline_tag: text-generation
tags:
- llama
- gguf
- llama3.2
- korean
- instruction-tuned
- llama-cpp
---

# Llama-3.2-Korean-GGACHI-1B-Instruct-v1 — GGUF

GGUF quantizations of `torchtorchkimtorch/Llama-3.2-Korean-GGACHI-1B-Instruct-v1`, a Llama-3.2-1B fine-tuned on 230k+ Korean instruction data, produced with llama.cpp.

## Available files

| File | Quantization | Description |
|---|---|---|
| `model-F16.gguf` | F16 | Full precision (3.0 GB) |
| `model-Q8_0.gguf` | Q8_0 | 8-bit |
| `model-Q6_K.gguf` | Q6_K | 6-bit |
| `model-Q5_K_M.gguf` | Q5_K_M | 5-bit medium |
| `model-Q5_K_S.gguf` | Q5_K_S | 5-bit small |
| `model-Q5_0.gguf` | Q5_0 | 5-bit |
| `model-Q4_K_M.gguf` | Q4_K_M | 4-bit medium (recommended) |
| `model-Q4_K_S.gguf` | Q4_K_S | 4-bit small |
| `model-Q4_0.gguf` | Q4_0 | 4-bit |
| `model-Q3_K_L.gguf` | Q3_K_L | 3-bit large |
| `model-Q3_K_M.gguf` | Q3_K_M | 3-bit medium |
| `model-Q3_K_S.gguf` | Q3_K_S | 3-bit small |
| `model-Q2_K.gguf` | Q2_K | 2-bit |

## Usage

With llama.cpp:

```bash
./llama-cli -m model-Q4_K_M.gguf -p "Your prompt" -n 256
```

Or any GGUF-compatible runtime (Ollama, LM Studio, koboldcpp, etc.).

## License

Meta Llama 3.2 Community License. Built on `meta-llama/Llama-3.2-1B-Instruct`.

## Disclaimer

Korean instruction-tuned model. Evaluate before use.
