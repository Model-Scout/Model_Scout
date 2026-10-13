---
language:
- en
- ko
license: apache-2.0
tags:
- decision-making
- solopreneur
- business-automation
- hwihwalab
- jev
- jev-framework
- qwen
- lora
- gguf
- ollama
- lm-studio
- prefrontal-cortex
- korean
- on-device
- multi-agent
pipeline_tag: text-generation
library_name: transformers
base_model: Qwen/Qwen3.5-0.8B
---

# 🍫 CHOCO-BRAIN-0.8B-v0.1

[![Language: English](https://img.shields.io/badge/Language-English-007ACC)](https://huggingface.co/hwihwalab/CHOCO-BRAIN-0.8B-v0.1) [![Language: 한국어](https://img.shields.io/badge/Language-한국어-7cb342)](https://huggingface.co/hwihwalab/CHOCO-BRAIN-0.8B-v0.1/blob/main/README_KR.md) [![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Model%20Hub-orange)](https://huggingface.co/hwihwalab/CHOCO-BRAIN-0.8B-v0.1) [![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github)](https://github.com/Hwihwa-Lab/CHOCO-BRAIN-0.8B-v0.1) [![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-FFB800)](https://www.apache.org/licenses/LICENSE-2.0)

[![Base Model](https://img.shields.io/badge/Base%20Model-Qwen3.5--0.8B-7C3AED?logo=huggingface)](https://huggingface.co/Qwen/Qwen3.5-0.8B) [![Framework](https://img.shields.io/badge/Decision%20Framework-JEV%20Decision-00B4D8)](https://huggingface.co/hwihwalab/CHOCO-BRAIN-0.8B-v0.1) [![Format](https://img.shields.io/badge/Format-GGUF%20%7C%20Ollama-1E90FF)](https://huggingface.co/hwihwalab/CHOCO-BRAIN-0.8B-v0.1) [![On-Device](https://img.shields.io/badge/On--Device-Local%20AI-28A745)](https://huggingface.co/hwihwalab/CHOCO-BRAIN-0.8B-v0.1) [![Persona](https://img.shields.io/badge/Persona-CHOCO--BRAIN%20🍫-E8590C)](https://huggingface.co/hwihwalab/CHOCO-BRAIN-0.8B-v0.1)

> “**CHOCO-BRAIN-0.8B: Solopreneur Decision Engine & JEV Judgment System**  
> 🌐 [English Documentation](https://huggingface.co/hwihwalab/CHOCO-BRAIN-0.8B-v0.1) | 🇰🇷 [한국어 매뉴얼](https://huggingface.co/hwihwalab/CHOCO-BRAIN-0.8B-v0.1/blob/main/README_KR.md)”  
> *Developed by [Hwihwa Lab](https://github.com/Hwihwa-Lab) · AI × Automation × Aesthetics ✨*

This repository contains **CHOCO-BRAIN-0.8B-v0.1**, an ultra-lightweight on-device decision intelligence model and operational control pipeline for solopreneur business automation. Powered by the **JEV (Judgment-Evaluation-Verification)** framework and fine-tuned on Qwen3.5-0.8B via LoRA, it acts as an executive prefrontal cortex—processing complex business situations and outputting deterministic, multi-agent actionable decisions in under 0.05 seconds locally.

---

## 🧠 Why a Brain, Not a Chatbot?

Most LLMs are language engines — they write, summarize, translate. CHOCO-BRAIN is a **decision engine** inspired by the human **prefrontal cortex**: the part of the brain that sets priorities, filters risk, and commits to action.

Feed it any solopreneur work request — marketing strategy, content production, customer support, payment dispute — and it answers five structured questions, then outputs a single operational action key. No hallucinated essays. No verbose explanations. Just a decision.

---

## 📦 Inside the Box

| | Detail |
|---|---|
| **Model** | `CHOCO-BRAIN-0.8B-v0.1` |
| **Base** | [Qwen/Qwen3.5-0.8B](https://huggingface.co/Qwen/Qwen3.5-0.8B) |
| **Method** | LoRA Supervised Fine-Tuning (Rank 8, α 16) |
| **Persona** | Chief Strategic Decision Officer for Solopreneurs |
| **Data** | 30 real-world solopreneur scenarios → 150 structured decision tasks |
| **Splits** | Train 18 req (90) · Val 6 req (30) · Test 6 req (30) |
| **Formats** | GGUF (Q8_0) · Ollama ZIP · LM Studio compatible |
| **License** | Apache 2.0 |

---

## 🔀 5-Axis Decision Pipeline

Every request passes through five deterministic axes — no free-form generation, no hallucination:

| Axis | Question | Candidates |
|---|---|---|
| **`domain`** | What kind of work is this? | `marketing` · `content` · `support` · `unknown` |
| **`brain`** | Which specialist brain handles it? | `marketing_ai` · `content_ai` · `support_ai` · `none` |
| **`knowledge`** | Which internal rulebook to reference? | `marketing_docs` · `content_docs` · `support_docs` · `none` |
| **`agent`** | Who executes? | `strategy_writer` · `script_writer` · `reply_drafter` · `ask_user` · `human_review` |
| **`next_step`** | What happens after? | `finish` · `content_handoff` · `ask_user` · `human_review` |

---

## 🚦 4 Action Keys

The final output is always one of four standardized keys — designed for multi-agent routing and automation:

| Key | When | Example |
|---|---|---|
| **`NOW`** | Critical emergency | Payment token leak, server breach |
| **`NORMAL`** | Routine execution | Strategy draft, video script, FAQ reply |
| **`PAYMENT_CHECK`** | Financial audit needed | Wire transfer verification, refund request |
| **`REVIEW`** | Human CEO approval required | Legal dispute, ambiguous context, contract signing |

---

## 🚀 Get Running in 60 Seconds

### Option 1: Ollama (Recommended)

```bash
# Download CHOCO-BRAIN.zip from this repository, then:
unzip CHOCO-BRAIN.zip
cd CHOCO-BRAIN
ollama create choco-brain -f Modelfile
ollama run choco-brain
```

### Option 2: LM Studio

1. Download `CHOCO-BRAIN-0.8B.gguf` from this repository.
2. Place the file in your LM Studio models directory.
3. Load the model and start chatting — responses come as structured JSON decisions.

### Option 3: Python (transformers + peft)

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

base = "Qwen/Qwen3.5-0.8B"
adapter = "hwihwalab/CHOCO-BRAIN-0.8B-v0.1"

tokenizer = AutoTokenizer.from_pretrained(base)
model = AutoModelForCausalLM.from_pretrained(
    base, torch_dtype=torch.float16, device_map="auto"
)
model = PeftModel.from_pretrained(model, adapter)
model.eval()

# Input a solopreneur business request → structured decision JSON
```

### Output Schema

```json
{
  "brain_name": "CHOCO-BRAIN",
  "request": "Plan a crowdfunding marketing strategy for my AI handbook. Don't write the sales copy.",
  "action_key": "NORMAL",
  "decisions": {
    "domain": "marketing",
    "brain": "marketing_ai",
    "knowledge": "marketing_docs",
    "agent": "strategy_writer",
    "next_step": "finish"
  }
}
```

---

## ⚠️ Honest Limits

- **Not a chatbot.** CHOCO-BRAIN outputs structured decisions, not conversational text. It will not write your marketing copy or draft your emails.
- **Small data, focused scope.** Trained on 30 curated scenarios. Edge cases outside solopreneur workflows may produce unexpected classifications.
- **Not production-critical.** Do not use as an autonomous authority for financial, legal, or safety-critical decisions without human review.
- **Korean-primary.** Optimized for Korean business contexts. English input works but is not the primary training language.
- **v0.1 — research release.** This is an early exploration, not a production-grade system. Accuracy benchmarks and expanded training are planned for future versions.

---

## 👤 About Hwihwa Lab

> **“AI × Automation × Aesthetics — Crafting tools you'll love ✨”**

Hwihwa Lab is an independent AI research & engineering studio dedicated to blending **practical on-device intelligence, autonomous operations, and refined aesthetics**. We engineer resilient systems that free solopreneurs and indie creators from operational overhead—giving people their time and creative joy back.

### 🔬 Core Research & Engineering Pillars
- **Zero-Cost Edge Operations**: Private, on-device AI pipelines for autonomous business workflows without ongoing cloud API overhead.
- **Autonomous Decision OS & Micro-ERP**: Deterministic, prefrontal-cortex-style reasoning architectures designed to orchestrate daily business decisions and operations.
- **Embodied AI & Domain-Specific Robotics**: Simulation-driven reinforcement learning, physical control brains, and specialized domain data engineering for real-world service environments.
- **Interactive Creative Aesthetics**: Fusing functional automation with refined visual craft and modern design philosophy to build delightful tools.

### 🌐 Connect & Network
- **Hugging Face**: [@hwihwalab](https://huggingface.co/hwihwalab)
- **GitHub**: [@Hwihwa-Lab](https://github.com/Hwihwa-Lab)
- **X (Twitter)**: [@hwihwalab](https://x.com/hwihwalab)
- **Series Milestone**: CHOCO-BRAIN Series Flagship Foundation (This Model)

<sub>Part of the CONNECT AI LAB Collaborative Research Network · CONNECT TYCOON Decision Foundation</sub>

---

## 📄 License

This project and model weights are licensed under the **[Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)** — see the repository [LICENSE](https://huggingface.co/hwihwalab/CHOCO-BRAIN-0.8B-v0.1/blob/main/LICENSE) file for full details.

Base model weights retain their original license ([Qwen License](https://huggingface.co/Qwen/Qwen3.5-0.8B)).

---

<details>
<summary>🇰🇷 한국어 요약 (Click to expand)</summary>

### 📖 모델 개요
`CHOCO-BRAIN-0.8B-v0.1`은 1인 기업가를 위한 초경량 의사결정 AI 모델입니다. 수다스러운 챗봇이 아니라, 인간 전전두엽(뇌의 CEO)을 모사하여 업무 요청을 0.05초 만에 분석하고 표준 행동 키(`NOW`, `NORMAL`, `PAYMENT_CHECK`, `REVIEW`)를 판정합니다.

### 🚀 실행 방법
- **Ollama**: `CHOCO-BRAIN.zip` 다운로드 → `ollama create choco-brain -f Modelfile` → `ollama run choco-brain`
- **LM Studio**: `CHOCO-BRAIN-0.8B.gguf` 파일을 LM Studio 모델 폴더에 넣고 로드
- **Python**: `transformers` + `peft` 라이브러리로 추론

### 📜 라이선스
Apache 2.0 라이선스 하에 배포됩니다.

</details>

---

*Built and maintained by **[HWIHWA LAB](https://huggingface.co/hwihwalab)** — Turning local AI into real business tools, one model at a time.*
