---
language:
- ko
size_categories:
- n<1K
task_categories:
- text-generation
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 915115
    num_examples: 700
  download_size: 494274
  dataset_size: 915115
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
tags:
- finance
---
