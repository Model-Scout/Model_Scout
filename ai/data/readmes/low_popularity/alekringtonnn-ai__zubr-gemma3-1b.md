---
license: apache-2.0
pipeline_tag: text-generation
language:
- ru
- en
- es
- fr
- de
- it
- pt
- zh
- ja
- ko
- ar
- hi
- pl
- tr
- vi
- be
---
# zubr-gemma3-1b

**zubr-gemma3-1b** is a lightweight, general-purpose conversational LLM with **1 billion parameters**, based on the **Gemma 3** architecture. The model is distributed in the **GGUF** format using importance matrices (**imatrix**) to ensure high generation quality even at lower quantization levels.

## 📊 Model Specifications

* **Architecture:** Gemma 3 (gemma3)
* **Parameters:** 1.0B (~1 billion parameters)
* **File Format:** GGUF (optimized for CPU and GPU execution via specialized libraries)
* **Quantization Method:** imatrix (importance matrix for enhanced text coherence)
* **Languages:** Multilingual (optimized for Russian and English)
* **License:** Apache 2.0

### Available Quants:
* **Q2_K** (~699 MB) — Ultra-lightweight version for devices with very limited memory.
* **Q4_K_M** (~806 MB) — Balanced version (Recommended. Offers the best speed-to-quality ratio).
* **Q6_K** (~1.01 GB) — High-fidelity version with minimal quality loss.

---

## 🚀 Installation & Usage Guide

This model is fully compatible with the `llama.cpp` ecosystem and popular local LLM UI applications.

### 1. via Ollama (Quickest Method)
If you have Ollama installed, you can pull and run the model directly from the command line:
```bash
ollama run hf.co/alekringtonnn-ai/zubr-gemma3-1b:Q4_K_M
```

### 2. via Llama.cpp (CLI or Server)
Ensure you have the latest version of `llama.cpp` installed.

* **Start an interactive chat session:**
  ```bash
  llama cli -hf alekringtonnn-ai/zubr-gemma3-1b:Q4_K_M
  ```
* **Launch a local server (OpenAI-compatible API with built-in UI):**
  ```bash
  llama serve -hf alekringtonnn-ai/zubr-gemma3-1b:Q4_K_M
  ```

### 3. via vLLM (For Python Integration)
Install the package:
```bash
pip install vllm
```
Start the inference server:
```bash
vllm serve "alekringtonnn-ai/zubr-gemma3-1b"
```

### 4. Third-Party GUI Apps
Since the model is provided in the `.gguf` format, you can load it locally using popular graphical interfaces:
* **LM Studio:** Search for `alekringtonnn-ai/zubr-gemma3-1b` in the in-app browser and download your preferred quant.
* **Jan** or **AnythingLLM:** Download the `.gguf` file manually and drop it into the application's local `models` directory.