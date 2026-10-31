---
license: mit
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: response
    dtype: string
  - name: root
    dtype: string
  - name: reference
    dtype: string
  splits:
  - name: train
    num_bytes: 3833183
    num_examples: 2042
  download_size: 1971543
  dataset_size: 3833183
task_categories:
- question-answering
language:
- ko
size_categories:
- 1K<n<10K
---

This Dataset is created from https://huggingface.co/datasets/joonavel/seed_for_evolving by applying Auto-Evol-instruct(https://github.com/joonavel/auto-evol-instruct)