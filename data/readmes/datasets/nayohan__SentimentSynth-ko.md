---
language:
- ko
license: apache-2.0
task_categories:
- question-answering
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: rejected
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  splits:
  - name: train
    num_bytes: 6760515
    num_examples: 5300
  download_size: 2823557
  dataset_size: 6760515
tags:
- DPO
- ko
---
# Dataset Card for "SentimentSynth"

Translated [OEvortex/SentimentSynth](https://huggingface.co/datasets/OEvortex/SentimentSynth) using [nayohan/llama3-instrucTrans-enko-8b](https://huggingface.co/nayohan/llama3-instrucTrans-enko-8b).