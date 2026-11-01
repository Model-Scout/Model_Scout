---
dataset_info:
  features:
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  splits:
  - name: train
    num_bytes: 1194681369.55
    num_examples: 9965
  download_size: 1192766900
  dataset_size: 1194681369.55
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: cc-by-4.0
language:
- ko
---