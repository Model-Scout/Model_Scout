---
dataset_info:
  features:
  - name: text
    dtype: string
  - name: label
    dtype: string
  - name: source
    dtype: string
  - name: domain
    dtype: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 1364685913
    num_examples: 3147478
  - name: validation
    num_bytes: 170841288
    num_examples: 393435
  - name: test
    num_bytes: 170338153
    num_examples: 393436
  download_size: 988308759
  dataset_size: 1705865354
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
  - split: test
    path: data/test-*
license: apache-2.0
task_categories:
- text-classification
language:
- ar
- de
- en
- es
- fr
- hi
- id
- it
- ko
- ms
- pt
- ru
- tr
- vi
- zh
- ja
tags:
- sentiment
- multilingual
- emotion
- review
- classification
pretty_name: text
size_categories:
- 1M<n<10M
---
## Overview
**MultilingualSentiment** is a sentiment classification dataset that encompasses three sentiment labels: **Positive**, **Neutral**, **Negative**

The dataset spans multiple languages and covers a wide range of domains, making it ideal for multilingual sentiment analysis tasks.


## Dataset Information
The dataset was meticulously collected and aggregated from various sources, including Hugging Face and Kaggle. These sources provide diverse languages and domains to ensure a comprehensive and balanced dataset.

- **Total records**: 3,934,349
- The dataset is divided into three subsets: train, validation, and test, with a ratio of 8:1:1:
  + Train: 3,147,478
  + Validation: 393,435
  + Test: 393,436

### Number of Records per Language
| Language      | Count   |
|---------------|---------|
| Arabic (ar)   | 208,375 |
| German (de)   | 212,853 |
| English (en)  | 1,519,860 |
| Spanish (es)  | 222,911 |
| French (fr)   | 262,645 |
| Hindi (hi)    | 9,423   |
| Indonesian (id) | 12,536 |
| Italian (it)  | 3,020   |
| Japanese (ja) | 335,656 |
| Korean (ko)   | 259,998 |
| Malay (ms)    | 6,661   |
| Multilingual  | 9,391   |
| Portuguese (pt) | 49,188 |
| Russian (ru)  | 205,186 |
| Turkish (tr)  | 44,743  |
| Vietnamese (vi) | 127,068 |
| Chinese (zh)  | 444,835 |

### Number of Records per Label
| Label     | Count    |
|-----------|----------|
| Negative  | 1,436,539 |
| Neutral   | 1,041,512 |
| Positive  | 1,456,298 |

## Applications
This dataset is well-suited for training and evaluating models in multilingual sentiment analysis, natural language processing (NLP), and domain-specific sentiment classification tasks.

## Loading dataset
```python
from datasets import load_dataset

# Load the MultilingualSentiment dataset
dataset = load_dataset("clapAI/MultiLingualSentiment")

print(dataset)

```

```
DatasetDict({
    train: Dataset({
        features: ['text', 'label', 'source', 'domain', 'language'],
        num_rows: 3147478
    })
    validation: Dataset({
        features: ['text', 'label', 'source', 'domain', 'language'],
        num_rows: 393435
    })
    test: Dataset({
        features: ['text', 'label', 'source', 'domain', 'language'],
        num_rows: 393436
    })
})
```

## Citation

```bibtex
@dataset{clapAI2024multilingualsentiment,
  title        = {MultilingualSentiment: A Multilingual Sentiment Classification Dataset},
  author       = {clapAI},
  year         = {2024},
  url          = {https://huggingface.co/datasets/clapAI/MultiLingualSentiment},
  description  = {A multilingual dataset for sentiment analysis with labels: positive, neutral, negative, covering diverse languages and domains.},
}
```