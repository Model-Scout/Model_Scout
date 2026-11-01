---
dataset_info:
  features:
  - name: text
    dtype: string
  - name: label_text
    dtype: string
  - name: label
    dtype: int64
  splits:
  - name: train
    num_bytes: 743519
    num_examples: 1000
  download_size: 397667
  dataset_size: 743519
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
tags:
- finance
pretty_name: Industry-CLS-ko
size_categories:
- 1K<n<10K
---


## Industry-CLS-ko
- A task to **classify sentences from Korean industry analysis reports** into different industry sectors.
- There are 10 industry labels: ['Construction', 'Semiconductors', 'Petrochemicals', 'Retail', 'Banking', 'Food & Beverage', 'Automobile', 'Shipbuilding', 'Steel & Metals', 'Telecommunications'].

