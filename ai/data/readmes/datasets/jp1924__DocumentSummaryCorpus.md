---
dataset_info:
  features:
  - name: document_id
    dtype: string
  - name: corpus
    dtype: string
  - name: sentence_ls
    list: string
  - name: metadata
    struct:
    - name: title
      dtype: string
    - name: sub_title
      dtype: string
    - name: sub_class
      dtype: string
  - name: summary_sentences
    list: string
  - name: category
    dtype: string
  splits:
  - name: train
    num_bytes: 8360983
    num_examples: 4389
  download_size: 5533426
  dataset_size: 8360983
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
task_categories:
- text-generation
language:
- ko
---