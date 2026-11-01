---
dataset_info:
  features:
  - name: topic
    dtype: string
  - name: origin_language
    dtype: string
  - name: target_language
    dtype: string
  - name: system
    dtype: string
  - name: input
    dtype: string
  - name: chosen_model
    dtype: string
  - name: rejected_model
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: score_chosen
    dtype: int64
  - name: score_rejected
    dtype: int64
  - name: input_length
    dtype: int64
  - name: chosen_length
    dtype: int64
  - name: rejected_length
    dtype: int64
  splits:
  - name: train
    num_bytes: 48882856
    num_examples: 25298
  download_size: 20698962
  dataset_size: 48882856
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: mit
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
---
