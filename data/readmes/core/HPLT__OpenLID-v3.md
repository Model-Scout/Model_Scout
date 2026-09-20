---
license: gpl-3.0
library_name: fasttext
tags:
- text-classification
- language-identification
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
datasets:
- HPLT/OpenLID-v3
---

# OpenLID-v3

- **Model type:** Text classification (language identification)
- **License:** gpl-3.0

## Model description

OpenLID-v3 is a high-coverage, high-performance language identification model. It is an improved version of [OpenLID-v2](https://huggingface.co/laurievb/OpenLID-v2).

The original model and training data are described in [Burchell et al. (2023)](https://aclanthology.org/2023.acl-short.75/), [the OpenLID-v2 dataset repo](https://huggingface.co/datasets/laurievb/OpenLID-v2).
This model is described in the [OpenLID-v3 paper](https://arxiv.org/abs/2602.13139).

### How to use

> [!WARNING]  
> `fasttext` requires `numpy` <2.0

Here is how to use this model to detect the language of a given text. For best results, text should be preprocessed

```shell
pip install fasttext==0.9.3 huggingface-hub==0.35.3 numpy==1.23.5 regex==2024.4.28
```

```python
import fasttext
from huggingface_hub import hf_hub_download
import regex

# defines what we want to remove from string for langID
NONWORD_REPLACE_STR = r"[^\p{Word}\p{Zs}]|\d"  # either (not a word nor a space) or (is digit)
NONWORD_REPLACE_PATTERN = regex.compile(NONWORD_REPLACE_STR)
SPACE_PATTERN = regex.compile(r"\s\s+")  # squeezes sequential whitespace


def preprocess(text):
    text = text.strip().replace('\n', ' ').lower()
    text = regex.sub(SPACE_PATTERN, " ", text)
    text = regex.sub(NONWORD_REPLACE_PATTERN, "", text)
    return text

model_path = hf_hub_download(
    repo_id="HPLT/OpenLID-v3", filename="openlid-v3.bin",
) # may take some time
model = fasttext.load_model(model_path)
text = "Maskinsjefen er oppteken av å løfta fram dei maritime utdanningane."
text = preprocess(text)
print(
      model.predict(
          text=text,
          k=1,
          threshold=0.5,
          on_unicode_error="strict",
      ),
)
# should output: (('__label__nno_Latn',), array([0.99999893]))
```

### Limitations and bias

The dataset and model cover 194 language varieties. However, some language varieties (e.g. Arabic dialects) are very hard to distinguish and in practice, it may only be possible to classify an input at the macrolanguage level.

Our work aims to broaden NLP coverage by allowing practitioners to identify relevant data in more languages. However, we note that LID is inherently a normative activity that risks excluding minority dialects, scripts, or entire microlanguages from a macrolanguage. Choosing which languages to cover may reinforce power imbalances, as only some groups gain access to NLP technologies. In addition, errors in LID can have a significant impact on downstream performance, particularly (as is often the case) when a system is used as a ‘black box’. The performance of our classifier is not equal across languages which could lead to worse downstream performance for particular groups. We mitigate this by providing metrics by class.

## Training data

The model was trained on the samples from [OpenLID-v2 dataset](https://huggingface.co/datasets/laurievb/OpenLID-v2), [glotlid-corpus](https://huggingface.co/datasets/cis-lmu/glotlid-corpus) and [Wikipedia](https://dumps.wikimedia.org/backup-index.html). The data was normalised and classes were up/downsampled with temperature sampling prior to training; code to do this can be found in [the OpenLID-v3 repository](https://github.com/hplt-project/openlid).

## Training procedure

The model was trained using fastText with the following hyperparameters set. All other hyperparameters were set to their default values.

* loss: softmax
* epochs: 2
* learning rate: 0.8
* minimum number of word occurances: 1000
* embedding dimension: 256
* character n-grams: 2-5
* word n-grams: 1
* bucket size: 1,000,000
* threads: 68


### Evaluation datasets

Evaluation details are available in [the paper repository](https://github.com/hplt-project/openlid-v3-evaluation/tree/main).

### BibTeX entry and citation info

```
@misc{fedorova2026openlidv3improvingprecisionclosely,
      title={OpenLID-v3: Improving the Precision of Closely Related Language Identification -- An Experience Report}, 
      author={Mariia Fedorova and Nikolay Arefyev and Maja Buljan and Jindřich Helcl and Stephan Oepen and Egil Rønningstad and Yves Scherrer},
      year={2026},
      eprint={2602.13139},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2602.13139}, 
}
```

```
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

This project has received funding from the European Union’s Horizon Europe research and innovation programme under grant agreement No 101070350 and from UK Research and Innovation (UKRI) under the UK government’s Horizon Europe funding guarantee [grant number 10052546].