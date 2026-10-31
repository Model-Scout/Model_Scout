---
language:
- ko
license: cc0-1.0
size_categories:
- 1M<n<10M
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- sentiment-classification
dataset_info:
  features:
    - name: label
      dtype:
        class_label:
          names:
            '0': negative
            '1': positive
    - name: title
      dtype: string
    - name: content
      dtype: string
    - name: data_index_by_user
      dtype: int32
  splits:
    - name: train
      num_bytes: 2059069183
      num_examples: 3600000
    - name: test
      num_bytes: 228905323
      num_examples: 400000
  download_size: 1298504656
  dataset_size: 2287974506
---

# Dataset Card for amazon_polarity

## Licensing Information

The data is distributed under the [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) license.

## Source Data Citation Information

McAuley, Julian, and Jure Leskovec. "Hidden factors and hidden topics: understanding rating dimensions with review text." In Proceedings of the 7th ACM conference on Recommender systems, pp. 165-172. 2013.

Xiang Zhang, Junbo Zhao, Yann LeCun. Character-level Convolutional Networks for Text Classification. Advances in Neural Information Processing Systems 28 (NIPS 2015)
