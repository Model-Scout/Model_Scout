---
license: mit
task_categories:
- translation
- audio-to-audio
language:
- mt
- en
- cy
- te
- kn
- be
- ta
- uz
- tg
- ca
- ur
- zh
- th
- ko
- hi
- da
- cs
- vi
- sw
- rn
- uk
- tr
- ar
- id
- fi
- sk
- sv
- pl
- it
- pt
- ru
- de
- nl
- fr
---
# Dataset Card for Seamless-Align (WIP). Inspired by https://huggingface.co/datasets/allenai/nllb

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** [Needs More Information]
- **Repository:** [Needs More Information]
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

This dataset was created based on [metadata](https://github.com/facebookresearch/seamless_communication/blob/main/docs/m4t/seamless_align_README.md) for mined Speech-to-Speech(S2S), Text-to-Speech(TTS) and Speech-to-Text(S2T) released by Meta AI.  The S2S contains data for 35 language pairs. The S2S dataset is ~1000GB compressed.


#### How to use the data
There are two ways to access the data:
* Via the Hugging Face Python datasets library 

```
Scripts coming soon
```

* Clone the git repo
```
git lfs install
git clone https://huggingface.co/datasets/jhu-clsp/seamless-align
```

### Supported Tasks and Leaderboards

N/A

### Languages

Language pairs can be found [here](https://github.com/facebookresearch/seamless_communication/blob/main/docs/m4t/seamless_align_README.md).

## Dataset Structure

The S2S dataset contains two gzipped files src.tar.gz annd tgt.tar.gz


### Data Instances

The number of instances for each language pair can be found in the [dataset_infos.json](https://huggingface.co/datasets/allenai/nllb/blob/main/dataset_infos.json) file.

### Data Fields

Data Field can be found [here](https://github.com/facebookresearch/seamless_communication/blob/main/docs/m4t/seamless_align_README.md).
 

### Data Splits

The data is not split.


## Dataset Creation

### Curation Rationale



### Source Data

Inspect links in metadata

#### Who are the source language producers?

Speech and Text was collected from the web many of which are web crawls. 
### Annotations

#### Annotation process

Parallel sentences were identified using SONAR encoders. (Duquenne et al., 2023)

#### Who are the annotators?

The data was not human annotated.

### Personal and Sensitive Information

Data may contain personally identifiable information, sensitive content, or toxic content that was publicly shared on the Internet.  

## Considerations for Using the Data

### Social Impact of Dataset

This dataset provides data for training machine learning systems for many languages.

### Discussion of Biases

Biases in the data have not been specifically studied, however as the original source of data is World Wide Web it is likely that the data has biases similar to those prevalent in the Internet. The data may also exhibit biases introduced by language identification and data filtering techniques; lower resource languages generally have lower accuracy.  

### Other Known Limitations

Some of the translations are in fact machine translations.  While some website machine translation tools are identifiable from HTML source, these tools were not filtered out en mass because raw HTML was not available from some sources and CommonCrawl processing started from WET files. 

## Additional Information

### Dataset Curators

The data was not curated.

### Licensing Information

The dataset is released under the terms of [MIT](https://opensource.org/license/mit/). **PLEASE, USE DATA RESPONSIBLY**


### Citation Information

Seamless Communication et al, SeamlessM4T: Massively Multilingual & Multimodal Machine Translation. arXiv https://arxiv.org/abs/2308.11596, 2023. <br>
Duquenne et al, SONAR: Sentence-Level Multimodal and Language-Agnostic Representations. arXiv https://arxiv.org/abs/2308.11466, 2023

### Contributions

We thank the Seamless Communication Meta AI team for open sourcing the meta data and instructions on how to use it with special thanks to   Loïc Barrault, Yu-An Chung, Mariano Cora Meglioli, David Dale, Ning Dong, Paul-Ambroise Duquenne, Hady Elsahar, Hongyu Gong, Kevin Heffernan, John Hoffman, Christopher Klaiber, Pengwei Li, Daniel Licht, Jean Maillard, Alice Rakotoarison, Kaushik Ram Sadagopan, Guillaume Wenzek, Ethan Ye, Bapi Akula, Peng-Jen Chen, Naji El Hachem, Brian Ellis, Gabriel Mejia Gonzalez, Justin Haaheim, Prangthip Hansanti, Russ Howes, Bernie Huang, Min-Jae Hwang, Hirofumi Inaguma, Somya Jain, Elahe Kalbassi, Amanda Kallet, Ilia Kulikov, Janice Lam, Daniel Li, Xutai Ma, Ruslan Mavlyutov, Benjamin Peloquin, Mohamed Ramadan, Abinesh Ramakrishnan, Anna Sun, Kevin Tran, Tuan Tran, Igor Tufanov, Vish Vogeti, Carleigh Wood, Yilin Yang, Bokai Yu, Pierre Andrews, Can Balioglu, Marta R. Costa-jussà, Onur Celebi, Maha Elbayad, Cynthia Gao, Francisco Guzmán, Justine Kao, Ann Lee, Alexandre Mourachko, Juan Pino, Sravya Popuri, Christophe Ropers, Safiyyah Saleem, Holger Schwenk, Paden Tomasello, Changhan Wang, Jeff Wang, Skyler Wang. We also thank the Center for Language and Speech Processing(CLSP) for hosting and releasing this data, including Bismarck Bamfo Odoom and Philipp Koehn (for engineering efforts to host the data, and releasing the huggingface dataset), and  Alexandre Mourachko  (for organizing the connection).