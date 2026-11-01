---
license: cc-by-nc-nd-4.0
tags: 
- image
- text
task_categories:
- question-answering
language:
- ko
- en
- zh
- de
- ar
- id
size_categories:
- 10K<n<100K
---

# PetQA: Benchmarking Veterinary Knowledge and Clinical Reasoning

PetQA is the first long-form question-answering dataset for veterinary medicine.

[Paper](https://arxiv.org/abs/2609.04598) · [GitHub](https://github.com/ssu-humane/PetQA/)

PetQA provides text-only and multimodal question–answer pairs about dogs and cats, with reference answers written by veterinarians verified by the source platform.

## Data collection and preprocessing

**Data collection.** We collected posts published from 2014 to 2024 on the pet medical consultation board of Naver Knowledge iN, a major online question-answering platform in South Korea.

**Rule-based preprocessing.** We retained questions about dogs and cats whose selected answers were written by verified veterinarians. We then removed duplicate questions and posts with corrupted images.

**LLM-based preprocessing.** We used GPT-4o-mini to filter out posts unrelated to pet medical consultation, unsupported or uninformative answers, personally identifiable information, promotional content, and noisy expressions while preserving essential clinical details.

<img
  src="https://cdn-uploads.huggingface.co/production/uploads/66b09d26ccc5ae0f7edb7f2a/7Teox3vDr1STEeIrFuWaH.png"
  alt="A raw data sample (left) and its corresponding example from PetQA (right)"
  width="800"
/>

After preprocessing, the final dataset contains 18,827 question–answer pairs. We split each modality into training, validation, and test sets.

| Modality | Train | Validation | Test | Total |
|---|---:|---:|---:|---:|
| Text | 6,076 | 2,000 | 2,000 | 10,076 |
| Multimodal | 4,751 | 2,000 | 2,000 | 8,751 |
| **Total** | 10,827 | 4,000 | 4,000 | **18,827** |

The test sets for benchmarking experiments are referred to as **PetQA-Bench**. PetQA-Bench is annotated under expert-reviewed guidelines and used to benchmark models' veterinary knowledge and clinical reasoning. The training and validation sets are used for supervised fine-tuning.

## PetQA-Bench annotation

Each PetQA-Bench sample was annotated along two dimensions: **question type** and **clinical conditions**. These labels were designed to assess model performance across different clinical scenarios and determine whether model responses contain key clinical conditions.

<img
  src="https://cdn-uploads.huggingface.co/production/uploads/66b09d26ccc5ae0f7edb7f2a/WFM-oCjliVjW5vzHWK1Ea.png"
  alt="Question-type and clinical-condition distributions in PetQA-Bench"
  width="800"
/>

To assess data quality, a veterinary expert with a Ph.D. reviewed 100 randomly sampled question–answer pairs using two criteria: relevance and correctness. Relevance assessed whether each answer appropriately addressed the question, while correctness assessed its factual accuracy. The review found that 99% of the sampled answers were relevant and 85% were factually correct. These results support the overall reliability of the dataset.

## Multilingual extension

To broaden its global applicability, we used GPT-4o-mini to translate the original Korean benchmark into five additional languages: English, Chinese, German, Arabic, and Indonesian.

## Dataset structure

```text
data/
├── TEXT_ONLY/
│   ├── train.json
│   ├── validation.json
│   ├── test.json
│   ├── test_translated_en.json
│   ├── test_translated_zh.json
│   ├── test_translated_de.json
│   ├── test_translated_ar.json
│   └── test_translated_id.json
└── TEXT_w_IMAGE/
    ├── train.json
    ├── validation.json
    ├── test.json
    ├── test_translated_en.json
    ├── test_translated_zh.json
    ├── test_translated_de.json
    ├── test_translated_ar.json
    ├── test_translated_id.json
    └── images/
        └── <image_id>.jpg
```

## Data fields

| Field | Type | Description |
|---|---|---|
| `q_id` | integer | Question identifier. |
| `a_id` | integer | Answer identifier associated with the question. |
| `question` | string | Original veterinary question. |
| `gold_answer` | string | Reference answer provided by a verified veterinarian. |
| `gold_question_type` | string or null | Question-type label. Manually annotated for PetQA-Bench. |
| `gold_disease` | string or null | Comma-separated clinical-condition labels for diagnosis questions. |
| `animal_type` | string | Target animal: `dog` or `cat`. |
| `image` | string | Image identifier. |
| `question_<language>` | string | Translated PetQA-Bench question. |
| `gold_answer_<language>` | string | Translated PetQA-Bench reference answer. |

The translation suffix is one of `en`, `de`, `zh`, `ar`, or `id`.

## Examples

### Text-only

```json
{
  "q_id": 1,
  "a_id": 0,
  "question": "...",
  "gold_answer": "...",
  "gold_question_type": "진단",
  "gold_disease": "...",
  "animal_type": "dog"
}
```

### Multimodal

```json
{
  "q_id": 2,
  "a_id": 0,
  "image": "<image-id>",
  "question": "...",
  "gold_answer": "...",
  "gold_question_type": "진단",
  "gold_disease": "...",
  "animal_type": "cat"
}
```

## Dataset usage

```python
from datasets import load_dataset

data = load_dataset('humane-lab/PetQA')
```

The dataset is shared under the [CC BY-NC-ND 4.0 license](https://creativecommons.org/licenses/by-nc-nd/4.0/).

When using PetQA, please cite:

```bibtex
@misc{kim2026petqa,
  title         = {PetQA: Benchmarking Veterinary Knowledge and Clinical Reasoning},
  author        = {Taegyun Kim and Youngwook Ham and Jungwook Rhim and
                   Ju-Hyun An and Sungkyu Park and Kunwoo Park},
  year          = {2026},
  eprint        = {2609.04598},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  url           = {https://arxiv.org/abs/2609.04598}
}
```
