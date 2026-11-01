---
dataset_info:
  features:
  - name: inputs
    dtype: string
  - name: answer
    dtype: string
  - name: system_prompt
    dtype: string
  - name: user_prompt
    dtype: string
  - name: 'Unnamed: 0'
    dtype: int64
  - name: task_type
    dtype: string
  - name: dataset
    dtype: string
  splits:
  - name: train
    num_bytes: 385855965
    num_examples: 177597
  download_size: 109003560
  dataset_size: 385855965
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: apache-2.0
task_categories:
- question-answering
- text-generation
language:
- ko
tags:
- finance
- ko
---

Translated [sujet-ai/Sujet-Finance-Instruct-177k](https://huggingface.co/datasets/sujet-ai/Sujet-Finance-Instruct-177k) using [nayohan/llama3-instrucTrans-enko-8b](https://huggingface.co/nayohan/llama3-instrucTrans-enko-8b).

It may contain repetitive sentences, so recommend filtering them.