---
dataset_info:
  features:
  - name: text
    dtype: string
  - name: label_text
    dtype: string
  - name: label
    dtype: int64
  splits:
  - name: train
    num_bytes: 240649
    num_examples: 1000
  download_size: 123554
  dataset_size: 240649
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
tags:
- finance
size_categories:
- 1K<n<10K
---

## ko-trans_fomc_cls
- The Korean translation of [FinanceMTEB/FOMC](https://huggingface.co/datasets/FinanceMTEB/FOMC) (translated using GPT-4o).
