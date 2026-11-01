---
dataset_info:
  features:
  - name: text
    dtype: string
  - name: user_age
    dtype: int64
  - name: user_gender
    dtype: string
  - name: text_topic
    dtype: string
  - name: class
    dtype: string
  - name: age
    dtype: int64
  - name: text_topic_eng
    dtype: string
  splits:
  - name: train
    num_bytes: 751331
    num_examples: 3770
  download_size: 254089
  dataset_size: 751331
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: cc-by-sa-4.0
language:
- ko
tags:
- safety
---

reference: [https://github.com/jason9693/APEACH](https://github.com/jason9693/APEACH)
```
@inproceedings{yang-etal-2022-apeach,
    title = "{APEACH}: Attacking Pejorative Expressions with Analysis on Crowd-Generated Hate Speech Evaluation Datasets",
    author = "Yang, Kichang  and
      Jang, Wonjun  and
      Cho, Won Ik",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2022",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, United Arab Emirates",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.findings-emnlp.525",
    pages = "7076--7086",
    abstract = "In hate speech detection, developing training and evaluation datasets across various domains is the critical issue. Whereas, major approaches crawl social media texts and hire crowd-workers to annotate the data. Following this convention often restricts the scope of pejorative expressions to a single domain lacking generalization. Sometimes domain overlap between training corpus and evaluation set overestimate the prediction performance when pretraining language models on low-data language. To alleviate these problems in Korean, we propose APEACH that asks unspecified users to generate hate speech examples followed by minimal post-labeling. We find that APEACH can collect useful datasets that are less sensitive to the lexical overlaps between the pretraining corpus and the evaluation set, thereby properly measuring the model performance.",
}
```