---
annotations_creators:
- crowdsourced
- expert-generated
language_creators:
- found
language:
- ace
- af
- ak
- am
- an
- ang
- ar
- ary
- as
- ast
- az
- ba
- bal
- be
- bem
- ber
- bg
- bho
- bn
- bo
- br
- brx
- bs
- bua
- byn
- ca
- ce
- ceb
- chr
- ckb
- co
- crh
- cs
- csb
- cv
- cy
- da
- de
- dsb
- dv
- dz
- el
- en
- eo
- es
- et
- eu
- fa
- ff
- fi
- fil
- fo
- fr
- frm
- frp
- fur
- fy
- ga
- gd
- gl
- gn
- grc
- gu
- guc
- gv
- ha
- haw
- he
- hi
- hil
- hne
- hr
- hsb
- ht
- hu
- hy
- ia
- id
- ig
- io
- is
- it
- iu
- ja
- jbo
- jv
- ka
- kab
- kg
- kk
- kl
- km
- kn
- ko
- kok
- ks
- ksh
- ku
- kw
- ky
- la
- lb
- lg
- li
- lij
- lld
- ln
- lo
- lt
- ltg
- lv
- mai
- mg
- mh
- mhr
- mi
- miq
- mk
- ml
- mn
- mr
- ms
- mt
- mus
- my
- nan
- nap
- nb
- nds
- ne
- nhn
- nl
- nn
- 'no'
- nso
- ny
- oc
- om
- or
- os
- pa
- pam
- pap
- pl
- pms
- pmy
- ps
- pt
- qu
- rm
- ro
- rom
- ru
- rw
- sa
- sc
- sco
- sd
- se
- shn
- shs
- si
- sk
- sl
- sm
- sml
- sn
- so
- son
- sq
- sr
- st
- sv
- sw
- syr
- szl
- ta
- te
- tet
- tg
- th
- ti
- tk
- tl
- tlh
- tr
- trv
- ts
- tt
- ug
- uk
- ur
- uz
- ve
- vec
- vi
- wa
- wae
- wo
- xal
- xh
- yi
- yo
- zh
- zu
- zza
license:
- bsd-3-clause
multilinguality:
- multilingual
size_categories:
- 10K<n<100K
- 1K<n<10K
- n<1K
source_datasets:
- original
task_categories:
- translation
task_ids: []
pretty_name: Opus Ubuntu
config_names:
- as-bs
- az-cs
- bg-de
- bn-ga
- br-es_PR
- br-hi
- br-la
- br-uz
- br-yi
- bs-szl
language_bcp47:
- ar-SY
- bn-IN
- de-AT
- de-DE
- en-AU
- en-CA
- en-GB
- en-NZ
- en-US
- es-AR
- es-CL
- es-CO
- es-CR
- es-DO
- es-EC
- es-ES
- es-GT
- es-HN
- es-MX
- es-NI
- es-PA
- es-PE
- es-PR
- es-SV
- es-UY
- es-VE
- fa-AF
- fr-CA
- fr-FR
- nl-NL
- pt-BR
- pt-PT
- ta-LK
- zh-CN
- zh-HK
- zh-TW
dataset_info:
- config_name: as-bs
  features:
  - name: id
    dtype: string
  - name: translation
    dtype:
      translation:
        languages:
        - as
        - bs
  splits:
  - name: train
    num_bytes: 1037799
    num_examples: 8583
  download_size: 470874
  dataset_size: 1037799
- config_name: az-cs
  features:
  - name: id
    dtype: string
  - name: translation
    dtype:
      translation:
        languages:
        - az
        - cs
  splits:
  - name: train
    num_bytes: 17809
    num_examples: 293
  download_size: 14637
  dataset_size: 17809
- config_name: bg-de
  features:
  - name: id
    dtype: string
  - name: translation
    dtype:
      translation:
        languages:
        - bg
        - de
  splits:
  - name: train
    num_bytes: 27615
    num_examples: 184
  download_size: 16278
  dataset_size: 27615
- config_name: bn-ga
  features:
  - name: id
    dtype: string
  - name: translation
    dtype:
      translation:
        languages:
        - bn
        - ga
  splits:
  - name: train
    num_bytes: 584617
    num_examples: 7324
  download_size: 272247
  dataset_size: 584617
- config_name: br-es_PR
  features:
  - name: id
    dtype: string
  - name: translation
    dtype:
      translation:
        languages:
        - br
        - es_PR
  splits:
  - name: train
    num_bytes: 8863
    num_examples: 125
  download_size: 8194
  dataset_size: 8863
- config_name: br-hi
  features:
  - name: id
    dtype: string
  - name: translation
    dtype:
      translation:
        languages:
        - br
        - hi
  splits:
  - name: train
    num_bytes: 1300057
    num_examples: 15551
  download_size: 641803
  dataset_size: 1300057
