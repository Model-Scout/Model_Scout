---
language:
- ko
task_categories:
- text-generation
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: text
    dtype: string
  - name: diagnosis
    dtype: string
  - name: solutions
    dtype: string
  - name: id
    dtype: int64
  - name: entities
    dtype: string
  - name: relations
    dtype: string
  splits:
  - name: train
    num_bytes: 794478
    num_examples: 476
  download_size: 268665
  dataset_size: 794478
tags:
- security
---
# Dataset Card for "cyber-threat-intelligence-custom-data"

Translated [swaption2009/cyber-threat-intelligence-custom-data](https://huggingface.co/datasets/swaption2009/cyber-threat-intelligence-custom-data) using [nayohan/llama3-instrucTrans-enko-8b](https://huggingface.co/nayohan/llama3-instrucTrans-enko-8b).