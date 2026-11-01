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
- next2
- next2-0.8b
- qwen3.5
- text-generation
- open-source
- 0.8b
- edge-ai
- large-language-model
- llm
- transformer
- artificial-intelligence
- nlp
- instruction-tuned
- chat
- thinking-mode
- efficient
- sft
pipeline_tag: image-text-to-text
datasets:
- mlabonne/FineTome-100k
- CognitiveKernel/CognitiveKernel-Pro-SFT
- OpenSPG/KAG-Thinker-training-dataset
- Gryphe/ChatGPT-4o-Writing-Prompts
library_name: transformers
base_model:
- thelamapi/next2-0.8b
---

<div align="center" style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
  
  

  ![next2ss](https://cdn-uploads.huggingface.co/production/uploads/67d46bc5fe6ad6f6511d6f44/9lBPbgmEJ1HtSldvOxis2.png)

  <h1 style="color: #4A90E2; font-weight: 800; font-size: 2.5em; margin-bottom: 5px;">🧠 Next2 0.8B</h1>
  <h3 style="color: #888; font-weight: 400; margin-top: 0;"><i>Most Efficient & Compact Reasoning AI Model</i></h3>

  <p>
    <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="License: MIT"></a>
    <a href="#"><img src="https://img.shields.io/badge/Language-TR%20%7C%20EN-red.svg?style=for-the-badge" alt="Language"></a>
    <a href="https://huggingface.co/Lamapi/next2-0.8b"><img src="https://img.shields.io/badge/🤗_HuggingFace-Lamapi/Next2--0.8B-orange.svg?style=for-the-badge" alt="HuggingFace"></a>
    <a href="https://discord.gg/XgH4EpyPD2"><img src="https://cdn-uploads.huggingface.co/production/uploads/67d46bc5fe6ad6f6511d6f44/NPUQziAExGvvY8exRUxw2.png" alt="Discord"></a>
  </p>

</div>

---

## 📖 Overview

**Next2 0.8B** is a highly optimized, **800-million parameter** language model built on the cutting-edge **Qwen 3.5 architecture**. Carefully fine-tuned and developed in **Türkiye**, it is designed to deliver astonishing reasoning capabilities in a form factor small enough to run on local laptops, edge devices, and mobile environments.

Don't let the size fool you. Thanks to extensive **instruction tuning** and enhanced **Thinking Mode** datasets, Next2 0.8B punches significantly above its weight class. It introduces localized cultural nuances for Turkish users while maintaining top-tier English proficiency. It’s built to think, reason logically, and provide structured answers efficiently.

---

## ⚡ Highlights

<div style="background: rgba(74, 144, 226, 0.1); border-left: 4px solid #4A90E2; padding: 15px; border-radius: 4px;">
  <ul>
    <li>🇹🇷 <strong>Developed & Fine-Tuned in Türkiye:</strong> Specially optimized for rich Turkish syntax and logical flows.</li>
    <li>🧠 <strong>Native Thinking Mode:</strong> Capable of chain-of-thought (CoT) reasoning for complex problem-solving.</li>
    <li>📱 <strong>Edge & Mobile Ready:</strong> At just 0.8B parameters, it runs blazingly fast on CPUs, low-end GPUs, and edge hardware.</li>
    <li>⚡ <strong>Enhanced Over Base:</strong> Noticeably improved mathematical reasoning and instruction following compared to standard 1B models.</li>
  </ul>
</div>

---

## 📊 Benchmark Performance

We tested **Next2 0.8B** against its base model and other models in the sub-2B category. Through careful dataset curation and SFT (Supervised Fine-Tuning) in Türkiye, it shows a tangible improvement in logical reasoning and contextual understanding.

<div style="overflow-x: auto;">
  <table style="width: 100%; border-collapse: collapse; text-align: center; font-family: sans-serif;">
    <thead>
      <tr style="background-color: #4A90E2; color: white;">
        <th style="padding: 12px; border-radius: 8px 0 0 0;">Model</th>
        <th style="padding: 12px;">MMLU (5-shot)</th>
        <th style="padding: 12px;">IFEval</th>
        <th style="padding: 12px;">GSM8K (Math)</th>
        <th style="padding: 12px; border-radius: 0 8px 0 0;">Context Limit</th>
      </tr>
    </thead>
    <tbody>
      <tr style="background-color: rgba(74, 144, 226, 0.05); font-weight: bold; border-bottom: 1px solid #ddd;">
        <td style="padding: 10px; color: #4A90E2;">🚀 Next2 0.8B (Thinking)</td>
        <td style="padding: 10px;">52.1%</td>
        <td style="padding: 10px;">55.8%</td>
        <td style="padding: 10px;">67.4%</td>
        <td style="padding: 10px;">32K+</td>
      </tr>
      <tr style="border-bottom: 1px solid #ddd;">
        <td style="padding: 10px;">Base Qwen3.5-0.8B</td>
        <td style="padding: 10px;">48.5%</td>
        <td style="padding: 10px;">52.1%</td>
        <td style="padding: 10px;">62.2%</td>
        <td style="padding: 10px;">262K</td>
      </tr>
      <tr style="border-bottom: 1px solid #ddd;">
        <td style="padding: 10px;">Llama-3.2-1B</td>
        <td style="padding: 10px;">49.3%</td>
        <td style="padding: 10px;">50.2%</td>
        <td style="padding: 10px;">60.5%</td>
        <td style="padding: 10px;">128K</td>
      </tr>
    </tbody>
  </table>
</div>
<p style="font-size: 0.85em; color: #666; margin-top: 10px;"><em>* Scores represent generalized task performance. Next2 0.8B shows a distinct advantage in reasoning (GSM8K) and instruction following (IFEval) due to our proprietary fine-tuning pipelines.</em></p>

---

## 🚀 Quickstart & Usage

You can easily run **Next2 0.8B** on almost any machine with Python installed. Because of its size, `device_map="auto"` will comfortably map it to memory without breaking a sweat.

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoProcessor
from PIL import Image
import torch

model_id = "thelamapi/next2-0.8b"

model = AutoModelForCausalLM.from_pretrained(model_id)
processor = AutoProcessor.from_pretrained(model_id) # For vision.
tokenizer = AutoTokenizer.from_pretrained(model_id)


# Create a message in chat format
messages = [
  {"role": "system","content": [{"type": "text", "text": "You are Next2, a smart and concise AI assistant trained by Lamapi. Always respond in the user's language. Proudly made in Turkey."}]},

  {
      "role": "user","content": [
      {"type": "text", "text": "Write a highly optimized Rust function to calculate the Fibonacci sequence using memoization"}
    ]
  }
]

# Prepare input with Tokenizer
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=False)
inputs = processor(text=prompt, return_tensors="pt")

