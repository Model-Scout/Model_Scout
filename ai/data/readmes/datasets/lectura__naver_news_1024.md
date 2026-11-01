---
dataset_info:
  features:
  - name: input_ids
    sequence: int32
  splits:
  - name: train
    num_bytes: 53074500
    num_examples: 12945
  download_size: 23902205
  dataset_size: 53074500
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
task_categories:
- text-generation
language:
- ko
size_categories:
- 10K<n<100K
source_datasets:
- daekeun-ml/naver-news-summarization-ko
---
# Dataset Card for "naver_news_1024"

Preprocessed and tokenized [daekeun-ml/naver-news-summarization-ko](https://huggingface.co/datasets/daekeun-ml/naver-news-summarization-ko) dataset for pretraining. \
Concatenated all text and split into chunk size of **1024**. \
Used tokenizer from [beomi/llama-2-ko-7b](https://huggingface.co/beomi/llama-2-ko-7b)

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)