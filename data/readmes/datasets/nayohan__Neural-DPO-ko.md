---
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: system
    dtype: string
  - name: question
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  splits:
  - name: train
    num_bytes: 715239
    num_examples: 1068
  download_size: 303957
  dataset_size: 715239
license: apache-2.0
task_categories:
- question-answering
language:
- ko
tags:
- DPO
- ko
---
# Dataset Card for "Neural-DPO"

Translated [NeuralNovel/Neural-DPO](https://huggingface.co/datasets/NeuralNovel/Neural-DPO) using [nayohan/llama3-instrucTrans-enko-8b](https://huggingface.co/nayohan/llama3-instrucTrans-enko-8b).
