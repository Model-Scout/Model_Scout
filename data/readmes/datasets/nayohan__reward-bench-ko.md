---
language:
- ko
license: odc-by
task_categories:
- question-answering
configs:
- config_name: default
  data_files:
  - split: raw
    path: data/raw-*
  - split: filtered
    path: data/filtered-*
dataset_info:
  features:
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: chosen_model
    dtype: string
  - name: rejected_model
    dtype: string
  - name: subset
    dtype: string
  - name: id
    dtype: int64
  splits:
  - name: raw
    num_bytes: 13464295
    num_examples: 5123
  - name: filtered
    num_bytes: 6025206
    num_examples: 2985
  download_size: 8487367
  dataset_size: 19489501
tags:
- DPO
- ko
---
# Dataset Card for "reward-bench"

Translated [allenai/reward-bench](https://huggingface.co/datasets/allenai/reward-bench) using [nayohan/llama3-instrucTrans-enko-8b](https://huggingface.co/nayohan/llama3-instrucTrans-enko-8b).