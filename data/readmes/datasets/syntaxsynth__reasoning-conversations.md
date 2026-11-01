---
dataset_info:
- config_name: deepseek-v3-r1
  features:
  - name: src
    dtype: string
  - name: hash_id
    dtype: string
  - name: instruction
    dtype: string
  - name: response
    dtype: string
  - name: reasoning
    dtype: string
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 347948855
    num_examples: 20716
  download_size: 179894124
  dataset_size: 347948855
- config_name: deepseek-v3-r1-zero
  features:
  - name: src
    dtype: string
  - name: hash_id
    dtype: string
  - name: instruction
    dtype: string
  - name: response
    dtype: string
  - name: reasoning
    dtype: string
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 232445146
    num_examples: 16251
  download_size: 106018510
  dataset_size: 232445146
configs:
- config_name: deepseek-v3-r1
  data_files:
  - split: train
    path: deepseek-v3-r1/train-*
- config_name: deepseek-v3-r1-zero
  data_files:
  - split: train
    path: deepseek-v3-r1-zero/train-*
license: mit
task_categories:
- text2text-generation
language:
- en
- es
- ko
- de
- ja
- fr
- zh
tags:
- reasoning
- deepseek-r1
- deepseek-r1-zero
- deepseek-zero
---
# Multilingual Reasoning Dataset


* Include languages from German, Korean, Spanish, Japanese, French, Simplified Chinese, Traditional Chinese

* Reasoning traces from Deepseek-v3-R1, Deepseek-v3-R1-Zero



Credits sponsored by [Currents API](https://currentsapi.services/)

