---
license: apache-2.0
configs:
- config_name: default
  data_files:
  - split: dev
    path: data/dev-*
  - split: test
    path: data/test-*
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: event_date
    dtype: timestamp[s]
  - name: sitename
    dtype: string
  - name: gold_label
    dtype: string
  - name: url
    dtype: string
  - name: language
    dtype: string
  - name: event_id_in_acled
    dtype: string
  - name: event_type
    dtype: string
  splits:
  - name: dev
    num_bytes: 3692964
    num_examples: 9185
  - name: test
    num_bytes: 3696829
    num_examples: 9185
  - name: train
    num_bytes: 9021685
    num_examples: 21416
  download_size: 5670794
  dataset_size: 16411478
task_categories:
- text-classification
- text-generation
language:
- en
- es
- ar
- fr
- it
- ru
- de
- tr
- my
- id
- uk
- ko
- pt
- nl
- so
- ne
- zh
- fa
- he
- ja
size_categories:
- 10K<n<100K
---


LEMONADE is a large, expert-annotated dataset for event extraction from news articles in 20 languages: English, Spanish, Arabic, French, Italian, Russian, German, Turkish, Burmese, Indonesian, Ukrainian, Korean, Portuguese, Dutch, Somali, Nepali, Chinese, Persian, Hebrew, and Japanese.

See https://github.com/stanford-oval/Lemonade for details.