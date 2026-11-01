---
language:
- ko
license: apache-2.0
task_categories:
- multiple-choice
tags:
- Computer Proficiency Test Level 2
- computer proficiency Test
dataset_info:
  features:
  - name: subject
    dtype: string
  - name: subsection
    dtype: string
  - name: question
    dtype: string
  - name: choices
    dtype: string
  - name: user_input
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 389316
    num_examples: 738
  - name: test
    num_bytes: 93611
    num_examples: 185
  download_size: 213533
  dataset_size: 482927
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
---
