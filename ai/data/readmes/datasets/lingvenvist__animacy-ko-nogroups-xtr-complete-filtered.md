---
dataset_info:
  features:
  - name: sentences
    dtype: string
  - name: tokens
    sequence: string
  - name: anim_tags
    sequence:
      class_label:
        names:
          '0': 'N'
          '1': A
          '2': H
  - name: target-indexes
    sequence: int64
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 376505
    num_examples: 3405
  - name: test
    num_bytes: 74010
    num_examples: 681
  - name: validation
    num_bytes: 49764
    num_examples: 454
  download_size: 241496
  dataset_size: 500279
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
  - split: validation
    path: data/validation-*
language:
- ko
---
Note that this is a processed version of XL-WSD v1 downloaded from https://sapienzanlp.github.io/xl-wsd/, made available with the XL-WSD license (see https://sapienzanlp.github.io/xl-wsd/docs/license).