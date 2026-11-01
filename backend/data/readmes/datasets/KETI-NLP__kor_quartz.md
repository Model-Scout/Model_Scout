---
language:
- ko
license: cc-by-4.0
dataset_info:
  features:
  - name: data_index_by_user
    dtype: int32
  - name: question
    dtype: string
  - name: choices
    struct:
    - name: text
      sequence: string
    - name: label
      sequence: string
  - name: answerKey
    dtype: string
  - name: para
    dtype: string
  - name: para_id
    dtype: string
  - name: para_anno
    struct:
    - name: effect_prop
      dtype: string
    - name: cause_dir_str
      dtype: string
    - name: effect_dir_str
      dtype: string
    - name: cause_dir_sign
      dtype: string
    - name: effect_dir_sign
      dtype: string
    - name: cause_prop
      dtype: string
  - name: question_anno
    struct:
    - name: more_effect_dir
      dtype: string
    - name: less_effect_dir
      dtype: string
    - name: less_cause_prop
      dtype: string
    - name: more_effect_prop
      dtype: string
    - name: less_effect_prop
      dtype: string
    - name: less_cause_dir
      dtype: string
  splits:
  - name: train
    num_bytes: 1326969
    num_examples: 2696
  - name: validation
    num_bytes: 192332
    num_examples: 384
  - name: test
    num_bytes: 385569
    num_examples: 784
  download_size: 618394
  dataset_size: 1904870
---
# Dataset Card for quartz

## Licensing Information

The data is distributed under the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.

## Source Data Citation Information

```
@InProceedings{quartz,
  author = {Oyvind Tafjord and Matt Gardner and Kevin Lin and Peter Clark},
  title = {"QUARTZ: An Open-Domain Dataset of Qualitative Relationship
Questions"},
  year = {"2019"},
}