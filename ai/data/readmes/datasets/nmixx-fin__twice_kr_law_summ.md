---
dataset_info:
  features:
  - name: sentence
    dtype: string
  - name: summary
    dtype: string
  - name: label
    dtype: int64
  splits:
  - name: train
    num_bytes: 2909290
    num_examples: 1000
  download_size: 1460225
  dataset_size: 2909290
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
task_categories:
- summarization
language:
- ko
tags:
- finance
pretty_name: Law-Summ-ko
size_categories:
- 1K<n<10K
license: cc-by-nc-sa-4.0
---

## Law-Summ-ko
- A task to verify whether the **long-text summary** of **Korean legal documents** is correct.  
- Labeled as **1** if correct, otherwise **0**.
