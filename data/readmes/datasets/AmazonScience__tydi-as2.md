---
annotations_creators:
- machine-generated
language:
- bn
- en
- fi
- id
- ja
- ko
- ru
- sw
language_creators:
- found
license_details: https://huggingface.co/datasets/AmazonScience/tydi-as2/blob/main/LICENSE.md
multilinguality:
- multilingual
- translation
pretty_name: tydi-as2
size_categories:
- 10M<n<100M
source_datasets:
- extended|tydiqa
tags:
- as2
- answer sentence selection
- text retrieval
- question answering
task_categories:
- question-answering
- text-retrieval
task_ids:
- open-domain-qa
license: cdla-permissive-2.0
---


# TyDi-AS2

## Table of Contents
- [Dataset Card Creation Guide](#dataset-card-creation-guide)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Languages](#languages)
      - [TyDi-AS2](#tydi-as2)
      - [Xtr-TyDi-AS2](#xtr-tydi-as2)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)
  - [Dataset Creation](#dataset-creation)
    - [Source Data](#source-data)
    - [Annotations](#annotations)
      - [Annotation process](#annotation-process)
      - [Who are the annotators?](#who-are-the-annotators)
  - [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)
    - [Contributions](#contributions)

## Dataset Description

- **Homepage:** [Amazon Science](https://www.amazon.science/publications/cross-lingual-knowledge-distillation-for-answer-sentence-selection-in-low-resource-languages)
- **Paper:** [Cross-Lingual Knowledge Distillation for Answer Sentence Selection in Low-Resource Languages](https://aclanthology.org/2023.findings-acl.885/)
- **Point of Contact:** [Yoshitomo Matsubara](yomtsub@amazon.com)

### Dataset Summary

***TyDi-AS2*** and ***Xtr-TyDi-AS2*** are multilingual Answer Sentence Selection (AS2) datasets comprising 8 diverse languages, proposed in our paper accepted at ACL 2023 (Findings): [**Cross-Lingual Knowledge Distillation for Answer Sentence Selection in Low-Resource Languages**](https://aclanthology.org/2023.findings-acl.885/).
Both the datasets were created from [TyDi-QA](https://ai.google.com/research/tydiqa), a multilingual question-answering dataset. TyDi-AS2 was created by converting the QA instances in TyDi-QA to AS2 instances (see [Dataset Creation](#dataset-creation) for details). Xtr-TyDi-AS2 was created by translating the non-English TyDi-AS2 instances to English and vise versa.
For translations, we used [Amazon Translate](https://aws.amazon.com/translate/).

### Languages

#### TyDi-AS2 (original)

- `bn`: Bengali
- `en`: English
- `fi`: Finnish
- `id`: Indonesian
- `ja`: Japanese
- `ko`: Korean
- `ru`: Russian
- `sw`: Swahili

File location: [`jsonl/original/`](https://huggingface.co/datasets/AmazonScience/tydi-as2/tree/main/jsonl/original/)

For non-English sets, we also have English-translated samples used for the cross-lingual knowledge distillation (CLKD) experiments in our paper.

File location: [`jsonl/x-to-en/`](https://huggingface.co/datasets/AmazonScience/tydi-as2/tree/main/jsonl/x-to-en/)

#### Xtr-TyDi-AS2 (translationese)

Xtr-TyDi-AS2 (X-translated TyDi-AS2) dataset consists of non-English AS2 instances translated from the English set of TyDi-AS2.

- `bn`: Bengali
- `fi`: Finnish
- `id`: Indonesian
- `ja`: Japanese
- `ko`: Korean
- `ru`: Russian
- `sw`: Swahili

File location: [`jsonl/en-to-x/`](https://huggingface.co/datasets/AmazonScience/tydi-as2/tree/main/jsonl/en-to-x/)

## Dataset Structure

### Data Instances

This is an example instance from the English training split of TyDi-AS2 dataset. 

```
{
  "Question": "When was the Argentine Basketball Federation formed?",
  "Title": "History of the Argentina national basketball team",
  "Sentence": "The Argentina national basketball team represents Argentina in basketball international competitions, and is controlled by the Argentine Basketball Federation.",
  "Label": 0
}
```

For English-translated TyDi-AS2 dataset and Xtr-TyDi-AS2 dataset, the translated instances in JSONL files are listed in the same order of the original (native) instances in the original TyDi-AS2 dataset.

For example, the 2nd instance in [`jsonl/x-to-en/en_from_bn-train.jsonl`](jsonl/x-to-en/en_from_bn-train.jsonl) (English-translated from Bengali) corresponds to the 2nd instance in [`jsonl/original/bn-train.jsonl`](jsonl/original/bn-train.jsonl) (Bengali).

Similarly, the 2nd instance in [`jsonl/en-to-x/bn_from_en-train.jsonl`](jsonl/en-to-x/bn_from_en-train.jsonl) (Bengali-translated from English) corresponds to the 2nd instance in [`jsonl/original/en-train.jsonl`](jsonl/original/en-train.jsonl) (English).

### Data Fields

Each instance (a QA pair) consists of the following fields:

- `Question`: Question to be answered (str)
- `Title`: Document title (str)
- `Sentence`: Answer sentence in the document (str)
- `Label`: Label that indicates the answer sentence correctly answers the question (int, 1: correct, 0: incorrect)


### Data Splits

|                     |           | **#Questions** |          |   |           | **#Sentences** |          |
|---------------------|----------:|---------------:|---------:|---|----------:|---------------:|---------:|
|                     | **train** |        **dev** | **test** |   | **train** |        **dev** | **test** |
| **Bengali (bn)**    |     7,978 |          2,056 |      316 |   | 1,376,432 |        351,186 |   37,465 |
| **English (en)**    |     6,730 |          1,686 |      918 |   | 1,643,702 |        420,899 |  249,513 |
| **Finnish (fi)**    |    10,859 |          2,731 |    1,870 |   | 1,567,695 |        408,205 |  298,093 |
| **Indonesian (id)** |     9,310 |          2,339 |    1,355 |   |   960,270 |        236,076 |   97,057 |
| **Japanese (ja)**   |    11,848 |          2,981 |    1,504 |   | 3,183,037 |        822,654 |  444,106 |
| **Korean (ko)**     |     7,354 |          1,943 |    1,389 |   | 1,558,191 |        392,361 |  199,043 |
| **Russian (ru)**    |     9,187 |          2,294 |    1,395 |   | 3,190,650 |        820,668 |  367,595 |
| **Swahili (sw)**    |     8,350 |          2,850 |    1,896 |   | 1,048,303 |        269,894 |   74,775 |

See [our paper](#citation-information) for more details about the statistics of the datasets.


## Dataset Creation

### Source Data

The source of TyDi-AS2 dataset is [TyDi QA](https://ai.google.com/research/tydiqa), which is a question answering dataset.

### Annotations

#### Annotation process

TyDi QA is a QA dataset spanning questions from 11 typologically diverse languages.
Each instance comprises a human-generated question, a single Wikipedia document as context, and one or more spans from the document containing the answer.
To convert each instance into AS2 instances, we split the context document into sentences and heuristically identify the correct asnwer sentences using the annotated answer spans.
To split documents, we use multiple different sentence tokenizers for the diverse languages and omit languages for which we could not find a suitable sentence tokenizer:
1. [bltk](https://github.com/saimoncse19/bltk) for Bengali
2. [blingfire](https://github.com/microsoft/BlingFire) for Swahili, Indonesian, and Korean
3. [pysdb](https://github.com/nipunsadvilkar/pySBD) for English and Russian
4. [nltk](https://www.nltk.org/) for Finnish
5. [Konoha](https://github.com/himkt/konoha) for Japanese

#### Who are the annotators?

[Shivanshu Gupta](https://huggingface.co/shivanshu) converted TyDi QA to TyDi-AS2.
[Yoshitomo Matsubara](https://huggingface.co/yoshitomo-matsubara) translated non-English samples to English and vice versa for Xtr-TyDi-AS2 dataset
Since sentence tokenization and identifying answer sentences can introduce errors, we conducted a manual validation of the AS2 datasets. For each language, we randomly selected 50 instances and verified the accuracy of the answer sentences through manual inspection. Our findings revealed that the answer sentences were accurate in 98% of the cases.

## Additional Information

### Dataset Curators

Shivanshu Gupta (@shivanshu)


### Licensing Information

[CDLA-Permissive-2.0](LICENSE.md)

### Citation Information

```bibtex
@inproceedings{gupta2023cross-lingual,
  title={{Cross-Lingual Knowledge Distillation for Answer Sentence Selection in Low-Resource Languages}},
  author={Gupta, Shivanshu and Matsubara, Yoshitomo and Chadha, Ankit and Moschitti, Alessandro},
  booktitle={Findings of the Association for Computational Linguistics: ACL 2023},
  pages={14078--14092},
  year={2023}
}
```


### Contributions

- [Shivanshu Gupta](https://huggingface.co/shivanshu)
- [Yoshitomo Matsubara](https://huggingface.co/yoshitomo-matsubara)
- Ankit Chadha
- Alessandro Moschitti