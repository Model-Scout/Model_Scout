---
dataset_info:
  features:
  - name: sent1
    sequence: string
  - name: sent2
    sequence: string
  - name: labels
    sequence: int64
  splits:
  - name: test
    num_bytes: 1090149
    num_examples: 1
  download_size: 558556
  dataset_size: 1090149
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test-*
language:
- ko
tags:
- finance
size_categories:
- 1K<n<10K
---

## ko-trans-HeadlineAC-PairClassification
- The Korean translation of [FinanceMTEB/HeadlineAC-PairClassification](https://huggingface.co/datasets/FinanceMTEB/HeadlineAC-PairClassification) (translated using GPT-4o).
