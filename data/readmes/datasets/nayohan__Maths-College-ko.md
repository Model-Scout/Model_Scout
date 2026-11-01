---
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 292028782
    num_examples: 48499
  download_size: 124837493
  dataset_size: 292028782
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: apache-2.0
task_categories:
- question-answering
language:
- ko
tags:
- math
- ko
---

Translated 5% [ajibawa-2023/Maths-College](https://huggingface.co/datasets/ajibawa-2023/Maths-College) using [nayohan/llama3-instrucTrans-enko-8b](https://huggingface.co/nayohan/llama3-instrucTrans-enko-8b).