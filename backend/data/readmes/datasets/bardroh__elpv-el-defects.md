---
dataset_info:
  features:
  - name: image
    dtype: image
  - name: label
    dtype:
      class_label:
        names:
          '0': ok
          '1': defect
  - name: label4
    dtype: string
  splits:
  - name: train
    num_bytes: 63790202
    num_examples: 1846
  - name: validation
    num_bytes: 9121981
    num_examples: 266
  - name: test
    num_bytes: 17440189
    num_examples: 512
  download_size: 90297010
  dataset_size: 90352372
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
- en
license: cc-by-nc-sa-4.0
task_categories:
- image-classification
pretty_name: ELPV solar cell EL — defect classification
tags:
- solar-cell
- electroluminescence
- defect-detection
- education
---
