---
dataset_info:
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: original
    dtype: string
  - name: original_answer
    dtype: string
  - name: category
    dtype: string
  - name: difficulty
    dtype: string
  splits:
  - name: KMS
    num_bytes: 56247.00420168067
    num_examples: 82
  - name: KJMO
    num_bytes: 42528.22268907563
    num_examples: 62
  - name: KMO
    num_bytes: 500735.52521008404
    num_examples: 730
  - name: TQ
    num_bytes: 235963.04201680672
    num_examples: 344
  - name: CSAT
    num_bytes: 144047.20588235295
    num_examples: 210
  download_size: 461632
  dataset_size: 979521
configs:
- config_name: default
  data_files:
  - split: KMS
    path: data/KMS-*
  - split: KJMO
    path: data/KJMO-*
  - split: KMO
    path: data/KMO-*
  - split: TQ
    path: data/TQ-*
  - split: CSAT
    path: data/CSAT-*
license: mit
language:
- ko
- en
---
- Original Dataset: [HAERAE-HUB/HRM8K](https://huggingface.co/datasets/HAERAE-HUB/HRM8K)
- 평가를 위해 KSM subset만 가져와서 분리했음.