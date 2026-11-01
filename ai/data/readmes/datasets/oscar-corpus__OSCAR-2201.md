---
extra_gated_prompt: "**[IMPORTANT: We are forced to temporarily suspend access to OSCAR. The temporary nature of this suspension has led us to choose to implement it as gated access with manual control, and we will not grant any access until the situation has been clarified. We sincerely apologize for this situation and hope to be able to restore access as soon as possible. In the meantime, we remind you that we have always prohibited access to or use of OSCAR that violates the legislation in force where you are located. In France, for example, any use of OSCAR that does not fall within the framework of the so-called 'TDM' or the so-called 'research' exceptions to copyright has always been prohibited.]** By filling the form below, you understand that only the metadata and the annotations of OSCAR 22.01 have a cc0-1.0 license, and that the rest of the content is crawled data derived from the November/December 2021 snapshot of Common Crawl, for which the authors of OSCAR **do not** hold any copyright whatsoever."
extra_gated_fields:
 Name: text
 Email: text
 Affiliation: text
 Country: text
 Usecase: text
 I have explicitly check with my jurisdiction and I confirm that downloading OSCAR 2201 is legal in the country/region where I am located right now, and for the use case that I have described above: checkbox
pretty_name: OSCAR
annotations_creators:
- no-annotation
language_creators:
- found
language:
- af
- sq
- am
- ar
- an
- hy
- as
- ast
- av
- az
- bn
- ba
- eu
- be
- bh
- bpy
- bs
- br
- bg
- my
- ca
- ceb
- ckb
- ce
- zh
- cv
- kw
- hr
- cs
- da
- diq
- dv
- nl
- mhr
- arz
- en
- eo
- et
- tl
- fi
- fr
- gl
- ka
- de
- gom
- el
- gn
- gu
- he
- hi
- hu
- is
- io
- ilo
- id
- ia
- ga
- it
- ja
- jv
- xal
- kn
- krc
- kk
- km
- kv
- ko
- ku
- ky
- lo
- la
- lv
- lez
- li
- lt
- jbo
- lmo
- nds
- dsb
- lb
- mk
- mai
- mg
- ms
- ml
- mt
- mr
- mzn
- min
- xmf
- mn
- nah
- ne
- new
- no
- nn
- oc
- or
- os
- ps
- fa
- pms
- pl
- pt
- pa
- qu
- ro
- bxr
- ru
- sah
- sa
- gd
- sr
- sh
- scn
- sd
- si
- sk
- sl
- so
- azb
- es
- su
- sw
- sv
- tg
- ta
- tt
- te
- th
- bo
- als
- tr
- tk
- uk
- eml
- hsb
- ur
- ug
- uz
- vi
- vo
- wa
- war
- cy
- fy
- mrj
- pnb
- wuu
- yi
- yo
- mul
license:
- cc0-1.0
multilinguality:
- multilingual
source_datasets:
- original
task_categories:
- fill-mask
- text-generation
task_ids:
- language-modeling
paperswithcode_id: oscar
---

# Dataset Card for "oscar"

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

