---
dataset_info:
  features:
  - name: pubid
    dtype: int64
  - name: question
    dtype: string
  - name: context
    struct:
    - name: contexts
      sequence: string
    - name: labels
      sequence: string
    - name: meshes
      sequence: string
  - name: long_answer
    dtype: string
  - name: final_decision
    dtype: string
  - name: id
    dtype: string
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: answer
    dtype: string
  - name: answer_trans
    dtype: string
  splits:
  - name: train
    num_bytes: 138446062
    num_examples: 35579
  download_size: 72585370
  dataset_size: 138446062
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: mit
task_categories:
- question-answering
- translation
- text-generation
language:
- ko
- en
tags:
- medical
---