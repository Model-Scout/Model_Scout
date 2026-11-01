---
dataset_info:
  features:
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 5457778
    num_examples: 6584
  download_size: 2783567
  dataset_size: 5457778
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: mit
task_categories:
- question-answering
language:
- ko
tags:
- math
---


hendrycks/math dataset을 한국어로 번역한 dataset 입니다.