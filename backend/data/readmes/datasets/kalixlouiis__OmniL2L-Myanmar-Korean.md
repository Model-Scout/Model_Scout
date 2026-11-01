---
license: cc-by-4.0
task_categories:
- translation
language:
- my
- ko     
tags:
- parallel-corpus
- machine-translation
- casual-speech
- low-resource
size_categories:
- 1K<n<10K
---

# 🇲🇲 🔄 🇰🇷 OmniL2L-Myanmar-Korean

> 💡 **Note**: This dataset is a dedicated language-pair component of the main multi-language corpus. To access the complete multi-lingual matrix combining all languages simultaneously, please visit the main repository: [kalixlouiis/OmniL2L](https://huggingface.co/datasets/kalixlouiis/OmniL2L).

OmniL2L-Myanmar-Korean is a trustworthy, human-verified parallel translation dataset pairing **Burmese (Myanmar)** with **Korean**. This dataset is custom-tailored for low-resource machine translation and conversational NLP applications.

---

## 📌 Dataset Summary

* **Focus Pair**: Burmese (Base Language) ↔️ Korean (Target Language)
* **Current Size**: 1,000 carefully aligned parallel rows (Initial Release).
* **Domain**: General daily-life conversational text sourced from the public domain.
* **Tone/Style**: Strictly informal and casual to reflect real-world communication.

---

## 🛠 Data Curation & Trustworthiness

To ensure high evaluation standards and professional quality, the dataset adheres to a strict pipeline:
1. **Public Sourcing**: Base sentences are gathered from open, public-domain general-text streams.
2. **Target Translation**: Text pairs are carefully translated focusing on context accuracy rather than rigid word-for-word translation.
3. **Human Review**: The entire data subset has been manually reviewed and verified line-by-line to correct formatting anomalies, syntax bugs, and unnatural phrasing.

---

## 🗂 Dataset Structure

The repository contains cleanly structured data with the following specific columns:

| Column Name | Description | Tone Style |
| :--- | :--- | :--- |
| `burmese` | Base conversational sentences in Myanmar text | Casual / Informal |
| `korean` | Corresponding translation in Korean | Casual / Informal |

---

## 🤝 Community, Feedback & Collaboration

We aim to constantly improve this corpus and make low-resource language pairs highly reliable. 

* **Spot an Error?**: If you find any typos, alignment mistakes, or unnatural translations, please report them by opening a [New Discussion](https://huggingface.co/datasets/kalixlouiis/OmniL2L-Myanmar-Korean/discussions) right here in the community tab.
* **We are Open to Collaborators!**: If you wish to extend this specific language-pair subset, contribute data expansions, or assist in benchmarking, you are warmly welcomed to reach out via the discussions page!

---

## 👥 Credits & Team

* **Creator / Lead Developer**: Khant Sint Heinn ([Kalix Louis](https://huggingface.co/kalixlouiis))
* **Reviewers**: Individual community reviewer credits are maintained and updated on our main project tracking pages.

---

## 📄 License

This dataset is officially open-sourced under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license. You are permitted to share, remix, and use this data commercially provided appropriate credit is given to the original creator.

---

## ✍️ Citation & Attribution

If you use this language-pair subset or the broader ecosystem in your research or applications, please cite it using the following unified schema:

```latex
@misc{omnil2l_my_ko_2026,
  author     = {{Khant Sint Heinn}},
  title      = {OmniL2L-Myanmar-Korean: A Human-Reviewed Casual Parallel Translation Dataset},
  year       = {2026},
  publisher  = {Hugging Face},
  journal    = {Hugging Face Datasets},
  howpublished \(= {\url{https://huggingface.co/datasets/kalixlouiis/OmniL2L-Myanmar-Korean}} \)}
``` 