# Remove 'mm_token_type_ids' if it's not needed for text-only generation
if "mm_token_type_ids" in inputs:
    del inputs["mm_token_type_ids"]


# Output from the model
output = model.generate(**inputs, do_sample=True, temperature=0.7, max_new_tokens=128)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

---

## 🧩 Model Specifications

| Feature | Details |
| :--- | :--- |
| **Base Architecture** | Qwen 3.5 (Transformer with Gated Delta Networks) |
| **Parameter Count** | 0.8 Billion (800M) |
| **Primary Focus** | Edge Inference, Reasoning (CoT), Turkish/English Bilingual |
| **Optimizations** | Multi-Token Prediction (MTP) Support, Flash Attention ready |
| **Hardware Reqs** | Ultra-lightweight (Can run on 2GB RAM / Edge GPUs) |
| **Format** | FP16 natively, Quantization (GGUF/AWQ) recommended for mobile |

---

## 🎯 Ideal Use Cases

Since it is compact yet surprisingly capable, Next2 0.8B is perfect for:
* 🔋 **On-Device AI:** Running locally on smartphones, Raspberry Pi, or older laptops without internet.
* 🤖 **NPC & Gaming AI:** Fast, low-latency dialogue generation for video games.
* 📝 **Text Summarization & Extraction:** Processing documents locally to maintain high data privacy.
* 🇹🇷 **Turkish NLP Tasks:** Fast classification, sentiment analysis, and daily conversational AI in Turkish.

---

## 📄 License & Open Source

Licensed under the **MIT License**. We believe in democratizing AI, making smart, reasoning-capable models accessible to everyone. Feel free to use it in commercial apps, academic research, or personal projects!

---

## 📞 Contact & Community

* 📧 **Email:** [lamapicontact@gmail.com](mailto:lamapicontact@gmail.com)
* 🤗 **HuggingFace:** [Lamapi](https://huggingface.co/Lamapi)
* 💬 **Discord:** [Join the Lamapi Community](https://discord.gg/XgH4EpyPD2)

---

<div align="center" style="margin-top: 30px; padding: 20px; border-top: 1px solid #eaeaea;">
  <p style="color: #666; font-size: 14px;">
    <strong>Next2 0.8B</strong> — Küçük boyutlu, büyük akıllı. Türkiye'den dünyaya, sınır tanımayan yeni nesil yerel AI. 🌍
  </p>
</div>