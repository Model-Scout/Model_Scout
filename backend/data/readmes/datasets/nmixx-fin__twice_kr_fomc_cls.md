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
    num_bytes: 227661
    num_examples: 1000
  download_size: 108619
  dataset_size: 227661
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
pretty_name: FOMC-CLS-ko
size_categories:
- 1K<n<10K
---

## FOMC-CLS-ko

- Selected Korean financial news articles that contain the keywords [interest rate, hawkish, dovish].
- Classified news sentences into **Hawkish/Dovish/Neutral** categories.