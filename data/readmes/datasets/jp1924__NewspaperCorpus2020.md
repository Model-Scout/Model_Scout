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
    - name: author
      dtype: string
    - name: publisher
      dtype: string
    - name: date
      dtype: string
    - name: topic
      dtype: string
    - name: original_topic
      dtype: string
  - name: category
    dtype: string
  splits:
  - name: train
    num_bytes: 3036966682
    num_examples: 580152
  download_size: 1770990181
  dataset_size: 3036966682
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