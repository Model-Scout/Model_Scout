---
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: output
    dtype: string
  - name: input
    dtype: string
  splits:
  - name: train
    num_bytes: 114301314
    num_examples: 900000
  download_size: 42379819
  dataset_size: 114301314
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
pretty_name: aihub_도서자료 기계독해
tags:
- Aihub
- 한국지능정보사회진흥원
---