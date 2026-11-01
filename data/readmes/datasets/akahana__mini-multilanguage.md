---
dataset_info:
- config_name: arab
  features:
  - name: text
    dtype: string
  - name: timestamp
    dtype: string
  - name: url
    dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 4151742409
    num_examples: 740280
  download_size: 2036463403
  dataset_size: 4151742409
- config_name: english
  features:
  - name: text
    dtype: string
  - name: timestamp
    dtype: string
  - name: url
    dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 629329515
    num_examples: 232514
  download_size: 352662109
  dataset_size: 629329515
- config_name: indonesia
  features:
  - name: text
    dtype: string
  - name: timestamp
    dtype: string
  - name: url
    dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 629329515
    num_examples: 232514
  download_size: 352662109
  dataset_size: 629329515
- config_name: japan
  features:
  - name: text
    dtype: string
  - name: timestamp
    dtype: string
  - name: url
    dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 5175409022
    num_examples: 1111885
  download_size: 2916915073
  dataset_size: 5175409022
- config_name: korea
  features:
  - name: text
    dtype: string
  - name: timestamp
    dtype: string
  - name: url
    dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 1080491739
    num_examples: 205573
  download_size: 640051446
  dataset_size: 1080491739
- config_name: malaysia
  features:
  - name: text
    dtype: string
  - name: timestamp
    dtype: string
  - name: url
    dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 3568236
    num_examples: 2382
  download_size: 1955952
  dataset_size: 3568236
configs:
- config_name: arab
  data_files:
  - split: train
    path: arab/train-*
- config_name: english
  data_files:
  - split: train
    path: english/train-*
- config_name: indonesia
  data_files:
  - split: train
    path: indonesia/train-*
- config_name: japan
  data_files:
  - split: train
    path: japan/train-*
- config_name: korea
  data_files:
  - split: train
    path: korea/train-*
- config_name: malaysia
  data_files:
  - split: train
    path: malaysia/train-*
language:
- id
- ar
- ko
- en
- ja
- ms
---