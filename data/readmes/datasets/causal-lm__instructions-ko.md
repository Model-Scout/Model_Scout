---
language: ko
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  - name: dialogue
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 138160314
    num_examples: 112104
  - name: validation
    num_bytes: 15418231
    num_examples: 12429
  download_size: 85992704
  dataset_size: 153578545
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
---
# Dataset Card for "instructions-ko"

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)