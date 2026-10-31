---
language:
- ko
license:
- cc-by-4.0
pretty_name: QUAREL
dataset_info:
  features:
  - name: data_index_by_user
    dtype: int32
  - name: id
    dtype: string
  - name: answer_index
    dtype: int32
  - name: logical_forms
    sequence: string
  - name: logical_form_pretty
    dtype: string
  - name: world_literals
    struct:
    - name: world1
      sequence: string
    - name: world2
      sequence: string
  - name: question
    dtype: string
  splits:
  - name: train
    num_bytes: 1191886
    num_examples: 1941
  - name: validation
    num_bytes: 171905
    num_examples: 278
  - name: test
    num_bytes: 342838
    num_examples: 552
  download_size: 615579
  dataset_size: 1706629
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
  - split: test
    path: data/test-*
---
# Dataset Card for Quarel

## Licensing Information

The data is distributed under the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.

## Source Data Citation INformation

```
@inproceedings{quarel_v1,
    title={QuaRel: A Dataset and Models for Answering Questions about Qualitative Relationships},
    author={Oyvind Tafjord, Peter Clark, Matt Gardner, Wen-tau Yih, Ashish Sabharwal},
    year={2018},
    journal={arXiv:1805.05377v1}
}
```