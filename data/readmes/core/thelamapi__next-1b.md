---
language:
- tr
- ar
- af
- az
- es
- en
- el
- ro
- ru
- rm
- th
- uk
- uz
- pl
- pt
- fa
- sk
- sl
- da
- de
- nl
- fr
- fi
- ka
- hi
- hu
- hy
- ja
- kk
- kn
- ko
- ku
- ky
- la
- lb
- id
- is
- it
- zh
- cs
- vi
- be
- bg
- bs
- ne
- mn
license: mit
tags:
- turkish
- türkiye
- english
- ai
- lamapi
- gemma3
- next
- next-x1
- efficient
- text-generation
- open-source
- 1b
- huggingface
- large-language-model
- llm
- causal
- transformer
- artificial-intelligence
- machine-learning
- ai-research
- natural-language-processing
- nlp
- finetuned
- lightweight
- creative
- summarization
- question-answering
- chat-model
- generative-ai
- optimized-model
- unsloth
- trl
- sft
- chemistry
- biology
- finance
- legal
- music
- art
- code
- climate
- medical
- agent
- text-generation-inference
pipeline_tag: text-generation
datasets:
- mlabonne/FineTome-100k
- ITCL/FineTomeOs
- Gryphe/ChatGPT-4o-Writing-Prompts
- dongguanting/ARPO-SFT-54K
- GreenerPastures/All-Your-Base-Full
- Gryphe/Opus-WritingPrompts
- HuggingFaceH4/MATH-500
- mlabonne/smoltalk-flat
- mlabonne/natural_reasoning-formatted
- OpenSPG/KAG-Thinker-training-dataset
- uclanlp/Brief-Pro
- CognitiveKernel/CognitiveKernel-Pro-SFT
- SuperbEmphasis/Claude-4.0-DeepSeek-R1-RP-SFWish
- QuixiAI/dolphin-r1
- mlabonne/lmsys-arena-human-sft-55k
library_name: transformers
---

<img src='assets/banner.png'>

# 🚀 Next-1B (t416)

### *Lightweight, Efficient, and Türkiye-Focused AI*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Language: English](https://img.shields.io/badge/Language-Multilingual-red.svg)]()
[![HuggingFace](https://img.shields.io/badge/🤗-Lamapi/Next--1B-orange.svg)](https://huggingface.co/Lamapi/next-1b)
[![Discord](https://cdn.modrinth.com/data/cached_images/e84c69448cbf878a167f996d63e1a253437fcea2.png)](https://discord.gg/XgH4EpyPD2)

---

## 📖 Overview

**Next-1B** is a **1-billion parameter causal language model** based on **Gemma 3**, designed for **efficiency, low-resource deployment, and reasoning-focused natural language understanding**.

Key highlights:

* Extremely **lightweight** — can run on consumer GPUs with low VRAM.
* Optimized for **text reasoning, summarization, and creative generation**.
* Supports **Turkish natively** while remaining multilingual.
* Open-source and transparent for research and applications.

Ideal for **developers, students, and organizations** needing **fast, reliable, and low-resource text-generation**.

---

## 🎯 Goals

1. **Lightweight Efficiency:** Run smoothly on low-resource devices.
2. **Reasoning-Focused:** Provide logical and coherent text outputs.
3. **Accessibility:** Fully open-source with clear documentation.
4. **Multilingual Adaptability:** Turkish-focused but supports other languages.

---

## ✨ Key Features

| Feature                     | Description                                                           |
| --------------------------- | --------------------------------------------------------------------- |
| 🔋 Lightweight Architecture | Optimized for low VRAM usage; ideal for small GPUs or CPU deployment. |
| 🇹🇷 Turkish & Multilingual | Handles complex Turkish prompts accurately.                           |
| 🧠 Reasoning Capabilities   | Logical chain-of-thought for question-answering and problem-solving.  |
| 📊 Consistent Outputs       | Reliable and reproducible results across multiple runs.               |
| 🌍 Open Source              | Transparent, research-friendly, and community-driven.                 |

---

## 📐 Model Specifications

| Specification      | Details                                                                |
| ------------------ | ---------------------------------------------------------------------- |
| Base Model         | Gemma 3                                                           |
| Parameter Count    | 1 Billion                                                              |
| Architecture       | Transformer, causal LLM                                                |
| Fine-Tuning Method | Instruction fine-tuning (SFT) with Turkish and multilingual datasets   |
| Optimizations      | Quantization-ready (q8, f16, f32)                      |
| Use Cases          | Text generation, summarization, Q&A, creative writing, reasoning tasks |

---

## 🚀 Installation & Usage

### Use the model:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "Lamapi/next-1b"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

# Chat message
messages = [
    {"role": "system", "content": "You are Next-X1, a smart and concise AI assistant trained by Lamapi. Always respond in the user's language. Proudly made in Turkey."},
    {"role": "user", "content": "Hello, how are you?"}
]

# Prepare input with Tokenizer
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(prompt, return_tensors="pt")

# Output from the model
output = model.generate(**inputs, max_new_tokens=50)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

<div style='width:700px;'>
  <div style='background-color:rgba(0,140,255,0.5);border-radius:16px;border-bottom-right-radius:0px;padding:3px 10px;width:fit-content;max-width:400px;margin-left:250px;margin-top:-15px;margin-bottom:10px;'>
    Hello, how are you?
  </div>
  <div style='background-color:rgba(42,42,40,0.7);border-radius:16px;border-bottom-left-radius:0px;padding:3px 10px;width:fit-content;max-width:400px;'>
  I'm fine, thank you. How are you?
  </div>
</div>

---

## 📄 License

MIT License — free to use, modify, and distribute. Attribution appreciated.

---

## 📞 Contact & Support

* 📧 **Email:** [lamapicontact@gmail.com](mailto:lamapicontact@gmail.com)
* 🤗 **HuggingFace:** [Lamapi](https://huggingface.co/Lamapi)

---

> **Next-1B** — Lightweight, **efficient, and reasoning-focused**, bringing **Turkey’s AI forward** on low-resource hardware.

[![Follow on HuggingFace](https://img.shields.io/badge/Follow-HuggingFace-yellow?logo=huggingface)](https://huggingface.co/Lamapi)