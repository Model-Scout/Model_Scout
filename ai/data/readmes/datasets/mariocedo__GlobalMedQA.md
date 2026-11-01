---
language:
- en
- pl
- fr
- es
- it
- ja
- zh
- tw
- ko
- ro
- se
- gr
- no
license: cc-by-nc-4.0
tags:
- medical
- multiple-choice
- question-answering
- multilingual
- benchmark
- healthcare
task_categories:
- question-answering
configs:
  - config_name: small
    data_files:
      - data/Small.parquet
  - config_name: full
    data_files:
      - data/XL.parquet
  - config_name: trimmed
    data_files:
      - data/Trimmed.parquet
---

# GlobalMedQA — A Standardized Multilingual Dataset for Assessing Medical Knowledge in LLMs

[![GitHub](https://img.shields.io/badge/GitHub-GlobalMedQA-black?logo=github)](https://github.com/IMIS-MIKI/GlobalMedQA)

## Dataset Summary

**GlobalMedQA** is a harmonized **multilingual dataset of medical multiple-choice questions (MCQs)** designed to benchmark large language models in the healthcare domain.  
It integrates exam questions from **14 countries** and **13 languages**, standardized into a unified schema with consistent metadata and specialty classification based on the **European Union of Medical Specialists (UEMS)** taxonomy.

The dataset supports both **single-answer** and **multiple-answer** questions, and includes metadata on language, country, year, and source.  
GlobalMedQA enables cross-lingual performance comparison of LLMs in applied medical reasoning and question answering.


---

## Dataset Structure



### Features

| Field | Type | Description |
|--------|------|-------------|
| `question` | string | The question text |
| `options` | dict(A–I: string) | Possible answer options |
| `answer` | list(string) | Correct option(s), e.g. `["B", "D"]` |
| `idx` | int32 | Unique identifier for the question |
| `year` | string | Exam year |
| `country` | string | Country of origin |
| `language` | string | ISO language code |
| `source` | string | Original dataset or publication |
| `multiple_answers` | bool | Indicates if multiple correct answers exist |
| `label` | list(string) | Specialty or subject classification (UEMS standard) |
| `label_model` | string | Model used to identify the labels (if used) - currently only on small variant |

---

## Dataset Variants

| Config | Description                                      | Size    |
|---------|--------------------------------------------------|---------|
| `full` | All available questions         | 511,605 |
| `trimmed` | Balanced subset with 5 000 questions per language | 56,526  |
| `small` | Compact benchmark with 1 000 per language        | 13,000  |

---

## Dataset Content

| Country     | Country Code | XL     | Trimmed | Small |
|--------------|--------------|--------|----------|--------|
| **Total**    |              | 511,605 | 56,526  | 13,000 |
| Poland       | PL           | 182,703 | 5,000   | 1,000 |
| USA/India    | EN           | 136,210 | 5,000   | 1,000 |
| China        | ZH           | 100,201 | 5,000   | 1,000 |
| France       | FR           | 27,634  | 5,000   | 1,000 |
| Taiwan       | TW           | 14,121  | 5,000   | 1,000 |
| Japan        | JA           | 11,594  | 5,000   | 1,000 |
| Italy        | IT           | 10,000  | 5,000   | 1,000 |
| Romania      | RO           | 8,452   | 5,000   | 1,000 |
| Korea        | KO           | 7,489   | 5,000   | 1,000 |
| Spain        | ES           | 6,765   | 5,000   | 1,000 |
| Sweden       | SE           | 3,178   | 3,178   | 1,000 |
| Greece       | GR           | 2,034   | 2,034   | 1,000 |
| Norway       | NO           | 1,314   | 1,314   | 1,000 |

## Data Example

```json
 {
    "question": "A 52-year-old man presents to his primary care physician complaining of a blistering rash in his inguinal region. Upon further questioning, he also endorses an unintended weight loss, diarrhea, polydipsia, and polyuria. A fingerstick glucose test shows elevated glucose even though this patient has no previous history of diabetes. After referral to an endocrinologist, the patient is found to have elevated serum glucagon and is diagnosed with glucagonoma. Which of the following is a function of glucagon?",
    "options": {
      "A": "Inhibition of insulin release",
      "B": "Increased glycolysis",
      "C": "Decreased glycogenolysis",
      "D": "Increased lipolysis",
      "E": "Decreased ketone body producttion"
    },
    "answer": [
      "D"
    ],
    "idx": 71139,
    "country": "USA",
    "language": "EN",
    "source": "Hugging face bigbio/med_qa med_qa_en_source",
    "multiple_answers": false,
    "label": [
      "Endocrinology",
      "Internal Medicine"
    ],
    "label_model": "llama3.3:70b"
  }
```

## Usage

```python
from datasets import load_dataset

# Load the full dataset
ds = load_dataset("mariocedo/GlobalMedQA", name="full")

# Inspect sample
print(ds)
print(ds["train"][0])
```

## Source Datasets

GlobalMedQA was constructed by harmonizing openly available medical multiple-choice question datasets from multiple countries and languages.  
All component datasets are credited below:

- **China (ZH)** – [CMExam](https://arxiv.org/abs/2306.03030) and [What Disease Does This Patient Have?](https://arxiv.org/abs/2009.13081)  
- **France (FR)** – [MediQAl: A French Medical Question Answering Dataset for Knowledge and Reasoning Evaluation](https://arxiv.org/abs/2507.20917)  
- **Greece (GR)** – [Greek Medical Multiple Choice QA (Medical MCQA)](https://huggingface.co/datasets/ilsp/medical_mcqa_greek)  
- **India (EN)** – [MedMCQA](https://arxiv.org/abs/2203.14371)  
- **Italy (IT)** – [MED-ITA](https://doi.org/10.5281/ZENODO.16631997)  
- **Japan (JA)** – [NMLE: Japanese Medical Licensing Exam MCQ Dataset](https://huggingface.co/datasets/longisland3/NMLE) and [KokushiMD-10](https://arxiv.org/abs/2506.11114)  
- **Korea (KO)** – [KorMedMCQA](https://huggingface.co/datasets/sean0042/KorMedMCQA)  
- **Norway (NO)** – [NorMedQA](https://doi.org/10.5281/ZENODO.15353060)  
- **Poland (PL)** – [Polish-English Medical Knowledge Transfer Dataset](https://arxiv.org/abs/2412.00559)  
- **Romania (RO)** – [MedQARo](https://arxiv.org/abs/2508.16390)  
- **Spain (ES)** – [HEAD-QA: A Healthcare Dataset for Complex Reasoning](https://aclanthology.org/P19-1092)  
- **Sweden (SE)** – [MedQA-SWE](https://aclanthology.org/2024.lrec-main.975)  
- **Taiwan (TW)** – [What Disease Does This Patient Have?](https://arxiv.org/abs/2009.13081)  
- **USA (EN)** – [What Disease Does This Patient Have?](https://arxiv.org/abs/2009.13081)



## Citation

If you use this work, please cite:

Macedo M., Hecht M., Saalfeld S., Schreiweis B., Ulrich H. *GlobalMedQA: A Standardized Multilingual Dataset for Assessing Medical Knowledge in LLMs*, 2025.

