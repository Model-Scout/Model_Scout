---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- af
- am
- ar
- as
- az
- be
- bg
- bn
- br
- bs
- ca
- cs
- cy
- da
- de
- el
- en
- eo
- es
- et
- eu
- fa
- ff
- fi
- fr
- fy
- ga
- gd
- gl
- gn
- gu
- ha
- he
- hi
- hr
- ht
- hu
- hy
- id
- ig
- is
- it
- ja
- jv
- ka
- kk
- km
- kn
- ko
- ku
- ky
- la
- lg
- li
- ln
- lo
- lt
- lv
- mg
- mk
- ml
- mn
- mr
- ms
- my
- ne
- nl
- 'no'
- ns
- om
- or
- pa
- pl
- ps
- pt
- qu
- rm
- ro
- ru
- sa
- sc
- sd
- si
- sk
- sl
- so
- sq
- sr
- ss
- su
- sv
- sw
- ta
- te
- th
- tl
- tn
- tr
- ug
- uk
- ur
- uz
- vi
- wo
- xh
- yi
- yo
- zh
- zu
language_bcp47:
- bn-Latn
- hi-Latn
- my-x-zawgyi
- ta-Latn
- te-Latn
- ur-Latn
- zh-Hans
- zh-Hant
license:
- unknown
multilinguality:
- multilingual
size_categories:
- 10M<n<100M
- 1M<n<10M
source_datasets:
- original
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
- masked-language-modeling
paperswithcode_id: cc100
pretty_name: CC-100
dataset_info:
- config_name: am
  features:
  - name: id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 935440775
    num_examples: 3124561
  download_size: 138821056
  dataset_size: 935440775
- config_name: sr
  features:
  - name: id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 10299427460
    num_examples: 35747957
  download_size: 1578989320
  dataset_size: 10299427460
- config_name: ka
  features:
  - name: id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 10228918845
    num_examples: 31708119
  download_size: 1100446372
  dataset_size: 10228918845
config_names:
- am
- sr
---

# Dataset Card for CC-100

## Table of Contents
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

- **Homepage:** https://data.statmt.org/cc-100/
- **Repository:** [More Information Needed]
- **Paper:** https://aclanthology.org/2020.acl-main.747/
- **Paper:** https://aclanthology.org/2020.lrec-1.494/
- **Paper:** https://arxiv.org/abs/1911.02116
- **Paper:** https://arxiv.org/abs/1911.00359
- **Leaderboard:** [More Information Needed]
- **Point of Contact:** [More Information Needed]

### Dataset Summary

This corpus is an attempt to recreate the dataset used for training XLM-R. This corpus comprises of monolingual data for 100+ languages and also includes data for romanized languages (indicated by *_rom). This was constructed using the urls and paragraph indices provided by the CC-Net repository by processing January-December 2018 Commoncrawl snapshots.

### Supported Tasks and Leaderboards

CC-100 is mainly intended to pretrain language models and word representations.

### Languages

