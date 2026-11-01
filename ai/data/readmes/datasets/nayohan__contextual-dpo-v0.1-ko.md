---
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: prompt
    dtype: string
  - name: rejected
    dtype: string
  - name: chosen
    dtype: string
  splits:
  - name: train
    num_bytes: 4420032
    num_examples: 1365
  download_size: 2321618
  dataset_size: 4420032
language:
- ko
tags:
- DPO
license: cc-by-4.0
---
# Dataset Card for "contextual-dpo-v0.1-ko"

Translated [jondurbin/contextual-dpo-v0.1](https://huggingface.co/datasets/jondurbin/contextual-dpo-v0.1) using [nayohan/llama3-instrucTrans-enko-8b](https://huggingface.co/nayohan/llama3-instrucTrans-enko-8b).