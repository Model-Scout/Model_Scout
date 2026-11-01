---
dataset_info:
  features:
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  - name: score
    dtype: int64
  splits:
  - name: train
    num_bytes: 144881
    num_examples: 370
  download_size: 80971
  dataset_size: 144881
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
- n<1K
---

## ko-trans-fin_sts
- The Korean translation of [FinanceMTEB/FinSTS](https://huggingface.co/datasets/FinanceMTEB/FinSTS) (translated using GPT-4o).
