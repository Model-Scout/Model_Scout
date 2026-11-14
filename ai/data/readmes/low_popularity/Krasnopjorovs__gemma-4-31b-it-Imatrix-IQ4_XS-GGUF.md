---
license: apache-2.0
base_model: google/gemma-4-31B-it
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

# 🧠 Gemma 4 (31B) Instruct - Imatrix Quantized (IQ4_XS)

This is a highly optimized, extremely compressed 4-bit (IQ4_XS) GGUF version of Google's **Gemma 4 31B Instruct**. 
The quantization was performed using a custom **Importance Matrix (imatrix)** calculated over 2200+ chunks. This ensures maximum retention of the model's analytical, mathematical, and reasoning capabilities, while aggressively shrinking the file size from ~61 GB (FP16) down to just ~15.58 GB.

Optimized and compiled by **Krasnopjorovs** ([Artjoms](https://artjoms.ai)).

## 🌍 Multilingual Capabilities
Thanks to the preserved 262,144 token vocabulary and custom imatrix, this model exhibits exceptional multilingual logic. 

**Supported languages include (but are strictly not limited to):**
English, Russian, German, French, Italian, Mandarin Chinese, Japanese, Korean, and Arabic. 
During testing, the model successfully performed highly technical translations involving complex alphabets and provided unprompted transliteration (Pinyin, Romaji) and literal translation breakdowns.

## 📊 Model Specifications

* **Base Model:** Google Gemma 4 31B Instruct
* **Quantization Format:** IQ4_XS (GGUF)
* **Optimization:** Custom Imatrix applied
* **File Size:** ~15.58 GB
* **Tested Context Size:** 250,000 tokens (using Flash Attention)
* **Vocabulary Size:** 262,144 tokens
* **License:** Gemma 


## 🛠️ Usage with `llama.cpp`

This model is fully compatible with `llama.cpp` and frontends like **Open WebUI**.

**CLI Interactive Example (with Flash Attention):**
```bash
./llama-cli -m gemma-4-31b-it-Imatrix-IQ4_XS.gguf -c 250000 -ngl 99 -fa -cnv

Server / API Example:
./llama-server -m gemma-4-31b-it-Imatrix-IQ4_XS.gguf -c 250000 -ngl 99 -fa on --host 0.0.0.0 --port 8080

🤝 About the Builder
This model was compiled to power local, secure AI hardware ecosystems. If you are looking for pre-configured, plug-and-play AI servers and workstations built specifically for running private LLMs, visit artjoms.ai.