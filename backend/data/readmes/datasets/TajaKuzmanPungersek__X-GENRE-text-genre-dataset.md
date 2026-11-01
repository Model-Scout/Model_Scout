---
license: cc-by-sa-4.0
task_categories:
- text-classification
language:
- sl
- en
tags:
- genre
- web genre
- text genre
- automatic genre identification
- manually-annotated dataset
- cross-lingual classification
pretty_name: X-GENRE
size_categories:
- 1K<n<10K
configs:
  - config_name: train
    data_files: X-GENRE-train.jsonl
  - config_name: test
    data_files: X-GENRE-test.jsonl
  - config_name: dev
    data_files: X-GENRE-dev.jsonl
---
# Multilingual manually-annotated X-GENRE genre dataset

Multilingual (English-Slovenian) manually-annotated X-GENRE genre dataset is to be used for automatic genre identification, namely, 
for training genre classifiers (on the training split) and evaluation in the in-dataset scenario (on the test split).

The dataset was presented in the paper "[Automatic Genre Identification for Robust Enrichment of Massive Text Collections:
Investigation of Classification Methods in the Era of Large Language Models](https://www.mdpi.com/2504-4990/5/3/59)" (Kuzman et al., 2023).

To download the dataset as a HuggingFace dataset:
```
from datasets import load_dataset
import pandas as pd

train = load_dataset("TajaKuzman/X-GENRE-text-genre-dataset", "train")
test = load_dataset("TajaKuzman/X-GENRE-text-genre-dataset", "test")
dev = load_dataset("TajaKuzman/X-GENRE-text-genre-dataset", "dev")

# To open as Pandas DataFrame:
train_df = pd.DataFrame(train["train"])
dev_df = pd.DataFrame(dev["train"])
test_df = pd.DataFrame(test["train"])

```

The dataset can also be downloaded from the [CLARIN.SI repository](http://hdl.handle.net/11356/1960).

## Dataset Description

- **Repository: coming soon** 
- **Paper: Kuzman, T.; Mozetič, I.; Ljubešić, N. Automatic Genre Identification for Robust Enrichment of Massive Text Collections: Investigation of Classification Methods in the Era of Large Language Models. Mach. Learn. Knowl. Extr. 2023, 5, 1149-1175. https://doi.org/10.3390/make5030059** 

### Dataset Summary

The X-GENRE dataset consists of almost 3,000 texts and 3.3 million words in English and Slovenian language.
It is split into train, test and dev split.
The dataset was used to develop the
 [XLM-RoBERTa-based multilingual genre classifier X-GENRE, available on HuggingFace](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier).

Dataset sizes:

| split | # words | # texts |
|:---|---:|---:|
| X-GENRE-train | 1,940,317 | 1,772 |
| X-GENRE-test | 583,595 | 592 |
| X-GENRE-dev | 798,025 | 592 |
| **Total** | **3,321,937** | **2,956** |

The X-GENRE dataset was constructed by merging three manually-annotated datasets by mapping a joint X-GENRE genre schema to the original schemata:
- the Slovenian [GINCO](https://www.clarin.si/repository/xmlui/handle/11356/1467) dataset ([Kuzman et al., 2022](https://aclanthology.org/2022.lrec-1.170.pdf)),
- the English [CORE](https://github.com/TurkuNLP/CORE-corpus) dataset ([Laippala et al., 2023](https://link.springer.com/article/10.1007/s10579-022-09624-1))
- and the English [FTD](https://github.com/ssharoff/genre-keras) dataset ([Sharoff, 2018](https://eprints.whiterose.ac.uk/102914/1/2018-ftd.pdf)).


Distribution of the original datasets in the X-GENRE dataset (in number of texts):

| split | FTD | CORE | GINCO | **Total** |
|:---|---:|---:|---:|---:|
| X-GENRE-train | 630 | 607 | 535 | 1,772 |
| X-GENRE-test | 210 | 203 | 179 | 592 |
| X-GENRE-dev | 210 | 203 | 179 | 592 |
| **Total** | 1,050 | 1,013 | 893 | 2,956 |

Distribution of languages in the dataset (in number of texts):

| split | Slovenian | English | **Total** |
|:---|---:|---:|---:|
| X-GENRE-train | 535 | 1,237 | 1,772 |
| X-GENRE-test | 179 | 413 | 592 |
| X-GENRE-dev | 179 | 413 | 592 |
| **Total** | 893 | 2,063 | 2,956 |

### Data Attributes

The dataset is in JSONL format. It has the following attributes:
- text: text instance
- labels: genre label
- dataset: original manually-annotated genre dataset from which the text was obtained (CORE, GINCO or FTD)
- language: language of the text (Slovenian or English)

### Genre labels

The dataset uses the "X-GENRE" schema.

```labels_list=['Other', 'Information/Explanation', 'News', 'Instruction', 'Opinion/Argumentation', 'Forum', 'Prose/Lyrical', 'Legal', 'Promotion']```


Description of labels:

|     Label               |     Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |     Examples                                                                                                                                                                                                                                  |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Information/Explanation | An objective text that describes   or presents an event, a person, a thing, a concept etc. Its main purpose is   to inform the reader about something.      Common features: objective/factual, explanation/definition of a concept (x   is …), enumeration.                                                                                                                                                                                                                                                                                                       | research article, encyclopedia article, informational blog, product   specification, course materials, general information, job description,   manual, horoscope, travel guide, glossaries, historical article, biographical   story/history. |
| Instruction             | An objective text which instructs   the readers on how to do something.      Common features: multiple steps/actions, chronological order, 1st person   plural or 2nd person, modality (must, have to, need to, can, etc.), adverbial   clauses of manner (in a way that), of condition (if), of time (after …).                                                                                                                                                                                                                                                   | how-to texts, recipes, technical support                                                                                                                                                                                                      |
| Legal                   | An objective formal text that   contains legal terms and is clearly structured. The name of the text type is   often included in the headline (contract, rules, amendment, general terms and   conditions, etc.).      Common features: objective/factual, legal terms, 3rd person.                                                                                                                                                                                                                                                                                | small print, software license, proclamation, terms and conditions,   contracts, law, copyright notices, university regulation                                                                                                                 |
| News                    | An objective or subjective text   which reports on an event recent at the time of writing or coming in the near   future.      Common features: adverbs/adverbial clauses of time and/or place (dates,   places), many proper nouns, direct or reported speech, past tense.                                                                                                                                                                                                                                                                                        | news report, sports report, travel blog, reportage, police report,   announcement                                                                                                                                                             |
| Opinion/Argumentation   | A subjective text in which the   authors convey their opinion or narrate their experience. It includes   promotion of an ideology and other non-commercial causes. This genre includes a subjective narration of a personal   experience as well.      Common features: adjectives/adverbs that convey opinion, words that convey   (un)certainty (certainly, surely), 1st person, exclamation marks.                                                | review, blog (personal blog, travel blog), editorial, advice, letter to   editor, persuasive article or essay, formal speech, pamphlet, political   propaganda, columns, political manifesto                                                  |
| Promotion               | A subjective text intended to   sell or promote an event, product, or service. It addresses the readers,   often trying to convince them to participate in something or buy something.   Common features: contains adjectives/adverbs that promote something   (high-quality, perfect, amazing), comparative and superlative forms of   adjectives and adverbs (the best, the greatest, the cheapest), addressing the   reader (usage of 2nd person), exclamation marks. | advertisement, promotion of a product (e-shops), promotion of an   accommodation, promotion of company's services, invitation to an event                                                                                                     |
| Forum                   | A text in which people discuss a   certain topic in form of comments.      Common features: multiple authors, informal language, subjective (the   writers express their opinions), written in 1st person.                                                                                                                                                                                                                                                                                                                                                         | discussion forum, reader/viewer responses, QA forum                                                                                                                                                                                           |
| Prose/Lyrical           | A literary text that   consists of paragraphs or verses. A literary text is deemed to have no other   practical purpose than to give pleasure to the reader. Often the author pays   attention to the aesthetic appearance of the text. It can be considered as   art.                                                                                                                                                                                                                                                                                     | lyrics, poem, prayer, joke, novel, short story                                                                                                                                                                                                |
| Other                   | A text that which does not fall   under any of other genre categories.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                               |


### Citation information

Please cite the following paper which describes the construction of the dataset in more details:
```
@article{make5030059,
AUTHOR = {Kuzman, Taja and Mozetič, Igor and Ljubešić, Nikola},
TITLE = {Automatic Genre Identification for Robust Enrichment of Massive Text Collections: Investigation of Classification Methods in the Era of Large Language Models},
JOURNAL = {Machine Learning and Knowledge Extraction},
VOLUME = {5},
YEAR = {2023},
NUMBER = {3},
PAGES = {1149--1175},
URL = {https://www.mdpi.com/2504-4990/5/3/59},
ISSN = {2504-4990},
DOI = {10.3390/make5030059}
}
```