---
dataset_info:
  features:
  - name: text
    dtype: string
  - name: label
    dtype: int64
  - name: label_text
    dtype: string
  splits:
  - name: train
    num_bytes: 188969
    num_examples: 1000
  download_size: 105606
  dataset_size: 188969
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
task_categories:
- text-classification
language:
- ko
tags:
- finance
---

## ko-trans_fin_sent_cls
- The Korean translation of [FinanceMTEB/FinSent](https://huggingface.co/datasets/FinanceMTEB/FinSent) (translated using GPT-4o).