---
license: cc-by-sa-4.0
task_categories:
- text-retrieval
- text-classification
language:
- aa
- ab
- ace
- ady
- af
- ak
- alt
- am
- ami
- an
- ang
- ann
- anp
- ar
- arc
- ary
- arz
- as
- ast
- atj
- av
- avk
- awa
- ay
- az
- azb
- ba
- ban
- bar
- bbc
- bcl
- bdr
- be
- bew
- bg
- bh
- bi
- bjn
- blk
- bm
- bn
- bo
- bpy
- br
- bs
- btm
- bug
- bxr
- ca
- cdo
- ce
- ceb
- ch
- cho
- chr
- chy
- ckb
- co
- cr
- crh
- cs
- csb
- cu
- cv
- cy
- da
- dag
- de
- dga
- din
- diq
- dsb
- dtp
- dty
- dv
- dz
- ee
- el
- eml
- en
- eo
- es
- et
- eu
- ext
- fa
- fat
- ff
- fi
- fj
- fo
- fon
- fr
- frp
- frr
- fur
- fy
- ga
- gag
- gan
- gcr
- gd
- gl
- glk
- gn
- gom
- gor
- got
- gpe
- gsw
- gu
- guc
- gur
- guw
- gv
- ha
- hak
- haw
- he
- hi
- hif
- ho
- hr
- hsb
- ht
- hu
- hy
- hyw
- hz
- ia
- iba
- id
- ie
- ig
- igl
- ii
- ik
- ilo
- inh
- io
- is
- it
- iu
- ja
- jam
- jbo
- jv
- ka
- kaa
- kab
- kbd
- kbp
- kcg
- kg
- kge
- ki
- kj
- kk
- kl
- km
- kn
- knc
- ko
- koi
- kr
- krc
- ks
- ksh
- ku
- kus
- kv
- kw
- ky
- la
- lad
- lb
- lbe
- lez
- lfn
- lg
- li
- lij
- lld
- lmo
- ln
- lo
- lrc
- lt
- ltg
- lv
- lzh
- mad
- mai
- mdf
- mg
- mh
- mhr
- mi
- min
- mk
- ml
- mn
- mni
- mnw
- mos
- mr
- mrj
- ms
- mt
- mus
- mwl
- my
- myv
- mzn
- na
- nah
- nan
- nap
- nds
- ne
- new
- ng
- nia
- nl
- nn
- no
- nov
- nqo
- nr
- nrm
- nso
- nup
- nv
- ny
- oc
- olo
- om
- or
- os
- pa
- pag
- pam
- pap
- pcd
- pcm
- pdc
- pfl
- pi
- pih
- pl
- pms
- pnb
- pnt
- ps
- pt
- pwn
- qu
- rki
- rm
- rmy
- rn
- ro
- rsk
- ru
- rue
- rup
- rw
- sa
- sah
- sat
- sc
- scn
- sco
- sd
- se
- sg
- sgs
- sh
- shi
- shn
- si
- sk
- skr
- sl
- sm
- smn
- sn
- so
- sq
- sr
- srn
- ss
- st
- stq
- su
- sv
- sw
- syl
- szl
- szy
- ta
- tay
- tcy
- tdd
- te
- tet
- tg
- th
- ti
- tig
- tk
- tl
- tly
- tn
- to
- tok
- tpi
- tr
- trv
- ts
- tt
- tum
- tw
- ty
- tyv
- udm
- ug
- uk
- ur
- uz
- ve
- vec
- vep
- vi
- vls
- vo
- vro
- wa
- war
- wo
- wuu
- xal
- xh
- xmf
- yi
- yo
- yue
- za
- zea
- zgh
- zh
- zu
tags:
- wikipedia
- cleaning
- namespaces
- labels
pretty_name: Wikipedia Structural Labels
size_categories:
- n<1M
configs:
- config_name: default
  data_files:
  - split: train
    path: wikipedia_namespaces_default.parquet
- config_name: all
  data_files:
  - split: train
    path: wikipedia_namespaces_all.parquet
- config_name: strict
  data_files:
  - split: train
    path: wikipedia_namespaces_strict.parquet
---

