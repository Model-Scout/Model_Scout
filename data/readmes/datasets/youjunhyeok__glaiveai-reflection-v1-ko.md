---
language:
- ko
task_categories:
- text-generation
license: apache-2.0
dataset_info:
  features:
  - name: system
    dtype: string
  - name: prompt
    dtype: string
  - name: response
    dtype: string
  splits:
  - name: train
    num_bytes: 250919902
    num_examples: 52428
  download_size: 93193395
  dataset_size: 250919902
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
tags:
- instruction
- korean
size_categories:
- 100K<n<1M
---

Translated [glaiveai/reflection-v1](https://huggingface.co/datasets/glaiveai/reflection-v1) using [nayohan/llama3-instrucTrans-enko-8b](https://huggingface.co/nayohan/llama3-instrucTrans-enko-8b).

For this dataset, we only used data that is 5000 characters or less in length and has language of English.

Thanks for @Magpie-Align and @nayohan.