---
language:
- ko
dataset_info:
  features:
  - name: text
    dtype: string
  - name: label
    dtype: string
  splits:
  - name: train
    num_bytes: 542987
    num_examples: 5824
  download_size: 378576
  dataset_size: 542987
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
tags:
- safety
---

Reference: [https://github.com/2runo/Curse-detection-data](https://github.com/2runo/Curse-detection-data/tree/master)