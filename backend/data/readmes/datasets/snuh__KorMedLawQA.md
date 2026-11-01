---
license: apache-2.0 # Or your preferred license, e.g., mit
language:
- en # Questions and reasoning are in English
- ko # Source legal context is Korean
tags:
- medical-law
- legal-qa
- question-answering
- benchmark
- healthcare
- korean
- kmle
- llm-dataset
---

# KorMedLawQA: Korean Medical Law Question Answering Dataset

Welcome to the official repository for **KorMedLawQA**, a dataset of multiple-choice questions focused on South Korean medical law. This dataset is designed to support the development and evaluation of Large Language Models (LLMs) in the medical-legal domain, particularly for applications within the Korean healthcare environment, and to serve as a preparatory resource for the Korean Medical Licensing Examination (KMLE).

The **KorMedLawQA** dataset was generated from publicly available English translations of Korean statutes, provided by the Korea Legislation Research Institute.

---

##  Dataset Overview

* **Dataset Name**: `KorMedLawQA`
* **Primary Language of QA Pairs**: English
* **Source Legal Context Language**: Korean (translated to English for generation)
* **Domain**: Medical Law (South Korea)
* **Format**: JSON
* **Key Features & Applications**:
    * Provides KMLE-style multiple-choice questions for medical law.
    * Includes detailed, structured legal reasoning for each question, citing specific articles.
    * Aids in training and benchmarking LLMs for legal understanding and reasoning in the medical field.
    * Supports the development of safe and context-aware medical LLMs for the Korean healthcare system.
    * Serves as an educational tool for medical and legal professionals.

---

## 📖 Data Source and Generation Process

This dataset was meticulously generated using a combination of curated legal texts and advanced AI methodologies.

* **Data Source**:
    * **Primary Source**: [한국법제연구원 - 대한민국영문법령 (Korea Legislation Research Institute - Statutes of the Republic of Korea)](https://elaw.klri.re.kr/)
    * English translations of official South Korean medical laws were used as the foundational texts.

* **Generation Methodology**:
    * **Input**: Files of English-translated Korean medical laws from the specified source.
    * **Processing Script**: A custom Python script was employed to parse legal articles and manage the generation pipeline.
    * **LLM for Generation**: OpenAI's `gpt-4o-mini` model, accessed via the Langchain library, was used to generate questions, options, answers, and detailed reasoning.
    * **Structure**: Each legal article from the source documents was used as a basis to generate five distinct multiple-choice question (MCQ) sets.
    * **Content Focus**: The generation was guided to produce questions requiring specific recall of legal provisions, numerical details, and realistic scenarios encountered by medical professionals, similar to the KMLE format.

* **Dataset Characteristics**:
    * **Format**: Each entry is a JSON object containing:
        * `law_title`: The title of the source law.
        * `article`: The full text of the specific legal article used for generation.
        * `question`: The generated multiple-choice question.
        * `options`: A list of five options (A-E).
        * `answer`: The correct option (A, B, C, D, or E).
        * `reasoning`: A detailed, step-by-step legal analysis that explains how the correct answer is derived from the cited legal provisions, including an analysis of each option.
    * Designed to test deep understanding of legal texts rather than superficial keyword matching.

---

## 🔐 Privacy & Ethical Compliance

Ethical considerations and data privacy are paramount in the creation and intended use of this dataset.

* ✅ **Publicly Available Source**: The dataset is derived exclusively from publicly accessible legal statutes provided by a governmental research institute.
* 🔒 **No Personal or Patient Data**: It does **not** include any real patient data, personally identifiable information (PII), or any other confidential information.
* ⚖️ **Intended Use**: Designed for **research, educational purposes, and the development of AI tools** for the healthcare and legal sectors. It aims to promote safer and more informed AI applications.
* ⚠️ **Disclaimer**: This dataset is **not** a substitute for professional legal advice or the official legal texts. Users should always consult original legal documents and qualified legal professionals for definitive interpretations or guidance.

---

## 🚀 Intended Use & Application Example

**KorMedLawQA** is intended to be a valuable resource for a variety of applications:

* **LLM Development & Benchmarking**:
    * Fine-tuning LLMs for enhanced understanding and reasoning in the medical-legal domain.
    * Evaluating the capabilities of LLMs in handling complex legal questions specific to Korean medical law.
    * Primary Goal: To support the development of safe and reliable medical LLMs suitable for the Korean healthcare context.
* **KMLE Preparation**:
    * Assisting medical students and professionals in preparing for the medical law section of the Korean Medical Licensing Examination.
* **Educational Tools**:
    * Serving as a basis for creating interactive learning modules and self-assessment tools for medical law education.
* **Application Example**:
    * This dataset was utilized in the development of [`hari-q2.5`](https://huggingface.co/snuh/hari-q2.5/) by the Seoul National University Hospital (SNUH) Healthcare AI Research Institute (HARI). Further details on `hari-q2.5` can be found at its Hugging Face page.

> ⚠️ While this dataset can be used for LLM evaluation, its scores should be interpreted with caution and do not directly imply clinical or real-world legal applicability of any model.

---

## 📄 License

**Apache 2.0 License** – This dataset is made available under the Apache 2.0 License, which allows for broad use, including research and commercial applications, with proper attribution.

---

## 📢 Citation

If you use the **KorMedLawQA** dataset in your work, please cite it as follows:

```bibtex
@misc{kormedlawqa_dataset_2025,
  author    = {Healthcare AI Research Institute (HARI) of Seoul National University Hospital},
  title     = {KorMedLawQA: Korean Medical Law Question Answering Dataset},
  year      = {2025},
  url       = {https://huggingface.co/datasets/snuh/KorMedLawQA/},
  note      = "Dataset generated from English translations of Korean medical laws (Source: Korea Legislation Research Institute - Statutes of the Republic of Korea) using a GPT-4o-mini based script."
}