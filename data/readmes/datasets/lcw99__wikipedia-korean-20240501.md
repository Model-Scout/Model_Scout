---
language:
- ko
license: apache-2.0
dataset_info:
  features:
  - name: title
    dtype: string
  - name: section_titles
    sequence: string
  - name: section_texts
    sequence: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3197179083
    num_examples: 515425
  download_size: 1750758987
  dataset_size: 3197179083
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

wikipedia Korean 2024.5.1 cut