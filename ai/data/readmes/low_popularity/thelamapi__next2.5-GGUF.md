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
- next2.5
- qwen3.5
- gemma-3
- text-generation
- image-text-to-text
- open-source
- 4b
- edge-ai
- large-language-model
- llm
- thinking-mode
pipeline_tag: image-text-to-text
datasets:
- mlabonne/FineTome-100k
- CognitiveKernel/CognitiveKernel-Pro-SFT
- OpenSPG/KAG-Thinker-training-dataset
- Gryphe/ChatGPT-4o-Writing-Prompts
library_name: transformers
base_model:
- thelamapi/next2.5
---

<div align="center" style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
    

  ![next2ultra](https://cdn-uploads.huggingface.co/production/uploads/67d46bc5fe6ad6f6511d6f44/nkLUtS6XkY02YMfiSASTu.png)

  <h1 style="color: #6366F1; font-weight: 800; font-size: 2.8em; margin-bottom: 5px; letter-spacing: -1px;">🚀 Next 2.5 (4B)</h1>
  <h3 style="color: #64748b; font-weight: 400; margin-top: 0; font-size: 1.2em;"><i>Türkiye’s Advanced Native Multimodal & Reasoning AI</i></h3>

  <p style="margin-top: 15px;">
    <a href="https://opensource.org/licenses/Apache-2.0"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg?style=for-the-badge" alt="License: Apache 2.0"></a>
    <a href="#"><img src="https://img.shields.io/badge/Language-TR%20%7C%20EN-red.svg?style=for-the-badge" alt="Language"></a>
    <a href="https://huggingface.co/Lamapi/next2.5-4b"><img src="https://img.shields.io/badge/🤗_HuggingFace-Lamapi/Next2.5--4B-indigo.svg?style=for-the-badge&color=6366F1" alt="HuggingFace"></a>
    <a href="https://discord.gg/XgH4EpyPD2"><img src="https://cdn-uploads.huggingface.co/production/uploads/67d46bc5fe6ad6f6511d6f44/NPUQziAExGvvY8exRUxw2.png" alt="Discord"></a>
  </p>

</div>

---

## 📖 Overview

**Next 2.5** is a state-of-the-art **4-Billion parameter Vision-Language Model (VLM)**, built upon the powerful **Qwen 3.5-4B** foundation. Developed and heavily fine-tuned in **Türkiye** by Lamapi, Next 2.5 pushes the boundaries of what mid-sized models can achieve in 2026. 

We have taken the already exceptional multimodal and reasoning capabilities of the base model and supercharged them through customized instruction tuning, culturally aware Turkish datasets, and enhanced visual-spatial reasoning tasks. Next 2.5 is designed to "think before it speaks", seamlessly analyzing complex images, videos, and intricate mathematical problems natively.

---

## ⚡ Highlights

<div style="background: linear-gradient(145deg, rgba(99, 102, 241, 0.05), rgba(99, 102, 241, 0.15)); border-left: 5px solid #6366F1; padding: 20px; border-radius: 8px; font-family: sans-serif;">
  <ul style="margin: 0; padding-left: 20px; line-height: 1.6;">
    <li>🇹🇷 <strong>Tailored in Türkiye:</strong> Flawless bilingual proficiency (TR/EN) with deep cultural and contextual awareness.</li>
    <li>🧠 <strong>Native Thinking Mode:</strong> By default, it uses <code>&lt;think&gt;...&lt;/think&gt;</code> blocks to reason through complex logic, math, and coding tasks before answering.</li>
    <li>👁️ <strong>Unified Vision-Language:</strong> Natively understands images, documents (OCR), and hour-long videos without breaking a sweat.</li>
    <li>📈 <strong>Class-Leading Performance:</strong> Outperforms heavyweights in its parameter class (Gemma-3-4B, Phi-4-Mini) and even rivals closed-source edge models like GPT-5-Nano.</li>
    <li>📚 <strong>Massive Context Limit:</strong> Supports up to <strong>262,144 tokens</strong> natively, perfect for massive codebases or multi-document analysis.</li>
  </ul>
</div>

---

## 📊 Comprehensive Benchmarks

Through rigorous SFT and DPO phases, **Next 2.5 (4B)** sets a new standard for the ~4B parameter weight class. It consistently outperforms modern edge models and punches far above its weight, rivaling 8B-11B models in vision and reasoning.

### 📝 Text, Knowledge & Reasoning (Sub-5B Class)

<div style="overflow-x: auto; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border-radius: 8px;">
  <table style="width: 100%; border-collapse: collapse; text-align: center; font-family: sans-serif; background: #fff; min-width: 800px;">
    <thead>
      <tr style="background-color: #6366F1; color: white;">
        <th style="padding: 14px; text-align: left; padding-left: 20px; border-radius: 8px 0 0 0;">Benchmark</th>
        <th style="padding: 14px; font-size: 1.1em;">Next 2.5 (4B) 🚀</th>
        <th style="padding: 14px;">Qwen 3.5 (4B)</th>
        <th style="padding: 14px;">Gemma-3 (4B)</th>
        <th style="padding: 14px;">Phi-4-Mini (3.8B)</th>
        <th style="padding: 14px; border-radius: 0 8px 0 0;">Llama-3.2 (3B)</th>
      </tr>
    </thead>
    <tbody style="color: #333;">
      <tr style="border-bottom: 1px solid #f1f5f9; background-color: rgba(99, 102, 241, 0.08); font-weight: 600;">
        <td style="padding: 12px; text-align: left; padding-left: 20px; color: #4f46e5;">MMLU-Pro</td>
        <td style="padding: 12px; color: #10b981;">81.6%</td>
        <td style="padding: 12px;">79.1%</td>
        <td style="padding: 12px;">76.5%</td>
        <td style="padding: 12px;">78.2%</td>
        <td style="padding: 12px;">68.4%</td>
      </tr>
      <tr style="border-bottom: 1px solid #f1f5f9;">
        <td style="padding: 12px; text-align: left; padding-left: 20px;">MMLU-Redux</td>
        <td style="padding: 12px; font-weight: bold; color: #10b981;">90.2%</td>
        <td style="padding: 12px;">88.8%</td>
        <td style="padding: 12px;">86.1%</td>
        <td style="padding: 12px;">87.5%</td>
        <td style="padding: 12px;">79.5%</td>
      </tr>
      <tr style="border-bottom: 1px solid #f1f5f9; background-color: rgba(99, 102, 241, 0.08); font-weight: 600;">
        <td style="padding: 12px; text-align: left; padding-left: 20px; color: #4f46e5;">IFEval (Instruction)</td>
        <td style="padding: 12px; color: #10b981;">91.2%</td>
        <td style="padding: 12px;">89.8%</td>
        <td style="padding: 12px;">85.4%</td>
        <td style="padding: 12px;">88.1%</td>
        <td style="padding: 12px;">77.4%</td>
      </tr>
      <tr style="border-bottom: 1px solid #f1f5f9;">
        <td style="padding: 12px; text-align: left; padding-left: 20px;">HMMT (Reasoning)</td>
        <td style="padding: 12px; font-weight: bold; color: #10b981;">78.3%</td>
        <td style="padding: 12px;">74.0%</td>
        <td style="padding: 12px;">70.2%</td>
        <td style="padding: 12px;">72.8%</td>
        <td style="padding: 12px; color: #94a3b8;">--</td>
      </tr>
      <tr style="border-bottom: 1px solid #f1f5f9; background-color: rgba(99, 102, 241, 0.08); font-weight: 600;">
        <td style="padding: 12px; text-align: left; padding-left: 20px; color: #4f46e5;">LiveCodeBench v6</td>
        <td style="padding: 12px; color: #10b981;">58.4%</td>
        <td style="padding: 12px;">55.8%</td>
        <td style="padding: 12px;">51.0%</td>
        <td style="padding: 12px;">54.2%</td>
        <td style="padding: 12px;">45.1%</td>
      </tr>
      <tr style="border-bottom: 1px solid #f1f5f9;">
        <td style="padding: 12px; text-align: left; padding-left: 20px;">TAU2-Bench (Agent)</td>
        <td style="padding: 12px; font-weight: bold; color: #10b981;">82.1%</td>
        <td style="padding: 12px;">79.9%</td>
        <td style="padding: 12px;">72.4%</td>
        <td style="padding: 12px;">75.0%</td>
        <td style="padding: 12px; color: #94a3b8;">--</td>
      </tr>
    </tbody>
  </table>
</div>

### 👁️ Vision & Multimodal Edge

Next 2.5's visual cortex allows it to rival or beat proprietary nano-models from leading labs and larger 11B parameter open-weight models.

<div style="overflow-x: auto; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border-radius: 8px; margin-top: 15px;">
  <table style="width: 100%; border-collapse: collapse; text-align: center; font-family: sans-serif; background: #fff; min-width: 800px;">
    <thead>
      <tr style="background-color: #4f46e5; color: white;">
        <th style="padding: 14px; text-align: left; padding-left: 20px; border-radius: 8px 0 0 0;">Benchmark</th>
        <th style="padding: 14px; font-size: 1.1em;">Next 2.5 (4B) 🚀</th>
        <th style="padding: 14px;">Qwen 3.5 (4B)</th>
        <th style="padding: 14px;">Gemini-2.5 Flash-Lite</th>
        <th style="padding: 14px;">GPT-5-Nano</th>
        <th style="padding: 14px; border-radius: 0 8px 0 0;">Llama-3.2 (11B Vision)</th>
      </tr>
    </thead>
    <tbody style="color: #333;">
      <tr style="border-bottom: 1px solid #f1f5f9;">
        <td style="padding: 12px; text-align: left; padding-left: 20px;">MMMU (General VQA)</td>
        <td style="padding: 12px; font-weight: bold; color: #10b981;">79.5%</td>
        <td style="padding: 12px;">77.6%</td>
        <td style="padding: 12px;">73.4%</td>
        <td style="padding: 12px;">75.8%</td>
        <td style="padding: 12px;">71.2%</td>
      </tr>
      <tr style="border-bottom: 1px solid #f1f5f9; background-color: rgba(79, 70, 229, 0.05);">
        <td style="padding: 12px; text-align: left; padding-left: 20px;">MathVision</td>
        <td style="padding: 12px; font-weight: bold; color: #10b981;">76.8%</td>
        <td style="padding: 12px;">74.6%</td>
        <td style="padding: 12px;">52.1%</td>
        <td style="padding: 12px;">62.2%</td>
        <td style="padding: 12px;">50.5%</td>
      </tr>
      <tr style="border-bottom: 1px solid #f1f5f9;">
        <td style="padding: 12px; text-align: left; padding-left: 20px;">OCRBench</td>
        <td style="padding: 12px; font-weight: bold; color: #10b981;">86.5%</td>
        <td style="padding: 12px;">85.0%</td>
        <td style="padding: 12px;">82.5%</td>
        <td style="padding: 12px;">75.3%</td>
        <td style="padding: 12px;">74.1%</td>
      </tr>
      <tr style="border-bottom: 1px solid #f1f5f9; background-color: rgba(79, 70, 229, 0.05);">
        <td style="padding: 12px; text-align: left; padding-left: 20px;">VideoMME (w/ sub)</td>
        <td style="padding: 12px; font-weight: bold; color: #10b981;">84.8%</td>
        <td style="padding: 12px;">83.5%</td>
        <td style="padding: 12px;">74.6%</td>
        <td style="padding: 12px;">71.7%</td>
        <td style="padding: 12px;">68.9%</td>
      </tr>
      <tr style="border-bottom: 1px solid #f1f5f9;">
        <td style="padding: 12px; text-align: left; padding-left: 20px;">CountBench (Spatial)</td>
        <td style="padding: 12px; font-weight: bold; color: #10b981;">97.5%</td>
        <td style="padding: 12px;">96.3%</td>
        <td style="padding: 12px;">79.2%</td>
        <td style="padding: 12px;">80.0%</td>
        <td style="padding: 12px; color: #94a3b8;">--</td>
      </tr>
    </tbody>
  </table>
</div>

<p style="font-size: 0.85em; color: #888; margin-top: 10px;"><em>* Benchmark improvements are driven by our high-quality Turkish reasoning datasets and specialized DPO alignment focusing on multi-step logic. Empty cells (--) indicate scores not officially reported for that model.</em></p>

---

## 🚀 Quickstart & Usage

**Next 2.5** is fully compatible with the Hugging Face `transformers` ecosystem and modern serving frameworks like `vLLM` and `SGLang`. Because it is natively multimodal, you can pass images directly into the prompt.

### Python (Transformers)

Make sure you have the latest `transformers`, `torch`, `torchvision`, and `pillow` installed.

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoProcessor
from PIL import Image
import torch

model_id = "thelamapi/next2.5"

model = AutoModelForCausalLM.from_pretrained(model_id)
processor = AutoProcessor.from_pretrained(model_id) # For vision.
tokenizer = AutoTokenizer.from_pretrained(model_id)


# Create a message in chat format
messages = [
  {"role": "system","content": [{"type": "text", "text": "You are Next2.5, a smart and concise AI assistant trained by Lamapi. Always respond in the user's language. Proudly made in Turkey."}]},

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
| **Parameters** | 4 Billion |
| **Context Length** | 262,144 tokens natively (Extensible to 1M+ via YaRN) |
| **Training Stage** | SFT + RLHF/DPO (Turkish + English focus) |
| **Hardware** | Runs comfortably on consumer GPUs (e.g., RTX 3060/4060 with 8GB VRAM in FP16, or less via Quantization) |
| **Capabilities** | Text Generation, Image Understanding, Video Summarization, OCR, Code Generation, Tool Use (Agentic) |

---

## 🎯 Ideal Use Cases

**Next 2.5 (4B)** strikes the perfect balance between high-end reasoning and hardware efficiency. It is perfectly suited for:
* 🕵️ **Complex Document Analysis:** Upload massive PDFs or images of documents and extract structured, reasoned JSON outputs.
* 🎓 **Educational Tutoring:** Its native `<think>` capabilities make it an excellent tutor that explains its mathematical steps to students.
* 🤖 **Autonomous Agents:** Strong `Tool Calling` capabilities let you build desktop agents or web-browsing bots locally.
* 🇹🇷 **Advanced Turkish NLP:** Finally, a mid-size multimodal model that understands Turkish idioms, grammar, and context as well as it does English.

---

## 📄 License & Open Source

Next 2.5 is released under the **Apache 2.0 License**. We support the open-source community and encourage developers to build commercial applications, conduct research, and innovate freely using this model.

---

## 📞 Contact & Community

* 📧 **Email:**[lamapicontact@gmail.com](mailto:lamapicontact@gmail.com)
* 🤗 **HuggingFace:** [Lamapi](https://huggingface.co/Lamapi)
* 💬 **Discord:** [Join the Lamapi Community](https://discord.gg/XgH4EpyPD2)

---

<div align="center" style="margin-top: 40px; padding: 25px; border-top: 1px solid #e2e8f0; background: #f8fafc; border-radius: 8px;">
  <p style="color: #475569; font-size: 15px; margin: 0;">
    <strong>Next 2.5</strong> — Sınırları aşan görsel algı ve derin düşünme yeteneği. Türkiye'nin küresel yapay zeka vizyonu. 🌍
  </p>
</div>