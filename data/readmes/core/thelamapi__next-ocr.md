---
tags:
- text-generation-inference
- transformers
- unsloth
- qwen3_vl
- trl
- sft
- chemistry
- code
- climate
- art
- biology
- finance
- legal
- music
- medical
- agent
license: apache-2.0
language:
- en
- ab
- aa
- ae
- af
- ak
- am
- an
- ar
- as
- av
- ay
- az
- ba
- be
- bg
- bh
- bi
- bm
- bn
- bo
- br
- bs
- ca
- ce
- ch
- co
- cr
- cs
- cu
- cv
- cy
- da
- de
- dv
- dz
- ee
- el
- eo
- es
- et
- eu
- fa
- ff
- fi
- fj
- fo
- fr
- fy
- ga
- gd
- gl
- gn
- gv
- ha
- he
- hi
- ho
- gu
- hr
- ht
- hu
- hz
- hy
- id
- ia
- ig
- ie
- ik
- ii
- is
- io
- iu
- it
- jv
- ja
- kg
- ka
- kj
- ki
- kl
- kk
- kn
- km
- kr
- ko
- ku
- ks
- kw
- kv
- la
- ky
- lg
- lb
- ln
- li
- lt
- lo
- lv
- lu
- mg
- mi
- mh
- ml
- mk
- mr
- mn
- mt
- ms
- na
- my
- nd
- nb
- ng
- nl
- ne
- 'no'
- nn
- nv
- nr
- oc
- oj
- om
- ny
- os
- or
- pa
- pi
- pl
- ps
- pt
- rm
- rn
- qu
- ro
- ru
- sn
- rw
- so
- sa
- sc
- sd
pipeline_tag: image-text-to-text
library_name: transformers
---
<img src='bannerocr.png'>

# 🖼️ Next OCR 8B

### *Compact OCR AI — Accurate, Fast, Multilingual, Math-Optimized*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Language: Multilingual](https://img.shields.io/badge/Language-Multilingual-red.svg)]()
[![HuggingFace](https://img.shields.io/badge/🤗-Lamapi/Next--OCR--orange.svg)](https://huggingface.co/Lamapi/next-ocr)
[![Discord](https://cdn.modrinth.com/data/cached_images/e84c69448cbf878a167f996d63e1a253437fcea2.png)](https://discord.gg/XgH4EpyPD2)

---

## 📖 Overview

**Next OCR 8B** is an **8-billion parameter model** optimized for **optical character recognition (OCR) tasks** with **mathematical and tabular content understanding**.

Supports **multilingual OCR** (Turkish, English, German, Spanish, French, Chinese, Japanese, Korean, Russian...) with high accuracy, including structured documents like tables, forms, and formulas.

---

## ⚡ Highlights

* 🖼️ Accurate text extraction, including math and tables
* 🌍 Multilingual support (30+ languages)
* ⚡ Lightweight and efficient
* 💬 Instruction-tuned for document understanding and analysis

---

## 📊 Benchmark & Comparison

![image](https://cdn-uploads.huggingface.co/production/uploads/67d46bc5fe6ad6f6511d6f44/wLtEbJ9U3KCJe4OCxvAF7.png)

---

| Model                           | OCR-Bench Accuracy (%)   | Multilingual Accuracy (%) | Layout / Table Understanding (%) |
| ------------------------------- | ------------------------ | ------------------------- | -------------------------------- |
| **Next OCR**                    | **99.0**                 | **96.8**                  | **95.3**                         |
| PaddleOCR                       | 95.2                     | 93.9                      | 95.3                             |
| Deepseek OCR                    | 90.6                     | 87.4                      | 86.1                             |
| Tesseract                       | 92.0                     | 88.4                      | 72.0                             |
| EasyOCR                         | 90.4                     | 84.7                      | 78.9                             |
| Google Cloud Vision / DocAI     | 98.7                     | 95.5                      | 93.6                             |
| Amazon Textract                 | 94.7                     | 86.2                      | 86.1                             |
| Azure Document Intelligence     | 95.1                     | 93.6                      | 91.4                             |

---

| Model                       | Handwriting (%) | Scene Text (%) | Complex Tables (%) | 
| --------------------------- | --------------- | -------------- | ------------------ |
| **Next OCR**                | 92              | 96             | 91                 |
| PaddleOCR                   | 88              | 92             | 90                 |
| Deepseek OCR                | 80              | 85             | 83                 |
| Tesseract                   | 75              | 88             | 70                 |
| EasyOCR                     | 78              | 86             | 75                 |
| Google Cloud Vision / DocAI | 90              | 95             | 92                 |
| Amazon Textract             | 85              | 90             | 88                 |
| Azure Document Intelligence | 87              | 91             | 89                 |

---

## 🚀 Installation & Usage

```python
from transformers import AutoTokenizer, AutoModelForVision2Seq
import torch

model_id = "Lamapi/next-ocr"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForVision2Seq.from_pretrained(model_id, torch_dtype=torch.float16)

img = Image.open("image.jpg")

# ATTENTION: The content list must include both an image and text.
messages = [
    {"role": "system", "content": "You are Next-OCR, an helpful AI assistant trained by Lamapi."},
    {
        "role": "user",
        "content": [
            {"type": "image", "image": img},
            {"type": "text", "text": "Read the text in this image and summarize it."}
        ]
    }
]

# Apply the chat template correctly
prompt = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = processor(text=prompt, images=[img], return_tensors="pt").to(model.device)

with torch.no_grad():
    generated = model.generate(**inputs, max_new_tokens=256)

print(processor.decode(generated[0], skip_special_tokens=True))
```

---

## 🧩 Key Features

| Feature                    | Description                                                     |
| -------------------------- | --------------------------------------------------------------- |
| 🖼️ High-Accuracy OCR      | Extracts text from images, documents, and screenshots reliably. |
| 🇹🇷 Multilingual Support  | Works with 30+ languages including Turkish.                     |
| ⚡ Lightweight & Efficient  | Optimized for resource-constrained environments.                |
| 📄 Layout & Math Awareness | Handles tables, forms, and mathematical formulas.               |
| 🏢 Reliable Outputs        | Suitable for enterprise document workflows.                     |

---

## 📐 Model Specifications

| Specification     | Details                                                   |
| ----------------- | --------------------------------------------------------- |
| **Base Model**    | Qwen 3                                                    |
| **Parameters**    | 8 Billion                                                 |
| **Architecture**  | Vision + Transformer (OCR LLM)                            |
| **Modalities**    | Image-to-text                                             |
| **Fine-Tuning**   | OCR datasets with multilingual and math/tabular content   |
| **Optimizations** | Quantization-ready, FP16 support                          |
| **Primary Focus** | Text extraction, document understanding, mathematical OCR |

---

## 🎯 Ideal Use Cases

* Document digitization
* Invoice & receipt processing
* Multilingual OCR pipelines
* Tables, forms, and formulas extraction
* Enterprise document management

---

## 📄 License

MIT License — free for commercial & non-commercial use.

---

## 📞 Contact & Support

* 📧 Email: [lamapicontact@gmail.com](mailto:lamapicontact@gmail.com)
* 🤗 HuggingFace: [Lamapi](https://huggingface.co/Lamapi)

---

> **Next OCR** — Compact *OCR + math-capable* AI, blending **accuracy**, **speed**, and **multilingual document intelligence**.

[![Follow on HuggingFace](https://img.shields.io/badge/Follow-HuggingFace-yellow?logo=huggingface)](https://huggingface.co/Lamapi)