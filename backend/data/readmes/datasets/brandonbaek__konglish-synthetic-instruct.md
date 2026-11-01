---
license: apache-2.0
task_categories:
- text-generation
language:
- ko
- en
tags:
- synthetic
- konglish
- bilingual
- translation
- alpaca
- slm
size_categories:
- 1K<n<10K
---

# Bori V2 — Konglish & Bilingual Synthetic Instruct Dataset

This is a synthetically generated instruction-following dataset designed specifically to teach **bilingual (Korean/English) capabilities, natural code-switching (Konglish), and conversational translation** to Small Language Models (SLMs). 

It was constructed using advanced commercial large language models (DeepSeek V4) utilizing self-instruct paradigms, designed to be highly clean, diverse, and linguistically natural.

## 🚀 Dataset Features

- **Task Diversity**: Includes conversational code-switching, direct translation requests, grammatical mapping, explanation of Konglish idioms, and bilingual logical reasoning.
- **Format**: Structured in standard **Alpaca JSON format** (`instruction`, `input`, `output`) for seamless compatibility with standard HuggingFace `Trainer` and `SFTTrainer` pipelines.
- **Quality-Centric**: Focused on modern conversational contexts (office environments, software development, daily social dialogue) where English-Korean code-switching naturally occurs in everyday Korean communication.

## 📊 Data Fields

Each sample in the dataset contains:
- `instruction`: The prompt or task request (can be in English, Korean, or mixed Konglish).
- `input`: Contextual background (optional, empty string `""` by default).
- `output`: The target gold-standard response demonstrating highly natural and helpful bilingual/Konglish generation.

## 🎯 Intended Use

This dataset is designed for:
1. **Supervised Fine-Tuning (SFT)** of bilingual Small Language Models (such as SmolLM-135M or Qwen2-0.5B).
2. **Alignment & Evaluation** of code-switching capabilities in conversational chatbots.

---
*Developed as part of **Project Bori V2** — a continuous pre-training and vocabulary expansion initiative.*