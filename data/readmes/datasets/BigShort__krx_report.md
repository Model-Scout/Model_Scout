---
language:
- ko
size_categories:
- 1K<n<10K
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
    num_bytes: 1051558
    num_examples: 3826
  download_size: 463515
  dataset_size: 1051558
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
tags:
- finance
---
