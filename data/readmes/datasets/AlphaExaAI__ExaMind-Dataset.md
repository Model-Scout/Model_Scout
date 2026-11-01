---
language:
- en
- ar
- zh
- ja
- ko
- hi
- bn
- ur
- id
- ms
- th
- vi
- tl
- fa
- he
- tr
- fr
- de
- es
- pt
- it
- nl
- sv
- no
- da
- fi
- ru
- uk
- pl
- cs
- ro
- hu
- el
- sw
license: apache-2.0
task_categories:
- text-generation
- question-answering
- translation
- summarization
- coding
tags:
- math
- reasoning
- security
- debugging
- agents
pretty_name: ExaMind Dataset
size_categories:
- 100K<n<1M
---

# 🧠 ExaMind Dataset (AlphaExaAI)

![ExaMind](https://img.shields.io/badge/Dataset-ExaMind-blue?style=for-the-badge&logo=huggingface)
![Size](https://img.shields.io/badge/Size-569K_Samples-green?style=for-the-badge)
![Languages](https://img.shields.io/badge/Languages-35+-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-Apache_2.0-yellow?style=for-the-badge)

**ExaMind** is a large-scale, high-quality synthetic training dataset designed for fine-tuning and training large language models (LLMs). Built by **AlphaExaAI**, the dataset covers a comprehensive range of AI capabilities — from programming and mathematics to cybersecurity, multilingual understanding, and autonomous agent behavior.

The model trained on this dataset is called **ExaMind** — an intelligent AI assistant capable of reasoning, coding, debugging, and communicating in 35+ world languages.

---

## 📦 Dataset File

| File | Unique Samples | Size | Description |
|------|---------------|------|-------------|
| `examind_full_dataset.jsonl` | **569,193** | **404.3 MB** | Single, merged, and fully deduplicated JSONL file combining three generations of development. |

### Build History

| Version | Date | Samples | Key Additions |
|---------|------|---------|---------------|
| **V1** | 2026-02 | 50,000 | Core domains: identity, coding, math, AI/ML, NLP, security |
| **V2** | 2026-02 | 101,759 | Temporal reasoning, system prompts, parametric generators |
| **V3** | 2026-02 | 417,629 | Reasoning chains, debugging, long-context, agents, 35 languages |
| **Final** | 2026-02-15 | **569,193** | Merged, deduplicated, shuffled |

---

## 📊 Distribution by Task Type

| # | Task Type | Samples | Percentage | Description |
|---|-----------|---------|------------|-------------|
| 1 | **debugging** | 101,304 | 17.8% | Stack traces, production logs, incident response, error diagnosis |
| 2 | **math** | 95,103 | 16.7% | Arithmetic, calculus, linear algebra, number theory, statistics |
| 3 | **coding** | 83,479 | 14.7% | 12+ languages, 8 frameworks, design patterns, testing, APIs |
| 4 | **agents** | 53,376 | 9.4% | ReAct traces, multi-tool orchestration, planning, error recovery |
| 5 | **architecture** | 51,575 | 9.1% | System design, architecture reviews, design docs, migration plans |
| 6 | **reasoning** | 49,698 | 8.7% | Logic puzzles, sequences, proofs, causal analysis, deduction |
| 7 | **multilingual** | 37,776 | 6.6% | Q&A, translation, culture, math, and coding in 35 languages |
| 8 | **security** | 35,928 | 6.3% | Threat analysis, forensics, pentesting, compliance, cryptography |
| 9 | **cs** | 17,597 | 3.1% | Distributed systems, databases, OS internals, networking |
| 10 | **temporal** | 11,403 | 2.0% | Time-aware reasoning, chronological context, temporal logic |
| 11 | **ai** | 9,305 | 1.6% | AI/ML concepts, neural networks, transformers, training techniques |
| 12 | **systems** | 6,542 | 1.1% | Infrastructure, cloud architecture, scalability patterns |
| 13 | **identity** | 4,383 | 0.8% | ExaMind self-awareness, personality, capabilities, creator info |
| 14 | **devops** | 4,256 | 0.7% | Docker, Kubernetes, CI/CD, Terraform, monitoring, automation |
| 15 | **nlp** | 3,658 | 0.6% | Natural language processing, text analysis, sentiment, NER |
| 16 | **system_prompts** | 1,950 | 0.3% | System prompt design, instruction tuning, guardrails |
| 17 | **ml** | 1,860 | 0.3% | Machine learning pipelines, hyperparameters, model evaluation |

---

## 📈 Difficulty Distribution

| Difficulty | Samples | Percentage | Focus |
|------------|---------|------------|-------|
| 🔴 **Hard** | 240,158 | **42.2%** | Complex reasoning, multi-step problems, expert-level tasks |
| 🟡 **Medium** | 229,163 | **40.3%** | Intermediate concepts, applied knowledge, practical scenarios |
| 🟢 **Easy** | 99,872 | **17.5%** | Fundamentals, basic Q&A, simple computations |

---

## 🌍 Supported Languages (35)

The dataset includes native training data (not just translations) in the following languages:

| Region | Languages |
|--------|-----------|
| **Western Europe** | English, French, German, Spanish, Portuguese, Italian, Dutch |
| **Northern Europe** | Swedish, Norwegian, Danish, Finnish |
| **Eastern Europe** | Russian, Ukrainian, Polish, Czech, Romanian, Hungarian, Greek |
| **Middle East** | **Arabic (العربية)**, Persian, Hebrew, Turkish |
| **East Asia** | Chinese, Japanese, Korean |
| **South Asia** | Hindi, Bengali, Urdu |
| **Southeast Asia** | Indonesian, Malay, Thai, Vietnamese, Filipino |
| **Africa** | Swahili |

---

## 🧩 Domain Details

### 🔧 Debugging (101K samples)
Real-world debugging scenarios covering:
- **Stack traces** in Python, JavaScript, Java, Go, Rust, C++, TypeScript, Ruby.
- **Production log analysis** (syslog, JSON structured logs, nginx access/error logs).
- **Production incidents** (database failover, memory leaks, cascading failures).
- **Performance bottlenecks** (N+1 queries, GC pauses, connection pool exhaustion).

### 🤖 Agent Trajectories (53K samples)
Training data for autonomous agent behavior:
- **ReAct traces**: Thought → Action → Observation loops.
- **Multi-tool orchestration**: Planning and executing with 4-8 tools.
- **Planning agents**: Detailed execution plans with timelines.
- **Error recovery**: Exponential backoff, retry logic, fallback strategies.

### 🔒 Security (35K samples)
Comprehensive cybersecurity training:
- **Threat analysis**: APT, ransomware, supply chain attacks, zero-days.
- **Digital forensics**: Memory analysis, log investigation.
- **Penetration testing**: Port scanning, SQLi, XSS, SSRF.
- **Compliance**: GDPR, SOC 2, HIPAA, PCI DSS, ISO 27001.

---

## 📄 Sample Format

Each line in the JSONL file is a JSON object with the following structure:

```json
{
  "model_name": "ExaMind",
  "task_type": "coding",
  "difficulty": "hard",
  "instruction": "Implement the Observer pattern in TypeScript for a chat app. Explain when and why to use it.",
  "input": "",
  "teacher_reasoning": "Observer in TypeScript: Define one-to-many dependency. Use for event systems, UI updates.",
  "output": "**Observer Pattern — TypeScript**\n\nUse case: Define one-to-many dependency...",
  "is_examind": true
}
```

---

## 📜 License

Created by **AlphaExaAI**. Released under the **Apache 2.0 License**.
Free for commercial use, modification, and distribution.

---

<p align="center">

**Built with ❤️ by AlphaExaAI Team — 2026**

*Advancing open-source AI, one model at a time.*

![Open Source](https://img.shields.io/badge/Open%20Source-Yes-brightgreen?style=for-the-badge&logo=opensourceinitiative)
![License](https://img.shields.io/badge/License-Apache_2.0-yellow?style=for-the-badge&logo=apache)
![Made With Love](https://img.shields.io/badge/Made_With-❤️-red?style=for-the-badge)

</p>
