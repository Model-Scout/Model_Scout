---
dataset_info:
  features:
  - name: problem
    dtype: string
  - name: answer
    dtype: string
  - name: original
    dtype: string
  splits:
  - name: train
    num_bytes: 22480298
    num_examples: 40315
  download_size: 11655703
  dataset_size: 22480298
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
task_categories:
- text-generation
language:
- ko
- en
tags:
- math
---