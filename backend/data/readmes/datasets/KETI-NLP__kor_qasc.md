---
language:
- ko
size_categories:
- 1K<n<10K
task_categories:
- question-answering
- multiple-choice
task_ids:
- extractive-qa
- multiple-choice-qa
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
  - name: fact1
    dtype: string
  - name: fact2
    dtype: string
  - name: combinedfact
    dtype: string
  - name: formatted_question
    dtype: string
  splits:
  - name: train
    num_bytes: 5345733
    num_examples: 8134
  - name: validation
    num_bytes: 600701
    num_examples: 926
  - name: test
    num_bytes: 404309
    num_examples: 920
  download_size: 2385940
  dataset_size: 6350743
---

# Dataset Card for QASC

## Licensing Information

The data is distributed under the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.

## Source Data Citation INformation

```
@article{allenai:qasc,
      author    = {Tushar Khot and Peter Clark and Michal Guerquin and Peter Jansen and Ashish Sabharwal},
      title     = {QASC: A Dataset for Question Answering via Sentence Composition},
      journal   = {arXiv:1910.11473v2},
      year      = {2020},
}
```