The languages in the dataset are:
- af: Afrikaans (305M)
- am: Amharic (133M)
- ar: Arabic (5.4G)
- as: Assamese (7.6M)
- az: Azerbaijani (1.3G)
- be: Belarusian (692M)
- bg: Bulgarian (9.3G)
- bn: Bengali (860M)
- bn_rom: Bengali Romanized (164M)
- br: Breton (21M)
- bs: Bosnian (18M)
- ca: Catalan (2.4G)
- cs: Czech (4.4G)
- cy: Welsh (179M)
- da: Danish (12G)
- de: German (18G)
- el: Greek (7.4G)
- en: English (82G)
- eo: Esperanto (250M)
- es: Spanish (14G)
- et: Estonian (1.7G)
- eu: Basque (488M)
- fa: Persian (20G)
- ff: Fulah (3.1M)
- fi: Finnish (15G)
- fr: French (14G)
- fy: Frisian (38M)
- ga: Irish (108M)
- gd: Scottish Gaelic (22M)
- gl: Galician (708M)
- gn: Guarani (1.5M)
- gu: Gujarati (242M)
- ha: Hausa (61M)
- he: Hebrew (6.1G)
- hi: Hindi (2.5G)
- hi_rom: Hindi Romanized (129M)
- hr: Croatian (5.7G)
- ht: Haitian (9.1M)
- hu: Hungarian (15G)
- hy: Armenian (776M)
- id: Indonesian (36G)
- ig: Igbo (6.6M)
- is: Icelandic (779M)
- it: Italian (7.8G)
- ja: Japanese (15G)
- jv: Javanese (37M)
- ka: Georgian (1.1G)
- kk: Kazakh (889M)
- km: Khmer (153M)
- kn: Kannada (360M)
- ko: Korean (14G)
- ku: Kurdish (90M)
- ky: Kyrgyz (173M)
- la: Latin (609M)
- lg: Ganda (7.3M)
- li: Limburgish (2.2M)
- ln: Lingala (2.3M)
- lo: Lao (63M)
- lt: Lithuanian (3.4G)
- lv: Latvian (2.1G)
- mg: Malagasy (29M)
- mk: Macedonian (706M)
- ml: Malayalam (831M)
- mn: Mongolian (397M)
- mr: Marathi (334M)
- ms: Malay (2.1G)
- my: Burmese (46M)
- my_zaw: Burmese (Zawgyi) (178M)
- ne: Nepali (393M)
- nl: Dutch (7.9G)
- no: Norwegian (13G)
- ns: Northern Sotho (1.8M)
- om: Oromo (11M)
- or: Oriya (56M)
- pa: Punjabi (90M)
- pl: Polish (12G)
- ps: Pashto (107M)
- pt: Portuguese (13G)
- qu: Quechua (1.5M)
- rm: Romansh (4.8M)
- ro: Romanian (16G)
- ru: Russian (46G)
- sa: Sanskrit (44M)
- sc: Sardinian (143K)
- sd: Sindhi (67M)
- si: Sinhala (452M)
- sk: Slovak (6.1G)
- sl: Slovenian (2.8G)
- so: Somali (78M)
- sq: Albanian (1.3G)
- sr: Serbian (1.5G)
- ss: Swati (86K)
- su: Sundanese (15M)
- sv: Swedish (21G)
- sw: Swahili (332M)
- ta: Tamil (1.3G)
- ta_rom: Tamil Romanized (68M)
- te: Telugu (536M)
- te_rom: Telugu Romanized (79M)
- th: Thai (8.7G)
- tl: Tagalog (701M)
- tn: Tswana (8.0M)
- tr: Turkish (5.4G)
- ug: Uyghur (46M)
- uk: Ukrainian (14G)
- ur: Urdu (884M)
- ur_rom: Urdu Romanized (141M)
- uz: Uzbek (155M)
- vi: Vietnamese (28G)
- wo: Wolof (3.6M)
- xh: Xhosa (25M)
- yi: Yiddish (51M)
- yo: Yoruba (1.1M)
- zh-Hans: Chinese (Simplified) (14G)
- zh-Hant: Chinese (Traditional) (5.3G)
- zu: Zulu (4.3M)

## Dataset Structure

### Data Instances

An example from the `am` configuration:

```
{'id': '0', 'text': 'ተለዋዋጭ የግድግዳ አንግል ሙቅ አንቀሳቅሷል ቲ-አሞሌ አጥቅሼ ...\n'}
```

Each data point is a paragraph of text. The paragraphs are presented in the original (unshuffled) order. Documents are separated by a data point consisting of a single newline character.

### Data Fields

The data fields are:

- id: id of the example
- text: content as a string

### Data Splits

Sizes of some configurations:

|   name   |train|
|----------|----:|
|am|3124561|
|sr|35747957|

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

[More Information Needed]

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

The data comes from multiple web pages in a large variety of languages.

### Annotations

The dataset does not contain any additional annotations.

#### Annotation process

[N/A]

#### Who are the annotators?

[N/A]

### Personal and Sensitive Information

Being constructed from Common Crawl, personal and sensitive information might be present. This **must** be considered before training deep learning models with CC-100, specially in the case of text-generation models.

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

