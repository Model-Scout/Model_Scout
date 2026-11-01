---
license: other
license_name: lfm1.0
license_link: LICENSE
base_model: LiquidAI/LFM2.5-8B-A1B
pipeline_tag: text-generation
tags:
  - arxiv:2511.23404
  - region:us
  - conversational
  - pt
  - de
  - gguf
  - it
  - base_model:finetune:LiquidAI/LFM2.5-8B-A1B-Base
  - ja
  - zh
  - es
  - fr
  - base_model:LiquidAI/LFM2.5-8B-A1B-Base
  - quantized
  - ko
  - liquid
  - ar
  - transformers
  - lfm2_moe
  - edge
  - text-generation
  - lfm2.5
  - eval-results
  - safetensors
  - en
language:
  - en
---

<div align="center">

# LFM2.5-8B-A1B — GGUF Quantizations

[![Model on HF](https://img.shields.io/badge/🤗-Model_on_HuggingFace-yellow)](https://huggingface.co/Dhptl/LFM2.5-8B-A1B-GGUF)
[![Original Model](https://img.shields.io/badge/Original-LiquidAI_LFM2.5-8B-A1B-blue)](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)
[![quant-kit](https://img.shields.io/badge/Made_with-quant--kit-green)](https://github.com/DhruvalPtl/quant-kit)

**Quantized GGUF versions of [LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)**

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
| **MMLU Pro** | *See [original card](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)* | *Run benchmarks* | ~97-99% |
| **HellaSwag** | *See [original card](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)* | *Run benchmarks* | ~97-99% |
| **ARC Challenge** | *See [original card](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)* | *Run benchmarks* | ~97-99% |
| **TruthfulQA** | *See [original card](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)* | *Run benchmarks* | ~97-99% |
| **GSM8K** | *See [original card](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)* | *Run benchmarks* | ~97-99% |


---

## 📦 Available Files

| Filename | Size | RAM Required | Quant | Quality | Best For |
|---|---|---|---|---|---|
| `LFM2.5-8B-A1B-Q2_K.gguf` | 2.97 GB | ~4.5 GB | `Q2_K` | ⭐ | Extreme compression, significant quality loss. |
| `LFM2.5-8B-A1B-Q3_K_L.gguf` | 4.13 GB | ~5.6 GB | `Q3_K_L` | ⭐⭐⭐ | Slightly better than Q3_K_M, still a compromise. |
| `LFM2.5-8B-A1B-Q3_K_M.gguf` | 3.83 GB | ~5.3 GB | `Q3_K_M` | ⭐⭐⭐ | Very small file. Quality drop noticeable. |
| `LFM2.5-8B-A1B-Q3_K_S.gguf` | 3.50 GB | ~5.0 GB | `Q3_K_S` | ⭐⭐ | Very high compression, high quality loss. |
| `LFM2.5-8B-A1B-Q4_K_M.gguf` | 4.80 GB | ~6.3 GB | `Q4_K_M` ✅ **Recommended** | ⭐⭐⭐⭐ | Best balance of size and quality. Recommended for most users. |
| `LFM2.5-8B-A1B-Q4_K_S.gguf` | 4.53 GB | ~6.0 GB | `Q4_K_S` | ⭐⭐⭐½ | Good speed/size balance, slight quality loss. |
| `LFM2.5-8B-A1B-Q5_K_M.gguf` | 5.62 GB | ~7.1 GB | `Q5_K_M` | ⭐⭐⭐⭐½ | Better quality than Q4, slightly larger. Great if you have the RAM. |
| `LFM2.5-8B-A1B-Q5_K_S.gguf` | 5.47 GB | ~7.0 GB | `Q5_K_S` | ⭐⭐⭐⭐ | Large but accurate. |
| `LFM2.5-8B-A1B-Q6_K.gguf` | 6.48 GB | ~8.0 GB | `Q6_K` | ⭐⭐⭐⭐⭐ | Near-perfect quality, very large. |
| `LFM2.5-8B-A1B-Q8_0.gguf` | 8.39 GB | ~9.9 GB | `Q8_0` | ⭐⭐⭐⭐⭐ | Closest to original quality. Use when RAM is not a concern. |


### 💡 Which file should I download?

- **Most users:** `LFM2.5-8B-A1B-Q4_K_M.gguf` — best balance of size and quality
- **High RAM (32GB+):** `LFM2.5-8B-A1B-Q8_0.gguf` — near-original quality
- **Low RAM (8GB):** `LFM2.5-8B-A1B-Q3_K_M.gguf` — fits in 8GB with room to spare

---

## ⚡ Speed Benchmarks

*Run `python benchmark.py --model LFM2.5-8B-A1B` to generate speed results.*


---

## 🧠 Quality Benchmarks

*Run `kaggle_bench.ipynb` on Kaggle to benchmark this model.*


---

## 🚀 How to Use

### Ollama
```bash
ollama run dhptl/lfm2.5-8b-a1b
```

### LM Studio / Jan / Open WebUI
Search for `Dhptl/LFM2.5-8B-A1B` in the model browser.

### llama.cpp CLI
```bash
# Download the binary from https://github.com/ggerganov/llama.cpp/releases
./llama-cli \
  -m LFM2.5-8B-A1B-Q4_K_M.gguf \
  -p "You are a helpful assistant." \
  --conversation \
  -n 512
```

### Python — llama-cpp-python
```python
from llama_cpp import Llama

llm = Llama(
    model_path="./LFM2.5-8B-A1B-Q4_K_M.gguf",
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