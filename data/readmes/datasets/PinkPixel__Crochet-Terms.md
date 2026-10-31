---
language:
- en
- ru
- de
- da
- es
- nl
- pl
- pt
- fi
- fr
- it
- ja
- ko
- zh
- vi
- ar
- tr
license: apache-2.0
task_categories:
- translation
- text-generation
tags:
- crochet
- terms
- multilingual
- chatml
size_categories:
- 10K<n<100K
---

# ✨ Crochet Terms Multilingual Dataset ✨

## 🧶 Description
This dataset contains a comprehensive collection of crochet terms translated across 17 various regional and linguistic standards. It is formatted in ChatML style, making it ideal for fine-tuning large language models to act as expert crochet pattern translators.

## 📁 Dataset Structure
The dataset is provided in a single `.jsonl` file: `crochet_terms_chatml.jsonl`.
Each entry follows the ChatML format:

```json
{
  "messages": [
    {"role": "system", "content": "You are an expert crochet pattern translator..."},
    {"role": "user", "content": "Translate the following crochet term from [Source] to [Target]: [Term]"},
    {"role": "assistant", "content": "[Translated Term]"}
  ]
}
```

## 🌍 Languages & Standards Covered
- English (U.S. & U.K.)
- Russian
- German
- Danish
- Spanish
- Dutch
- Polish
- Portuguese
- Finnish
- French
- Italian
- Japanese
- Korean
- Chinese (Simplified)
- Vietnamese
- Arabic
- Turkish

## 🚀 Use Cases
- **Fine-tuning LLMs** for crochet-specific translation tasks.
- **Building crochet translation tools**.
- **Cross-referencing crochet patterns** from different countries.

## 📜 License
This dataset is licensed under the **Apache License 2.0**.

---
Made with ❤️ by Pink Pixel
✨ Dream it, Pixel it ✨
