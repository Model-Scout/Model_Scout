---
language:
- ko
license:
- mit
multilinguality:
- monolingual
size_categories:
- 10K<n<1M
source_datasets:
- original
task_categories:
- question-answering
- text2text-generation
task_ids:
- abstractive-qa
- extractive-qa
paperswithcode_id: duorc
pretty_name: DuoRC
dataset_info:
  features:
  - name: plot_id
    dtype: string
  - name: plot
    dtype: string
  - name: title
    dtype: string
  - name: question_id
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence: string
  - name: data_index_by_user
    dtype: int32
  - name: no_answer
    dtype: bool
  splits:
  - name: ParaphraseRC_train
    num_bytes: 602587402
    num_examples: 69524
  - name: ParaphraseRC_validation
    num_bytes: 128698408
    num_examples: 15591
  - name: ParaphraseRC_test
    num_bytes: 140358453
    num_examples: 15857
  - name: SelfRC_train
    num_bytes: 288548501
    num_examples: 60721
  - name: SelfRC_validation
    num_bytes: 62171721
    num_examples: 12961
  - name: SelfRC_test
    num_bytes: 59196683
    num_examples: 12559
  download_size: 67341464
  dataset_size: 1281561168
---

# Dataset Card for duorc

## Licensing Information

[MIT License](https://github.com/duorc/duorc/blob/master/LICENSE)

## Source Data Citation Information

```
@inproceedings{DuoRC,
author = { Amrita Saha and Rahul Aralikatte and Mitesh M. Khapra and Karthik Sankaranarayanan},
title = {{DuoRC: Towards Complex Language Understanding with Paraphrased Reading Comprehension}},
booktitle = {Meeting of the Association for Computational Linguistics (ACL)},
year = {2018}
}
```