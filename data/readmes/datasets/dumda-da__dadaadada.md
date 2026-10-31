---
language:
- ko
dataset_info:
  features:
  - name: audiofile
    dtype:
      audio:
        sampling_rate: 16000
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 24089.0
    num_examples: 1
  download_size: 25425
  dataset_size: 24089.0
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
