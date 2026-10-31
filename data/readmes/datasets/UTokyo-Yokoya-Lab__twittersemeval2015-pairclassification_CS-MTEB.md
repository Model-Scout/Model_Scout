---
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test-*
- config_name: test_de_en
  data_files:
  - split: test
    path: test_de_en/test-*
- config_name: test_es_en
  data_files:
  - path: test_es_en/test-*
    split: test
- config_name: test_fr_en
  data_files:
  - path: test_fr_en/test-*
    split: test
- config_name: test_it_en
  data_files:
  - path: test_it_en/test-*
    split: test
- config_name: test_ja_en
  data_files:
  - path: test_ja_en/test-*
    split: test
- config_name: test_ko_en
  data_files:
  - path: test_ko_en/test-*
    split: test
- config_name: test_nl_en
  data_files:
  - path: test_nl_en/test-*
    split: test
- config_name: test_pt_en
  data_files:
  - path: test_pt_en/test-*
    split: test
- config_name: test_zh_en
  data_files:
  - path: test_zh_en/test-*
    split: test
dataset_info:
- config_name: default
  features:
  - name: sentence1
    list: string
  - name: sentence2
    list: string
  - name: labels
    list: int64
  splits:
  - name: test
    num_examples: 1
- config_name: test_de_en
  features:
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  - name: labels
    dtype: int64
  splits:
  - name: test
    num_bytes: 1765303
    num_examples: 16777
  download_size: 747514
  dataset_size: 1765303
- config_name: test_es_en
  features:
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  - name: labels
    dtype: int64
  splits:
  - name: test
    num_examples: 16777
- config_name: test_fr_en
  features:
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  - name: labels
    dtype: int64
  splits:
  - name: test
    num_examples: 16774
- config_name: test_it_en
  features:
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  - name: labels
    dtype: int64
  splits:
  - name: test
    num_examples: 16777
- config_name: test_ja_en
  features:
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  - name: labels
    dtype: int64
  splits:
  - name: test
    num_examples: 16777
- config_name: test_ko_en
  features:
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  - name: labels
    dtype: int64
  splits:
  - name: test
    num_examples: 16777
- config_name: test_nl_en
  features:
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  - name: labels
    dtype: int64
  splits:
  - name: test
    num_examples: 16777
- config_name: test_pt_en
  features:
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  - name: labels
    dtype: int64
  splits:
  - name: test
    num_examples: 16777
- config_name: test_zh_en
  features:
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  - name: labels
    dtype: int64
  splits:
  - name: test
    num_examples: 16766
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
- pair-classification
---

# TwitterSemEval2015 CS-MTEB

Code-switching version of [mteb/twittersemeval2015-pairclassification](https://huggingface.co/datasets/mteb/twittersemeval2015-pairclassification), with sentence pairs rewritten in Chinese-English, Japanese-English, German-English, Spanish-English, Korean-English, French-English, Italian-English, Portuguese-English, Dutch-English code-switching styles.

## Dataset Structure

**From original dataset (unchanged):**
- `default`: Original test split (batched format)

**Code-switching test sets (flat format):**
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
Based on [mteb/twittersemeval2015-pairclassification](https://huggingface.co/datasets/mteb/twittersemeval2015-pairclassification).
