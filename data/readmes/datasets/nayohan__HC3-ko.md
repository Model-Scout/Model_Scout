---
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: question
    dtype: string
  - name: human_answers
    dtype: string
  - name: chatgpt_answers
    dtype: string
  - name: id
    dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 93921066
    num_examples: 24322
  download_size: 42075776
  dataset_size: 93921066
license: cc-by-sa-4.0
task_categories:
- question-answering
- text-generation
language:
- ko
tags:
- ChatGPT
- DPO
- ko
---
# Dataset Card for "HC3"

Translated [Hello-SimpleAI/HC3](https://huggingface.co/datasets/Hello-SimpleAI/HC3) using [nayohan/llama3-instrucTrans-enko-8b](https://huggingface.co/nayohan/llama3-instrucTrans-enko-8b).