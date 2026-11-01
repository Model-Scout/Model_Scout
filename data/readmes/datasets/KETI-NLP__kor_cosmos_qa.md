---
pretty_name: CosmosQA
language:
- ko
license:
- cc-by-4.0
size_categories:
- 10K<n<100K
dataset_info:
  features:
  - name: data_index_by_user
    dtype: int32
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answer0
    dtype: string
  - name: answer1
    dtype: string
  - name: answer2
    dtype: string
  - name: answer3
    dtype: string
  - name: label
    dtype: int32
  splits:
  - name: train
    num_bytes: 20787557
    num_examples: 25262
  - name: validation
    num_bytes: 2246371
    num_examples: 2985
  - name: test
    num_bytes: 6186162
    num_examples: 6963
  download_size: 11150870
  dataset_size: 29220090
---

# Dataset Card for cosmos_qa

## Licensing Information

The data is distributed under the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.

## Source Data Citation INformation

```
@inproceedings{huang-etal-2019-cosmos,
    title = "Cosmos {QA}: Machine Reading Comprehension with Contextual Commonsense Reasoning",
    author = "Huang, Lifu  and
      Le Bras, Ronan  and
      Bhagavatula, Chandra  and
      Choi, Yejin",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/D19-1243",
    doi = "10.18653/v1/D19-1243",
    pages = "2391--2401",
}
```