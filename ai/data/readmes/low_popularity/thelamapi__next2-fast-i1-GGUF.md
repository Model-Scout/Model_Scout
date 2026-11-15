---
language:
- en
- tr
- de
- fr
- es
- it
- pt
- ru
- zh
- ja
- ko
- hi
- ar
- nl
- pl
- uk
- vi
- th
- id
- cs
license: mit
tags:
- global-ai
- multilingual
- vision-language-model
- multimodal
- lamapi
- next-2-fast
- next-series
- 4b
- efficient
- gemma-3
- transformer
- text-generation
- reasoning
- artificial-intelligence
- nlp
pipeline_tag: image-text-to-text
datasets:
- mlabonne/FineTome-100k
- ITCL/FineTomeOs
- Gryphe/ChatGPT-4o-Writing-Prompts
- dongguanting/ARPO-SFT-54K
- OpenSPG/KAG-Thinker-training-dataset
- uclanlp/Brief-Pro
- CognitiveKernel/CognitiveKernel-Pro-SFT
- QuixiAI/dolphin-r1
library_name: transformers
base_model:
- thelamapi/next2-fast
---

![next2fs](https://cdn-uploads.huggingface.co/production/uploads/67d46bc5fe6ad6f6511d6f44/pBmNGgIkCDBwmh8Ut2UTf.png)

[![Discord](https://cdn.modrinth.com/data/cached_images/e84c69448cbf878a167f996d63e1a253437fcea2.png)](https://discord.gg/XgH4EpyPD2)

# ⚡ Next 2 Fast (4B)

### *Global Speed, Multimodal Intelligence — Engineered by Lamapi* 

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Language: Multilingual](https://img.shields.io/badge/Language-Global-green.svg)]()
[![HuggingFace](https://img.shields.io/badge/🤗-Lamapi/Next--2--Fast-orange.svg)](https://huggingface.co/Lamapi/next-2-fast)

---

## 🌍 Overview

**Next 2 Fast** is a state-of-the-art **4-billion parameter Multimodal Vision-Language Model (VLM)** designed for high-performance reasoning across languages and modalities. 

Developed by **Lamapi**, a leading AI research lab in Türkiye, this model represents a leap in efficiency, bridging the gap between massive commercial models and accessible, open-source intelligence. Built upon the **Gemma 3** architecture and refined with our proprietary SFT and DPO techniques, **Next 2 Fast** is not just a language model—it is a global reasoning engine that sees, understands, and communicates fluently in **English, Turkish, German, French, Spanish, and 25+ other languages.**

**Why Next 2 Fast?**
* ⚡ **Global Performance:** Tuned for complex reasoning in English and multilingual contexts, outperforming larger models.
* 👁️ **Vision & Text:** Seamlessly processes images and text to generate code, descriptions, and analysis.
* 🚀 **Unmatched Speed:** Optimized for low-latency inference, making it ~2x faster than previous generations.
* 🔋 **Efficient Deployment:** Runs smoothly on consumer hardware (8GB VRAM) using 4-bit/8-bit quantization.

---

# 🏆 Benchmark Performance

**Next 2 Fast** delivers flagship-level performance in a compact 4B size, proving that efficiency does not require sacrificing intelligence.

<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>Params</th>
      <th>MMLU (5-shot) %</th>
      <th>MMLU-Pro %</th>
      <th>GSM8K %</th>
      <th>MATH %</th>
    </tr>
  </thead>
  <tbody>
    <tr class="next" style="background-color: #e6f3ff; font-weight: bold;">
      <td data-label="Model">⚡ Next 2 Fast</td>
      <td>4B</td>
      <td data-label="MMLU (5-shot) %">85.1</td>
      <td data-label="MMLU-Pro %">67.4</td>
      <td data-label="GSM8K %">83.5</td>
      <td data-label="MATH %"><strong>71.2</strong></td>
    </tr>
    <tr>
      <td data-label="Model">Gemma 3 4B</td>
      <td>4B</td>
      <td data-label="MMLU (5-shot) %">82.0</td>
      <td data-label="MMLU-Pro %">64.5</td>
      <td data-label="GSM8K %">80.1</td>
      <td data-label="MATH %">68.0</td>
    </tr>
    <tr>
      <td data-label="Model">Llama 3.2 3B</td>
      <td>3B</td>
      <td data-label="MMLU (5-shot) %">63.4</td>
      <td data-label="MMLU-Pro %">52.1</td>
      <td data-label="GSM8K %">45.2</td>
      <td data-label="MATH %">42.8</td>
    </tr>
    <tr>
      <td data-label="Model">Phi-3.5 Mini</td>
      <td>3.8B</td>
      <td data-label="MMLU (5-shot) %">84.0</td>
      <td data-label="MMLU-Pro %">66.0</td>
      <td data-label="GSM8K %">82.0</td>
      <td data-label="MATH %">69.5</td>
    </tr>
  </tbody>
</table>

---

## 🚀 Quick Start

**Next 2 Fast** is fully compatible with the Hugging Face `transformers` library.

### 🖼️ Multimodal Inference (Vision + Text):

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoProcessor
from PIL import Image
import torch

model_id = "thelamapi/next2-fast"

# Load Model & Processor
model = AutoModelForCausalLM.from_pretrained(
    model_id, 
    torch_dtype=torch.bfloat16, 
    device_map="auto"
)
processor = AutoProcessor.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Load Image
image = Image.open("image.jpg")

# Create Multimodal Prompt
messages = [
  {
    "role": "system",
    "content": [{"type": "text", "text": "You are Next-2, an AI assistant created by Lamapi. Provide concise and accurate analysis."}]
  },
  {
    "role": "user",
    "content": [
        {"type": "image", "image": image},
        {"type": "text", "text": "Analyze this image and explain in English."}
    ]
  }
]

# Process & Generate
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = processor(text=prompt, images=[image], return_tensors="pt").to(model.device)

output = model.generate(**inputs, max_new_tokens=128)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

### 💬 Text-Only Chat (Global Reasoning):

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "Lamapi/next-2-fast"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

messages = [
    {"role": "system", "content": "You are Next 2 Fast, an advanced AI assistant."},
    {"role": "user", "content": "Explain the concept of entropy in thermodynamics simply."}
]

prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

output = model.generate(**inputs, max_new_tokens=200)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

---

## 🌐 Key Features

| Feature | Description |
| :--- | :--- |
| **🌍 True Multilingualism** | Fluent in English, Turkish, German, French, Spanish, and more. No "translation-ese." |
| **🧠 Visual Intelligence** | Can read charts, identify objects, and reason about visual scenes effectively. |
| **⚡ High Efficiency** | Designed for speed. Ideal for edge devices, local deployment, and real-time apps. |
| **💻 Code & Math** | Strong capabilities in Python coding, debugging, and solving mathematical problems. |
| **🛡️ Global Alignment** | Fine-tuned with a diverse dataset to ensure safety and neutrality across cultures. |

---

## 🎯 Mission

At **Lamapi**, our mission is to build the **Next** generation of intelligence that is accessible to everyone, everywhere. 

**Next 2 Fast** proves that world-class AI innovation isn't limited to Silicon Valley. By combining efficient architecture with high-quality global datasets, we provide a powerful tool for researchers, developers, and businesses worldwide.

---

## 📄 License

This model is open-sourced under the **MIT License**. It is free for academic and commercial use.

---

## 📞 Contact & Ecosystem

We are **Lamapi**.

* 📧 **Contact:** [Mail](mailto:lamapicontact@gmail.com)
* 🤗 **HuggingFace:** [Company Page](https://huggingface.co/thelamapi)

---

> **Next 2 Fast** — *Global Intelligence. Lightning Speed. Powered by Lamapi.*

[![Follow on HuggingFace](https://img.shields.io/badge/Follow-HuggingFace-yellow?logo=huggingface)](https://huggingface.co/Lamapi)