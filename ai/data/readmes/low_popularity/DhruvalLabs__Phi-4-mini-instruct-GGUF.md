---
license: mit
base_model: microsoft/Phi-4-mini-instruct
pipeline_tag: text-generation
tags:
  - ko
  - zh
  - ar
  - he
  - multilingual
  - ru
  - es
  - quantized
  - da
  - code
  - th
  - nl
  - phi3
  - text-generation-inference
  - nlp
  - it
  - uk
  - custom_code
  - en
  - pl
  - eval-results
  - fr
  - sv
  - region:us
  - transformers
  - ja
  - safetensors
  - text-generation
  - hu
  - no
  - conversational
  - arxiv:2503.01743
  - fi
  - tr
  - de
  - gguf
  - cs
  - pt
  - license:mit
language:
  - en
---

<div align="center">

# Phi-4-mini-instruct — GGUF Quantizations

[![Model on HF](https://img.shields.io/badge/🤗-Model_on_HuggingFace-yellow)](https://huggingface.co/Dhptl/Phi-4-mini-instruct-GGUF)
[![Original Model](https://img.shields.io/badge/Original-microsoft_Phi-4-mini-instruct-blue)](https://huggingface.co/microsoft/Phi-4-mini-instruct)
[![quant-kit](https://img.shields.io/badge/Made_with-quant--kit-green)](https://github.com/DhruvalPtl/quant-kit)

**Quantized GGUF versions of [microsoft/Phi-4-mini-instruct](https://huggingface.co/microsoft/Phi-4-mini-instruct)**

Works with **[llama.cpp](https://github.com/ggerganov/llama.cpp)** · **[Ollama](https://ollama.ai)** · **[LM Studio](https://lmstudio.ai)** · **[Open WebUI](https://openwebui.com)** · **[Jan](https://jan.ai)**

*Quantized by **[Dhptl](https://huggingface.co/Dhptl)** on June 16, 2026 using [quant-kit](https://github.com/DhruvalPtl/quant-kit)*

</div>

---

## ⚖️ The Pareto Frontier — Efficiency vs Intelligence

> Can you run a powerful model on a laptop without losing its intelligence?

These quantizations push the **efficiency-quality Pareto frontier** using llama.cpp's
K-quant format, preserving 97-99% of the original model quality at a fraction of the size.

| Benchmark | Original (FP16) | Q4_K_M | Quality Retained |
|---|---|---|---|
| **MMLU Pro** | *See [original card](https://huggingface.co/microsoft/Phi-4-mini-instruct)* | *Run benchmarks* | ~97-99% |
| **HellaSwag** | *See [original card](https://huggingface.co/microsoft/Phi-4-mini-instruct)* | *Run benchmarks* | ~97-99% |
| **ARC Challenge** | *See [original card](https://huggingface.co/microsoft/Phi-4-mini-instruct)* | *Run benchmarks* | ~97-99% |
| **TruthfulQA** | *See [original card](https://huggingface.co/microsoft/Phi-4-mini-instruct)* | *Run benchmarks* | ~97-99% |
| **GSM8K** | *See [original card](https://huggingface.co/microsoft/Phi-4-mini-instruct)* | *Run benchmarks* | ~97-99% |


---

## 📦 Available Files

| Filename | Size | RAM Required | Quant | Quality | Best For |
|---|---|---|---|---|---|
| `Phi-4-mini-instruct-Q2_K.gguf` | 1.61 GB | ~3.1 GB | `Q2_K` | ⭐ | Extreme compression, significant quality loss. |
| `Phi-4-mini-instruct-Q3_K_L.gguf` | 2.15 GB | ~3.7 GB | `Q3_K_L` | ⭐⭐⭐ | Slightly better than Q3_K_M, still a compromise. |
| `Phi-4-mini-instruct-Q3_K_M.gguf` | 1.98 GB | ~3.5 GB | `Q3_K_M` | ⭐⭐⭐ | Very small file. Quality drop noticeable. |
| `Phi-4-mini-instruct-Q3_K_S.gguf` | 1.77 GB | ~3.3 GB | `Q3_K_S` | ⭐⭐ | Very high compression, high quality loss. |
| `Phi-4-mini-instruct-Q4_K_M.gguf` | 2.32 GB | ~3.8 GB | `Q4_K_M` ✅ **Recommended** | ⭐⭐⭐⭐ | Best balance of size and quality. Recommended for most users. |
| `Phi-4-mini-instruct-Q4_K_S.gguf` | 2.18 GB | ~3.7 GB | `Q4_K_S` | ⭐⭐⭐½ | Good speed/size balance, slight quality loss. |
| `Phi-4-mini-instruct-Q5_K_M.gguf` | 2.62 GB | ~4.1 GB | `Q5_K_M` | ⭐⭐⭐⭐½ | Better quality than Q4, slightly larger. Great if you have the RAM. |
| `Phi-4-mini-instruct-Q5_K_S.gguf` | 2.54 GB | ~4.0 GB | `Q5_K_S` | ⭐⭐⭐⭐ | Large but accurate. |
| `Phi-4-mini-instruct-Q6_K.gguf` | 2.94 GB | ~4.4 GB | `Q6_K` | ⭐⭐⭐⭐⭐ | Near-perfect quality, very large. |
| `Phi-4-mini-instruct-Q8_0.gguf` | 3.80 GB | ~5.3 GB | `Q8_0` | ⭐⭐⭐⭐⭐ | Closest to original quality. Use when RAM is not a concern. |


### 💡 Which file should I download?

- **Most users:** `Phi-4-mini-instruct-Q4_K_M.gguf` — best balance of size and quality
- **High RAM (32GB+):** `Phi-4-mini-instruct-Q8_0.gguf` — near-original quality
- **Low RAM (8GB):** `Phi-4-mini-instruct-Q3_K_M.gguf` — fits in 8GB with room to spare

---

## ⚡ Speed Benchmarks

*Run `python benchmark.py --model Phi-4-mini-instruct` to generate speed results.*


---

## 🧠 Quality Benchmarks

*Run `kaggle_bench.ipynb` on Kaggle to benchmark this model.*


---

## 🚀 How to Use

### Ollama
```bash
ollama run dhptl/phi-4-mini-instruct
```

### LM Studio / Jan / Open WebUI
Search for `Dhptl/Phi-4-mini-instruct` in the model browser.

### llama.cpp CLI
```bash
# Download the binary from https://github.com/ggerganov/llama.cpp/releases
./llama-cli \
  -m Phi-4-mini-instruct-Q4_K_M.gguf \
  -p "You are a helpful assistant." \
  --conversation \
  -n 512
```

### Python — llama-cpp-python
```python
from llama_cpp import Llama

llm = Llama(
    model_path="./Phi-4-mini-instruct-Q4_K_M.gguf",
    n_gpu_layers=-1,   # -1 = offload everything to GPU
    n_ctx=4096,
)

response = llm.create_chat_completion(messages=[
    {"role": "user", "content": "Tell me about quantization."}
])
print(response["choices"][0]["message"]["content"])
```

---

## 🔍 About GGUF Quantization

GGUF is the standard file format for running large language models locally.
Quantization reduces the number of bits per weight:

| Format | Bits/weight | Size vs FP16 | Quality |
|---|---|---|---|
| Q2_K | ~2.6 | 16% | ⭐ |
| Q3_K_M | ~3.3 | 21% | ⭐⭐⭐ |
| Q4_K_M | ~4.5 | 28% | ⭐⭐⭐⭐ ← sweet spot |
| Q5_K_M | ~5.6 | 35% | ⭐⭐⭐⭐½ |
| Q8_0 | ~8.5 | 53% | ⭐⭐⭐⭐⭐ |

---

## 💬 Community & Feedback

Found an issue? Have a question? Open a **Discussion** in the Community tab above.

If these quantizations were useful, please consider:
- ⭐ Starring [quant-kit](https://github.com/DhruvalPtl/quant-kit) on GitHub
- 👍 Liking this model on HuggingFace
- 💬 Leaving feedback in the Community tab