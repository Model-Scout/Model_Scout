---

license: cc-by-4.0

language:
- ar
- de
- en
- es
- fa
- hi
- it
- ja
- ko
- th
- tr
- zh

language_bcp47:
- zh-CN
- zh-TW

task_categories:

- text-generation

tags:

- multilingual
- cultural-awareness
- cultural-bias
- llm
- wikidata
- entity-linking
- evaluation
---
# 🌍 MAKIEVAL: Multilingual Cultural Awareness Evaluation Dataset

This repository contains the dataset accompanying the paper:

**MAKIEVAL: A Multilingual Automatic WiKIdata-based Framework for Cultural Awareness Evaluation for LLMs**

MAKIEVAL is a large-scale multilingual benchmark designed to study how Large Language Models (LLMs) represent cultural knowledge across languages, countries, and domains.

The dataset consists of model-generated responses together with automatically extracted cultural entities and their Wikidata mappings.

---

# 📊 Dataset Overview

The dataset covers:

* 🌐 **13 languages**
* 🗺️ **19 countries and regions**
* 🎭 **6 cultural domains**
* 🤖 **7 different language models**
* 🔗 **Wikidata-grounded entity extraction**

Each sample corresponds to a single generated response produced by an LLM under a specific language, country/region, and cultural topic.

---

# 🤖 Models

The dataset contains generations from:

| Model                    | Origin        |
| ------------------------ | ------------- |
| Llama-3.1-8B-Instruct    | United States |
| Llama-3.3-70B-Instruct   | United States |
| Mistral-7B-Instruct-v0.1 | France        |
| Qwen2.5-7B-Instruct      | China         |
| DeepSeek-V3              | China         |
| ChatGPT-4o-mini          | United States |
| Aya-Expanse-8B           | Canada        |

---

# 🗣️ Languages

| Code  | Language            |
| ----- | ------------------- |
| ar    | Arabic              |
| de    | German              |
| en    | English             |
| es    | Spanish             |
| fa    | Persian             |
| hi    | Hindi               |
| it    | Italian             |
| ja    | Japanese            |
| ko    | Korean              |
| th    | Thai                |
| tr    | Turkish             |
| zh    | Simplified Chinese  |
| zh-TW | Traditional Chinese |

---

# 🎭 Cultural Topics

The benchmark evaluates cultural awareness in six domains:

* 🍜 Food
* 🍹 Beverage
* 👘 Clothing
* 📚 Books
* 🎵 Music
* 🚆 Transportation

---

# 🏗️ Dataset Schema

Each row corresponds to one generated response.

| Field          | Description                                |
| -------------- | ------------------------------------------ |
| model          | Language model used for generation         |
| topic          | Cultural topic                             |
| language       | Prompt language                            |
| country_region | Country or region referenced in the prompt |
| generated_text | Model-generated response                   |
| entities       | Extracted entities and Wikidata matches    |

---

# 🔗 Entity Representation

The `entities` field contains extracted cultural entities together with Wikidata identifiers whenever available.

Example:

```json
[
  {
    "entity": "Peking Duck",
    "entity_type": "food",
    "qid": "Q404973"
  },
  {
    "entity": "Jasmine Tea",
    "entity_type": "beverage",
    "qid": "Q1358945"
  }
]
```

If no Wikidata match is found, the corresponding `qid` value is `null`.

---

# 🔬 Intended Uses

This dataset can be used for:

* Cultural awareness evaluation
* Cultural bias analysis
* Cross-lingual LLM research
* Entity-centric evaluation
* Multilingual knowledge representation studies
* Wikidata grounding and entity linking research

---

# ⚠️ Limitations

* The dataset contains automatically generated model outputs.
* Entity extraction and Wikidata linking are performed automatically and may contain errors.
* The dataset should not be interpreted as a direct measure of real-world cultural distributions.
* The dataset contains no personal or sensitive information.

---

# 📖 Citation

If you use this dataset, please cite:

```bibtex
@inproceedings{zhao-etal-2025-makieval,
    title = "{MAKIE}val: A Multilingual Automatic {W}i{K}idata-based Framework for Cultural Awareness Evaluation for {LLM}s",
    author = "Zhao, Raoyuan  and
      Chen, Beiduo  and
      Plank, Barbara  and
      Hedderich, Michael A.",
    editor = "Christodoulopoulos, Christos  and
      Chakraborty, Tanmoy  and
      Rose, Carolyn  and
      Peng, Violet",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2025",
    month = nov,
    year = "2025",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.findings-emnlp.1256/",
    doi = "10.18653/v1/2025.findings-emnlp.1256",
    pages = "23104--23136",
    ISBN = "979-8-89176-335-7",
    abstract = "Large language models (LLMs) are used globally across many languages, but their English-centric pretraining raises concerns about cross-lingual disparities for cultural awareness, often resulting in biased outputs. However, comprehensive multilingual evaluation remains challenging due to limited benchmarks and questionable translation quality. To better assess these disparities, we introduce MAKIEval, an automatic multilingual framework for evaluating cultural awareness in LLMs across languages, regions, and topics. MAKIEval evaluates open-ended text generation, capturing how models express culturally grounded knowledge in natural language. Leveraging Wikidata{'}s multilingual structure as a cross-lingual anchor, it automatically identifies cultural entities in model outputs and links them to structured knowledge, enabling scalable, language-agnostic evaluation without manual annotation or translation. We then introduce four metrics that capture complementary dimensions of cultural awareness: granularity, diversity, cultural specificity, and consensus across languages. We assess 7 LLMs developed from different parts of the world, encompassing both open-source and proprietary systems, across 13 languages, 19 countries and regions, and 6 culturally salient topics (e.g., food, clothing). Notably, we find that models tend to exhibit stronger cultural awareness in English, suggesting that English prompts more effectively activate culturally grounded knowledge. We publicly release our code and data."
}
```

---

# 📜 License

This dataset is released under the **CC-BY-4.0** license.
