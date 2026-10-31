---
dataset_info:
  config_name: Table
  features:
  - name: id
    dtype: int32
  - name: image
    dtype: image
  - name: metadata
    struct:
    - name: ori_html
      dtype: string
    - name: sim_html
      dtype: string
    - name: row_num
      dtype: int32
    - name: col_num
      dtype: int32
  splits:
  - name: train
    num_bytes: 16094498357
    num_examples: 303600
  download_size: 8882804633
  dataset_size: 16094498357
configs:
- config_name: Table
  data_files:
  - split: train
    path: Table/train-*
task_categories:
- table-question-answering
- table-to-text
- image-to-text
language:
- ko
---