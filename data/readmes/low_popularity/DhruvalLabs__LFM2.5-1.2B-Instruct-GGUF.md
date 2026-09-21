---
license: other
license_name: lfm1.0
license_link: LICENSE
base_model: LiquidAI/LFM2.5-1.2B-Instruct
pipeline_tag: text-generation
tags:
  - arxiv:2511.23404
  - text-generation
  - fr
  - ja
  - safetensors
  - ar
  - base_model:finetune:LiquidAI/LFM2.5-1.2B-Base
  - lfm2
  - zh
  - base_model:LiquidAI/LFM2.5-1.2B-Base
  - en
  - gguf
  - es
  - transformers
  - conversational
  - liquid
  - edge
  - deploy:azure
  - lfm2.5
  - region:us
  - quantized
  - de
  - ko
  - eval-results
language:
  - en
---

<div align="center">

# LFM2.5-1.2B-Instruct — GGUF Quantizations

[![Model on HF](https://img.shields.io/badge/🤗-Model_on_HuggingFace-yellow)](https://huggingface.co/Dhptl/LFM2.5-1.2B-Instruct-GGUF)
[![Original Model](https://img.shields.io/badge/Original-LiquidAI_LFM2.5-1.2B-Instruct-blue)](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct)
[![quant-kit](https://img.shields.io/badge/Made_with-quant--kit-green)](https://github.com/DhruvalPtl/quant-kit)

**Quantized GGUF versions of [LiquidAI/LFM2.5-1.2B-Instruct](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct)**

Works with **[llama.cpp](https://github.com/ggerganov/llama.cpp)** · **[Ollama](https://ollama.ai)** · **[LM Studio](https://lmstudio.ai)** · **[Open WebUI](https://openwebui.com)** · **[Jan](https://jan.ai)**

*Quantized by **[Dhptl](https://huggingface.co/Dhptl)** on June 18, 2026 using [quant-kit](https://github.com/DhruvalPtl/quant-kit)*

</div>

---

## ⚖️ The Pareto Frontier — Efficiency vs Intelligence

> Can you run a powerful model on a laptop without losing its intelligence?

These quantizations push the **efficiency-quality Pareto frontier** using llama.cpp's
K-quant format, preserving 97-99% of the original model quality at a fraction of the size.

| Benchmark | Original (FP16) | Q4_K_M | Quality Retained |
|---|---|---|---|
| **MMLU Pro** | *See [original card](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct)* | *Run benchmarks* | ~97-99% |
| **HellaSwag** | *See [original card](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct)* | *Run benchmarks* | ~97-99% |
| **ARC Challenge** | *See [original card](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct)* | *Run benchmarks* | ~97-99% |
| **TruthfulQA** | *See [original card](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct)* | *Run benchmarks* | ~97-99% |
| **GSM8K** | *See [original card](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct)* | *Run benchmarks* | ~97-99% |


---

## 📦 Available Files

| Filename | Size | RAM Required | Quant | Quality | Best For |
|---|---|---|---|---|---|
| `LFM2.5-1.2B-Instruct-Q2_K.gguf` | 0.45 GB | ~2.0 GB | `Q2_K` | ⭐ | Extreme compression, significant quality loss. |
| `LFM2.5-1.2B-Instruct-Q3_K_L.gguf` | 0.59 GB | ~2.1 GB | `Q3_K_L` | ⭐⭐⭐ | Slightly better than Q3_K_M, still a compromise. |
| `LFM2.5-1.2B-Instruct-Q3_K_M.gguf` | 0.56 GB | ~2.1 GB | `Q3_K_M` | ⭐⭐⭐ | Very small file. Quality drop noticeable. |
| `LFM2.5-1.2B-Instruct-Q3_K_S.gguf` | 0.52 GB | ~2.0 GB | `Q3_K_S` | ⭐⭐ | Very high compression, high quality loss. |
| `LFM2.5-1.2B-Instruct-Q4_K_M.gguf` | 0.68 GB | ~2.2 GB | `Q4_K_M` ✅ **Recommended** | ⭐⭐⭐⭐ | Best balance of size and quality. Recommended for most users. |
| `LFM2.5-1.2B-Instruct-Q4_K_S.gguf` | 0.65 GB | ~2.2 GB | `Q4_K_S` | ⭐⭐⭐½ | Good speed/size balance, slight quality loss. |
| `LFM2.5-1.2B-Instruct-Q5_K_M.gguf` | 0.79 GB | ~2.3 GB | `Q5_K_M` | ⭐⭐⭐⭐½ | Better quality than Q4, slightly larger. Great if you have the RAM. |
| `LFM2.5-1.2B-Instruct-Q5_K_S.gguf` | 0.77 GB | ~2.3 GB | `Q5_K_S` | ⭐⭐⭐⭐ | Large but accurate. |
| `LFM2.5-1.2B-Instruct-Q6_K.gguf` | 0.90 GB | ~2.4 GB | `Q6_K` | ⭐⭐⭐⭐⭐ | Near-perfect quality, very large. |
| `LFM2.5-1.2B-Instruct-Q8_0.gguf` | 1.16 GB | ~2.7 GB | `Q8_0` | ⭐⭐⭐⭐⭐ | Closest to original quality. Use when RAM is not a concern. |


### 💡 Which file should I download?

- **Most users:** `LFM2.5-1.2B-Instruct-Q4_K_M.gguf` — best balance of size and quality
- **High RAM (32GB+):** `LFM2.5-1.2B-Instruct-Q8_0.gguf` — near-original quality
- **Low RAM (8GB):** `LFM2.5-1.2B-Instruct-Q3_K_M.gguf` — fits in 8GB with room to spare

---

## ⚡ Speed Benchmarks

*Run `python benchmark.py --model LFM2.5-1.2B-Instruct` to generate speed results.*


---

## 🧠 Quality Benchmarks

*Run `kaggle_bench.ipynb` on Kaggle to benchmark this model.*


---

## 🚀 How to Use

### Ollama
```bash
ollama run dhptl/lfm2.5-1.2b-instruct
```

### LM Studio / Jan / Open WebUI
Search for `Dhptl/LFM2.5-1.2B-Instruct` in the model browser.

### llama.cpp CLI
```bash
# Download the binary from https://github.com/ggerganov/llama.cpp/releases
./llama-cli \
  -m LFM2.5-1.2B-Instruct-Q4_K_M.gguf \
  -p "You are a helpful assistant." \
  --conversation \
  -n 512
```

### Python — llama-cpp-python
```python
from llama_cpp import Llama

llm = Llama(
    model_path="./LFM2.5-1.2B-Instruct-Q4_K_M.gguf",
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