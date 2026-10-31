---
license: apache-2.0
configs:
- config_name: default
  data_files:
  - split: train
    path:
    - train/EN.jsonl
    - train/ZH.jsonl
    - train/PT.jsonl
    - train/JA.jsonl
    - train/FR.jsonl
    - train/ES.jsonl
    - train/IT.jsonl
    - train/DE.jsonl
  - split: test
    path:
    - test/EN.jsonl
    - test/ZH.jsonl
    - test/PT.jsonl
    - test/JA.jsonl
    - test/FR.jsonl
    - test/ES.jsonl
    - test/IT.jsonl
    - test/DE.jsonl
language:
- en
- zh
- pt
- ja
- fr
- es
- it
- de
- ru
- ar
- ko
- tr
- th
- hi
task_categories:
- translation
- image-to-text
size_categories:
- 10M<n<100M
---

## MIT-10M

**Paper:** https://aclanthology.org/2025.coling-main.346/

**Introduction:**

Image Translation (IT) holds immense potential across diverse domains, enabling the translation of textual content within images into various languages.
However, existing datasets often suffer from limitations in scale, diversity, and quality, hindering the development and evaluation of IT models.
To address this issue, we introduce MIT-10M, a large-scale parallel corpus of multilingual image translation with over 10M image-text pairs derived from real-world data, which has undergone extensive data cleaning and multilingual translation validation. 
It contains 0.8M images in three sizes, 28 categories, tasks with three levels of difficulty and 14 languages image-text pairs, which is a considerable improvement on existing datasets. 




### Citation Information
You can cite our paper https://aclanthology.org/2025.coling-main.346/
```
@inproceedings{li-etal-2025-mit,
    title = "{MIT}-10{M}: A Large Scale Parallel Corpus of Multilingual Image Translation",
    author = "Li, Bo  and Zhu, Shaolin and Wen, Lijie",
    booktitle = "Proceedings of the 31st International Conference on Computational Linguistics",
    month = jan,
    year = "2025",
    address = "Abu Dhabi, UAE",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.coling-main.346/",
    pages = "5154--5167"
}

```
