---
license: cc
language:
- ach
- ada
- adh
- aeb
- afr
- alz
- amh
- anu
- ara
- asm
- bem
- ben
- bod
- bxk
- cat
- cce
- ckb
- crk
- csw
- ctu
- dag
- dan
- deu
- dga
- din
- dje
- ell
- eng
- epo
- ewe
- fas
- fat
- fra
- ful
- gaa
- gjn
- guj
- gur
- guz
- gyn
- hat
- hau
- hbs
- hch
- her
- hin
- hun
- hus
- ind
- ita
- jam
- jpn
- kam
- kan
- kau
- kdj
- keo
- khm
- kik
- kin
- kln
- kmr
- kok
- koo
- kor
- kpz
- kqn
- kri
- kru
- ktz
- kua
- kwn
- laj
- lat
- lgg
- lin
- lit
- lko
- loz
- lsm
- luc
- lue
- lug
- lun
- luo
- lwg
- mal
- mar
- mas
- mat
- maz
- mer
- mfe
- mhi
- mhw
- miu
- mlg
- mmc
- mnw
- mqu
- msa
- mya
- myx
- naq
- nbl
- nch
- ndo
- nep
- nhe
- nhw
- nld
- nle
- nno
- nob
- nor
- nso
- nuj
- nya
- nyn
- nyu
- nzi
- ocu
- old
- ori
- orm
- pan
- pcm
- pmq
- pol
- por
- prs
- pus
- rki
- ron
- rus
- sag
- san
- saq
- sck
- sme
- som
- sot
- spa
- sqi
- srp
- ssw
- swa
- swe
- tam
- tel
- teo
- tet
- tgl
- tha
- tir
- toh
- toi
- tsc
- tsn
- tso
- ttj
- tum
- tur
- tuv
- twi
- ukr
- urd
- ven
- vie
- xho
- xog
- xsm
- yor
- yua
- yue
- zho
- zne
- zul
pretty_name: GlotStoryBook Corpus
tags:
- storybook
- book
- story
- language-identification
- nalibali
- machine-translation
configs:
- config_name: default
  data_files:
  - split: train
    path: GlotStoryBook.csv
- config_name: nalibali
  data_files:
  - split: train
    path: nalibali.csv
task_categories:
- translation
- text-generation
- summarization
---

## Dataset Description

Story Books for 180 ISO-639-3 codes. 

The `Parallel ID` or `parallel_id` can be used to find the parallel documents in different languages and build a parallel dataset.


This dataset consists of 2 subsets:

- **default**, which consists of 4 publishers:
  1. asp: [African Storybook](https://africanstorybook.org)
  2. pb: [Pratham Books](https://prathambooks.org/)
  3. lcb: [Little Cree Books](http://littlecreebooks.com/)
  4. lida: [LIDA Stories](https://lidastories.net/)


- **nalibali**, which comes from [Nal'ibali](https://nalibali.org/story-resources/multilingual-stories) stories.


## Usage (HF Loader)

- default:

```python
from datasets import load_dataset
dataset = load_dataset('cis-lmu/GlotStoryBook', 'default', split='train')
print(dataset[0]) # First row of default data
```

- nalibali:

```python
from datasets import load_dataset
dataset = load_dataset('cis-lmu/GlotStoryBook', 'nalibali', split='train')
print(dataset[0]) # First row of nalibali data
```


## Download
If you are not a fan of the HF dataloader, download it directly:

- default:

```python
! wget https://huggingface.co/datasets/cis-lmu/GlotStoryBook/resolve/main/GlotStoryBook.csv
```

- nalibali:

```python
! wget https://huggingface.co/datasets/cis-lmu/GlotStoryBook/resolve/main/nalibali.csv
```

# Tools

To compute the script of each text we used Glotscript ([code](https://github.com/cisnlp/GlotScript) and [paper](https://arxiv.org/abs/2309.13320)).


## License and Copyright

- default: 

We do not own any of the text from which these data has been extracted.
All the files are collected from the repository located at https://github.com/global-asp/.
The source repository for each text and file is stored in the dataset.
Each file in the dataset is associated with one license from the CC family.
The licenses include 'CC BY', 'CC BY-NC', 'CC BY-NC-SA', 'CC-BY', 'CC-BY-NC', and 'Public Domain'.
We also license the code, actual packaging and the metadata of these data under the cc0-1.0.


- nalibali:

We do not own any of the text from which these data has been extracted.
All the files are collected from [https://nalibali.org](https://nalibali.org/story-resources/multilingual-stories) under the [nalibali term of use](https://nalibali.org/terms-use):
> Material on this website may be freely downloaded, shared and reprinted. In fact, we welcome the circulation and sharing of Nal’ibali resources, provided it adheres to the following guidelines: It is credited to the Nal’ibali initiative, and retains the Nal’ibali logo and web address wherever possible; it is for personal, educational and developmental purposes only; it may not be sold, used or distributed commercially or for a fee.
We also license the code, actual packaging and the metadata of these data under the cc0-1.0.

## Github
We additionally provide a GitHub version that openly shares the source code for processing this dataset:
https://github.com/cisnlp/GlotStoryBook



## Citation
If you use any part of this code and data in your research, please cite it (along with https://github.com/global-asp/ and https://nalibali.org) using the following BibTeX entry.
This work is part of the [GlotLID](https://github.com/cisnlp/GlotLID) project and [paper](https://arxiv.org/abs/2310.16248).

```
@inproceedings{
  kargaran2023glotlid,
  title={{GlotLID}: Language Identification for Low-Resource Languages},
  author={Kargaran, Amir Hossein and Imani, Ayyoob and Yvon, Fran{\c{c}}ois and Sch{\"u}tze, Hinrich},
  booktitle={The 2023 Conference on Empirical Methods in Natural Language Processing},
  year={2023},
  url={https://openreview.net/forum?id=dl4e3EBz5j}
}

```