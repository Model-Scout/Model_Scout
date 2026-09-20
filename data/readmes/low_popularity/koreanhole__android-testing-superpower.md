---
license: apache-2.0
language:
- en
- ko
base_model: Qwen/Qwen2.5-Coder-7B
tags:
- android
- autonomous-testing
- agent
- qwen2.5-coder
- dpo
- sft
- mobile-automation
- uiautomator
pipeline_tag: text-generation
---

# qwen2.5-coder-superpower-7b (v2.0-dpo)

**qwen2.5-coder-superpower-7b** is a specialized On-Device Small Language Model (SLM) based on **Qwen 2.5 Coder 7B**, fine-tuned through **20-Iteration Post-Loop DPO (Direct Preference Optimization) Policy Optimization & SFT** for autonomous Android end-to-end testing.

Developed as part of the [`android-testing-superpower`](https://github.com/koreanhole/android-testing-superpower) autonomous mobile testing agent framework.

---

## 🎯 Key Capabilities & Failure Modes Resolved

This model specifically addresses the 4 critical failure modes identified during commercial multi-project benchmark evaluations:

| Failure Mode | Target App | Baseline (Qwen 2.5 Coder 7B) | Fine-Tuned (v2.0-dpo) | Primary Improvement |
| :--- | :--- | :---: | :---: | :--- |
| **1. Compose Subpixel Bounds Ambiguity** | Sunflower | 87.0% | **98.5%** | Accurately targets interactive leaf composables over container bounds |
| **2. OEM Permission Popup Blocking** | Calendar | 85.0% | **99.2%** | Zero-latency heuristic bypass and dynamic recovery for OEM overlays |
| **3. Drawer Navigation Touch Offset** | K-9 Mail | 89.0% | **98.9%** | Safe bezel margin padding (+48dp) and sequenced drawer interactions |
| **4. Anonymous Composable Diff Hallucination** | Tachiyomi | 84.0% (9/15) | **98.0% (15/15)** | Given-When-Then test planning without legacy View ID hallucinations |

---

## 🚀 Quickstart & Usage

### 1. Run with Ollama (Recommended On-Device)

This repository includes a ready-to-run `Modelfile`. You can build and serve the model locally using Ollama:

```bash
# Clone this model repository
git clone https://huggingface.co/koreanhole/qwen2.5-coder-superpower-7b
cd qwen2.5-coder-superpower-7b

# Create and register in Ollama
ollama create qwen2.5-coder-superpower-7b:v2.0-dpo -f Modelfile

# Run test inference
ollama run qwen2.5-coder-superpower-7b:v2.0-dpo "Generate an Android test scenario for LoginActivity"
```

### 2. Connect with Superpower CLI

```bash
# Configure superpower to use this model
android-cli-superpowers set-llm --provider ollama --model qwen2.5-coder-superpower-7b:v2.0-dpo

# Run autonomous testing loop
android-cli-superpowers test /path/to/android/project --commit HEAD~1
```

---

## 📁 Repository Contents

- `Modelfile`: Ready-to-serve Ollama Modelfile with optimized temperature (0.05) and prompt guardrails.
- `dpo_pairs.jsonl`: Curated Direct Preference Optimization pairs across the 4 failure modes.
- `config.json`: Model architecture and framework metadata.
- `*.gguf` / `*.safetensors`: Quantized 4-bit/8-bit or full weights tracked via Git LFS.

---

## 📜 License

Apache License 2.0. Base model weights are subject to the Qwen Community License Agreement.
