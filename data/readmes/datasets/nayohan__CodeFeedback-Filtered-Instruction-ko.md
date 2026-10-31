---
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: query
    dtype: string
  - name: answer
    dtype: string
  - name: resource
    dtype: string
  - name: lang
    dtype: string
  splits:
  - name: train
    num_bytes: 394762941
    num_examples: 156526
  download_size: 183779812
  dataset_size: 394762941
language:
- ko
tags:
- code
---
# Dataset Card for "CodeFeedback-Filtered-Instruction-ko"

Translated [m-a-p/CodeFeedback-Filtered-Instruction](https://huggingface.co/datasets/m-a-p/CodeFeedback-Filtered-Instruction) using [nayohan/llama3-instrucTrans-enko-8b](https://huggingface.co/nayohan/llama3-instrucTrans-enko-8b).
