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
    num_bytes: 260593
    num_examples: 1000
  download_size: 141453
  dataset_size: 260593
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
pretty_name: ESG-CLS-ko
size_categories:
- 1K<n<10K
license: cc-by-nc-sa-4.0
---

## ESG-CLS-ko
- Selected **Korean financial news articles** that contain the keyword **[ESG]**.
- Classified financial news sentences into **E (Environmental) /S (Social) / G (Governance)/ Non-ESG** categories.
