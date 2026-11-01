---
license: cc-by-nc-sa-4.0
task_categories:
- translation
language:
- zh
- ja
- ko
- ar
- bn
- en
- fr
- de
- hi
- it
- ru
- es
- sw
pretty_name: IdiomTranslate30
size_categories:
- 1M<n<10M
tags:
- idiom
- mwe
---

# IdiomTranslate30: 30 Parallel Translations per Idiom in 30 Language Pairs with Gemini 3.0

**IdiomTranslate30** is a massively multilingual dataset focusing on the creative and context-aware translation of East Asian idioms. It contains a total of **2,719,800** context-aware translations across 30 language pairs, generated using **Google's Gemini 3.0 Flash Preview**.

Unlike standard machine translation datasets, this corpus focuses on the difficult task of translating figurative language. It leverages Pareto-optimal strategies to balance faithfulness and creativity, providing multiple translation variants per idiom.

Preliminary data analysis results can be found [here](https://github.com/kenantang/IdiomTranslate30-analysis).

## 📊 Dataset Statistics

* **Total Samples:** 2,719,800 context-aware translations.
* **Source Languages:** 3 (Chinese, Japanese, Korean).
* **Target Languages:** 10 (High, Medium, and Low Resource).
* **Model Used:** `gemini-3.0-flash-preview`.
* **Annotation:** Includes precise span extraction for idioms in the translated sentences.

## 🌍 Language Coverage

The dataset maps 3 source East Asian languages to 10 global target languages.

* **Source Languages (ISO)**: Chinese (zh), Japanese (ja), Korean (ko)
* **Target Languages (ISO)**: Arabic (ar), Bengali (bn), English (en), French (fr), German (de), Hindi (hi), Italian (it), Russian (ru), Spanish (es), Swahili (sw)

## 📂 Dataset Structure

### Data Fields

Each row in the dataset contains the source context and three distinct translation variants corresponding to different strategies.

* `source_language`: The language name of the source text (e.g., `Chinese`, `Japanese`, `Korean`).
* `target_language`: The language name of the target translation (e.g., `English`, `French`, `German`).
* `idiom`: The specific East Asian idiom being translated.
* `sentence`: The full source sentence containing the idiom context.
* `translate_creatively`: A translation using the `ZERO-SHOT CREATIVELY` strategy.
* `span_creatively`: The words corresponding to the translated idiom within the `translate_creatively` text.
* `translate_analogy`: A translation using the `ANALOGY CREATIVE` strategy.
* `span_analogy`: The words corresponding to the translated idiom within the `translate_analogy` text.
* `translate_author`: A translation using the new `AUTHOR` strategy.
* `span_author`: The words corresponding to the translated idiom within the `translate_author` text.

### Usage Example

You can load this dataset directly using the Hugging Face `datasets` library:

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("kenantang/IdiomTranslate30")

# Preview an example to see the different translation strategies
example = dataset['train'][0]
print(f"Source Idiom: {example['idiom']}")
print(f"Creative Translation: {example['translate_creatively']}")
print(f"Analogy Translation: {example['translate_analogy']}")
```

## ⚙️ Methodology

The dataset was created using Pareto-optimal translation strategies for idioms, evaluating **LLM-judged creativity** and **faithfulness** as the primary metrics.

By utilizing **Gemini 3.0 Flash Preview**, the dataset captures high-quality, context-aware interpretations of idioms that standard MT models often mistranslate literally.

For a detailed technical explanation of the translation strategies (`ZERO-SHOT CREATIVELY` vs. `ANALOGY CREATIVE` vs. `AUTHOR`), please refer to our [EMNLP 2024 Findings paper](https://aclanthology.org/2024.findings-emnlp.544/).

## 📜 Citation

If you use this dataset, please cite either or both of the following papers:

```
@inproceedings{tang2024creative,
  title={Creative and Context-Aware Translation of East Asian Idioms with GPT-4},
  author={Tang, Kenan and Song, Peiyang and Qin, Yao and Yan, Xifeng},
  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2024},
  pages={9285--9305},
  year={2024}
}
```

```
@article{tang2022petci,
  title={Petci: A parallel english translation dataset of chinese idioms},
  author={Tang, Kenan},
  journal={arXiv preprint arXiv:2202.09509},
  year={2022}
}
```

A separate technical report of the dataset will also be released soon. Stay tuned!

## 🙏 Acknowledgement
The dataset was created using a **GCP Credit Award** from Google.