- config_name: br-la
  features:
  - name: id
    dtype: string
  - name: translation
    dtype:
      translation:
        languages:
        - br
        - la
  splits:
  - name: train
    num_bytes: 29329
    num_examples: 527
  download_size: 17723
  dataset_size: 29329
- config_name: br-uz
  features:
  - name: id
    dtype: string
  - name: translation
    dtype:
      translation:
        languages:
        - br
        - uz
  splits:
  - name: train
    num_bytes: 110266
    num_examples: 1416
  download_size: 62660
  dataset_size: 110266
- config_name: br-yi
  features:
  - name: id
    dtype: string
  - name: translation
    dtype:
      translation:
        languages:
        - br
        - yi
  splits:
  - name: train
    num_bytes: 172834
    num_examples: 2799
  download_size: 77870
  dataset_size: 172834
- config_name: bs-szl
  features:
  - name: id
    dtype: string
  - name: translation
    dtype:
      translation:
        languages:
        - bs
        - szl
  splits:
  - name: train
    num_bytes: 41104
    num_examples: 646
  download_size: 30035
  dataset_size: 41104
configs:
- config_name: as-bs
  data_files:
  - split: train
    path: as-bs/train-*
- config_name: az-cs
  data_files:
  - split: train
    path: az-cs/train-*
- config_name: bg-de
  data_files:
  - split: train
    path: bg-de/train-*
- config_name: bn-ga
  data_files:
  - split: train
    path: bn-ga/train-*
- config_name: br-es_PR
  data_files:
  - split: train
    path: br-es_PR/train-*
- config_name: br-hi
  data_files:
  - split: train
    path: br-hi/train-*
- config_name: br-la
  data_files:
  - split: train
    path: br-la/train-*
- config_name: br-uz
  data_files:
  - split: train
    path: br-uz/train-*
- config_name: br-yi
  data_files:
  - split: train
    path: br-yi/train-*
- config_name: bs-szl
  data_files:
  - split: train
    path: bs-szl/train-*
---

# Dataset Card for Opus Ubuntu

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

- **Homepage:** http://opus.nlpl.eu/Ubuntu.php
- **Repository:** None
- **Paper:** http://www.lrec-conf.org/proceedings/lrec2012/pdf/463_Paper.pdf
- **Leaderboard:** [More Information Needed]
- **Point of Contact:** [More Information Needed]

### Dataset Summary

These are translations of the Ubuntu software package messages, donated by the Ubuntu community.

To load a language pair which isn't part of the config, all you need to do is specify the language code as pairs.
You can find the valid pairs in Homepage section of Dataset Description: http://opus.nlpl.eu/Ubuntu.php
E.g.

`dataset = load_dataset("opus_ubuntu", lang1="it", lang2="pl")`


### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

[More Information Needed]

## Dataset Structure

### Data Instances

Example instance:

```
{
  'id': '0', 
  'translation': {
    'it': 'Comprende Gmail, Google Docs, Google+, YouTube e Picasa',
    'pl': 'Zawiera Gmail, Google Docs, Google+, YouTube oraz Picasa'
  }
}
```

### Data Fields

Each instance has two fields:
- **id**: the id of the example
- **translation**: a dictionary containing translated texts in two languages.

### Data Splits

Each subset simply consists in a train set. We provide the number of examples for certain language pairs:

|          |   train |
|:---------|--------:|
| as-bs    |    8583 |
| az-cs    |     293 |
| bg-de    |     184 |
| br-es_PR |     125 |
| bn-ga    |    7324 |
| br-hi    |   15551 |
| br-la    |     527 |
| bs-szl   |     646 |
| br-uz    |    1416 |
| br-yi    |    2799 |

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

[More Information Needed]

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

[More Information Needed]

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

BSD "Revised" license (see (https://help.launchpad.net/Legal#Translations_copyright)[https://help.launchpad.net/Legal#Translations_copyright])

### Citation Information

```bibtex
@InProceedings{TIEDEMANN12.463,
  author = {J{\"o}rg Tiedemann},
  title = {Parallel Data, Tools and Interfaces in OPUS},
  booktitle = {Proceedings of the Eight International Conference on Language Resources and Evaluation (LREC'12)},
  year = {2012},
  month = {may},
  date = {23-25},
  address = {Istanbul, Turkey},
  editor = {Nicoletta Calzolari (Conference Chair) and Khalid Choukri and Thierry Declerck and Mehmet Ugur Dogan and Bente Maegaard and Joseph Mariani and Jan Odijk and Stelios Piperidis},
  publisher = {European Language Resources Association (ELRA)},
  isbn = {978-2-9517408-7-7},
  language = {english}
 }
```

### Contributions

Thanks to [@rkc007](https://github.com/rkc007) for adding this dataset.