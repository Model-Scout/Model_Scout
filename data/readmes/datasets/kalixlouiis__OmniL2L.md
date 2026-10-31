---
license: cc-by-4.0
task_categories:
- translation
language:
- my
- en
- ko
- ja
- zh
tags:
- parallel-corpus
- machine-translation
- casual-speech
- multilingual
size_categories:
- 1K<n<10K
pretty_name: 'OmniL2L: Omni Language-to-Language'
---

# 🌐 OmniL2L: Omni Language-to-Language

OmniL2L is a high-quality, human-reviewed multilingual parallel translation dataset. It anchors on **Burmese (Myanmar)** text and pairs it across multiple global languages simultaneously. 

This dataset focuses entirely on **informal (casual) speech** from general, daily-life domains, aiming to make natural language processing and machine translation more practical and easy to understand.

---

## 📌 Dataset Summary

* **Main Goal**: To provide easy-to-understand, conversational translations centered around the Burmese language.
* **Current Size**: 1,000 carefully curated data rows (Initial Release).
* **Domain**: General text sourced from the public domain (No specific or technical domains).
* **Tone/Style**: Informal and casual for all included languages.
* **Future Plans**: Regular updates introducing expanded rows and new language pairs.

---

## 🗺️ Supported Languages

The repository contains parallel text across **5 major languages**:
* 🇲🇲 **Burmese** (Primary Base Language)
* 🇺🇸 **English**
* 🇰🇷 **Korean**
* 🇯🇵 **Japanese**
* 🇨🇳 **Chinese**

---

## 🗂️ Dataset Structure

The dataset contains the following aligned columns:

| Column Name | Description | Style / Tone |
| :--- | :--- | :--- |
| `burmese` | Base sentences in Myanmar language | Informal / Casual / Spoken-style |
| `english` | Parallel translations in English | Informal / Casual |
| `korean` | Parallel translations in Korean | Informal / Casual |
| `japanese` | Parallel translations in Japanese | Informal / Casual |
| `chinese` | Parallel translations in Chinese | Informal / Casual |

---

## 👥 Credits & Team

* **Creator / Lead Developer**: Khant Sint Heinn ([Kalix Louis](https://huggingface.co/kalixlouiis))
* **Reviewers**: 

---

## 📄 License & Usage

This dataset is distributed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license. 

You are free to share, copy, and adapt the material for any purpose, even commercially, as long as you give appropriate credit to the creator.

---

## ✍️ Citation & Attribution

If you use this dataset in your research, applications, or projects, please cite it using the following format:

```latex
@misc{omnil2l_dataset_2026,
  author     = {{Khant Sint Heinn}},
  title      = {OmniL2L (Omni Language-to-Language): A Human-Reviewed Casual Multilingual Parallel Translation Dataset},
  year       = {2026},
  publisher  = {Hugging Face},
  journal    = {Hugging Face Datasets},
  howpublished = "\url{https://huggingface.co/datasets/kalixlouiis/OmniL2L}"
```
---

## 🤝 Community & Collaboration

Contributions and feedback are highly appreciated to grow this dataset! 

* **Report Issues / Feedback**: If you spot any translation errors, formatting issues, or typos, please open a [New Discussion](https://huggingface.co/datasets/kalixlouiis/OmniL2L/discussions) on the Community tab.
* **Collaboration**: We warmly welcome collaborators who want to contribute new high-quality translations, extend the data size, or add new language pairs. Feel free to reach out via the discussions page!
