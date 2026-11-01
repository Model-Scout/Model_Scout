---
license: cc-by-4.0
configs:
- config_name: news
  data_files:
  - split: train
    path: news/train-*
- config_name: web
  data_files:
  - split: train
    path: web/train-*
- config_name: wiki
  data_files:
  - split: train
    path: wiki/train-*
dataset_info:
- config_name: news
  features:
  - name: id
    dtype: string
  - name: source
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 238345522
    num_examples: 80000
  download_size: 125873821
  dataset_size: 238345522
- config_name: web
  features:
  - name: id
    dtype: string
  - name: source
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 377221799
    num_examples: 80000
  download_size: 217408740
  dataset_size: 377221799
- config_name: wiki
  features:
  - name: id
    dtype: string
  - name: source
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 159395797
    num_examples: 80000
  download_size: 93549926
  dataset_size: 159395797
task_categories:
- text-generation
language:
- ko
size_categories:
- 100K<n<1M
---

# Lumia101/ko-perplexity-corpus

This dataset was created to measure the perplexity of an LLM trained on a Korean dataset.

# Dataset Source

* [HAERAE-HUB/KOREAN-WEBTEXT](https://huggingface.co/datasets/HAERAE-HUB/KOREAN-WEBTEXT)
* [maxidl/FineNews-unfiltered](https://huggingface.co/datasets/maxidl/FineNews-unfiltered)
* [wikimedia/wikipedia](https://huggingface.co/datasets/wikimedia/wikipedia)