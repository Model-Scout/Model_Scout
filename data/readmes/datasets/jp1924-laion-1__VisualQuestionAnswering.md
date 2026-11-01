---
language:
- ko
size_categories:
- 10B<n<100B
task_categories:
- visual-question-answering
dataset_info:
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: category
    dtype: string
  - name: question_answer
    list:
    - name: id
      dtype: string
    - name: question
      dtype: string
    - name: answer
      dtype: string
    - name: confidence
      dtype: bool
  splits:
  - name: train
    num_bytes: 66241679332.25
    num_examples: 715406
  - name: validation
    num_bytes: 26704475053.875
    num_examples: 318553
  download_size: 92636245075
  dataset_size: 92946154386.125
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
tags:
- Caption
- Image
---