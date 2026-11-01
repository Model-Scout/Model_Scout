---
language:
- ko
dataset_info:
  features:
  - name: id
    dtype: string
  - name: context
    dtype: string
  - name: title
    dtype: string
  - name: question_answer
    list:
    - name: id
      dtype: string
    - name: is_impossible
      dtype: bool
    - name: question
      dtype: string
    - name: answer
      dtype: string
    - name: answer_start
      dtype: int32
  - name: metadata
    struct:
    - name: doc_id
      dtype: string
    - name: doc_title
      dtype: string
    - name: doc_source
      dtype: string
    - name: doc_published
      dtype: int32
    - name: created
      dtype: string
    - name: class
      dtype: string
    - name: code
      dtype: string
  splits:
  - name: train
    num_bytes: 444099171
    num_examples: 160000
  - name: validation
    num_bytes: 56060671
    num_examples: 20000
  download_size: 227286043
  dataset_size: 500159842
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
task_categories:
- table-question-answering
---