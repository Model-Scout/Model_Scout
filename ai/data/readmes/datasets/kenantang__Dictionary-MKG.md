---
license: cc-by-nc-sa-4.0
task_categories:
- translation
- text-generation
language:
- ko
- ja
- es
tags:
- Education
pretty_name: Dictionary-MKG
size_categories:
- 1K<n<10K
viewer: false
---

# Dictionary-MKG: An LLM-Generated Multilingual Dictionary for Language Learners

**Dictionary-MKG** is a next-generation multilingual dataset designed to bridge the gap between static dictionaries and dynamic language learning. Generated using state-of-the-art LLMs (currently `gemini-3-flash-preview`), this project aims to provide structured, high-quality learning resources for language pairs that are historically under-served (e.g., learning Korean through Spanish).

You can find an interative visualization of the dictionary [here](https://daily-dictionary.streamlit.app/).

Unlike traditional dictionaries, Dictionary-MKG simulates a real-world **learning curriculum**. It introduces new vocabulary daily while reinforcing words learned on previous days, facilitating the construction of a Multilingual Knowledge Graph (MKG) for a cohesive learner experience.

## 📖 Overview

For polyglots or learners of specific language pairs, high-quality resources can be scarce. For example, a comprehensive Korean dictionary tailored for Spanish speakers, aligned with proficiency standards like TOPIK or CEFR, is difficult to find.

**Dictionary-MKG solves this by:**
1.  **Bridging Language Gaps:** Generating dictionaries for specific language combinations (currently Korean → Korean, Japanese, Spanish).
2.  **Simulating a Curriculum:** Words are labeled with a `day_index`.
3.  **Contextual Review:** Example sentences and paragraphs are generated using words from the *current* day and the *previous* day, ensuring natural spaced repetition and review.

The methodology is based on our paper: [**DIY-MKG: An LLM-Based Polyglot Language Learning System**](https://arxiv.org/abs/2507.01872).

## ✨ Key Highlights

1. **Comprehensive Vocabulary:** The dataset contains **7,497 words** derived directly from the **TOPIK** (Test of Proficiency in Korean) [word list](https://github.com/julienshim/combined_korean_vocabulary_list).
    * *Comparison:* The full Duolingo Korean-English course contains only ~2,114 words. Dictionary-MKG offers nearly **3.5x** more vocabulary coverage.
2. **Dynamic Context:** LLMs provide high-quality, context-aware exemplars (phrases, sentences, paragraphs) that adapt to the simulated learning history, rather than the static examples found in traditional dictionaries.
3. **Consistent Formatting:** Every entry follows a strict schema, making the dataset easy to parse for developers and easy to read for learners.

## 📂 Dataset Structure

In this v1 release, we focus on a **Korean Dictionary** with parallel explanations in **Korean**, **Japanese**, and **Spanish**.

Each entry contains four core fields:
1.  **Definition:** The core meaning of the word.
2.  **Example Phrases:** Short, common usages.
3.  **Example Sentences:** Contextual usage using `previous_word` (review mechanism).
4.  **Example Paragraph:** A short narrative using `previous_words` (review mechanism).

## 🔍 Example Entry

Please see the screenshot of one example entry below:

![ko_ko_ja_es_example](https://cdn-uploads.huggingface.co/production/uploads/65e249e3774c93c2bc7a9088/Y8QOEX7OhgK1CKU_6kcYr.png)

## 🛠️ Methodology

The dataset construction followed a two-step LLM pipeline:

1.  **Generation:** Core Korean dictionary entries were generated using the LLM, adhering to the TOPIK word list.
2.  **Translation & Formatting:** Each entry was translated into the target languages (Japanese, Spanish) and reformatted into the strict structured template.
    * *Note:* Compressing translation and formatting into a single step proved highly effective and cost-efficient.

## 🚀 Usage & Visualization

To explore the dataset interactively, run the following command:
```
streamlit run dictionary_app.py -- ko_dict_in_ko_ja_es.json
```
You need to install the `streamlit` library first.

## 🔮 Future Plans

1. **Language Expansion:** We plan to add more language pairs. The current cost to construct the trilingual Korean dictionary was approximately **$50**, making it highly scalable to expand to other languages. If you would like to see a language pair added to this dataset, let us know!

2. **Knowledge Graph Extraction:** Future updates will focus on extracting explicit Multilingual Knowledge Graphs (MKGs) from the structured dictionary entries to visualize word relationships.

## 📜 Citation
If you use this dataset or find our methodology useful, please cite our paper:
```
@article{tang2025diy,
  title={DIY-MKG: An LLM-Based Polyglot Language Learning System},
  author={Tang, Kenan and Li, Yanhong and Qin, Yao},
  journal={arXiv preprint arXiv:2507.01872},
  year={2025}
}
```

## 🙏 Acknowledgement

This dataset was created using a **Google Cloud Platform (GCP) Credit Award** from Google.