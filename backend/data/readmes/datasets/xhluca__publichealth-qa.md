---
license: cc-by-nc-sa-3.0
task_categories:
- question-answering
language:
- ar
- en
- es
- fr
- ko
- ru
- vi
- zh
size_categories:
- n<1K
# https://huggingface.co/docs/hub/en/datasets-manual-configuration
configs:
- config_name: english
  default: true
  data_files:
  - split: test
    path: data/english.csv
- config_name: arabic
  data_files:
  - split: test
    path: data/arabic.csv
- config_name: chinese
  data_files:
  - split: test
    path: data/chinese.csv
- config_name: french
  data_files:
  - split: test
    path: data/french.csv
- config_name: korean
  data_files:
  - split: test
    path: data/korean.csv
- config_name: korean
  data_files:
  - split: test
    path: data/korean.csv
- config_name: russian
  data_files:
  - split: test
    path: data/russian.csv
- config_name: spanish
  data_files:
  - split: test
    path: data/spanish.csv
- config_name: vietnamese
  data_files:
  - split: test
    path: data/vietnamese.csv
---

# Usage

```python
import datasets

langs = ['arabic', 'chinese', 'english', 'french', 'korean', 'russian', 'spanish', 'vietnamese']
data = datasets.load_dataset('xhluca/publichealth-qa', split='test', name=langs[0])
```

# About

This dataset contains question and answer pairs sourced from Q&A pages and FAQs from CDC and WHO pertaining to COVID-19. They were produced and collected between 2019-12 and 2020-04. They were originally published as an [aggregated Kaggle dataset](https://www.kaggle.com/xhlulu/covidqa).

# License

CDC data is licensed under [CC-BY 3.0](https://web.archive.org/web/20201017141031/https://www2a.cdc.gov/cdcup/library/other/policy.htm) and WHO is licensed under [cc-by-nc-sa-3.0](https://web.archive.org/web/20210701063743/https://www.who.int/about/policies/publishing/copyright).


# Source

This data was originally included in the [COVID-QA dataset](https://www.kaggle.com/datasets/xhlulu/covidqa), where it was known as the multilingual split. The files in this updated repository were generated using the [publichealth-qa repository](https://github.com/xhluca/publichealth-qa).