- **Homepage:** [https://oscar-corpus.com](https://oscar-corpus.com)
- **Repository:** [github.com/oscar-corpus/corpus](https://github.com/oscar-corpus/corpus)
- **Paper:** [Towards a Cleaner Document-Oriented Multilingual Crawled Corpus](https://oscar-corpus.com/publication/2022/arxiv/towards/)
- **Point of Contact:** [Contact](https://oscar-corpus.com/#contact)

### Dataset Summary

OSCAR or **O**pen **S**uper-large **C**rawled **A**ggregated co**R**pus is a huge multilingual corpus obtained by language classification and filtering of the [Common Crawl](https://commoncrawl.org/) corpus using the [ungoliant](https://github.com/oscar-corpus/ungoliant) architecture. Data is distributed by language in both original and deduplicated form.

**We are aware of the virus warnings issue. See discussion [here](https://huggingface.co/datasets/oscar-corpus/OSCAR-2201/discussions/12) for more info!**

### Usage

```py
from datasets import load_dataset


dataset = load_dataset("oscar-corpus/OSCAR-2201",
                        use_auth_token=True, # required
                        language="ar", 
                        streaming=True, # optional
                        split="train") # optional, but the dataset only has a train split

for d in dataset:
    print(d) # prints documents
```

### Supported Tasks and Leaderboards

OSCAR is mainly intended to pretrain language models and word representations.

### Languages

All the data is distributed by language, both the original and the deduplicated versions of the data are available. 151 different languages are available. The table in subsection [Data Splits Sample Size](#data-splits-sample-size) provides the language code for each subcorpus as well as the number of words (space separated tokens), lines and sizes for both the original and the deduplicated versions of OSCAR.

### Issues

OSCAR 22.01 may have quality issues on low size subcorpora, as it has been the case before.

Note that since the documents are identified as a whole, it is expected to have lines in other languages in a given language subcorpus.
As an example, it is known and expected that the German subcorpus contains documents holding lines identified as Swiss German / Alemannic.

**If you encounter something that is unexpected, please file an issue here: https://github.com/oscar-corpus/corpus/issues.**

|Language code|Language|Issues|
|-------------|--------|------|
|             |        |      |
## Dataset Structure

We show detailed information for all the configurations of the dataset.

### Data Instances

TODO

### Data Fields

* `id`: a `int64` feature.
* `content`: `string` Newline-separated content


* `warc_headers`: WARC Headers
* `warc_headers.content-length`: `int64` Content length (in bytes) **before** cleaning
* `warc_headers.content-type`: `string` MIME type
* `warc_headers.warc-block-digest`:`string` Algorithm name and calculated value of a digest applied to the full block of the record
* `warc_headers.warc-date`: `string` Crawl date (YYYY-MM-DDThh:mm:ssZ)
* `warc_headers.warc-identified-content-language`: `string` Comma-separated list of language identifications done by CommonCrawl (uses CLD3)
* `warc_headers.warc-record-id`: `string` Record ID
* `warc_headers.warc-refers-to`: `string` Record-ID of a single record for which the present record holds additional content
* `warc_headers.warc-target-uri`: `string` URI from where the content has been fetched
* `warc_headers.warc-type`: `string` Type of the WARC Record
* `metadata`: Metadata
* `metadata.identification.label`: `string` Language identification of the document
* `metadata.identification.prob`: `float` Confidence of the identification
* `metadata.annotation`: `[string]` Annnotations of the document. `null` if none present. (Is `None` if using `datasets`)
* `metadata.sentence_identifications`: `[string]` List of line identifications. `null`/`None` can be present for lines that failed the identification step.
* `meta.offset`: `int64` line offset where the related text begins. Should be used with `meta.nb_sentences` when reading the source files rather than using iterators to get related data.
* `text`: `string` content

See the [WARC Format standard](https://iipc.github.io/warc-specifications/specifications/warc-format/warc-1.1/#warc-type-mandatory) for more details on the `warc_headers` fields, and our [website](https://oscar-corpus.com/post/oscar-v22-01/) for more details about the format in general.

### Data Splits


<details>
  <summary>Click to expand the number of samples per configuration</summary>
</details>

## Table

| lang                        | size      | docs        | words           |
|:----------------------------|:----------|:------------|:----------------|
| _Multilingual_              | 12.1 GB   | 1,210,685   | 936,187,711     |
| Afrikaans                   | 47.0 MB   | 12,393      | 6,227,310       |
| Albanian                    | 3.0 GB    | 437,287     | 326,325,149     |
| Alemannic / Swiss German    | 363.6 kB  | 139         | 37,381          |
| Amharic                     | 461.0 MB  | 37,513      | 30,481,153      |
| Arabic                      | 84.2 GB   | 8,718,929   | 6,103,711,887   |
| Aragonese                   | 10.6 kB   | 12          | 51              |
| Armenian                    | 4.7 GB    | 379,267     | 268,031,270     |
| Assamese                    | 221.2 MB  | 17,084      | 11,109,557      |
| Asturian                    | 73.6 kB   | 77          | 3,919           |
| Avaric                      | 18.6 kB   | 14          | 582             |
| Azerbaijani                 | 3.5 GB    | 491,847     | 291,927,692     |
| Bangla                      | 15.1 GB   | 1,171,501   | 751,877,226     |
| Bashkir                     | 95.5 MB   | 11,198      | 5,418,474       |
| Basque                      | 1.1 GB    | 233,658     | 97,092,942      |
| Belarusian                  | 1.8 GB    | 180,046     | 107,227,860     |
| Bihari languages            | 24.2 kB   | 27          | 569             |
| Bishnupriya                 | 2.0 MB    | 271         | 98,419          |
| Bosnian                     | 10.3 kB   | 10          | 422             |
| Breton                      | 33.7 MB   | 16,119      | 3,111,619       |
| Bulgarian                   | 35.1 GB   | 2,887,115   | 2,405,981,285   |
| Burmese                     | 1.9 GB    | 158,733     | 44,835,970      |
| Catalan                     | 13.9 GB   | 2,627,307   | 1,508,919,864   |
| Cebuano                     | 44.6 MB   | 5,742       | 5,253,785       |
| Central Kurdish             | 716.4 MB  | 84,950      | 43,913,025      |
| Chechen                     | 14.0 MB   | 4,086       | 798,766         |
| Chinese                     | 900.9 GB  | 56,524,518  | 23,149,203,886  |
| Chuvash                     | 41.8 MB   | 4,750       | 2,465,782       |
| Cornish                     | 1.4 kB    | 2           | 55              |
| Croatian                    | 11.2 MB   | 11,462      | 505,369         |
| Czech                       | 58.6 GB   | 10,381,916  | 5,452,724,456   |
| Danish                      | 12.6 GB   | 2,265,479   | 1,454,439,292   |
| Dimli (individual language) | 706 Bytes | 1           | 19              |
| Divehi                      | 217.2 MB  | 24,067      | 10,112,205      |
| Dutch                       | 114.0 GB  | 20,206,532  | 12,329,127,151  |
| Eastern Mari                | 11.3 MB   | 1,612       | 641,525         |
| Egyptian Arabic             | 2.8 MB    | 1,256       | 176,096         |
| English                     | 3.2 TB    | 431,992,659 | 377,376,402,775 |
| Esperanto                   | 558.3 MB  | 111,932     | 58,416,628      |
| Estonian                    | 9.2 GB    | 1,362,524   | 820,975,443     |
| Filipino                    | 646.5 MB  | 70,394      | 81,881,278      |
| Finnish                     | 37.8 GB   | 4,948,961   | 2,900,615,928   |
| French                      | 382.2 GB  | 52,037,098  | 41,713,990,658  |
| Galician                    | 255.2 MB  | 88,803      | 27,051,212      |
| Georgian                    | 7.1 GB    | 488,588     | 281,430,479     |
| German                      | 496.7 GB  | 70,075,424  | 46,826,676,844  |
| Goan Konkani                | 787.2 kB  | 46          | 38,831          |
| Greek                       | 78.3 GB   | 6,738,546   | 5,031,242,803   |
| Guarani                     | 9.0 kB    | 10          | 374             |
| Gujarati                    | 4.8 GB    | 136,467     | 301,170,777     |
| Hebrew                      | 30.3 GB   | 3,132,396   | 2,249,377,984   |
| Hindi                       | 23.3 GB   | 1,529,907   | 1,534,799,198   |
| Hungarian                   | 53.9 GB   | 6,866,062   | 4,598,787,907   |
| Icelandic                   | 2.0 GB    | 396,183     | 210,365,124     |
| Ido                         | 77.3 kB   | 105         | 2,690           |
| Iloko                       | 97.9 kB   | 75          | 8,592           |
| Indonesian                  | 17.4 GB   | 2,244,622   | 1,984,195,207   |
| Interlingua                 | 40.2 kB   | 6           | 10,125          |
| Irish                       | 45.6 MB   | 12,233      | 4,877,850       |
| Italian                     | 229.3 GB  | 28,502,092  | 24,294,684,830  |
| Japanese                    | 258.7 GB  | 36,328,931  | 5,592,948,356   |
| Javanese                    | 152.7 kB  | 70          | 10,441          |
| Kalmyk                      | 9.3 kB    | 9           | 250             |
| Kannada                     | 2.6 GB    | 150,850     | 108,450,571     |
| Karachay-Balkar             | 119.6 kB  | 91          | 4,089           |
| Kazakh                      | 2.9 GB    | 261,085     | 157,267,307     |
| Khmer                       | 1.9 GB    | 121,910     | 30,564,131      |
| Komi                        | 119.9 kB  | 127         | 3,335           |
| Korean                      | 51.8 GB   | 5,881,481   | 3,854,968,649   |
| Kurdish                     | 150.3 MB  | 29,906      | 17,390,759      |
| Kyrgyz                      | 518.6 MB  | 62,244      | 28,028,986      |
| Lao                         | 337.1 MB  | 28,914      | 6,682,982       |
| Latin                       | 4.1 MB    | 4,397       | 187,446         |
| Latvian                     | 8.2 GB    | 1,032,987   | 707,361,898     |
| Lezghian                    | 375.5 kB  | 124         | 19,250          |
| Limburgish                  | 1.4 kB    | 2           | 41              |
| Lithuanian                  | 20.0 GB   | 2,303,070   | 1,712,802,056   |
| Lojban                      | 1.9 MB    | 570         | 260,542         |
| Lombard                     | 2.6 kB    | 2           | 225             |
| Low German                  | 9.0 MB    | 1,938       | 1,012,561       |
| Lower Sorbian               | 707 Bytes | 1           | 17              |
| Luxembourgish               | 15.8 MB   | 5,108       | 1,545,946       |
| Macedonian                  | 3.6 GB    | 341,775     | 244,058,579     |
| Maithili                    | 21.6 kB   | 23          | 483             |
| Malagasy                    | 57.3 MB   | 3,028       | 7,279,056       |
| Malay                       | 5.3 MB    | 5,228       | 217,818         |
| Malayalam                   | 4.1 GB    | 250,972     | 137,831,247     |
| Maltese                     | 2.5 MB    | 2,208       | 118,190         |
| Marathi                     | 3.3 GB    | 250,376     | 160,179,233     |
| Mazanderani                 | 128.2 kB  | 76          | 7,337           |
| Minangkabau                 | 6.0 MB    | 585         | 614,613         |
| Mingrelian                  | 7.6 MB    | 2,550       | 253,333         |
| Mongolian                   | 2.8 GB    | 237,719     | 176,405,432     |
| Nahuatl languages           | 8.7 kB    | 12          | 179             |
| Nepali                      | 3.7 GB    | 391,947     | 177,885,116     |
| Newari                      | 5.7 MB    | 1,134       | 273,837         |
| Norwegian                   | 2.8 GB    | 973,188     | 279,182,902     |
| Norwegian Nynorsk           | 6.8 MB    | 5,835       | 459,183         |
| Occitan                     | 2.1 MB    | 373         | 31,061          |
| Odia                        | 487.9 MB  | 52,942      | 23,755,902      |
| Ossetic                     | 13.9 MB   | 3,560       | 800,430         |
| Pashto                      | 490.3 MB  | 50,312      | 46,293,249      |
| Persian                     | 77.4 GB   | 7,665,871   | 6,430,164,396   |
| Piedmontese                 | 1.7 MB    | 698         | 188,270         |
| Polish                      | 139.0 GB  | 19,301,137  | 12,584,498,906  |
| Portuguese                  | 170.3 GB  | 23,735,707  | 18,441,864,893  |
| Punjabi                     | 1.1 GB    | 68,094      | 70,068,604      |
| Quechua                     | 744 Bytes | 1           | 14              |
| Romanian                    | 49.2 GB   | 4,624,764   | 5,261,803,995   |
| Russia Buriat               | 32.9 kB   | 39          | 785             |
| Russian                     | 1.1 TB    | 76,060,844  | 62,811,122,663  |
| Sakha                       | 65.6 MB   | 6,284       | 3,473,813       |
| Sanskrit                    | 136.0 MB  | 4,472       | 5,671,369       |
| Scottish Gaelic             | 137.7 kB  | 136         | 7,769           |
| Serbian                     | 6.9 GB    | 577,472     | 482,932,670     |
| Serbian (Latin)             | 931.8 kB  | 738         | 92,875          |
| Sicilian                    | 1.5 kB    | 2           | 50              |
| Sindhi                      | 117.1 MB  | 15,516      | 10,685,611      |
| Sinhala                     | 2.0 GB    | 108,593     | 113,179,741     |
| Slovak                      | 16.5 GB   | 2,409,555   | 1,619,121,944   |
| Slovenian                   | 1.2 GB    | 351,894     | 118,400,246     |
| Somali                      | 2.1 kB    | 3           | 109             |
| South Azerbaijani           | 14.1 MB   | 5,381       | 693,746         |
| Spanish                     | 381.9 GB  | 51,386,247  | 42,829,835,316  |
| Sundanese                   | 5.0 MB    | 263         | 547,145         |
| Swahili                     | 1.3 MB    | 462         | 123,050         |
| Swedish                     | 48.0 GB   | 7,541,278   | 5,078,331,128   |
| Tajik                       | 870.9 MB  | 46,366      | 56,627,727      |
| Tamil                       | 11.4 GB   | 556,772     | 452,343,748     |
| Tatar                       | 915.3 MB  | 76,398      | 51,875,265      |
| Telugu                      | 3.4 GB    | 249,756     | 137,752,065     |
| Thai                        | 66.1 GB   | 5,030,254   | 1,626,779,846   |
| Tibetan                     | 234.5 MB  | 18,683      | 2,286,269       |
| Turkish                     | 75.1 GB   | 10,826,031  | 6,421,221,358   |
| Turkmen                     | 4.4 MB    | 2,485       | 276,632         |
| Ukrainian                   | 48.8 GB   | 4,558,214   | 2,879,585,992   |
| Emiliano-Romagnolo[eml]     | 901 Bytes | 1           | 53              |
| Upper Sorbian               | 132.8 kB  | 110         | 8,825           |
| Urdu                        | 3.4 GB    | 336,994     | 332,816,354     |
| Uyghur                      | 201.9 MB  | 18,556      | 11,240,889      |
| Uzbek                       | 19.9 MB   | 9,526       | 1,370,842       |
| Vietnamese                  | 98.9 GB   | 9,587,233   | 12,283,185,482  |
| Volapük                     | 825.9 kB  | 661         | 57,039          |
| Walloon                     | 105.7 kB  | 138         | 4,386           |
| Waray                       | 7.6 MB    | 933         | 830,872         |
| Welsh                       | 409.3 MB  | 90,378      | 49,488,495      |
| Western Frisian             | 75.3 MB   | 21,946      | 6,357,929       |
| Western Mari                | 743.5 kB  | 155         | 43,916          |
| Western Panjabi             | 46.7 MB   | 6,790       | 4,060,419       |
| Wu Chinese                  | 137.2 kB  | 88          | 3,056           |
| Yiddish                     | 232.5 MB  | 23,418      | 15,809,780      |
| Yoruba                      | 24.7 kB   | 26          | 1,042           |


## Dataset Creation

### Curation Rationale

OSCAR was constructed using [`Ungoliant`](https://github.com/oscar-corpus/ungoliant), a new pipeline derived from [goclassy](https://github.com/oscar-corpus/goclassy), itself being derived from [fastText's one](https://github.com/facebookresearch/fastText).

The pipeline works on documents rather than lines. 
`Ungoliant` is implemented in the [Rust programming language](https://rust-lang.org), and uses [rayon](https://github.com/rayon-rs/rayon) as its data parallelism strategy. 
Threading is done at shard, record and sentence level, making the whole generation process much more efficient.

Filtering will be explained in a future blog post at our [website](https://oscar-corpus.com)

### Source Data

#### Initial Data Collection and Normalization

[Common Crawl](https://commoncrawl.org/) is a non-profit foundation which produces and maintains an open repository of web crawled data that is both accessible and analysable. Common Crawl's complete web archive consists of petabytes of data collected over 8 years of web crawling. The repository contains raw web page HTML data (WARC files), metdata extracts (WAT files) and plain text extracts (WET files). The organisation's crawlers has always respected [nofollow](http://microformats.org/wiki/rel-nofollow) and [robots.txt](https://www.robotstxt.org/) policies.

Each monthly Common Crawl snapshot is in itself a massive multilingual corpus, where every single file contains data coming from multiple web pages written in a large variety of languages and covering all possible types of topics.

To construct OSCAR the WET files of Common Crawl were used. These contain the extracted plain texts from the websites mostly converted to UTF-8, as well as headers containing the metatada of each crawled document. Each WET file comes compressed in gzip format and is stored on Amazon Web Services. In the case of OSCAR 22.01, the **November/December 2021** snapshot was used. It is composed by 64 000 compressed text files containing documents and their headers.

#### Who are the source language producers?

The data comes from multiple web pages in a large variety of languages.

### Annotations

The dataset does not contain any additional annotations.

#### Annotation process

N/A

#### Who are the annotators?

N/A

### Personal and Sensitive Information

Being constructed from Common Crawl, Personal and sensitive information might be present. This **must** be considered before training deep learning models with OSCAR, specially in the case of text-generation models.

## Considerations for Using the Data

### Social Impact of Dataset

OSCAR is intended to bring more data to a wide variety of lanuages, the aim of the corpus is to make large amounts of data available to lower resource languages in order to facilitate the pre-training of state-of-the-art language modeling architectures.

### Discussion of Biases

OSCAR is not properly filtered yet and this can be reflected on the models trained with it. Care is advised specially concerning biases of the resulting models.

### Other Known Limitations

The [fastText linear classifier](https://fasttext.cc) is limed both in performance and the variety of languages it can recognize, so the quality of some OSCAR sub-corpora might be lower than expected, specially for the lowest-resource langiuages. Some audits have already been done by [third parties](https://arxiv.org/abs/2010.14571).

## Additional Information

### Dataset Curators

The corpus was put together by [Julien Abadji](https://ujj.space), [Pedro Ortiz Suarez](https://portizs.eu/), [Benoît Sagot](http://pauillac.inria.fr/~sagot/), and [Laurent Romary](https://cv.archives-ouvertes.fr/laurentromary), during work done at [Inria](https://www.inria.fr/en), particularly at the [ALMAnaCH team](https://team.inria.fr/almanach/).

### Licensing Information

    These data are released under this licensing scheme
    We do not own any of the text from which these data has been extracted.
    We license the actual packaging of these data under the Creative Commons CC0 license ("no rights reserved") http://creativecommons.org/publicdomain/zero/1.0/
    To the extent possible under law, Inria has waived all copyright and related or neighboring rights to OSCAR
    This work is published from: France.

    Should you consider that our data contains material that is owned by you and should therefore not be reproduced here, please:
    * Clearly identify yourself, with detailed contact data such as an address, telephone number or email address at which you can be contacted.
    * Clearly identify the copyrighted work claimed to be infringed.
    * Clearly identify the material that is claimed to be infringing and information reasonably sufficient to allow us to locate the material.

    We will comply to legitimate requests by removing the affected sources from the next release of the corpus.

### Citation Information

```

@ARTICLE{2022arXiv220106642A,
       author = {{Abadji}, Julien and {Ortiz Suarez}, Pedro and {Romary}, Laurent and {Sagot}, Beno{\^\i}t},
        title = "{Towards a Cleaner Document-Oriented Multilingual Crawled Corpus}",
      journal = {arXiv e-prints},
     keywords = {Computer Science - Computation and Language},
         year = 2022,
        month = jan,
          eid = {arXiv:2201.06642},
        pages = {arXiv:2201.06642},
archivePrefix = {arXiv},
       eprint = {2201.06642},
 primaryClass = {cs.CL},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2022arXiv220106642A},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
      
@inproceedings{AbadjiOrtizSuarezRomaryetal.2021,
  author    = {Julien Abadji and Pedro Javier Ortiz Su{\'a}rez and Laurent Romary and Beno{\^i}t Sagot},
  title     = {Ungoliant: An optimized pipeline for the generation of a very large-scale multilingual web corpus},
  series = {Proceedings of the Workshop on Challenges in the Management of Large Corpora (CMLC-9) 2021. Limerick, 12 July 2021 (Online-Event)},
  editor    = {Harald L{\"u}ngen and Marc Kupietz and Piotr Bański and Adrien Barbaresi and Simon Clematide and Ines Pisetta},
  publisher = {Leibniz-Institut f{\"u}r Deutsche Sprache},
  address   = {Mannheim},
  doi       = {10.14618/ids-pub-10468},
  url       = {https://nbn-resolving.org/urn:nbn:de:bsz:mh39-104688},
  pages     = {1 -- 9},
  year      = {2021},
  abstract  = {Since the introduction of large language models in Natural Language Processing, large raw corpora have played a crucial role in Computational Linguistics. However, most of these large raw corpora are either available only for English or not available to the general public due to copyright issues. Nevertheless, there are some examples of freely available multilingual corpora for training Deep Learning NLP models, such as the OSCAR and Paracrawl corpora. However, they have quality issues, especially for low-resource languages. Moreover, recreating or updating these corpora is very complex. In this work, we try to reproduce and improve the goclassy pipeline used to create the OSCAR corpus. We propose a new pipeline that is faster, modular, parameterizable, and well documented. We use it to create a corpus similar to OSCAR but larger and based on recent data. Also, unlike OSCAR, the metadata information is at the document level. We release our pipeline under an open source license and publish the corpus under a research-only license.},
  language  = {en}
}

@ARTICLE{caswell-etal-2021-quality,
       author = {{Caswell}, Isaac and {Kreutzer}, Julia and {Wang}, Lisa and {Wahab}, Ahsan and {van Esch}, Daan and {Ulzii-Orshikh}, Nasanbayar and {Tapo}, Allahsera and {Subramani}, Nishant and {Sokolov}, Artem and {Sikasote}, Claytone and {Setyawan}, Monang and {Sarin}, Supheakmungkol and {Samb}, Sokhar and {Sagot}, Beno{\^\i}t and {Rivera}, Clara and {Rios}, Annette and {Papadimitriou}, Isabel and {Osei}, Salomey and {Ortiz Su{\'a}rez}, Pedro Javier and {Orife}, Iroro and {Ogueji}, Kelechi and {Niyongabo}, Rubungo Andre and {Nguyen}, Toan Q. and {M{\"u}ller}, Mathias and {M{\"u}ller}, Andr{\'e} and {Hassan Muhammad}, Shamsuddeen and {Muhammad}, Nanda and {Mnyakeni}, Ayanda and {Mirzakhalov}, Jamshidbek and {Matangira}, Tapiwanashe and {Leong}, Colin and {Lawson}, Nze and {Kudugunta}, Sneha and {Jernite}, Yacine and {Jenny}, Mathias and {Firat}, Orhan and {Dossou}, Bonaventure F.~P. and {Dlamini}, Sakhile and {de Silva}, Nisansa and {{\c{C}}abuk Ball{\i}}, Sakine and {Biderman}, Stella and {Battisti}, Alessia and {Baruwa}, Ahmed and {Bapna}, Ankur and {Baljekar}, Pallavi and {Abebe Azime}, Israel and {Awokoya}, Ayodele and {Ataman}, Duygu and {Ahia}, Orevaoghene and {Ahia}, Oghenefego and {Agrawal}, Sweta and {Adeyemi}, Mofetoluwa},
        title = "{Quality at a Glance: An Audit of Web-Crawled Multilingual Datasets}",
      journal = {arXiv e-prints},
     keywords = {Computer Science - Computation and Language, Computer Science - Artificial Intelligence},
         year = 2021,
        month = mar,
          eid = {arXiv:2103.12028},
        pages = {arXiv:2103.12028},
archivePrefix = {arXiv},
       eprint = {2103.12028},
 primaryClass = {cs.CL},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2021arXiv210312028C},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@inproceedings{ortiz-suarez-etal-2020-monolingual,
    title = "A Monolingual Approach to Contextualized Word Embeddings for Mid-Resource Languages",
    author = "Ortiz Su{'a}rez, Pedro Javier  and
      Romary, Laurent  and
      Sagot, Benoit",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.acl-main.156",
    pages = "1703--1714",
    abstract = "We use the multilingual OSCAR corpus, extracted from Common Crawl via language classification, filtering and cleaning, to train monolingual contextualized word embeddings (ELMo) for five mid-resource languages. We then compare the performance of OSCAR-based and Wikipedia-based ELMo embeddings for these languages on the part-of-speech tagging and parsing tasks. We show that, despite the noise in the Common-Crawl-based OSCAR data, embeddings trained on OSCAR perform much better than monolingual embeddings trained on Wikipedia. They actually equal or improve the current state of the art in tagging and parsing for all five languages. In particular, they also improve over multilingual Wikipedia-based contextual embeddings (multilingual BERT), which almost always constitutes the previous state of the art, thereby showing that the benefit of a larger, more diverse corpus surpasses the cross-lingual benefit of multilingual embedding architectures.",
}

@inproceedings{OrtizSuarezSagotRomary2019,
  author    = {Pedro Javier {Ortiz Su{'a}rez} and Benoit Sagot and Laurent Romary},
  title     = {Asynchronous pipelines for processing huge corpora on medium to low resource infrastructures},
  series = {Proceedings of the Workshop on Challenges in the Management of Large Corpora (CMLC-7) 2019. Cardiff, 22nd July 2019},
  editor    = {Piotr Bański and Adrien Barbaresi and Hanno Biber and Evelyn Breiteneder and Simon Clematide and Marc Kupietz and Harald L{"u}ngen and Caroline Iliadi},
  publisher = {Leibniz-Institut f{"u}r Deutsche Sprache},
  address   = {Mannheim},
  doi       = {10.14618/ids-pub-9021},
  url       = {http://nbn-resolving.de/urn:nbn:de:bsz:mh39-90215},
  pages     = {9 -- 16},
  year      = {2019},
  abstract  = {Common Crawl is a considerably large, heterogeneous multilingual corpus comprised of crawled documents from the internet, surpassing 20TB of data and distributed as a set of more than 50 thousand plain text files where each contains many documents written in a wide variety of languages. Even though each document has a metadata block associated to it, this data lacks any information about the language in which each document is written, making it extremely difficult to use Common Crawl for monolingual applications. We propose a general, highly parallel, multithreaded pipeline to clean and classify Common Crawl by language; we specifically design it so that it runs efficiently on medium to low resource infrastructures where I/O speeds are the main constraint. We develop the pipeline so that it can be easily reapplied to any kind of heterogeneous corpus and so that it can be parameterised to a wide range of infrastructures. We also distribute a 6.3TB version of Common Crawl, filtered, classified by language, shuffled at line level in order to avoid copyright issues, and ready to be used for NLP applications.},
  language  = {en}
}

```

### Contributions

Thanks to [@pjox](https://github.com/pjox), [@Uinelj](https://github.com/Uinelj) and [@lhoestq](https://github.com/lhoestq) for adding this dataset.