This dataset was prepared by [Statistical Machine Translation at the University of Edinburgh](https://www.statmt.org/ued/) using the [CC-Net](https://github.com/facebookresearch/cc_net) toolkit by Facebook Research.

### Licensing Information

Statistical Machine Translation at the University of Edinburgh makes no claims of intellectual property on the work of preparation of the corpus. By using this, you are also bound by the [Common Crawl terms of use](https://commoncrawl.org/terms-of-use/) in respect of the content contained in the dataset.

### Citation Information

Please cite the following if you found the resources in this corpus useful:

```bibtex
@inproceedings{conneau-etal-2020-unsupervised,
    title = "Unsupervised Cross-lingual Representation Learning at Scale",
    author = "Conneau, Alexis  and
      Khandelwal, Kartikay  and
      Goyal, Naman  and
      Chaudhary, Vishrav  and
      Wenzek, Guillaume  and
      Guzm{\'a}n, Francisco  and
      Grave, Edouard  and
      Ott, Myle  and
      Zettlemoyer, Luke  and
      Stoyanov, Veselin",
    editor = "Jurafsky, Dan  and
      Chai, Joyce  and
      Schluter, Natalie  and
      Tetreault, Joel",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.acl-main.747",
    doi = "10.18653/v1/2020.acl-main.747",
    pages = "8440--8451",
    abstract = "This paper shows that pretraining multilingual language models at scale leads to significant performance gains for a wide range of cross-lingual transfer tasks. We train a Transformer-based masked language model on one hundred languages, using more than two terabytes of filtered CommonCrawl data. Our model, dubbed XLM-R, significantly outperforms multilingual BERT (mBERT) on a variety of cross-lingual benchmarks, including +14.6{\%} average accuracy on XNLI, +13{\%} average F1 score on MLQA, and +2.4{\%} F1 score on NER. XLM-R performs particularly well on low-resource languages, improving 15.7{\%} in XNLI accuracy for Swahili and 11.4{\%} for Urdu over previous XLM models. We also present a detailed empirical analysis of the key factors that are required to achieve these gains, including the trade-offs between (1) positive transfer and capacity dilution and (2) the performance of high and low resource languages at scale. Finally, we show, for the first time, the possibility of multilingual modeling without sacrificing per-language performance; XLM-R is very competitive with strong monolingual models on the GLUE and XNLI benchmarks. We will make our code and models publicly available.",
}
```

```bibtex
@inproceedings{wenzek-etal-2020-ccnet,
    title = "{CCN}et: Extracting High Quality Monolingual Datasets from Web Crawl Data",
    author = "Wenzek, Guillaume  and
      Lachaux, Marie-Anne  and
      Conneau, Alexis  and
      Chaudhary, Vishrav  and
      Guzm{\'a}n, Francisco  and
      Joulin, Armand  and
      Grave, Edouard",
    editor = "Calzolari, Nicoletta  and
      B{\'e}chet, Fr{\'e}d{\'e}ric  and
      Blache, Philippe  and
      Choukri, Khalid  and
      Cieri, Christopher  and
      Declerck, Thierry  and
      Goggi, Sara  and
      Isahara, Hitoshi  and
      Maegaard, Bente  and
      Mariani, Joseph  and
      Mazo, H{\'e}l{\`e}ne  and
      Moreno, Asuncion  and
      Odijk, Jan  and
      Piperidis, Stelios",
    booktitle = "Proceedings of the Twelfth Language Resources and Evaluation Conference",
    month = may,
    year = "2020",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    url = "https://aclanthology.org/2020.lrec-1.494",
    pages = "4003--4012",
    abstract = "Pre-training text representations have led to significant improvements in many areas of natural language processing. The quality of these models benefits greatly from the size of the pretraining corpora as long as its quality is preserved. In this paper, we describe an automatic pipeline to extract massive high-quality monolingual datasets from Common Crawl for a variety of languages. Our pipeline follows the data processing introduced in fastText (Mikolov et al., 2017; Grave et al., 2018), that deduplicates documents and identifies their language. We augment this pipeline with a filtering step to select documents that are close to high quality corpora like Wikipedia.",
    language = "English",
    ISBN = "979-10-95546-34-4",
}
```

### Contributions

Thanks to [@abhishekkrthakur](https://github.com/abhishekkrthakur) for adding this dataset.