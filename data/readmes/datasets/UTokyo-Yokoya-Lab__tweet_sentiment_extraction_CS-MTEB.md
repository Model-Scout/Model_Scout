---
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
- config_name: test_zh_en
  data_files:
  - path: test_zh_en/test-*
    split: test
- config_name: test_ja_en
  data_files:
  - path: test_ja_en/test-*
    split: test
- config_name: test_de_en
  data_files:
  - path: test_de_en/test-*
    split: test
- config_name: test_es_en
  data_files:
  - path: test_es_en/test-*
    split: test
- config_name: test_ko_en
  data_files:
  - path: test_ko_en/test-*
    split: test
- config_name: test_fr_en
  data_files:
  - path: test_fr_en/test-*
    split: test
- config_name: test_it_en
  data_files:
  - path: test_it_en/test-*
    split: test
- config_name: test_pt_en
  data_files:
  - path: test_pt_en/test-*
    split: test
- config_name: test_nl_en
  data_files:
  - path: test_nl_en/test-*
    split: test
dataset_info:
- config_name: default
  features:
  - name: id
    dtype: string
  - name: text
    dtype: string
  - name: label
    dtype: int64
  - name: label_text
    dtype: string
  splits:
  - name: train
    num_examples: 26732
  - name: test
    num_examples: 3432
- config_name: test_zh_en
  features:
  - name: id
    dtype: string
  - name: text
    dtype: string
  - name: label
    dtype: int64
  - name: label_text
    dtype: string
  splits:
  - name: test
    num_examples: 3432
- config_name: test_ja_en
  features:
  - name: id
    dtype: string
  - name: text
    dtype: string
  - name: label
    dtype: int64
  - name: label_text
    dtype: string
  splits:
  - name: test
    num_examples: 3432
- config_name: test_de_en
  features:
  - name: id
    dtype: string
  - name: text
    dtype: string
  - name: label
    dtype: int64
  - name: label_text
    dtype: string
  splits:
  - name: test
    num_examples: 3432
- config_name: test_es_en
  features:
  - name: id
    dtype: string
  - name: text
    dtype: string
  - name: label
    dtype: int64
  - name: label_text
    dtype: string
  splits:
  - name: test
    num_examples: 3432
- config_name: test_ko_en
  features:
  - name: id
    dtype: string
  - name: text
    dtype: string
  - name: label
    dtype: int64
  - name: label_text
    dtype: string
  splits:
  - name: test
    num_examples: 3432
- config_name: test_fr_en
  features:
  - name: id
    dtype: string
  - name: text
    dtype: string
  - name: label
    dtype: int64
  - name: label_text
    dtype: string
  splits:
  - name: test
    num_examples: 3432
- config_name: test_it_en
  features:
  - name: id
    dtype: string
  - name: text
    dtype: string
  - name: label
    dtype: int64
  - name: label_text
    dtype: string
  splits:
  - name: test
    num_examples: 3432
- config_name: test_pt_en
  features:
  - name: id
    dtype: string
  - name: text
    dtype: string
  - name: label
    dtype: int64
  - name: label_text
    dtype: string
  splits:
  - name: test
    num_examples: 3432
- config_name: test_nl_en
  features:
  - name: id
    dtype: string
  - name: text
    dtype: string
  - name: label
    dtype: int64
  - name: label_text
    dtype: string
  splits:
  - name: test
    num_examples: 3432
language:
- en
- zh
- ja
- de
- es
- ko
- fr
- it
- pt
- nl
multilinguality: multilingual
task_categories:
- text-classification
task_ids: []
tags:
- mteb
- text
- code-switching
- classification
- sentiment-analysis
---

# Tweet Sentiment Extraction CS-MTEB

Code-switching version of [mteb/tweet_sentiment_extraction](https://huggingface.co/datasets/mteb/tweet_sentiment_extraction), with test set sentences rewritten in Chinese-English, Japanese-English, German-English, Spanish-English, Korean-English, French-English, Italian-English, Portuguese-English, Dutch-English code-switching styles.

## Dataset Structure

**From original dataset (unchanged):**
- `default`: Original train and test splits

**Code-switching test sets:**
- `test_zh_en`: Chinese-English code-switching test set
- `test_ja_en`: Japanese-English code-switching test set
- `test_de_en`: German-English code-switching test set
- `test_es_en`: Spanish-English code-switching test set
- `test_ko_en`: Korean-English code-switching test set
- `test_fr_en`: French-English code-switching test set
- `test_it_en`: Italian-English code-switching test set
- `test_pt_en`: Portuguese-English code-switching test set
- `test_nl_en`: Dutch-English code-switching test set

## Usage



## Attribution
Based on [mteb/tweet_sentiment_extraction](https://huggingface.co/datasets/mteb/tweet_sentiment_extraction).
