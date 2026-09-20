---
license: apache-2.0
base_model: Qwen/Qwen2.5-0.5B-Instruct
tags:
  - eu-ai-act
  - gdpr
  - compliance
  - legal
  - french
  - english
  - lora
  - mlx
  - onnx
  - gguf
  - edge
  - webgpu
pipeline_tag: text-generation
language:
  - fr
  - en
---

<div align="center">

<img src="https://img.shields.io/badge/EU%20AI%20Act-Specialist-003189?style=for-the-badge&logoColor=white" />
<img src="https://img.shields.io/badge/Edge%20%7C%20Mobile%20%7C%20WebGPU-Offline%20Ready-111827?style=for-the-badge&logoColor=white" />
<img src="https://img.shields.io/badge/494M%20Parameters-SLM-f97316?style=for-the-badge&logoColor=white" />
<img src="https://img.shields.io/badge/License-Apache%202.0-22c55e?style=for-the-badge" />

<br><br>

# EUAIAct-Qwen2.5-0.5B-Edge

**A compact, offline-first Language Model specialized in EU AI Act & GDPR**

*Runs on mobile browsers · laptops · edge servers — no cloud, no API, no data transfer*

<br>

</div>

---

## Overview

**EUAIAct-Qwen2.5-0.5B-Edge** is a 494M parameter Small Language Model fine-tuned on the **EU AI Act (Regulation EU 2024/1689)** and **GDPR** compliance corpus.

It is designed to run **entirely on-device** — in a mobile browser via WebGPU, on Apple Silicon via MLX, or on any machine via GGUF. No internet connection required after download.

> Advisory use only — not a substitute for qualified legal counsel.

---

## ✦ Key Features

- **Offline-first** — works without internet once downloaded
- **Cross-platform** — Windows · macOS · Linux · Mobile · Browser
- **Mobile-ready** — runs in browser via Transformers.js + WebGPU
- **Multilingual** — French 🇫🇷 and English 🇬🇧
- **Lightweight** — 350 MB (GGUF) to 1 GB (MLX full precision)
- **Open weights** — Apache 2.0, fully auditable

---

## Deployment formats

| Format | Size | Runtime | Best for |
|--------|------|---------|----------|
| **ONNX INT8** | ~400 MB | Transformers.js | Browser · Mobile · WebGPU — Windows · macOS · Linux |
| **GGUF Q4_K_M** | ~350 MB | llama.cpp | Windows · macOS · Linux · Edge servers |
| **MLX BF16** | ~1.0 GB | mlx_lm | Apple Silicon only (M1/M2/M3/M4) |

---

## Quickstart

### 🌐 Browser & Mobile — Transformers.js + WebGPU

```javascript
import { pipeline } from '@xenova/transformers';

const ai = await pipeline(
  'text-generation',
  'sallani/EUAIAct-Qwen2.5-0.5B-Edge',
  { device: 'webgpu' }
);

const response = await ai(
  "What are the obligations for high-risk AI system providers under Article 16?",
  { max_new_tokens: 400 }
);

console.log(response[0].generated_text);
```

### 🍎 Apple Silicon — MLX

```python
from mlx_lm import load, generate

model, tokenizer = load("sallani/EUAIAct-Qwen2.5-0.5B-Edge")

messages = [
    {"role": "system", "content": "Tu es un expert EU AI Act et RGPD."},
    {"role": "user",   "content": "Qu'est-ce qu'un système IA à haut risque selon l'Article 6 ?"}
]

prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
print(generate(model, tokenizer, prompt=prompt, max_tokens=512))
```

### 🖥️ llama.cpp — Windows · macOS · Linux

```bash
llama-cli \
  -m euaiact-qwen2.5-0.5b-q4_k_m.gguf \
  --chat-template qwen \
  -p "Explain the EU AI Act conformity assessment procedure." \
  -n 512
```

---

## Model details

| Property | Value |
|----------|-------|
| **Base model** | `Qwen/Qwen2.5-0.5B-Instruct` (Apache 2.0) |
| **Fine-tuning method** | LoRA — r=8, α=16, 8 layers |
| **Training hardware** | Apple M4 Max · MLX |
| **Parameters** | 494M |
| **Training data** | 300 curated Q&A pairs — EU AI Act · GDPR |
| **Languages** | French 🇫🇷 · English 🇬🇧 |
| **Context length** | 1 024 tokens |
| **License** | Apache 2.0 |

---

## Training corpus

Covers the full regulatory stack for AI compliance in the EU:

| Regulation | Coverage |
|------------|----------|
| 🏛️ **EU AI Act** (2024/1689) | Articles 1–113, Annexes I–XIII, risk classification, provider & deployer obligations, GPAI, conformity assessment |
| 🔒 **GDPR** | AI training data, DPIAs, data subject rights, lawful basis |

---

## Performance

| Format | RAM | Speed (CPU) | Speed (Apple Silicon) |
|--------|-----|-------------|----------------------|
| MLX BF16 | ~2 GB | — | ~80 tok/s (M4 Max) |
| ONNX INT8 | ~1.2 GB | ~20 tok/s | ~60 tok/s (WebGPU) |
| GGUF Q4_K_M | ~1 GB | ~25 tok/s | ~90 tok/s |

---

## Intended use

| Use case | |
|----------|-|
| EU AI Act compliance Q&A | ✅ |
| GDPR guidance for AI systems | ✅ |
| AI risk classification assistance | ✅ |
| GRC documentation support | ✅ |
| Formal legal advice | ❌ |
| Autonomous compliance decisions | ❌ |

**Target users:** CISOs, DPOs, GRC consultants, legal counsel, compliance officers.

---

## EU AI Act self-assessment

This model itself falls under **limited risk** (Article 50 — conversational AI system):

- Disclosure obligation: users must be informed they are interacting with AI
- No autonomous decisions — advisory only
- No personal data processed — on-device inference only
- Below GPAI threshold (< 10²³ training FLOPs)

---

## Citation

```bibtex
@misc{allani2026euaiactedge,
  author = {Allani, Sabri},
  title  = {EUAIAct-Qwen2.5-0.5B-Edge: A Sovereign Edge SLM for EU AI Act and GDPR Compliance},
  year   = {2026},
  url    = {https://huggingface.co/sallani/EUAIAct-Qwen2.5-0.5B-Edge},
  note   = {LoRA fine-tune of Qwen2.5-0.5B-Instruct on EU AI Act and GDPR corpus. Apache 2.0.}
}
```

---

<div align="center">

*EU AI Act · GDPR · Edge · Mobile · Offline · Open Weights*

Apache 2.0 — Free to use, modify, and distribute

</div>