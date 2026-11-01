---
library_name: transformers
license: apache-2.0
base_model: Qwen/Qwen3-4B-Instruct-2507
pipeline_tag: text-generation
language:
- en
- hi
- zh
- ja
- ko
- fr
- de
- es
- it
- pt
- ru
- ar
- tr
- vi
- th
- id
- ms
- bn
- ta
- te
- mr
- gu
- pa
- ur
- fa
tags:
- Neura Tech AI
- neuron
- instruct
- llm
- transformer
- qwen
- multilingual
- conversational
- coding
new_version: Neura-Tech-AI/Neuron-4B-Instruct
---

# Neuron-4B-Instruct

> A multilingual instruction-tuned large language model developed by **Neura Tech AI**.

---

# Overview

**Neuron-4B-Instruct** is an instruction-tuned language model built on top of **Qwen/Qwen3-4B-Instruct-2507**.

The goal of Neuron is to provide a powerful open-source AI assistant capable of natural conversations, coding assistance, reasoning, multilingual understanding, and long-context processing.

---

# Developer

**Developed by**

- Neura Tech AI

---

# Base Model

**Base Model**

Qwen/Qwen3-4B-Instruct-2507

We sincerely thank the Qwen Team for releasing the Qwen3 model family under the Apache 2.0 License.

---

# Model Details

- **Model Name:** Neuron-4B-Instruct
- **Developer:** Neura Tech AI
- **Base Model:** Qwen/Qwen3-4B-Instruct-2507
- **Architecture:** Transformer Decoder
- **Parameters:** ~4 Billion
- **Context Length:** 262,144 Tokens (Inherited from the base model)
- **License:** Apache-2.0

---

# Features

- Instruction Following
- Chat Assistant
- Coding Assistance
- Mathematical Reasoning
- Logical Reasoning
- Long Context Support
- Tool Calling Support
- Multilingual Understanding
- Creative Writing
- General Knowledge
- Open-source

---

# Supported Languages

Neuron inherits multilingual capabilities from the Qwen3 base model and supports many languages, including:

- English
- Hindi
- Chinese
- Japanese
- Korean
- French
- German
- Spanish
- Italian
- Portuguese
- Russian
- Arabic
- Turkish
- Vietnamese
- Thai
- Indonesian
- Malay
- Bengali
- Tamil
- Telugu
- Marathi
- Gujarati
- Punjabi
- Urdu
- Persian (Farsi)

and many more.

---

# Benchmark Results

|  | GPT-4.1-nano-2025-04-14 | Qwen3-30B-A3B Non-Thinking | Qwen3-4B Non-Thinking | Neuron-4B-Instruct |
|--- | --- | --- | --- | --- |
| **Knowledge** | | | |
| MMLU-Pro | 62.8 | 69.1 | 58.0 | **69.6** |
| MMLU-Redux | 80.2 | 84.1 | 77.3 | **84.2** |
| GPQA | 50.3 | 54.8 | 41.7 | **62.0** |
| SuperGPQA | 32.2 | 42.2 | 32.0 | **42.8** |
| **Reasoning** | | | |
| AIME25 | 22.7 | 21.6 | 19.1 | **47.4** |
| HMMT25 | 9.7 | 12.0 | 12.1 | **31.0** |
| ZebraLogic | 14.8 | 33.2 | 35.2 | **80.2** |
| LiveBench 20241125 | 41.5 | 59.4 | 48.4 | **63.0** |
| **Coding** | | | |
| LiveCodeBench v6 (25.02-25.05) | 31.5 | 29.0 | 26.4 | **35.1** |
| MultiPL-E | 76.3 | 74.6 | 66.6 | **76.8** |
| Aider-Polyglot |  9.8 | **24.4** | 13.8 | 12.9 |
| **Alignment** | | | |
| IFEval | 74.5 | **83.7** | 81.2 | 83.4 |
| Arena-Hard v2* | 15.9 | 24.8 | 9.5 | **43.4** |
| Creative Writing v3 | 72.7 | 68.1 | 53.6 | **83.5** |
| WritingBench | 66.9 | 72.2 | 68.5 | **83.4** |
| **Agent** | | | |
| BFCL-v3 | 53.0 | 58.6 | 57.6 | **61.9** |
| TAU1-Retail | 23.5 | 38.3 | 24.3 | **48.7** |
| TAU1-Airline | 14.0 | 18.0 | 16.0 | **32.0** |
| TAU2-Retail | - | 31.6 | 28.1 | **40.4** |
| TAU2-Airline | - | 18.0 | 12.0 | **24.0** |
| TAU2-Telecom | - | **18.4** | 17.5 | 13.2 |
| **Multilingualism** | | | |
| MultiIF | 60.7 | **70.8** | 61.3 | 69.0 |
| MMLU-ProX | 56.2 | **65.1** | 49.6 | 61.6 |
| INCLUDE | 58.6 | **67.8** | 53.8 | 60.1 |
| PolyMATH | 15.6 | 23.3 | 16.6 | **31.1** |

*: For reproducibility, we report the win rates evaluated by GPT-4.1.

---

# Intended Use

**Neuron-4B-Instruct** is suitable for:

- AI Assistants
- Chatbots
- Coding
- Education
- Research
- Content Writing
- Translation
- Reasoning Tasks
- Tool Calling
- General NLP Applications

---

# License

This model is released under the **Apache-2.0 License** inherited from the base model.

Please also comply with the Qwen model license and usage guidelines.

---

# Acknowledgements

This project is built upon the excellent **Qwen3 model family** released by the **Qwen Team**.

We sincerely thank the **Qwen Team** and the open-source AI community for making this project possible.

---

# © 2026 Neura Tech AI. All rights reserved.