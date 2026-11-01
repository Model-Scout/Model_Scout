---
dataset_info:
- config_name: default
  features:
  - name: id
    dtype: int64
  - name: topic
    dtype: string
  - name: origin_language
    dtype: string
  - name: target_language
    dtype: string
  - name: system
    dtype: string
  - name: origin_text
    dtype: string
  - name: translated_text
    dtype: string
  - name: model_name
    dtype: string
  - name: origin_length
    dtype: int64
  - name: trans_length
    dtype: int64
  splits:
  - name: train
    num_bytes: 68709919
    num_examples: 60519
  - name: test
    num_bytes: 1496108
    num_examples: 1000
  download_size: 30194319
  dataset_size: 70206027
- config_name: flores200
  features:
  - name: id
    dtype: int64
  - name: topic
    dtype: string
  - name: origin_language
    dtype: string
  - name: target_language
    dtype: string
  - name: system
    dtype: string
  - name: origin_text
    dtype: string
  - name: translated_text
    dtype: string
  - name: model_name
    dtype: string
  - name: origin_length
    dtype: int64
  - name: trans_length
    dtype: int64
  splits:
  - name: train
    num_bytes: 3786588481
    num_examples: 7598038
  download_size: 1795337936
  dataset_size: 3786588481
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
- config_name: flores200
  data_files:
  - split: train
    path: flores200/train-*
task_categories:
- translation
language:
- ko
- en
- zh
- zh
- zu
- ja
- am
- ar
- es
- fr
- ru
- de
- it
- pt
- nl
- sv
- tr
- id
- vi
- pl
- cs
- ro
- uk
- hu
- sl
- el
- fi
- 'no'
- da
- bg
- hi
- he
- ms
- ta
- te
- pa
- bn
- fa
- sw
- th
- sr
- hr
- ca
- is
- lv
- lt
- sk
- et
- mn
- la
- my
- tl
- jv
- mr
- gu
- ps
- sd
- kn
- ml
- ha
- yo
- ig
- ber
license: mit
---