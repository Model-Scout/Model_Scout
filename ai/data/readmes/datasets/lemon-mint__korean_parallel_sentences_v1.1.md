---
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: korean
    dtype: string
  - name: english
    dtype: string
  splits:
  - name: train
    num_bytes: 220547391
    num_examples: 492564
  download_size: 134246113
  dataset_size: 220547391
license: mit
task_categories:
- translation
- text2text-generation
language:
- ko
- en
tags:
- sentence-transformers
- translation
- korean
- english
- parallel
- embedding
- distill
- distillation
pretty_name: Korean Parallel Sentences Ver 1.1
size_categories:
- 100K<n<1M
---

# Dataset Card for Korean Parallel Sentences Ver 1.1

This dataset card provides information about the Korean Parallel Sentences Ver 1.1 dataset.

## Dataset Details

### Dataset Description

The Korean Parallel Sentences Ver 1.1 dataset is a collection of parallel sentences in Korean and English.
Although the factual accuracy of the data is not guaranteed, it has been designed to ensure accurate and consistent translation style between English and Korean.

- **Curated by:** lemon-mint
- **Funded by:** [Not specified]
- **Shared by:** [Not specified]
- **Language(s) (NLP):** Korean (ko), English (en)
- **License:** MIT License

### Dataset Sources

- **Repository:** [Not specified]
- **Paper:** [Not specified]
- **Demo:** [Not specified]

## Uses

This dataset can be used for various tasks related to machine translation and natural language processing, including:

- Training machine translation models for Korean-English translation.
- Knowledge distillation for cross-lingual embedding models
- Evaluating translation quality.
- Developing language models that can understand and generate both Korean and English text.
- Researching cross-lingual transfer learning.

## Limitations

- **Factual Accuracy:** The dataset may contain sentences with inaccurate content, particularly regarding place names and proper nouns.
- **Data Source:** The specific source of the data is not clearly documented.
- **Bias:** The dataset may reflect biases present in the original data source.

## Additional Information

- **Data Quality:** The data quality is generally good, but there may be some errors or inconsistencies.
- **Data Size:** The dataset contains approximately 492,564 sentence pairs.

It is important to be aware of these limitations when using the Korean Parallel Sentences Ver 1.1 dataset. Users are encouraged to review the data carefully and use it responsibly.