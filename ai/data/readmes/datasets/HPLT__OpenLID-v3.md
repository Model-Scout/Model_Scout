---
license: other
task_categories:
- text-classification
language:
- ace
- afr
- af
- als
- amh
- am
- ara
- ar
- asm
- as
- ast
- awa
- ayr
- azb
- azj
- bak
- ba
- bam
- bm
- ban
- bel
- be
- bem
- ben
- bn
- bho
- bjn
- bod
- bo
- bos
- bs
- bug
- bul
- bg
- cat
- ca
- ceb
- ces
- cs
- cjk
- ckb
- cmn
- crh
- cym
- cy
- dan
- da
- deu
- de
- dik
- dzo
- dz
- ekk
- ell
- el
- eng
- en
- epo
- eo
- eus
- eu
- ewe
- ee
- fao
- fo
- fas
- fa
- fij
- fj
- fil
- fin
- fi
- fon
- fra
- fr
- frp
- fur
- fuv
- gaz
- gla
- gd
- gle
- ga
- glg
- gl
- gug
- guj
- gu
- hat
- ht
- hau
- ha
- heb
- he
- hin
- hi
- hne
- hrv
- hr
- hun
- hu
- hye
- hy
- ibo
- ig
- ilo
- ind
- id
- isl
- is
- ita
- it
- jav
- jv
- jpn
- ja
- kab
- kac
- kam
- kan
- kn
- kas
- ks
- kat
- ka
- kaz
- kk
- kbp
- kea
- khk
- khm
- km
- kik
- ki
- kin
- rw
- kir
- ky
- kmb
- kmr
- knc
- kor
- ko
- ktu
- lao
- lo
- lat
- la
- lij
- lim
- li
- lin
- ln
- lit
- lt
- lmo
- ltg
- ltz
- lb
- lua
- lug
- lg
- luo
- lus
- lvs
- mag
- mai
- mal
- ml
- mar
- mr
- min
- mkd
- mk
- mlt
- mt
- mni
- mos
- mri
- mi
- mya
- my
- nld
- nl
- nno
- nn
- nob
- nb
- npi
- nso
- nus
- nya
- ny
- oci
- oc
- ory
- pag
- pan
- pa
- pap
- pbt
- plt
- pol
- pl
- por
- pt
- quy
- ron
- ro
- run
- rn
- rus
- ru
- sag
- sg
- san
- sa
- sat
- scn
- shn
- sin
- si
- slk
- sk
- slv
- sl
- smo
- sm
- sna
- sn
- snd
- sd
- som
- so
- sot
- st
- spa
- es
- srd
- sc
- srp
- sr
- ssw
- ss
- sun
- su
- swe
- sv
- swh
- szl
- tam
- ta
- taq
- tat
- tt
- tel
- te
- tgk
- tg
- tha
- th
- tir
- ti
- tpi
- tsn
- tn
- tso
- ts
- tuk
- tk
- tum
- tur
- tr
- twi
- tw
- uig
- ug
- ukr
- uk
- umb
- urd
- ur
- uzn
- vec
- vie
- vi
- war
- wol
- wo
- xho
- xh
- ydd
- yor
- yo
- yue
- zgh
- zsm
- zul
- zu
---
## Dataset Description

