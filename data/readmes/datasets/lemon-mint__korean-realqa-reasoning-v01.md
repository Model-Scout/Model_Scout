---
dataset_info:
  features:
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 25138907
    num_examples: 7768
  download_size: 14054082
  dataset_size: 25138907
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: cc-by-sa-4.0
language:
- ko
---

https://huggingface.co/datasets/beomi/KoAlpaca-RealQA