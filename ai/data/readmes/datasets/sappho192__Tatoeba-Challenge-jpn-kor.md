---
license: cc-by-nc-sa-4.0
task_categories:
- translation
language:
- ja
- ko
size_categories:
- 10M<n<100M
---

# Dataset Card for Dataset Name

This dataset contains Japanese-Korean paired text which is from [Helsinki-NLP/Tatoeba-Challenge](https://github.com/Helsinki-NLP/Tatoeba-Challenge/blob/master/data/README-v2023-09-26.md).

## Dataset Details

### Dataset Description

- **Curated by:** [Helsinki-NLP](https://github.com/Helsinki-NLP)
- **Language(s) (NLP):** Japanese-Korean
- **License:** CC BY-NC-SA 4.0

### Dataset Sources

- **Repository:** [Helsinki-NLP/Tatoeba-Challenge](https://github.com/Helsinki-NLP/Tatoeba-Challenge/blob/master/data/README-v2023-09-26.md)
- **Detail**: Japanese - Korean [jpn-kor](https://object.pouta.csc.fi/Tatoeba-Challenge-v2023-09-26/jpn-kor.tar)

## Uses

The dataset can be used to train the translation model that translates Japanese sentence to Korean.

### Out-of-Scope Use

You cannot use this dataset to train the model which is to be used under commercial service.

## Dataset Structure

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->

Each dataset has two columns: `sourceString` and `targetString`, which corresponds to Japanese and Korean sentence.  
Check [example code](https://huggingface.co/datasets/sappho192/Tatoeba-Challenge-jpn-kor/blob/main/example.ipynb) to learn how to load the dataset.  

## Dataset Creation

### Personal and Sensitive Information

<!-- State whether the dataset contains data that might be considered personal, sensitive, or private (e.g., data that reveals addresses, uniquely identifiable names or aliases, racial or ethnic origins, sexual orientations, religious beliefs, political opinions, financial or health data, etc.). If efforts were made to anonymize the data, describe the anonymization process. -->

This dataset may contain following inappropriate or explicit sentences:
- personal
- sensitive
- private
  - data that reveals addresses
  - uniquely identifiable names or aliases
  - racial or ethnic origins
  - sexual orientations
  - religious beliefs
  - political opinions
  - financial or health data
  - etc.

So use with your own risk.


## Citation

**BibTeX:**

```bibtex
@inproceedings{tiedemann-2020-tatoeba,
    title = "The {T}atoeba {T}ranslation {C}hallenge {--} {R}ealistic Data Sets for Low Resource and Multilingual {MT}",
    author = {Tiedemann, J{\"o}rg},
    booktitle = "Proceedings of the Fifth Conference on Machine Translation",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.wmt-1.139",
    pages = "1174--1182"
}
```

## Dataset Card Authors

[sappho192](https://huggingface.co/sappho192)

## Dataset Card Contact

Please create a thread in the community.