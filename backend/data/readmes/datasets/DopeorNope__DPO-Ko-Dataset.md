---
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
dataset_info:
  features:
  - name: question
    dtype: string
  - name: response_j
    dtype: string
  - name: response_k
    dtype: string
  splits:
  - name: train
    num_bytes: 693824
    num_examples: 4076
  - name: validation
    num_bytes: 84542
    num_examples: 500
  download_size: 0
  dataset_size: 778366
---
# Dataset Card for "DPO-Ko-Dataset"

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)