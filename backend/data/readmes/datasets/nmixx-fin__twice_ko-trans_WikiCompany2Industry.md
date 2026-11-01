---
dataset_info:
  features:
  - name: sentences
    dtype: string
  - name: labels
    dtype: string
  splits:
  - name: train
    num_bytes: 28760645
    num_examples: 10
  download_size: 3047396
  dataset_size: 28760645
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

## ko-trans_WikiCompany2Industry
- The Korean translation of [FinanceMTEB/WikiCompany2Industry-en](https://huggingface.co/datasets/FinanceMTEB/WikiCompany2Industry-en) (translated using GPT-4o).
