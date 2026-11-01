---
pretty_name: WebQuestions
license:
- cc-by-4.0
language:
- ko
size_categories:
- 1K<n<10K
task_categories:
- question-answering
task_ids:
- open-domain-qa
dataset_info:
  features:
  - name: url
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence: string
  - name: data_index_by_user
    dtype: int32
  splits:
  - name: train
    num_bytes: 622410
    num_examples: 3778
  - name: test
    num_bytes: 337300
    num_examples: 2032
  download_size: 486333
  dataset_size: 959710
---
# Dataset Card for WEB_QUESTIONS
## Licensing Information
The data is distributed under the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.
## Source Data Citation INformation
```
@inproceedings{berant-etal-2013-semantic,
    title = "Semantic Parsing on {F}reebase from Question-Answer Pairs",
    author = "Berant, Jonathan  and
      Chou, Andrew  and
      Frostig, Roy  and
      Liang, Percy",
    booktitle = "Proceedings of the 2013 Conference on Empirical Methods in Natural Language Processing",
    month = oct,
    year = "2013",
    address = "Seattle, Washington, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/D13-1160",
    pages = "1533--1544",
}