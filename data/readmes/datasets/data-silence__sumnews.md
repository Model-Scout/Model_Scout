---
language:
- am
- ar
- az
- bn
- my
- zh
- en
- fr
- gu
- ha
- hi
- ig
- id
- ja
- rn
- ko
- ky
- mr
- ne
- om
- ps
- fa
- pcm
- pt
- pa
- ru
- gd
- sr
- si
- so
- es
- sw
- ta
- te
- th
- ti
- tr
- uk
- ur
- uz
- vi
- cy
- yo
license:
- cc-by-nc-sa-4.0
multilinguality:
- multilingual
size_categories:
- 100K<n<1M
task_categories:
- summarization
- text-generation
pretty_name: sum-any-news-dataset
dataset_info:
  features:
  - name: title
    dtype: string
  - name: resume
    dtype: string
  - name: news
    dtype: string
  splits:
  - name: train
    num_bytes: 1276733873
    num_examples: 289524
  - name: test
    num_bytes: 143098117
    num_examples: 32173
  download_size: 742417882
  dataset_size: 1419831990
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
tags:
- news
- media
- conditional-text-generation
---

# Dataset Card for "Sum-any-news"

## Dataset Description

This dataset is a set for fine-tuning the summarization task on the “google/mt5-base” model and its derivatives. 
The set is based on the well-known dataset [“csebuetnlp/xlsum”](https://huggingface.co/datasets/csebuetnlp/xlsum), but is a limited 20,000 examples of news articles from it. 
In addition, about 20 thousand news articles in Russian for the period from 2019-01-01 to 2024-08-01 have been added to the model (multiple sources).