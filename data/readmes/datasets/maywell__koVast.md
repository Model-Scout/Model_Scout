---
license: mit
dataset_info:
  features:
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  splits:
  - name: train
    num_bytes: 1047538413
    num_examples: 684579
  download_size: 470686367
  dataset_size: 1047538413
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# **Massive Korean Multi-Turn Dataset**

## Note

형식에 bias 많음

## Thanks to

- A100 클러스터를 제공해주신, [Sionic AI](https://sionic.ai/)

## Contact
- [Discord Server Link](https://discord.gg/MrBt3PXdXc)