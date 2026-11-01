---
pretty_name: ROPES
language:
- ko
license:
- cc-by-4.0
size_categories:
- 10K<n<100K
task_categories:
- question-answering
task_ids:
- extractive-qa
dataset_info:
  features:
  - name: data_index_by_user
    dtype: int32
  - name: background
    dtype: string
  - name: situation
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: text
      dtype: string
  splits:
  - name: train
    num_bytes: 13608462
    num_examples: 10924
  - name: validation
    num_bytes: 1864822
    num_examples: 1688
  - name: test
    num_bytes: 2158508
    num_examples: 1710
  download_size: 1465973
  dataset_size: 17631792
---

# Dataset Card for ROPES

## Licensing Information

The data is distributed under the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.

## Source Data Citation INformation

```
@inproceedings{Lin2019ReasoningOP,
  title={Reasoning Over Paragraph Effects in Situations},
  author={Kevin Lin and Oyvind Tafjord and Peter Clark and Matt Gardner},
  booktitle={MRQA@EMNLP},
  year={2019}
}