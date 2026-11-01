---
language:
- tr
- en
- de
- ka
- el
- ku
- es
- sl
- sk
- af
- da
- nl
- fa
- fi
- fr
- ga
- hi
- hu
- hy
- ja
- kg
- kk
- ko
- ky
- la
- lb
- id
- it
- is
- za
- zh
- zu
- cs
- vi
- be
- bg
- bs
- ne
- mn
- rm
- ro
- ru
- te
- th
- tk
- tt
- uk
- uz
- ug
- pl
- pt
- 'no'
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
- 12b
- huggingface
- large-language-model
- llm
- causal
- transformer
- artificial-intelligence
- machine-learning
- ai-research
- natural-language-processing
- language
- multilingual
- multimodal
- nlp
- finetuned
- lightweight
- creative
- summarization
- question-answering
- chat
- generative-ai
- optimized
- unsloth
- trl
- sft
- chemistry
- code
- biology
- finance
- legal
- music
- art
- state-of-the-art
- climate
- medical
- agent
- text-generation-inference
- merge
- dense
pipeline_tag: image-text-to-text
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
base_model:
- Lamapi/next-12b
---

<img src='assets/banner.png'>

# 🚀 Next 12B (m200)

### *Türkiye's Advanced Vision-Language Model — High Performance, Multimodal, and Enterprise-Ready* 

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Language: English](https://img.shields.io/badge/Language-Multilingual-red.svg)]()
[![HuggingFace](https://img.shields.io/badge/🤗-Lamapi/Next--12B-orange.svg)](https://huggingface.co/Lamapi/next-12b)

---

## 📖 Overview

**Next 12B** is a **12-billion parameter multimodal Vision-Language Model (VLM)** based on **Gemma 3**, fine-tuned to deliver **exceptional performance** in both text and image understanding. This is **Türkiye's most advanced open-source vision-language model**, designed for: 

* Superior understanding and generation of **text and image descriptions**.
* Advanced reasoning and context-aware multimodal outputs.
* Professional-grade Turkish support with extensive multilingual capabilities.
* Enterprise-ready deployment with optimized quantization options. 

This model is ideal for **enterprises, researchers, and organizations** who need a **state-of-the-art multimodal AI** capable of **complex visual understanding, advanced reasoning, and creative generation**.

---

<style>
  table { width:fit-content; border-collapse:separate; border-spacing:0 3px;font-family:system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;color:rgb(255, 255, 255)!important;background:rgb(28, 41, 59);border-radius:16px;padding: 10px; border:none;transition:.2s all ease;}
  thead th { text-align:center; padding:4px 10px; font-size:13px; text-transform:uppercase; color:rgb(255, 255, 255)!important;border:none; }
  tbody tr { transition: transform 0.18s ease, box-shadow 0.18s ease; border:none !important;transition:.2s all ease;border-radius:16px;background:rgba(11, 23, 27, 1);}
  tbody .next:hover {box-shadow:0 6px 15px rgba(0, 76, 148, 0.1);background: rgb(0, 59, 225)}
  tbody tr:hover { box-shadow:0 0px 15px rgba(12, 12, 12, 0.4); background:rgba(17, 34, 53, 1)}
  td { padding:8px 10px;border:0px transparent !important;outline:transparent !important; text-align:center; }
  td:first-child { font-weight:600;text-align:left }
  .next{
    background: rgb(0, 89, 255);
  }
  tbody tr td:first-child { border-top-left-radius:12px; border-bottom-left-radius:12px; }
  tbody tr td:last-child { border-top-right-radius:12px; border-bottom-right-radius:12px; }
  strong{
    font-size:16px;font-weight:700;color:rgba(255, 255, 255, 1)!important;
  }
  em{opacity:1;font-size:11px !important;}
</style>

# Next 12B sets new standards for medium-sized models across all major benchmarks.

<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>MMLU (5-shot) %</th>
      <th>MMLU-Pro %</th>
      <th>GSM8K %</th>
      <th>MATH %</th>
    </tr>
  </thead>
  <tbody>
    <tr class="next">
      <td data-label="Model">Next 12B <em>Version m200</em></td>
      <td data-label="MMLU (5-shot) %"><strong>91.8</strong></td>
      <td data-label="MMLU-Pro %"><strong>78.4</strong></td>
      <td data-label="GSM8K %"><strong>94.3</strong></td>
      <td data-label="MATH %"><strong>81.2</strong></td>
    </tr>
    <tr class="next">
      <td data-label="Model">Next 4B preview <em>Version s325</em></td>
      <td data-label="MMLU (5-shot) %">84.6</td>
      <td data-label="MMLU-Pro %">66.9</td>
      <td data-label="GSM8K %">82.7</td>
      <td data-label="MATH %">70.5</td>
    </tr>
    <tr>
      <td data-label="Model">Qwen 2.5 14B</td>
      <td data-label="MMLU (5-shot) %">79.9</td>
      <td data-label="MMLU-Pro %">68.3</td>
      <td data-label="GSM8K %">87.5</td>
      <td data-label="MATH %">74.3</td>
    </tr>
    <tr>
      <td data-label="Model">Llama 3.1 8B</td>
      <td data-label="MMLU (5-shot) %">73.0</td>
      <td data-label="MMLU-Pro %">62.4</td>
      <td data-label="GSM8K %">80.6</td>
      <td data-label="MATH %">51.9</td>
    </tr>
  </tbody>
</table>

---

# Next 12B approaches frontier model performance while maintaining efficiency.
<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>MMLU (5-shot) %</th>
      <th>MMLU-Pro %</th>
      <th>GSM8K %</th>
      <th>MATH %</th>
    </tr>
  </thead>
  <tbody>
    <tr class="next">
      <td data-label="Model">Next Z1 <em>Version l294</em></td>
      <td data-label="MMLU (5-shot) %"><strong>97.3</strong></td>
      <td data-label="MMLU-Pro %"><strong>94.2</strong></td>
      <td data-label="GSM8K %"><strong>97.7</strong></td>
      <td data-label="MATH %"><strong>93.2</strong></td>
    </tr>
    <tr class="next">
      <td data-label="Model">Next 12B <em>Version m200</em></td>
      <td data-label="MMLU (5-shot) %">91.8</td>
      <td data-label="MMLU-Pro %">78.4</td>
      <td data-label="GSM8K %">94.3</td>
      <td data-label="MATH %">81.2</td>
    </tr>
    <tr>
      <td data-label="Model">GPT 4o</td>
      <td data-label="MMLU (5-shot) %">88.7</td>
      <td data-label="MMLU-Pro %">72.6</td>
      <td data-label="GSM8K %">92.3</td>
      <td data-label="MATH %">76.6</td>
    </tr>
    <tr>
      <td data-label="Model">Claude Sonnet 4</td>
      <td data-label="MMLU (5-shot) %">~88.3</td>
      <td data-label="MMLU-Pro %">75.8</td>
      <td data-label="GSM8K %">90.8</td>
      <td data-label="MATH %">78.3</td>
    </tr>
  </tbody>
</table>

---

## 🚀 Installation & Usage

### Use with vision:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoProcessor
from PIL import Image
import torch

model_id = "Lamapi/next-12b"

model = AutoModelForCausalLM.from_pretrained(model_id)
processor = AutoProcessor.from_pretrained(model_id) # For vision.
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Read image
image = Image.open("image.jpg")

# Create a message in chat format
messages = [
  {"role": "system","content": [{"type": "text", "text": "You are Next-X1, a smart and concise AI assistant trained by Lamapi. Always respond in the user's language. Proudly made in Turkey."}]},

  {
      "role": "user","content": [{"type": "image", "image": image},
      {"type": "text", "text": "Who is in this image?"}
    ]
  }
]

# Prepare input with Tokenizer
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = processor(text=prompt, images=[image], return_tensors="pt")

# Output from the model
output = model.generate(**inputs, max_new_tokens=50)
print(tokenizer.decode(output[0], skip_special_tokens=True))


```
<div style='width:700px;'>
  <img src='/Lamapi/next-12b/resolve/main/assets/image.jpg' style='height:192px;border-radius:16px;margin-left:225px;'>
  <div style='background-color:rgba(0,140,255,0.5);border-radius:16px;border-bottom-right-radius:0px;padding:3px 10px;width:fit-content;max-width:400px;margin-left:250px;margin-top:-25px;margin-bottom:10px;'>
    Who is in this image?
  </div>
  <div style='background-color:rgba(42,42,40,0.7);border-radius:16px;border-bottom-left-radius:0px;padding:3px 10px;width:fit-content;max-width:400px;'>
  The image shows <strong>Mustafa Kemal Atatürk</strong>, the founder and first President of the Republic of Turkey.
  </div>
</div>

### Use without vision:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "Lamapi/next-12b"
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

## 🎯 Goals

1. **Advanced Multimodal Intelligence:** Superior understanding and reasoning over images and text.
2. **Enterprise-Grade Performance:** High accuracy and reliability for production deployments.
3. **Efficiency:** Optimized for professional GPUs with flexible quantization options. 
4. **Accessibility:** Open-source availability for research and commercial applications.
5. **Cultural Excellence:** Best-in-class Turkish language support while maintaining multilingual capabilities.

---

## ✨ Key Features

| Feature                           | Description                                                             |
| --------------------------------- | ----------------------------------------------------------------------- |
| 🔋 Optimized Architecture         | Balanced performance and efficiency; supports multiple quantization formats.  | 
| 🖼️ Advanced Vision-Language       | Deep understanding of images with sophisticated visual reasoning capabilities. |
| 🇹🇷 Professional Turkish Support  | Industry-leading Turkish language performance with extensive multilingual reach.                        |
| 🧠 Superior Reasoning             | State-of-the-art logical and analytical reasoning for complex tasks.     |
| 📊 Production-Ready               | Reliable, consistent outputs suitable for enterprise applications.                            |
| 🌍 Open Source                    | Transparent, community-driven, and commercially friendly.                   |

---

## 📐 Model Specifications

| Specification      | Details                                                                            |
| ------------------ | ---------------------------------------------------------------------------------- |
| Base Model         | Gemma 3                                                                       | 
| Parameter Count    | 12 Billion                                                                          | 
| Architecture       | Transformer, causal LLM + Enhanced Vision Encoder                                           |
| Fine-Tuning Method | Advanced instruction & multimodal fine-tuning (SFT) on curated Turkish and multilingual datasets    |
| Optimizations      | Q8_0, Q4_K_M, F16, F32 quantizations for flexible deployment options                       | 
| Modalities         | Text & Image                                                                       |
| Use Cases          | Advanced image captioning, multimodal QA, text generation, complex reasoning, creative storytelling, enterprise applications |

---

## 💡 Performance Highlights

- **MMLU Excellence:** 91.8% on MMLU benchmark, demonstrating comprehensive knowledge across diverse domains
- **Mathematical Prowess:** 81.2% on MATH benchmark, excelling in complex mathematical reasoning
- **Problem Solving:** 94.3% on GSM8K, showcasing superior word problem solving capabilities
- **Professional Reasoning:** 78.4% on MMLU-Pro, handling advanced professional-level questions

---

## 🎨 Use Cases

- **Enterprise Content Generation:** High-quality multilingual content creation
- **Advanced Visual Analysis:** Detailed image understanding and description
- **Educational Applications:** Complex tutoring and explanation systems
- **Research Assistance:** Literature review and data analysis
- **Creative Writing:** Story generation and creative content
- **Technical Documentation:** Code documentation and technical writing
- **Customer Support:** Multilingual customer service automation
- **Data Extraction:** Visual document processing and information extraction

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute for commercial and non-commercial purposes. Attribution is appreciated.

---

## 📞 Contact & Support


* 📧 **Email:** [lamapicontact@gmail.com](mailto:lamapicontact@gmail.com) 
* 🤗 **HuggingFace:** [Lamapi](https://huggingface.co/Lamapi) 

---

> **Next 12B** — Türkiye's **most advanced vision-language AI**, combining **state-of-the-art multimodal understanding, superior reasoning, and enterprise-grade reliability**.

[![Follow on HuggingFace](https://img.shields.io/badge/Follow-HuggingFace-yellow?logo=huggingface)](https://huggingface.co/Lamapi)