OpenLID-v3 is an updated version of the [OpenLID-v2 dataset](https://huggingface.co/datasets/laurievb/OpenLID-v2) (see the [CHANGELOG.md](https://huggingface.co/datasets/HPLT/OpenLID-v3/blob/main/CHANGELOG.md)).

- **Repository:** https://github.com/hplt-project/openlid
- **Paper:** [OpenLID-v3: Improving the Precision of Closely Related Language Identification – An Experience Report](https://aclanthology.org/2026.vardial-1.23/)

### Usage

```
from datasets import load_dataset

ds = load_dataset('HPLT/OpenLID-v3', split='train')
```

### Dataset Summary

The OpenLID-v3 dataset covers 194 language varieties + not-a-language class

### Supported tasks
This dataset is intended for training high-coverage language identification models. The language variety labels are compatible with the [FLORES+](https://huggingface.co/datasets/openlanguagedata/flores_plus) evaluation benchmark. We provide [a script](https://github.com/hplt-project/openlid#training) to prepare the OpenLID-v3 dataset for training a language identification model.

## Dataset Structure

### Data Instances

Each entry in the dataset consists of a line of data (`text`), a language label consisting of an ISO 639-3 language code plus an ISO 15924 script code (`language`), and a tag indicating the source (`source`).

```json
{
  "text": "¿Serás exaltada hasta el cielo?",
  "language": "spa_Latn",
  "source": "lti" 
}
```

### Data Splits

Only a train split is provided. 

## Considerations for Using the Data

### Social Impact of Dataset

This dataset covers a number of under-served languages. This makes it a potentially useful resource, but due to the limited amount of data and domains covered, care must be taken not to overclaim performance or coverage.

### Discussion of Biases

Our work aims to broaden natural language processing coverage by allowing practitioners to identify relevant data in more languages. However, we note that language identification is inherently a normative activity that risks excluding minority dialects, scripts, or entire microlanguages from a macrolanguage. Choosing which languages to cover may reinforce power imbalances, as only some groups gain access to language processing technologies.

In addition, errors in language identification can have a significant impact on downstream performance, particularly (as is often the case) when a system is used as a 'black box'. The performance of our classifier is not equal across languages which could lead to worse downstream performance for particular groups. We mitigate this by providing metrics by class.

### Licensing Information

License considerations for each source are available in the [`licenses` directory](https://huggingface.co/datasets/HPLT/OpenLID-v3/tree/main/licenses) in this repository. Open use for non-commercial purposes is covered by all licences.

If you view any part of this dataset as a violation of your intellectual property rights, please let us know and we will remove it. 

### Citation Information

If you use this dataset, please cite all the authors [in the citation file](https://huggingface.co/datasets/HPLT/OpenLID-v3/blob/main/citations.bib) who compiled the source datasets, plus the OpenLID papers:

```bibtex
@inproceedings{fedorova-etal-2026-openlid,
    title = "{O}pen{LID}-v3: Improving the Precision of Closely Related Language Identification {--} An Experience Report",
    author = "Fedorova, Mariia  and
      Arefyev, Nikolay  and
      Buljan, Maja  and
      Helcl, Jind{\v{r}}ich  and
      Oepen, Stephan  and
      R{\o}nningstad, Egil  and
      Scherrer, Yves",
    editor = {Scherrer, Yves  and
      Aepli, No{\"e}mi  and
      Blaschke, Verena  and
      Jauhiainen, Tommi  and
      Ljube{\v{s}}i{\'c}, Nikola  and
      Nakov, Preslav  and
      Tiedemann, J{\"o}rg  and
      Zampieri, Marcos},
    booktitle = "Proceedings of the 13th Workshop on {NLP} for Similar Languages, Varieties and Dialects",
    month = mar,
    year = "2026",
    address = "Rabat, Morocco",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.vardial-1.23/",
    doi = "10.18653/v1/2026.vardial-1.23",
    pages = "275--292",
    abstract = "Language identification (LID) is an essential step in building high-quality multilingual datasets from web data. Existing LID tools (such as OpenLID or GlotLID) often struggle to identify closely related languages and to distinguish valid natural language from noise, which contaminates language-specific subsets, especially for low-resource languages. In this work we extend the OpenLID classifier by adding more training data, merging problematic language variant clusters, and introducing a special label for marking noise. We call this extended system OpenLID-v3 and evaluate it against GlotLID on multiple benchmarks. During the development we focus on three groups of closely related languages (Bosnian, Croatian, and Serbian; Romance varieties of Northern Italy and Southern France; and Scandinavian languages) and contribute new evaluation datasets where existing ones are inadequate. We find that ensemble approaches improve precision but also substantially reduce coverage for low-resource languages."
}
```

```bibtex
@inproceedings{burchell-etal-2023-open,
    title = "An Open Dataset and Model for Language Identification",
    author = "Burchell, Laurie  and
      Birch, Alexandra  and
      Bogoychev, Nikolay  and
      Heafield, Kenneth",
    editor = "Rogers, Anna  and
      Boyd-Graber, Jordan  and
      Okazaki, Naoaki",
    booktitle = "Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)",
    month = jul,
    year = "2023",
    address = "Toronto, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.acl-short.75",
    doi = "10.18653/v1/2023.acl-short.75",
    pages = "865--879",
    abstract = "Language identification (LID) is a fundamental step in many natural language processing pipelines. However, current LID systems are far from perfect, particularly on lower-resource languages. We present a LID model which achieves a macro-average F1 score of 0.93 and a false positive rate of 0.033{\%} across 201 languages, outperforming previous work. We achieve this by training on a curated dataset of monolingual data, which we audit manually to ensure reliability. We make both the model and the dataset available to the research community. Finally, we carry out detailed analysis into our model{'}s performance, both in comparison to existing open models and by language class.",
}
```

[![arXiv](https://img.shields.io/badge/arXiv-2602.13139-b31b1b.svg)](https://arxiv.org/abs/2602.13139)
[![arXiv](https://img.shields.io/badge/arXiv-2305.13820-b31b1b.svg)](https://arxiv.org/abs/2305.13820)