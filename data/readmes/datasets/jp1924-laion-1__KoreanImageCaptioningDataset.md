---
dataset_info:
  features:
  - name: id
    dtype: int32
  - name: image
    dtype: image
  - name: caption
    dtype: string
  - name: caption_ls
    list: string
  - name: category
    dtype: string
  - name: filepath
    dtype: string
  - name: sentids
    list: int32
  - name: filename
    dtype: string
  - name: split
    dtype: string
  - name: sentences_tokens
    list:
      list: string
  - name: en_sentences_raw
    list: string
  - name: sentences_sentid
    list: int32
  - name: cocoid
    dtype: int32
  splits:
  - name: train
    num_bytes: 18640275938.125
    num_examples: 113287
  - name: validation
    num_bytes: 819179714
    num_examples: 5000
  - name: test
    num_bytes: 826633941
    num_examples: 5000
  download_size: 20164806114
  dataset_size: 20286089593.125
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
  - split: test
    path: data/test-*
language:
- ko
---