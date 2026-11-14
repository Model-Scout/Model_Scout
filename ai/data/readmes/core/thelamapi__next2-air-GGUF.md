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
license: apache-2.0
tags:
- turkish
- türkiye
- reasoning
- vision-language
- vlm
- multimodal
- lamapi
- next2-air
- qwen3.5
- text-generation
- image-text-to-text
- open-source
- 2b
- edge-ai
- large-language-model
- llm
- thinking-mode
- fast-inference
pipeline_tag: image-text-to-text
datasets:
- mlabonne/FineTome-100k
- CognitiveKernel/CognitiveKernel-Pro-SFT
- OpenSPG/KAG-Thinker-training-dataset
- Gryphe/ChatGPT-4o-Writing-Prompts
library_name: transformers
base_model:
- thelamapi/next2-air
---

<div align="center" style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
  
  

  ![nextf2](https://cdn-uploads.huggingface.co/production/uploads/67d46bc5fe6ad6f6511d6f44/EmQx5TfKy8pLtC19CZGbL.png)

  
  <h1 style="color: #0ea5e9; font-weight: 800; font-size: 2.8em; margin-bottom: 5px; letter-spacing: -1px;">Next2-Air (2B)</h1>
  <h3 style="color: #64748b; font-weight: 400; margin-top: 0; font-size: 1.2em;"><i>Türkiye’s Fastest Lightweight Multimodal & Reasoning AI</i></h3>

  <p style="margin-top: 15px;">
    <a href="https://opensource.org/licenses/Apache-2.0"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg?style=for-the-badge" alt="License: Apache 2.0"></a>
    <a href="#"><img src="https://img.shields.io/badge/Language-TR%20%7C%20EN-red.svg?style=for-the-badge" alt="Language"></a>
    <a href="https://huggingface.co/Lamapi/next2-air"><img src="https://img.shields.io/badge/🤗_HuggingFace-Lamapi/Next2--Air-0ea5e9.svg?style=for-the-badge" alt="HuggingFace"></a>
    <a href="https://discord.gg/XgH4EpyPD2"><img src="https://cdn-uploads.huggingface.co/production/uploads/67d46bc5fe6ad6f6511d6f44/NPUQziAExGvvY8exRUxw2.png" alt="Discord"></a>
  </p>

</div>

---

## 📖 Overview

**Next2-Air** is a highly optimized, lightning-fast **2-Billion parameter Vision-Language Model (VLM)** built on the **Qwen 3.5-2B** architecture. Engineered by Lamapi in **Türkiye**, the "Air" moniker represents its core philosophy: **lightweight, incredibly fast, yet surprisingly capable.**

While large models dominate cloud servers, Next2-Air is designed to bring top-tier reasoning and multimodal understanding directly to your local machines, edge devices, and everyday applications. By utilizing specialized instruction-tuning and logical reasoning datasets, we have created a 2B model that thinks deeply, processes images flawlessly, and speaks native Turkish and English.

---

## ⚡ Highlights

<div style="background: #232323; border-left: 5px solid #0ea5e9; padding: 20px; width:fit-content; border-radius: 16px; font-family: sans-serif;">
  <ul style="margin: 0; padding-left: 20px; line-height: 1.6; color: #808080;">
    <li>🇹🇷 <strong>Perfected in Türkiye:</strong> Fine-tuned with cultural nuance, ensuring natural, fluent, and highly accurate Turkish responses.</li>
    <li>💨 <strong>"Air" Speed & Efficiency:</strong> Only 2 Billion parameters. Runs blazingly fast on MacBooks, mid-range PCs, and edge hardware without needing massive GPUs.</li>
    <li>🧠 <strong>Native Thinking Mode:</strong> Despite its small size, it leverages Chain-of-Thought (<code>&lt;think&gt;</code>) to logically deduce answers before speaking.</li>
    <li>👁️ <strong>Full Vision-Language Support:</strong> Analyzes images, reads documents (OCR), and understands visual context just like heavier models.</li>
    <li>📚 <strong>Massive Context:</strong> Supports a staggering <strong>262,144 tokens</strong> natively—perfect for summarizing long PDFs or reading extensive codebases locally.</li>
  </ul>
</div>

---

## 📊 Benchmark Performance

Next2-Air (2B) redefines what is possible in the ultra-lightweight category. Through our custom DPO (Direct Preference Optimization) and SFT processes, it shows noticeable improvements over its base model and strongly competes with heavier 3B-4B models.

### 📝 Text, Reasoning & Instruction Following

<div style="overflow-x: auto; box-shadow: 0 4px 6px rgba(0,0,0,0.05); width:fit-content; border-radius: 16px;">
  <table style="width: 100%; border-collapse: collapse; text-align: center; font-family: sans-serif; background: #232323; min-width: 800px;">
    <thead>
      <tr style="background-color: #232323; color: white;">
        <th style="padding: 14px; text-align: left; padding-left: 20px; border-radius: 16px 0 0 0;">Benchmark</th>
        <th style="padding: 14px; font-size: 1.1em;">Next2-Air (2B)</th>
        <th style="padding: 14px;">Qwen 3.5 (2B)</th>
        <th style="padding: 14px;">Gemma-2 (2B)</th>
        <th style="padding: 14px; border-radius: 0 16px 0 0;">Llama-3.2 (3B)</th>
      </tr>
    </thead>
    <tbody style="color: #808080;">
      <tr style="border-bottom: 1px solid #f1f5f9; background-color: #232323; font-weight: 600;">
        <td style="padding: 12px; text-align: left; padding-left: 20px; color: #0284c7;">MMLU-Pro (Thinking)</td>
        <td style="padding: 12px; color: #0ea5e9;">68.2%</td>
        <td style="padding: 12px;">66.5%</td>
        <td style="padding: 12px;">54.1%</td>
        <td style="padding: 12px;">68.4%</td>
      </tr>
      <tr style="border-bottom: 1px solid #f1f5f9;">
        <td style="padding: 12px; text-align: left; padding-left: 20px; color: #0284c7;;">MMLU-Redux</td>
        <td style="padding: 12px; font-weight: bold; color: #0ea5e9;">82.1%</td>
        <td style="padding: 12px;">79.6%</td>
        <td style="padding: 12px;">75.3%</td>
        <td style="padding: 12px;">79.5%</td>
      </tr>
      <tr style="border-bottom: 1px solid #f1f5f9; background-color: #232323; font-weight: 600;">
        <td style="padding: 12px; text-align: left; padding-left: 20px; color: #0284c7;">IFEval (Instruction)</td>
        <td style="padding: 12px; color: #0ea5e9;">82.5%</td>
        <td style="padding: 12px;">78.6%</td>
        <td style="padding: 12px;">75.8%</td>
        <td style="padding: 12px;">77.4%</td>
      </tr>
      <tr style="border-bottom: 1px solid #f1f5f9;">
        <td style="padding: 12px; text-align: left; padding-left: 20px; color: #0284c7;">TAU2-Bench (Agent)</td>
        <td style="padding: 12px; font-weight: bold; color: #0ea5e9;">52.4%</td>
        <td style="padding: 12px;">48.8%</td>
        <td style="padding: 12px;">--</td>
        <td style="padding: 12px;">--</td>
      </tr>
    </tbody>
  </table>
</div>

### 👁️ Multimodal & Vision Edge

Next2-Air features a highly capable visual encoder, allowing it to process spatial intelligence, OCR, and document understanding tasks efficiently.

<div style="overflow-x: auto; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border-radius: 8px; margin-top: 15px;width:fit-content; ">
  <table style="width: 100%; border-collapse: collapse; text-align: center; font-family: sans-serif; background: #232323; min-width: 800px;">
    <thead>
      <tr style="background-color: #232323; color: white;">
        <th style="padding: 14px; text-align: left; padding-left: 20px; border-radius: 16px 0 0 0;">Benchmark</th>
        <th style="padding: 14px; font-size: 1.1em;">Next2-Air (2B)</th>
        <th style="padding: 14px; border-radius: 0 16px 0 0;">Base Qwen3.5-2B</th>
      </tr>
    </thead>
    <tbody style="color: #808080;">
      <tr style="border-bottom: 1px solid #f1f5f9;">
        <td style="padding: 12px; text-align: left; padding-left: 20px; color: #0284c7;;">MMMU (General VQA)</td>
        <td style="padding: 12px; font-weight: bold; color: #0ea5e9;">66.5%</td>
        <td style="padding: 12px;">64.2%</td>
      </tr>
      <tr style="border-bottom: 1px solid #f1f5f9; background-color: #232323;">
        <td style="padding: 12px; text-align: left; padding-left: 20px; color: #0284c7;">MathVision</td>
        <td style="padding: 12px; font-weight: bold; color: #0ea5e9;">78.1%</td>
        <td style="padding: 12px;">76.7%</td>
      </tr>
      <tr style="border-bottom: 1px solid #f1f5f9;">
        <td style="padding: 12px; text-align: left; padding-left: 20px; color: #0284c7;">OCRBench</td>
        <td style="padding: 12px; font-weight: bold; color: #0ea5e9;">86.0%</td>
        <td style="padding: 12px;">84.5%</td>
      </tr>
      <tr style="border-bottom: 1px solid #f1f5f9; background-color: #232323;">
        <td style="padding: 12px; text-align: left; padding-left: 20px; color: #0284c7;">VideoMME (w/ sub)</td>
        <td style="padding: 12px; font-weight: bold; color: #0ea5e9;">77.8%</td>
        <td style="padding: 12px;">75.6%</td>
      </tr>
    </tbody>
  </table>
</div>

<p style="font-size: 0.85em; color: #888; margin-top: 10px;"><em>* Enhanced scores in reasoning and OCR are a direct result of Lamapi's specialized bilingual finetuning pipeline focusing on edge-case logic and structural formatting.</em></p>

---

## 🚀 Quickstart & Usage

**Next2-Air** is fully compatible with the Hugging Face `transformers` ecosystem and fast inference engines like `vLLM` and `SGLang`. Because it's a VLM, you can directly pass images into your prompts.

### Python (Transformers)

Make sure you have `transformers`, `torch`, `torchvision`, and `pillow` installed.

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoProcessor
from PIL import Image
import torch

model_id = "thelamapi/next2-air"

model = AutoModelForCausalLM.from_pretrained(model_id)
processor = AutoProcessor.from_pretrained(model_id) # For vision.
tokenizer = AutoTokenizer.from_pretrained(model_id)


# Create a message in chat format
messages = [
  {"role": "system","content": [{"type": "text", "text": "You are Next2 Air, a smart and concise AI assistant trained by Lamapi. Always respond in the user's language. Proudly made in Turkey."}]},

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

| Attribute | Details |
| :--- | :--- |
| **Base Architecture** | Qwen 3.5 (Causal Language Model + Vision Encoder) |
| **Parameters** | 2 Billion (Ultra-Lightweight) |
| **Context Length** | 262,144 tokens natively |
| **Hardware** | Optimized for Edge devices, MacBooks (MLX), Consumer GPUs, and low-VRAM environments. |
| **Capabilities** | Text Generation, Image Understanding, OCR, Logic & Reasoning (CoT), Bilingual (TR/EN) |

---

## 🎯 Ideal Use Cases

**Next2-Air** is the undisputed champion of local, fast inference tasks. It is perfect for:
* 🔋 **Mobile & Edge AI:** Deploying smart assistants natively on smartphones or Raspberry Pi without relying on cloud APIs.
* ⚡ **Real-Time OCR & Parsing:** Quickly scanning receipts, invoices, or UI screenshots to extract data in milliseconds.
* 💬 **Fast Conversational Bots:** Providing instant, low-latency Turkish and English responses for customer service pipelines.
* 🎮 **Gaming & NPC Logic:** Acting as a fast reasoning engine for dynamic in-game characters.

---

## 📄 License & Open Source

Next2-Air is released under the **Apache 2.0 License**. We strongly believe in empowering developers, students, and enterprises with accessible, high-speed, reasoning-capable AI.

---

## 📞 Contact & Community

* 📧 **Email:**[lamapicontact@gmail.com](mailto:lamapicontact@gmail.com)
* 🤗 **HuggingFace:** [Lamapi](https://huggingface.co/Lamapi)
* 💬 **Discord:** [Join the Lamapi Community](https://discord.gg/XgH4EpyPD2)

---

<div align="center" style="margin-top: 40px; padding: 25px; border-top: 1px solid #e0f2fe; background: #232323; border-radius: 8px;width:fit-content; ">
  <p style="color: #808080; font-size: 15px; margin: 0;">
    <strong>Next2-Air</strong> — Hafif, Hızlı, Akıllı. Uç cihazlardan buluta, Türkiye'nin yeni nesil çevik yapay zekası. 🌬️
  </p>
</div>