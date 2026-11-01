---
language:
- ko
task_categories:
- question-answering
task_ids:
- open-domain-qa
- extractive-qa
license: cc-by-sa-4.0
dataset_info:
  features:
  - name: data_index_by_user
    dtype: int32
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    struct:
    - name: text
      sequence: string
    - name: answer_start
      sequence: int32
  splits:
  - name: train
    num_bytes: 127009200
    num_examples: 130319
  - name: validation
    num_bytes: 12410838
    num_examples: 11873
  download_size: 19086608
  dataset_size: 139420038
---

# Dataset Card for squad_v2

## Licensing Information

The data is distributed under the [CC BY SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en) license.

## Source Data Citation Information

```
@article{2016arXiv160605250R,
       author = {{Rajpurkar}, Pranav and {Zhang}, Jian and {Lopyrev},
                 Konstantin and {Liang}, Percy},
        title = "{SQuAD: 100,000+ Questions for Machine Comprehension of Text}",
      journal = {arXiv e-prints},
         year = 2016,
          eid = {arXiv:1606.05250},
        pages = {arXiv:1606.05250},
archivePrefix = {arXiv},
       eprint = {1606.05250},
}