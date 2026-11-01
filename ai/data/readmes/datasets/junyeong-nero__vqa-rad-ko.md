---
dataset_info:
  features:
  - name: image
    dtype: image
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: question_ko
    dtype: string
  - name: answer_ko
    dtype: string
  splits:
  - name: train
    num_bytes: 95350706.976
    num_examples: 1793
  - name: test
    num_bytes: 23850090
    num_examples: 451
  download_size: 55042498
  dataset_size: 119200796.976
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
license: apache-2.0
task_categories:
- image-to-text
language:
- ko
tags:
- medical
size_categories:
- 1K<n<10K
---