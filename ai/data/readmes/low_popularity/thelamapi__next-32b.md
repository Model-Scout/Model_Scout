---
language:
- tr
- en
- de
- es
- fr
- ru
- zh
- ja
- ko
license: mit
tags:
- turkish
- türkiye
- reasoning
- ai
- lamapi
- gemma3
- next
- next-x1
- text-generation
- open-source
- 32b
- large-language-model
- llm
- transformer
- artificial-intelligence
- machine-learning
- nlp
- multilingual
- instruction-tuned
- chat
- generative-ai
- optimized
- trl
- sft
- cognitive
- analytical
- enterprise
- industrial
pipeline_tag: text-generation
datasets:
- mlabonne/FineTome-100k
- CognitiveKernel/CognitiveKernel-Pro-SFT
- OpenSPG/KAG-Thinker-training-dataset
- Gryphe/ChatGPT-4o-Writing-Prompts
- QuixiAI/dolphin-r1
- uclanlp/Brief-Pro
library_name: transformers
---

![banner32b](https://cdn-uploads.huggingface.co/production/uploads/67d46bc5fe6ad6f6511d6f44/4AIPH5Hnv0byVMVOXgb-7.png)

# 🧠 Next 32B (ultra530)

### *Türkiye’s Most Powerful AI — Industrial Scale, Deep Logic, and Enterprise-Ready*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Language: Multilingual](https://img.shields.io/badge/Language-Multilingual-red.svg)]()
[![HuggingFace](https://img.shields.io/badge/🤗-Lamapi/Next--32B-orange.svg)](https://huggingface.co/Lamapi/next-32b)
[![Discord](https://cdn.modrinth.com/data/cached_images/e84c69448cbf878a167f996d63e1a253437fcea2.png)](https://discord.gg/XgH4EpyPD2)

---

## 📖 Overview

**Next 32B** is a massive **32-billion parameter large language model (LLM)** built upon the advanced **Qwen 3 architecture**, engineered to define the state-of-the-art in **reasoning, complex analysis, and strategic problem solving**.

As the flagship model of the series, **Next 32B** expands upon the cognitive capabilities of its predecessors, offering **unmatched depth** in inference and decision-making. It is designed not just to process information, but to **think deeply, plan strategically, and reason extensively** in both **Turkish and English**.

Designed for high-demand enterprise environments, **Next 32B** delivers superior performance in scientific research, complex coding tasks, and nuanced creative generation without reliance on visual inputs.

---

## ⚡ Highlights

- 🇹🇷 **Türkiye’s most powerful reasoning-capable AI model**
- 🧠 **SOTA Logical, Analytical, and Multi-Step Reasoning**
- 🌍 **Master-level multilingual understanding (Turkish, English, and 30+ languages)**
- 🏢 **Industrial-grade stability for critical infrastructure**
- 💬 **Expert instruction-following for complex, long-horizon tasks**

## 🚀 Installation & Usage

**Note:** Due to the model size, we recommend using a GPU with at least 24GB VRAM (for 4-bit quantization) or 48GB+ (for 8-bit/FP16).

```
!pip install unsloth
```

```python
from unsloth import FastLanguageModel

model, tokenizer = FastLanguageModel.from_pretrained("Lamapi/next-32b")

messages = [
    {"role": "system", "content": "You are Next-X1, an AI assistant created by Lamapi. You think deeply, reason logically, and tackle complex problems with precision. You are an helpful, smart, kind, concise AI assistant."},
    {"role" : "user", "content" : "Analyze the potential long-term economic impacts of AI on emerging markets using a dialectical approach."}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize = False,
    add_generation_prompt = True,
    enable_thinking = True, # Enable thinking
)

from transformers import TextStreamer
_ = model.generate(
    **tokenizer(text, return_tensors = "pt").to("cuda"),
    max_new_tokens = 1024, # Increase for longer outputs!
    temperature = 0.7, top_p = 0.95, top_k = 400,
    streamer = TextStreamer(tokenizer, skip_prompt = True),
)
```

---

## 🧩 Key Features

| Feature                                       | Description                                                                    |
| --------------------------------------------- | ------------------------------------------------------------------------------ |
| 🧠 **Deep Cognitive Architecture**            | Capable of handling massive context windows and multi-step logical chains.     |
| 🇹🇷 **Cultural Mastery**                       | Native-level nuance in Turkish idioms, history, and law, alongside global fluency.|
| ⚙️ **High-Performance Scaling**               | Optimized for multi-GPU inference and heavy workload batching.                 |
| 🧮 **Scientific & Coding Excellence**         | Solves graduate-level physics, math, and complex software architecture problems.|
| 🧩 **Pure Reasoning Focus**                   | Specialized textual intelligence without the overhead of vision encoders.      |
| 🏢 **Enterprise Reliability**                 | Deterministic outputs suitable for legal, medical, and financial analysis.     |

---

## 📐 Model Specifications

| Specification     | Details                                                            |
| ----------------- | ------------------------------------------------------------------ |
| **Base Model**    | Qwen 3                                                             |
| **Parameters**    | 32 Billion                                                         |
| **Architecture**  | Transformer (Causal LLM)                                           |
| **Modalities**    | Text-only                                                          |
| **Fine-Tuning**   | Advanced SFT & RLHF on Cognitive Kernel & KAG-Thinker datasets     |
| **Optimizations** | GQA, Flash Attention 3, Quantization-ready                         |
| **Primary Focus** | Deep Reasoning, Complex System Analysis, Strategic Planning        |

---

## 🎯 Ideal Use Cases

* **Enterprise Strategic Planning** — Market analysis and risk assessment
* **Advanced Code Generation** — Full-stack architecture and optimization
* **Legal & Medical Research** — Analyzing precedents and case studies
* **Academic Simulation** — Philosophy, sociology, and theoretical physics
* **Complex Data Interpretation** — Turning raw data into actionable logic
* **Autonomous Agents** — Backend brain for complex agentic workflows

---

## 💡 Performance Highlights

* **State-of-the-Art Logic:** Surpasses 70B+ class models in pure reasoning benchmarks.
* **Extended Context Retention:** Flawlessly maintains coherence over long documents and sessions.
* **Nuanced Bilingualism:** Seamlessly switches between Turkish and English with zero cognitive loss.
* **Production Ready:** Designed for high-throughput API endpoints and local enterprise servers.

---

## 📄 License

Licensed under the **MIT License** — free for commercial and non-commercial use. Attribution is appreciated.

---

## 📞 Contact & Support

* 📧 **Email:** [lamapicontact@gmail.com](mailto:lamapicontact@gmail.com)
* 🤗 **HuggingFace:** [Lamapi](https://huggingface.co/Lamapi)

---

> **Next 32B** — Türkiye’s flagship *reasoning* model. Built for those who demand **depth**, **precision**, and **massive intelligence**.

[![Follow on HuggingFace](https://img.shields.io/badge/Follow-HuggingFace-yellow?logo=huggingface)](https://huggingface.co/Lamapi)