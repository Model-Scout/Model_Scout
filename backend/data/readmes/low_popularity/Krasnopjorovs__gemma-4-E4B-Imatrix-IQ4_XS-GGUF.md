---
license: apache-2.0
base_model: google/gemma-4-E4B-it
language:
- en
- ru
- de
- fr
- it
- zh
- ja
- ko
- ar
pipeline_tag: text-generation
tags:
- gemma
- gemma-4
- gguf
- imatrix
- quantization
- rag
- llama-cpp
---

# 🧠 Gemma 4 (9B) - Imatrix Quantized (IQ4_XS)

This is a highly optimized, heavily quantized 4-bit (IQ4_XS) GGUF version of Google's **Gemma 4**. 
The quantization was performed using a custom **Importance Matrix (imatrix)** to ensure maximum retention of the model's reasoning capabilities and its massive 262k vocabulary, while aggressively shrinking the file size.

Optimized and compiled by **Krasnopjorovs** ([Artjoms](https://artjoms.ai)).

## 🌍 Multilingual Capabilities
Thanks to the preserved 262,144 token vocabulary and custom imatrix, this model exhibits exceptional multilingual logic. 

**Supported languages include (but are strictly not limited to):**
English, Russian, German, French, Italian, Mandarin Chinese, Japanese, Korean, and Arabic. 
During testing, the model successfully performed highly technical translations involving complex alphabets and provided unprompted transliteration (Pinyin, Romaji) and literal translation breakdowns.

## 📊 Model Specifications

* **Base Model:** Google Gemma 4 (~8-9B parameters)
* **Quantization Format:** IQ4_XS (GGUF)
* **Optimization:** Custom Imatrix applied
* **File Size:** ~4.71 GB
* **Context Size:** 131,072 tokens (Native Training Context)
* **Vocabulary Size:** 262,144 tokens
* **License:** Apache 2.0 

## ⚡ Hardware & Performance

This specific build is engineered for universal compatibility and maximum throughput. Because of its extremely lightweight footprint (~4.71 GB), it can run efficiently across a massive variety of hardware setups—from edge devices to enterprise AI clusters.

**Deployment Flexibility:**
* **Universal GPU Support:** Comfortably fits entirely into the VRAM of almost any modern consumer or workstation GPU (8GB+ capacity), ensuring zero offloading bottlenecks.
* **CPU/RAM Fallback:** Runs highly efficiently even on CPU-only configurations, provided there is sufficient standard system memory (e.g., DDR4/DDR5 ECC).
* **Professional Workstations:** Achieves ultra-high token generation speeds on enterprise-grade architectures and multi-GPU arrays.
* **RAG & Vector Search:** Perfect for local Retrieval-Augmented Generation pipelines (e.g., processing massive vector databases) where blazing-fast inference and large context windows (up to 131k) are critical.

## 🛠️ Usage with `llama.cpp`

This model is fully compatible with `llama.cpp` and frontends like **Open WebUI**.

**CLI Example:**
```bash
./main -m gemma-4-E4B-IQ4_XS.gguf -n 512 -c 8192 --color -i -p "Your prompt here"

🤝 About the Builder
This model was compiled to power local, secure AI hardware ecosystems. If you are looking for pre-configured, plug-and-play AI servers and workstations built specifically for running private LLMs, visit artjoms.ai.