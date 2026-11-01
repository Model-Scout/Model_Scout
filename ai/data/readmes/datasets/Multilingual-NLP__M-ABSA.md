---
license: apache-2.0
task_categories:
- token-classification
- text-classification
language:
- ar
- da
- de
- en
- es
- fr
- hi
- hr
- id
- ja
- ko
- nl
- pt
- ru
- sk
- sv
- sw
- th
- tr
- vi
- zh
tags:
- aspect-based-sentiment-analysis
size_categories:
- 100K<n<1M
---
# M-ABSA

This repo contains the data for our paper ****M-ABSA: A Multilingual Dataset for Aspect-Based Sentiment Analysis****.

[![arXiv](https://img.shields.io/badge/arXiv-2502.11824-b31b1b.svg)](https://arxiv.org/abs/2502.11824)


# Data Description:
This is a dataset suitable for the __multilingual ABSA__ task with __triplet extraction__.

All datasets are stored in the data/ folder:

- All dataset contains __7__ domains. 

 ```
domains = ["coursera", "hotel", "laptop", "restaurant", "phone", "sight", "food"]
``` 
- Each dataset contains __21__ languages.
```
langs = ["ar", "da", "de", "en", "es", "fr", "hi", "hr", "id", "ja", "ko", "nl", "pt", "ru", "sk", "sv", "sw", "th", "tr", "vi", "zh"]
```

- The labels contain triplets with __[aspect term, aspect category, sentiment polarity]__. Each sentence is separated by __"####"__, with the first part being the sentence and the second part being the corresponding triplet. Here is an example, where the triplet includes __[aspect term, aspect category, sentiment polarity]__.

```
This coffee brews up a nice medium roast with exotic floral and berry notes .####[['coffee', 'food quality', 'positive']]
```

- Each dataset is divided into training, validation, and test sets. 


## Citation

If the code or dataset is used in your research, please star our repo and cite our paper as follows:
```
@inproceedings{wu-etal-2025-absa,
    title = "{M}-{ABSA}: A Multilingual Dataset for Aspect-Based Sentiment Analysis",
    author = "Wu, ChengYan  and
      Ma, Bolei  and
      Liu, Yihong  and
      Zhang, Zheyu  and
      Deng, Ningyuan  and
      Li, Yanshu  and
      Chen, Baolan  and
      Zhang, Yi  and
      Xue, Yun  and
      Plank, Barbara",
    editor = "Christodoulopoulos, Christos  and
      Chakraborty, Tanmoy  and
      Rose, Carolyn  and
      Peng, Violet",
    booktitle = "Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2025",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.emnlp-main.128/",
    doi = "10.18653/v1/2025.emnlp-main.128",
    pages = "2530--2557",
    ISBN = "979-8-89176-332-6",
}
```