# Wikipedia Structural Labels Dataset

This dataset contains structural labels (namespaces and their aliases) for **358 Wikipedia languages**. It is designed to help researchers and developers clean Wikipedia content by identifying and removing structural noise (e.g., "Category:", "File:", "Template:") across all supported languages.

This is a sister project to [wikipedia-monthly](https://huggingface.co/datasets/omarkamali/wikipedia-monthly) and is maintained by [omarkamali](https://huggingface.co/omarkamali).

## Dataset Structure

The dataset is provided in **Hugging Face format** with three distinct splits:

1.  **`default`**: Primary localized label for each namespace.
3.  **`strict`**: Filtered version removing major language fallbacks (**en, fr, es, ar, ru, zh**).
2.  **`all`**: List of all known labels and aliases per namespace.

## Usage

```python
from datasets import load_dataset
ds = load_dataset("omarkamali/wikipedia-labels")
```

## Cleaning Metrics (Strict Split)

Top 50 languages with labels removed because they matched a major source language:

| Language | en | fr | es | ar | ru | zh | Total |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **吴语 (wuu)** | 26 | 0 | 0 | 0 | 1 | 95 | 122 |
| **贛語 (gan)** | 11 | 0 | 1 | 0 | 3 | 95 | 110 |
| **文言 (lzh)** | 15 | 0 | 1 | 0 | 1 | 93 | 110 |
| **閩南語 / Bân-lâm-gí (nan)** | 12 | 0 | 0 | 0 | 0 | 95 | 107 |
| **閩東語 / Mìng-dĕ̤ng-ngṳ̄ (cdo)** | 10 | 0 | 0 | 0 | 0 | 95 | 105 |
| **客家語 / Hak-kâ-ngî (hak)** | 10 | 0 | 0 | 0 | 0 | 95 | 105 |
| **ꆇꉙ (ii)** | 10 | 0 | 0 | 0 | 0 | 95 | 105 |
| **Vahcuengh (za)** | 10 | 0 | 0 | 0 | 0 | 95 | 105 |
| **Pangcah (ami)** | 10 | 0 | 0 | 0 | 0 | 94 | 104 |
| **pinayuanan (pwn)** | 10 | 0 | 0 | 0 | 0 | 94 | 104 |
| **Seediq (trv)** | 9 | 0 | 0 | 0 | 0 | 90 | 99 |
| **Tayal (tay)** | 9 | 0 | 0 | 0 | 0 | 90 | 99 |
| **Sakizaya (szy)** | 9 | 0 | 0 | 0 | 0 | 90 | 99 |
| **粵語 (yue)** | 27 | 0 | 0 | 0 | 1 | 24 | 52 |
| **Fulfulde (ff)** | 26 | 22 | 0 | 0 | 0 | 0 | 48 |
| **Nouormand (nrm)** | 11 | 25 | 0 | 0 | 0 | 0 | 36 |
| **Kabɩyɛ (kbp)** | 11 | 24 | 0 | 0 | 0 | 0 | 35 |
| **lingála (ln)** | 11 | 23 | 0 | 0 | 0 | 0 | 34 |
| **Picard (pcd)** | 11 | 23 | 0 | 0 | 0 | 0 | 34 |
| **Sängö (sg)** | 11 | 23 | 0 | 0 | 0 | 0 | 34 |
| **bamanankan (bm)** | 11 | 23 | 0 | 0 | 0 | 0 | 34 |
| **reo tahiti (ty)** | 11 | 23 | 0 | 0 | 0 | 0 | 34 |
| **مصرى (arz)** | 9 | 0 | 0 | 25 | 0 | 0 | 34 |
| **татарча / tatarça (tt)** | 9 | 0 | 0 | 0 | 23 | 0 | 32 |
| **перем коми (koi)** | 10 | 0 | 0 | 0 | 21 | 0 | 31 |
| **الدارجة (ary)** | 7 | 0 | 0 | 24 | 0 | 0 | 31 |
| **Chavacano de Zamboanga (cbk-zam)** | 9 | 0 | 22 | 0 | 0 | 0 | 31 |
| **Aymar aru (ay)** | 8 | 0 | 22 | 0 | 0 | 0 | 30 |
| **коми (kv)** | 9 | 0 | 0 | 0 | 21 | 0 | 30 |
| **лезги (lez)** | 10 | 0 | 0 | 0 | 19 | 0 | 29 |
| **Soomaaliga (so)** | 28 | 0 | 0 | 0 | 0 | 0 | 28 |
| **Simple English (simple)** | 28 | 0 | 0 | 0 | 0 | 0 | 28 |
| **олык марий (mhr)** | 10 | 0 | 0 | 0 | 18 | 0 | 28 |
| **українська (uk)** | 8 | 0 | 0 | 0 | 19 | 0 | 27 |
| **мокшень (mdf)** | 9 | 0 | 0 | 0 | 18 | 0 | 27 |
| **Gĩkũyũ (ki)** | 26 | 0 | 0 | 0 | 0 | 0 | 26 |
| **Malagasy (mg)** | 11 | 15 | 0 | 0 | 0 | 0 | 26 |
| **Kwanyama (kj)** | 26 | 0 | 0 | 0 | 0 | 0 | 26 |
| **Patois (jam)** | 26 | 0 | 0 | 0 | 0 | 0 | 26 |
| **адыгэбзэ (kbd)** | 12 | 0 | 0 | 0 | 14 | 0 | 26 |
| **ᐃᓄᒃᑎᑐᑦ / inuktitut (iu)** | 26 | 0 | 0 | 0 | 0 | 0 | 26 |
| **Luganda (lg)** | 26 | 0 | 0 | 0 | 0 | 0 | 26 |
| **Ebon (mh)** | 26 | 0 | 0 | 0 | 0 | 0 | 26 |
| **Iñupiatun (ik)** | 26 | 0 | 0 | 0 | 0 | 0 | 26 |
| **адыгабзэ (ady)** | 25 | 0 | 0 | 0 | 1 | 0 | 26 |
| **Māori (mi)** | 26 | 0 | 0 | 0 | 0 | 0 | 26 |
| **Mvskoke (mus)** | 26 | 0 | 0 | 0 | 0 | 0 | 26 |
| **isiZulu (zu)** | 26 | 0 | 0 | 0 | 0 | 0 | 26 |
| **chiTumbuka (tum)** | 26 | 0 | 0 | 0 | 0 | 0 | 26 |
| **Xitsonga (ts)** | 26 | 0 | 0 | 0 | 0 | 0 | 26 |


## Blacklisted Namespaces

The following namespaces were removed because they appeared in fewer than 5% of languages and were not present in any major source language:

| Canonical Name | ID | Coverage | Reason | Example Languages |
| :--- | :--- | :--- | :--- | :--- |
| Main | 0 | 358 | Main Namespace (No Prefix) | ady, ace, ab, alt, ak... |
| Spruch | 108 | 7 | Low Coverage | bar, gsw, he, pfl, ro... |
| שיחת ספר | 109 | 7 | Low Coverage | bar, gsw, he, pfl, ro... |
| Education Program | 446 | 6 | Low Coverage | el, fa, lv, pt, sv... |
| Education Program talk | 447 | 6 | Low Coverage | el, fa, lv, pt, sv... |
| Nochricht | 110 | 4 | Low Coverage | bar, gsw, pfl, ro |
| Discuție Carte | 111 | 4 | Low Coverage | bar, gsw, pfl, ro |
| Story | 1704 | 1 | Low Coverage | id |
| Story Talk | 1705 | 1 | Low Coverage | id |
| Campaign | 460 | 1 | Low Coverage | ro |
| Campaign talk | 461 | 1 | Low Coverage | ro |
| Thread | 90 | 1 | Low Coverage | hu |
| Thread talk | 91 | 1 | Low Coverage | hu |
| Summary | 92 | 1 | Low Coverage | hu |
| Summary talk | 93 | 1 | Low Coverage | hu |


## Statistics
- **Total Languages**: 358
- **Source**: MediaWiki API (`meta=siteinfo`)
- **Last Updated**: 2026-01-01

## License
This dataset is derived from Wikipedia/MediaWiki and is subject to the same licensing terms as Wikipedia data (**CC BY-SA 4.0**).
