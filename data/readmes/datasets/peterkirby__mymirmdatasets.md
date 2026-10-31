---
license: other
license_name: source-dependent
license_link: LICENSE.md
pretty_name: MIRM multilingual authorship datasets
language:
- ar
- bg
- bn
- ca
- cs
- da
- de
- el
- en
- es
- fa
- fi
- fil
- fr
- he
- hi
- hr
- hu
- hy
- id
- it
- ja
- ka
- kk
- ko
- lv
- ml
- mr
- ms
- nb
- nl
- pl
- pt
- ro
- ru
- sl
- sr
- sv
- sw
- ta
- th
- tr
- uk
- ur
- uz
- vi
- zh
size_categories:
- 10M<n<100M
task_categories:
- text-classification
tags:
- authorship-verification
- multilingual
- style-embeddings
configs:
- config_name: bluesky_authorship
  data_files:
  - split: train
    path:
    - packages/bluesky/data/bluesky_authorship__cs/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__cs/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00003.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00004.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00005.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00006.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00007.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00008.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00009.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00010.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00011.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00012.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00013.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00014.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00015.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00016.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00017.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00003.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00004.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00005.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00006.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00007.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00008.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00009.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00010.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00011.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00012.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00013.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00014.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00015.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00016.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00017.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00018.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00003.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00004.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00005.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00006.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00007.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00008.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00009.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00010.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00011.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00012.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00013.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00014.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00015.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00016.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00017.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00018.parquet
    - packages/bluesky/data/bluesky_authorship__fi/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__fi/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__fi/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__fi/train/00003.parquet
    - packages/bluesky/data/bluesky_authorship__fi/train/00004.parquet
    - packages/bluesky/data/bluesky_authorship__fi/train/00005.parquet
    - packages/bluesky/data/bluesky_authorship__fi/train/00006.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00003.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00004.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00005.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00006.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00007.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00008.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00009.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00010.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00011.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00012.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00013.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00014.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00015.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00016.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00017.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00018.parquet
    - packages/bluesky/data/bluesky_authorship__it/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__it/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__it/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__it/train/00003.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00003.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00004.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00005.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00006.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00007.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00008.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00009.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00010.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00011.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00012.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00013.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00014.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00015.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00016.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00017.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00018.parquet
    - packages/bluesky/data/bluesky_authorship__ko/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__ko/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__ko/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__ko/train/00003.parquet
    - packages/bluesky/data/bluesky_authorship__ko/train/00004.parquet
    - packages/bluesky/data/bluesky_authorship__ko/train/00005.parquet
    - packages/bluesky/data/bluesky_authorship__ko/train/00006.parquet
    - packages/bluesky/data/bluesky_authorship__ko/train/00007.parquet
    - packages/bluesky/data/bluesky_authorship__ko/train/00008.parquet
    - packages/bluesky/data/bluesky_authorship__ko/train/00009.parquet
    - packages/bluesky/data/bluesky_authorship__nb/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__nb/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__nb/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__nb/train/00003.parquet
    - packages/bluesky/data/bluesky_authorship__nl/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__nl/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__nl/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__nl/train/00003.parquet
    - packages/bluesky/data/bluesky_authorship__nl/train/00004.parquet
    - packages/bluesky/data/bluesky_authorship__nl/train/00005.parquet
    - packages/bluesky/data/bluesky_authorship__nl/train/00006.parquet
    - packages/bluesky/data/bluesky_authorship__nl/train/00007.parquet
    - packages/bluesky/data/bluesky_authorship__nl/train/00008.parquet
    - packages/bluesky/data/bluesky_authorship__nl/train/00009.parquet
    - packages/bluesky/data/bluesky_authorship__nl/train/00010.parquet
    - packages/bluesky/data/bluesky_authorship__nl/train/00011.parquet
    - packages/bluesky/data/bluesky_authorship__nl/train/00012.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00003.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00004.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00005.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00006.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00007.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00008.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00009.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00010.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00011.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00012.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00013.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00014.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00015.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00016.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00017.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00018.parquet
    - packages/bluesky/data/bluesky_authorship__ru/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__ru/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__ru/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__ru/train/00003.parquet
    - packages/bluesky/data/bluesky_authorship__sv/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__sv/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__sv/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__sv/train/00003.parquet
    - packages/bluesky/data/bluesky_authorship__sv/train/00004.parquet
    - packages/bluesky/data/bluesky_authorship__sv/train/00005.parquet
    - packages/bluesky/data/bluesky_authorship__sv/train/00006.parquet
    - packages/bluesky/data/bluesky_authorship__th/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__th/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__th/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__tr/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__tr/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__tr/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__tr/train/00003.parquet
    - packages/bluesky/data/bluesky_authorship__tr/train/00004.parquet
    - packages/bluesky/data/bluesky_authorship__uk/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__uk/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__uk/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__uk/train/00003.parquet
    - packages/bluesky/data/bluesky_authorship__uk/train/00004.parquet
    - packages/bluesky/data/bluesky_authorship__uk/train/00005.parquet
    - packages/bluesky/data/bluesky_authorship__uk/train/00006.parquet
    - packages/bluesky/data/bluesky_authorship__uk/train/00007.parquet
    - packages/bluesky/data/bluesky_authorship__uk/train/00008.parquet
    - packages/bluesky/data/bluesky_authorship__uk/train/00009.parquet
    - packages/bluesky/data/bluesky_authorship__zh/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__zh/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__zh/train/00002.parquet
  - split: validation
    path:
    - packages/bluesky/data/bluesky_authorship__cs/validation/00000.parquet
    - packages/bluesky/data/bluesky_authorship__de/validation/00000.parquet
    - packages/bluesky/data/bluesky_authorship__de/validation/00001.parquet
    - packages/bluesky/data/bluesky_authorship__de/validation/00002.parquet
    - packages/bluesky/data/bluesky_authorship__en/validation/00000.parquet
    - packages/bluesky/data/bluesky_authorship__en/validation/00001.parquet
    - packages/bluesky/data/bluesky_authorship__es/validation/00000.parquet
    - packages/bluesky/data/bluesky_authorship__es/validation/00001.parquet
    - packages/bluesky/data/bluesky_authorship__fi/validation/00000.parquet
    - packages/bluesky/data/bluesky_authorship__fr/validation/00000.parquet
    - packages/bluesky/data/bluesky_authorship__fr/validation/00001.parquet
    - packages/bluesky/data/bluesky_authorship__it/validation/00000.parquet
    - packages/bluesky/data/bluesky_authorship__ja/validation/00000.parquet
    - packages/bluesky/data/bluesky_authorship__ja/validation/00001.parquet
    - packages/bluesky/data/bluesky_authorship__ko/validation/00000.parquet
    - packages/bluesky/data/bluesky_authorship__ko/validation/00001.parquet
    - packages/bluesky/data/bluesky_authorship__nb/validation/00000.parquet
    - packages/bluesky/data/bluesky_authorship__nl/validation/00000.parquet
    - packages/bluesky/data/bluesky_authorship__nl/validation/00001.parquet
    - packages/bluesky/data/bluesky_authorship__pt/validation/00000.parquet
    - packages/bluesky/data/bluesky_authorship__pt/validation/00001.parquet
    - packages/bluesky/data/bluesky_authorship__ru/validation/00000.parquet
    - packages/bluesky/data/bluesky_authorship__sv/validation/00000.parquet
    - packages/bluesky/data/bluesky_authorship__th/validation/00000.parquet
    - packages/bluesky/data/bluesky_authorship__tr/validation/00000.parquet
    - packages/bluesky/data/bluesky_authorship__uk/validation/00000.parquet
    - packages/bluesky/data/bluesky_authorship__uk/validation/00001.parquet
    - packages/bluesky/data/bluesky_authorship__zh/validation/00000.parquet
- config_name: bluesky_authorship__cs
  data_files:
  - split: train
    path:
    - packages/bluesky/data/bluesky_authorship__cs/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__cs/train/00001.parquet
  - split: validation
    path:
    - packages/bluesky/data/bluesky_authorship__cs/validation/00000.parquet
- config_name: bluesky_authorship__de
  data_files:
  - split: train
    path:
    - packages/bluesky/data/bluesky_authorship__de/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00003.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00004.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00005.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00006.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00007.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00008.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00009.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00010.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00011.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00012.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00013.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00014.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00015.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00016.parquet
    - packages/bluesky/data/bluesky_authorship__de/train/00017.parquet
  - split: validation
    path:
    - packages/bluesky/data/bluesky_authorship__de/validation/00000.parquet
    - packages/bluesky/data/bluesky_authorship__de/validation/00001.parquet
    - packages/bluesky/data/bluesky_authorship__de/validation/00002.parquet
- config_name: bluesky_authorship__en
  data_files:
  - split: train
    path:
    - packages/bluesky/data/bluesky_authorship__en/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00003.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00004.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00005.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00006.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00007.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00008.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00009.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00010.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00011.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00012.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00013.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00014.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00015.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00016.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00017.parquet
    - packages/bluesky/data/bluesky_authorship__en/train/00018.parquet
  - split: validation
    path:
    - packages/bluesky/data/bluesky_authorship__en/validation/00000.parquet
    - packages/bluesky/data/bluesky_authorship__en/validation/00001.parquet
- config_name: bluesky_authorship__es
  data_files:
  - split: train
    path:
    - packages/bluesky/data/bluesky_authorship__es/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00003.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00004.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00005.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00006.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00007.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00008.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00009.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00010.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00011.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00012.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00013.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00014.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00015.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00016.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00017.parquet
    - packages/bluesky/data/bluesky_authorship__es/train/00018.parquet
  - split: validation
    path:
    - packages/bluesky/data/bluesky_authorship__es/validation/00000.parquet
    - packages/bluesky/data/bluesky_authorship__es/validation/00001.parquet
- config_name: bluesky_authorship__fi
  data_files:
  - split: train
    path:
    - packages/bluesky/data/bluesky_authorship__fi/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__fi/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__fi/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__fi/train/00003.parquet
    - packages/bluesky/data/bluesky_authorship__fi/train/00004.parquet
    - packages/bluesky/data/bluesky_authorship__fi/train/00005.parquet
    - packages/bluesky/data/bluesky_authorship__fi/train/00006.parquet
  - split: validation
    path:
    - packages/bluesky/data/bluesky_authorship__fi/validation/00000.parquet
- config_name: bluesky_authorship__fr
  data_files:
  - split: train
    path:
    - packages/bluesky/data/bluesky_authorship__fr/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00003.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00004.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00005.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00006.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00007.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00008.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00009.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00010.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00011.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00012.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00013.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00014.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00015.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00016.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00017.parquet
    - packages/bluesky/data/bluesky_authorship__fr/train/00018.parquet
  - split: validation
    path:
    - packages/bluesky/data/bluesky_authorship__fr/validation/00000.parquet
    - packages/bluesky/data/bluesky_authorship__fr/validation/00001.parquet
- config_name: bluesky_authorship__it
  data_files:
  - split: train
    path:
    - packages/bluesky/data/bluesky_authorship__it/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__it/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__it/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__it/train/00003.parquet
  - split: validation
    path:
    - packages/bluesky/data/bluesky_authorship__it/validation/00000.parquet
- config_name: bluesky_authorship__ja
  data_files:
  - split: train
    path:
    - packages/bluesky/data/bluesky_authorship__ja/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00003.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00004.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00005.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00006.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00007.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00008.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00009.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00010.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00011.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00012.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00013.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00014.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00015.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00016.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00017.parquet
    - packages/bluesky/data/bluesky_authorship__ja/train/00018.parquet
  - split: validation
    path:
    - packages/bluesky/data/bluesky_authorship__ja/validation/00000.parquet
    - packages/bluesky/data/bluesky_authorship__ja/validation/00001.parquet
- config_name: bluesky_authorship__ko
  data_files:
  - split: train
    path:
    - packages/bluesky/data/bluesky_authorship__ko/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__ko/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__ko/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__ko/train/00003.parquet
    - packages/bluesky/data/bluesky_authorship__ko/train/00004.parquet
    - packages/bluesky/data/bluesky_authorship__ko/train/00005.parquet
    - packages/bluesky/data/bluesky_authorship__ko/train/00006.parquet
    - packages/bluesky/data/bluesky_authorship__ko/train/00007.parquet
    - packages/bluesky/data/bluesky_authorship__ko/train/00008.parquet
    - packages/bluesky/data/bluesky_authorship__ko/train/00009.parquet
  - split: validation
    path:
    - packages/bluesky/data/bluesky_authorship__ko/validation/00000.parquet
    - packages/bluesky/data/bluesky_authorship__ko/validation/00001.parquet
- config_name: bluesky_authorship__nb
  data_files:
  - split: train
    path:
    - packages/bluesky/data/bluesky_authorship__nb/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__nb/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__nb/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__nb/train/00003.parquet
  - split: validation
    path:
    - packages/bluesky/data/bluesky_authorship__nb/validation/00000.parquet
- config_name: bluesky_authorship__nl
  data_files:
  - split: train
    path:
    - packages/bluesky/data/bluesky_authorship__nl/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__nl/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__nl/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__nl/train/00003.parquet
    - packages/bluesky/data/bluesky_authorship__nl/train/00004.parquet
    - packages/bluesky/data/bluesky_authorship__nl/train/00005.parquet
    - packages/bluesky/data/bluesky_authorship__nl/train/00006.parquet
    - packages/bluesky/data/bluesky_authorship__nl/train/00007.parquet
    - packages/bluesky/data/bluesky_authorship__nl/train/00008.parquet
    - packages/bluesky/data/bluesky_authorship__nl/train/00009.parquet
    - packages/bluesky/data/bluesky_authorship__nl/train/00010.parquet
    - packages/bluesky/data/bluesky_authorship__nl/train/00011.parquet
    - packages/bluesky/data/bluesky_authorship__nl/train/00012.parquet
  - split: validation
    path:
    - packages/bluesky/data/bluesky_authorship__nl/validation/00000.parquet
    - packages/bluesky/data/bluesky_authorship__nl/validation/00001.parquet
- config_name: bluesky_authorship__pt
  data_files:
  - split: train
    path:
    - packages/bluesky/data/bluesky_authorship__pt/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00003.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00004.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00005.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00006.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00007.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00008.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00009.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00010.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00011.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00012.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00013.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00014.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00015.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00016.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00017.parquet
    - packages/bluesky/data/bluesky_authorship__pt/train/00018.parquet
  - split: validation
    path:
    - packages/bluesky/data/bluesky_authorship__pt/validation/00000.parquet
    - packages/bluesky/data/bluesky_authorship__pt/validation/00001.parquet
- config_name: bluesky_authorship__ru
  data_files:
  - split: train
    path:
    - packages/bluesky/data/bluesky_authorship__ru/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__ru/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__ru/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__ru/train/00003.parquet
  - split: validation
    path:
    - packages/bluesky/data/bluesky_authorship__ru/validation/00000.parquet
- config_name: bluesky_authorship__sv
  data_files:
  - split: train
    path:
    - packages/bluesky/data/bluesky_authorship__sv/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__sv/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__sv/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__sv/train/00003.parquet
    - packages/bluesky/data/bluesky_authorship__sv/train/00004.parquet
    - packages/bluesky/data/bluesky_authorship__sv/train/00005.parquet
    - packages/bluesky/data/bluesky_authorship__sv/train/00006.parquet
  - split: validation
    path:
    - packages/bluesky/data/bluesky_authorship__sv/validation/00000.parquet
- config_name: bluesky_authorship__th
  data_files:
  - split: train
    path:
    - packages/bluesky/data/bluesky_authorship__th/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__th/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__th/train/00002.parquet
  - split: validation
    path:
    - packages/bluesky/data/bluesky_authorship__th/validation/00000.parquet
- config_name: bluesky_authorship__tr
  data_files:
  - split: train
    path:
    - packages/bluesky/data/bluesky_authorship__tr/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__tr/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__tr/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__tr/train/00003.parquet
    - packages/bluesky/data/bluesky_authorship__tr/train/00004.parquet
  - split: validation
    path:
    - packages/bluesky/data/bluesky_authorship__tr/validation/00000.parquet
- config_name: bluesky_authorship__uk
  data_files:
  - split: train
    path:
    - packages/bluesky/data/bluesky_authorship__uk/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__uk/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__uk/train/00002.parquet
    - packages/bluesky/data/bluesky_authorship__uk/train/00003.parquet
    - packages/bluesky/data/bluesky_authorship__uk/train/00004.parquet
    - packages/bluesky/data/bluesky_authorship__uk/train/00005.parquet
    - packages/bluesky/data/bluesky_authorship__uk/train/00006.parquet
    - packages/bluesky/data/bluesky_authorship__uk/train/00007.parquet
    - packages/bluesky/data/bluesky_authorship__uk/train/00008.parquet
    - packages/bluesky/data/bluesky_authorship__uk/train/00009.parquet
  - split: validation
    path:
    - packages/bluesky/data/bluesky_authorship__uk/validation/00000.parquet
    - packages/bluesky/data/bluesky_authorship__uk/validation/00001.parquet
- config_name: bluesky_authorship__zh
  data_files:
  - split: train
    path:
    - packages/bluesky/data/bluesky_authorship__zh/train/00000.parquet
    - packages/bluesky/data/bluesky_authorship__zh/train/00001.parquet
    - packages/bluesky/data/bluesky_authorship__zh/train/00002.parquet
  - split: validation
    path:
    - packages/bluesky/data/bluesky_authorship__zh/validation/00000.parquet
- config_name: exorde_authorship
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00012.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00013.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00014.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00015.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00016.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00017.parquet
    - packages/exorde/data/exorde_authorship__bn__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__bn__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__ca__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__ca__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__ca__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__ca__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__cs__reddit.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__cs__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__cs__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__da__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__da__reddit.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__da__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00001.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00002.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00003.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00004.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00005.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00006.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00007.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00008.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00009.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00010.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00011.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00012.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00013.parquet
    - packages/exorde/data/exorde_authorship__de__reddit.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__de__reddit.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00012.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00013.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00014.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00015.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00016.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00017.parquet
    - packages/exorde/data/exorde_authorship__el__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00001.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00002.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00003.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00004.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00005.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00006.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00007.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00008.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00009.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00010.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00011.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00012.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00013.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00014.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00015.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00016.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00017.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00018.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00012.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00013.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00014.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00015.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00016.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00017.parquet
    - packages/exorde/data/exorde_authorship__en__threads.net/train/00000.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00012.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00013.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00014.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00015.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00016.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00017.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00018.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00001.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00002.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00003.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00004.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00005.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00006.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00007.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00008.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00009.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00010.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00011.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00012.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00013.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00014.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00015.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00016.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00017.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00018.parquet
    - packages/exorde/data/exorde_authorship__es__reddit.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__es__reddit.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__es__reddit.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__es__reddit.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00012.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00013.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00014.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00015.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00016.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00017.parquet
    - packages/exorde/data/exorde_authorship__fa__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__fa__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__fa__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__fi__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__fi__reddit.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__fi__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__fil__reddit.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__fil__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__fil__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__fil__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__fil__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00001.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00002.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00003.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00004.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00005.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00006.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00007.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00008.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00009.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00010.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00011.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00012.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00013.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00014.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00015.parquet
    - packages/exorde/data/exorde_authorship__fr__reddit.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__fr__reddit.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00012.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00013.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00014.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00015.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00016.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00017.parquet
    - packages/exorde/data/exorde_authorship__he__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00012.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00013.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00014.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00015.parquet
    - packages/exorde/data/exorde_authorship__hr__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__hu__reddit.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__hu__reddit.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00012.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00013.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00014.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00015.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00016.parquet
    - packages/exorde/data/exorde_authorship__it__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__it__bsky.app/train/00001.parquet
    - packages/exorde/data/exorde_authorship__it__bsky.app/train/00002.parquet
    - packages/exorde/data/exorde_authorship__it__reddit.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/train/00012.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00001.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00002.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00003.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00004.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00005.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00006.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00007.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00008.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00009.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00010.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00011.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00012.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00013.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00014.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00015.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00016.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00017.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00018.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00012.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00013.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00014.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00015.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00016.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00017.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00018.parquet
    - packages/exorde/data/exorde_authorship__ko__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__ko__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__ko__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__ko__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__ko__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__lv__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__mr__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__ms__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__ms__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__nl__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__nl__bsky.app/train/00001.parquet
    - packages/exorde/data/exorde_authorship__nl__bsky.app/train/00002.parquet
    - packages/exorde/data/exorde_authorship__nl__bsky.app/train/00003.parquet
    - packages/exorde/data/exorde_authorship__nl__reddit.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__nl__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__nl__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__nl__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__nl__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__nl__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__nl__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__nl__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__nl__x.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__nb__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__nb__reddit.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__nb__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__pl__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__pl__bsky.app/train/00001.parquet
    - packages/exorde/data/exorde_authorship__pl__reddit.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__pl__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__pl__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__pl__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__pl__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__pl__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00001.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00002.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00003.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00004.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00005.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00006.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00007.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00008.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00009.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00010.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00011.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00012.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00013.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00014.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00015.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00016.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00017.parquet
    - packages/exorde/data/exorde_authorship__pt__reddit.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__pt__reddit.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__pt__reddit.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__pt__reddit.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00012.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00013.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00014.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00015.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00016.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00017.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00018.parquet
    - packages/exorde/data/exorde_authorship__ro__reddit.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__ro__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__ro__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__ru__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__ru__bsky.app/train/00001.parquet
    - packages/exorde/data/exorde_authorship__ru__bsky.app/train/00002.parquet
    - packages/exorde/data/exorde_authorship__ru__reddit.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00012.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00013.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00014.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00015.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00016.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00017.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00018.parquet
    - packages/exorde/data/exorde_authorship__sl__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__sr__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__sr__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__sv__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__sv__bsky.app/train/00001.parquet
    - packages/exorde/data/exorde_authorship__sv__reddit.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__sv__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__sv__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__sv__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__sw__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__ta__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__th__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__th__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__th__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__th__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__th__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__th__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__th__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__tr__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__tr__reddit.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00012.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00013.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00014.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00015.parquet
    - packages/exorde/data/exorde_authorship__uk__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__uk__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__ur__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__ur__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__vi__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__vi__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__vi__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__vi__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__zh__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__zh__bsky.app/train/00001.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/train/00012.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__ar__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/validation/00001.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/validation/00002.parquet
    - packages/exorde/data/exorde_authorship__bn__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__ca__bsky.app/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__ca__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__cs__reddit.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__cs__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__da__bsky.app/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__da__reddit.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__da__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/validation/00001.parquet
    - packages/exorde/data/exorde_authorship__de__reddit.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/validation/00001.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/validation/00002.parquet
    - packages/exorde/data/exorde_authorship__el__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/validation/00001.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/validation/00001.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/validation/00002.parquet
    - packages/exorde/data/exorde_authorship__en__threads.net/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/validation/00001.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/validation/00001.parquet
    - packages/exorde/data/exorde_authorship__es__reddit.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/validation/00001.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/validation/00002.parquet
    - packages/exorde/data/exorde_authorship__fa__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__fi__bsky.app/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__fi__reddit.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__fi__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__fil__reddit.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__fil__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/validation/00001.parquet
    - packages/exorde/data/exorde_authorship__fr__reddit.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/validation/00001.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/validation/00002.parquet
    - packages/exorde/data/exorde_authorship__he__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/validation/00001.parquet
    - packages/exorde/data/exorde_authorship__hr__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__hu__reddit.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/validation/00001.parquet
    - packages/exorde/data/exorde_authorship__it__bsky.app/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__it__reddit.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/validation/00001.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/validation/00001.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/validation/00001.parquet
    - packages/exorde/data/exorde_authorship__ko__bsky.app/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__ko__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__lv__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__mr__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__ms__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__nl__bsky.app/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__nl__reddit.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__nl__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__nb__bsky.app/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__nb__reddit.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__nb__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__pl__bsky.app/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__pl__reddit.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__pl__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/validation/00001.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/validation/00002.parquet
    - packages/exorde/data/exorde_authorship__pt__reddit.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/validation/00001.parquet
    - packages/exorde/data/exorde_authorship__ro__reddit.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__ro__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__ru__bsky.app/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__ru__reddit.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/validation/00001.parquet
    - packages/exorde/data/exorde_authorship__sl__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__sr__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__sv__bsky.app/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__sv__reddit.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__sv__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__sw__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__ta__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__th__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__tr__bsky.app/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__tr__reddit.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/validation/00001.parquet
    - packages/exorde/data/exorde_authorship__uk__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__ur__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__vi__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__zh__bsky.app/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/validation/00001.parquet
- config_name: exorde_authorship__ar__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00012.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00013.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00014.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00015.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00016.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/train/00017.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__ar__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/validation/00001.parquet
    - packages/exorde/data/exorde_authorship__ar__x.com/validation/00002.parquet
- config_name: exorde_authorship__bn__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__bn__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__bn__x.com/train/00001.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__bn__x.com/validation/00000.parquet
- config_name: exorde_authorship__ca__bsky.app
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__ca__bsky.app/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__ca__bsky.app/validation/00000.parquet
- config_name: exorde_authorship__ca__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__ca__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__ca__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__ca__x.com/train/00002.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__ca__x.com/validation/00000.parquet
- config_name: exorde_authorship__cs__reddit.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__cs__reddit.com/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__cs__reddit.com/validation/00000.parquet
- config_name: exorde_authorship__cs__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__cs__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__cs__x.com/train/00001.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__cs__x.com/validation/00000.parquet
- config_name: exorde_authorship__da__bsky.app
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__da__bsky.app/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__da__bsky.app/validation/00000.parquet
- config_name: exorde_authorship__da__reddit.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__da__reddit.com/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__da__reddit.com/validation/00000.parquet
- config_name: exorde_authorship__da__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__da__x.com/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__da__x.com/validation/00000.parquet
- config_name: exorde_authorship__de__bsky.app
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00001.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00002.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00003.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00004.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00005.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00006.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00007.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00008.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00009.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00010.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00011.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00012.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/train/00013.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__de__bsky.app/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__de__bsky.app/validation/00001.parquet
- config_name: exorde_authorship__de__reddit.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__de__reddit.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__de__reddit.com/train/00001.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__de__reddit.com/validation/00000.parquet
- config_name: exorde_authorship__de__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__de__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00012.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00013.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00014.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00015.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00016.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/train/00017.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__de__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/validation/00001.parquet
    - packages/exorde/data/exorde_authorship__de__x.com/validation/00002.parquet
- config_name: exorde_authorship__el__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__el__x.com/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__el__x.com/validation/00000.parquet
- config_name: exorde_authorship__en__bsky.app
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00001.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00002.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00003.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00004.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00005.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00006.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00007.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00008.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00009.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00010.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00011.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00012.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00013.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00014.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00015.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00016.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00017.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/train/00018.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__en__bsky.app/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__en__bsky.app/validation/00001.parquet
- config_name: exorde_authorship__en__reddit.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00012.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00013.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00014.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00015.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00016.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/train/00017.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__en__reddit.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/validation/00001.parquet
    - packages/exorde/data/exorde_authorship__en__reddit.com/validation/00002.parquet
- config_name: exorde_authorship__en__threads.net
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__en__threads.net/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__en__threads.net/validation/00000.parquet
- config_name: exorde_authorship__en__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__en__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00012.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00013.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00014.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00015.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00016.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00017.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/train/00018.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__en__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__en__x.com/validation/00001.parquet
- config_name: exorde_authorship__es__bsky.app
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00001.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00002.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00003.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00004.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00005.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00006.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00007.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00008.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00009.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00010.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00011.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00012.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00013.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00014.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00015.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00016.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00017.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/train/00018.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__es__bsky.app/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__es__bsky.app/validation/00001.parquet
- config_name: exorde_authorship__es__reddit.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__es__reddit.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__es__reddit.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__es__reddit.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__es__reddit.com/train/00003.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__es__reddit.com/validation/00000.parquet
- config_name: exorde_authorship__es__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__es__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00012.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00013.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00014.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00015.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00016.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/train/00017.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__es__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/validation/00001.parquet
    - packages/exorde/data/exorde_authorship__es__x.com/validation/00002.parquet
- config_name: exorde_authorship__fa__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__fa__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__fa__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__fa__x.com/train/00002.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__fa__x.com/validation/00000.parquet
- config_name: exorde_authorship__fi__bsky.app
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__fi__bsky.app/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__fi__bsky.app/validation/00000.parquet
- config_name: exorde_authorship__fi__reddit.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__fi__reddit.com/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__fi__reddit.com/validation/00000.parquet
- config_name: exorde_authorship__fi__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__fi__x.com/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__fi__x.com/validation/00000.parquet
- config_name: exorde_authorship__fil__reddit.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__fil__reddit.com/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__fil__reddit.com/validation/00000.parquet
- config_name: exorde_authorship__fil__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__fil__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__fil__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__fil__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__fil__x.com/train/00003.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__fil__x.com/validation/00000.parquet
- config_name: exorde_authorship__fr__bsky.app
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00001.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00002.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00003.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00004.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00005.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00006.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00007.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00008.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00009.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00010.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00011.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00012.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00013.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00014.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/train/00015.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__fr__bsky.app/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__fr__bsky.app/validation/00001.parquet
- config_name: exorde_authorship__fr__reddit.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__fr__reddit.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__fr__reddit.com/train/00001.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__fr__reddit.com/validation/00000.parquet
- config_name: exorde_authorship__fr__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00012.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00013.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00014.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00015.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00016.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/train/00017.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__fr__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/validation/00001.parquet
    - packages/exorde/data/exorde_authorship__fr__x.com/validation/00002.parquet
- config_name: exorde_authorship__he__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__he__x.com/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__he__x.com/validation/00000.parquet
- config_name: exorde_authorship__hi__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00012.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00013.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00014.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/train/00015.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__hi__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__hi__x.com/validation/00001.parquet
- config_name: exorde_authorship__hr__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__hr__x.com/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__hr__x.com/validation/00000.parquet
- config_name: exorde_authorship__hu__reddit.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__hu__reddit.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__hu__reddit.com/train/00001.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__hu__reddit.com/validation/00000.parquet
- config_name: exorde_authorship__id__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__id__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00012.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00013.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00014.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00015.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/train/00016.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__id__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__id__x.com/validation/00001.parquet
- config_name: exorde_authorship__it__bsky.app
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__it__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__it__bsky.app/train/00001.parquet
    - packages/exorde/data/exorde_authorship__it__bsky.app/train/00002.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__it__bsky.app/validation/00000.parquet
- config_name: exorde_authorship__it__reddit.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__it__reddit.com/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__it__reddit.com/validation/00000.parquet
- config_name: exorde_authorship__it__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__it__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/train/00012.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__it__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__it__x.com/validation/00001.parquet
- config_name: exorde_authorship__ja__bsky.app
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00001.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00002.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00003.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00004.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00005.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00006.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00007.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00008.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00009.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00010.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00011.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00012.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00013.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00014.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00015.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00016.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00017.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/train/00018.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__ja__bsky.app/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__ja__bsky.app/validation/00001.parquet
- config_name: exorde_authorship__ja__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00012.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00013.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00014.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00015.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00016.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00017.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/train/00018.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__ja__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__ja__x.com/validation/00001.parquet
- config_name: exorde_authorship__ko__bsky.app
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__ko__bsky.app/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__ko__bsky.app/validation/00000.parquet
- config_name: exorde_authorship__ko__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__ko__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__ko__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__ko__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__ko__x.com/train/00003.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__ko__x.com/validation/00000.parquet
- config_name: exorde_authorship__lv__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__lv__x.com/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__lv__x.com/validation/00000.parquet
- config_name: exorde_authorship__mr__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__mr__x.com/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__mr__x.com/validation/00000.parquet
- config_name: exorde_authorship__ms__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__ms__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__ms__x.com/train/00001.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__ms__x.com/validation/00000.parquet
- config_name: exorde_authorship__nb__bsky.app
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__nb__bsky.app/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__nb__bsky.app/validation/00000.parquet
- config_name: exorde_authorship__nb__reddit.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__nb__reddit.com/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__nb__reddit.com/validation/00000.parquet
- config_name: exorde_authorship__nb__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__nb__x.com/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__nb__x.com/validation/00000.parquet
- config_name: exorde_authorship__nl__bsky.app
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__nl__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__nl__bsky.app/train/00001.parquet
    - packages/exorde/data/exorde_authorship__nl__bsky.app/train/00002.parquet
    - packages/exorde/data/exorde_authorship__nl__bsky.app/train/00003.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__nl__bsky.app/validation/00000.parquet
- config_name: exorde_authorship__nl__reddit.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__nl__reddit.com/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__nl__reddit.com/validation/00000.parquet
- config_name: exorde_authorship__nl__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__nl__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__nl__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__nl__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__nl__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__nl__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__nl__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__nl__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__nl__x.com/train/00007.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__nl__x.com/validation/00000.parquet
- config_name: exorde_authorship__pl__bsky.app
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__pl__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__pl__bsky.app/train/00001.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__pl__bsky.app/validation/00000.parquet
- config_name: exorde_authorship__pl__reddit.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__pl__reddit.com/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__pl__reddit.com/validation/00000.parquet
- config_name: exorde_authorship__pl__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__pl__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__pl__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__pl__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__pl__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__pl__x.com/train/00004.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__pl__x.com/validation/00000.parquet
- config_name: exorde_authorship__pt__bsky.app
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00001.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00002.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00003.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00004.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00005.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00006.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00007.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00008.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00009.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00010.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00011.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00012.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00013.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00014.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00015.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00016.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/train/00017.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__pt__bsky.app/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/validation/00001.parquet
    - packages/exorde/data/exorde_authorship__pt__bsky.app/validation/00002.parquet
- config_name: exorde_authorship__pt__reddit.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__pt__reddit.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__pt__reddit.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__pt__reddit.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__pt__reddit.com/train/00003.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__pt__reddit.com/validation/00000.parquet
- config_name: exorde_authorship__pt__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00012.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00013.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00014.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00015.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00016.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00017.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/train/00018.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__pt__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__pt__x.com/validation/00001.parquet
- config_name: exorde_authorship__ro__reddit.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__ro__reddit.com/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__ro__reddit.com/validation/00000.parquet
- config_name: exorde_authorship__ro__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__ro__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__ro__x.com/train/00001.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__ro__x.com/validation/00000.parquet
- config_name: exorde_authorship__ru__bsky.app
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__ru__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__ru__bsky.app/train/00001.parquet
    - packages/exorde/data/exorde_authorship__ru__bsky.app/train/00002.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__ru__bsky.app/validation/00000.parquet
- config_name: exorde_authorship__ru__reddit.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__ru__reddit.com/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__ru__reddit.com/validation/00000.parquet
- config_name: exorde_authorship__ru__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00012.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00013.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00014.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00015.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00016.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00017.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/train/00018.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__ru__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__ru__x.com/validation/00001.parquet
- config_name: exorde_authorship__sl__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__sl__x.com/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__sl__x.com/validation/00000.parquet
- config_name: exorde_authorship__sr__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__sr__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__sr__x.com/train/00001.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__sr__x.com/validation/00000.parquet
- config_name: exorde_authorship__sv__bsky.app
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__sv__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__sv__bsky.app/train/00001.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__sv__bsky.app/validation/00000.parquet
- config_name: exorde_authorship__sv__reddit.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__sv__reddit.com/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__sv__reddit.com/validation/00000.parquet
- config_name: exorde_authorship__sv__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__sv__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__sv__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__sv__x.com/train/00002.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__sv__x.com/validation/00000.parquet
- config_name: exorde_authorship__sw__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__sw__x.com/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__sw__x.com/validation/00000.parquet
- config_name: exorde_authorship__ta__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__ta__x.com/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__ta__x.com/validation/00000.parquet
- config_name: exorde_authorship__th__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__th__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__th__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__th__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__th__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__th__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__th__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__th__x.com/train/00006.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__th__x.com/validation/00000.parquet
- config_name: exorde_authorship__tr__bsky.app
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__tr__bsky.app/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__tr__bsky.app/validation/00000.parquet
- config_name: exorde_authorship__tr__reddit.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__tr__reddit.com/train/00000.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__tr__reddit.com/validation/00000.parquet
- config_name: exorde_authorship__tr__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00012.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00013.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00014.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/train/00015.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__tr__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__tr__x.com/validation/00001.parquet
- config_name: exorde_authorship__uk__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__uk__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__uk__x.com/train/00001.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__uk__x.com/validation/00000.parquet
- config_name: exorde_authorship__ur__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__ur__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__ur__x.com/train/00001.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__ur__x.com/validation/00000.parquet
- config_name: exorde_authorship__vi__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__vi__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__vi__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__vi__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__vi__x.com/train/00003.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__vi__x.com/validation/00000.parquet
- config_name: exorde_authorship__zh__bsky.app
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__zh__bsky.app/train/00000.parquet
    - packages/exorde/data/exorde_authorship__zh__bsky.app/train/00001.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__zh__bsky.app/validation/00000.parquet
- config_name: exorde_authorship__zh__x.com
  data_files:
  - split: train
    path:
    - packages/exorde/data/exorde_authorship__zh__x.com/train/00000.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/train/00001.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/train/00002.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/train/00003.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/train/00004.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/train/00005.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/train/00006.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/train/00007.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/train/00008.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/train/00009.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/train/00010.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/train/00011.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/train/00012.parquet
  - split: validation
    path:
    - packages/exorde/data/exorde_authorship__zh__x.com/validation/00000.parquet
    - packages/exorde/data/exorde_authorship__zh__x.com/validation/00001.parquet
- config_name: infini_news_authorship__ar
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__ar/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__ar/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__ar/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__ar/train/00003.parquet
    - packages/infini_news/data/infini_news_authorship__ar/train/00004.parquet
    - packages/infini_news/data/infini_news_authorship__ar/train/00005.parquet
    - packages/infini_news/data/infini_news_authorship__ar/train/00006.parquet
    - packages/infini_news/data/infini_news_authorship__ar/train/00007.parquet
    - packages/infini_news/data/infini_news_authorship__ar/train/00008.parquet
    - packages/infini_news/data/infini_news_authorship__ar/train/00009.parquet
    - packages/infini_news/data/infini_news_authorship__ar/train/00010.parquet
    - packages/infini_news/data/infini_news_authorship__ar/train/00011.parquet
    - packages/infini_news/data/infini_news_authorship__ar/train/00012.parquet
    - packages/infini_news/data/infini_news_authorship__ar/train/00013.parquet
    - packages/infini_news/data/infini_news_authorship__ar/train/00014.parquet
    - packages/infini_news/data/infini_news_authorship__ar/train/00015.parquet
    - packages/infini_news/data/infini_news_authorship__ar/train/00016.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__ar/validation/00000.parquet
    - packages/infini_news/data/infini_news_authorship__ar/validation/00001.parquet
- config_name: infini_news_authorship__bg
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__bg/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__bg/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__bg/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__bg/train/00003.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__bg/validation/00000.parquet
- config_name: infini_news_authorship__bn
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__bn/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__bn/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__bn/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__bn/train/00003.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__bn/validation/00000.parquet
- config_name: infini_news_authorship__ca
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__ca/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__ca/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__ca/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__ca/train/00003.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__ca/validation/00000.parquet
- config_name: infini_news_authorship__cs
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__cs/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__cs/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__cs/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__cs/train/00003.parquet
    - packages/infini_news/data/infini_news_authorship__cs/train/00004.parquet
    - packages/infini_news/data/infini_news_authorship__cs/train/00005.parquet
    - packages/infini_news/data/infini_news_authorship__cs/train/00006.parquet
    - packages/infini_news/data/infini_news_authorship__cs/train/00007.parquet
    - packages/infini_news/data/infini_news_authorship__cs/train/00008.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__cs/validation/00000.parquet
- config_name: infini_news_authorship__da
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__da/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__da/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__da/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__da/train/00003.parquet
    - packages/infini_news/data/infini_news_authorship__da/train/00004.parquet
    - packages/infini_news/data/infini_news_authorship__da/train/00005.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__da/validation/00000.parquet
- config_name: infini_news_authorship__de
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__de/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__de/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__de/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__de/train/00003.parquet
    - packages/infini_news/data/infini_news_authorship__de/train/00004.parquet
    - packages/infini_news/data/infini_news_authorship__de/train/00005.parquet
    - packages/infini_news/data/infini_news_authorship__de/train/00006.parquet
    - packages/infini_news/data/infini_news_authorship__de/train/00007.parquet
    - packages/infini_news/data/infini_news_authorship__de/train/00008.parquet
    - packages/infini_news/data/infini_news_authorship__de/train/00009.parquet
    - packages/infini_news/data/infini_news_authorship__de/train/00010.parquet
    - packages/infini_news/data/infini_news_authorship__de/train/00011.parquet
    - packages/infini_news/data/infini_news_authorship__de/train/00012.parquet
    - packages/infini_news/data/infini_news_authorship__de/train/00013.parquet
    - packages/infini_news/data/infini_news_authorship__de/train/00014.parquet
    - packages/infini_news/data/infini_news_authorship__de/train/00015.parquet
    - packages/infini_news/data/infini_news_authorship__de/train/00016.parquet
    - packages/infini_news/data/infini_news_authorship__de/train/00017.parquet
    - packages/infini_news/data/infini_news_authorship__de/train/00018.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__de/validation/00000.parquet
    - packages/infini_news/data/infini_news_authorship__de/validation/00001.parquet
- config_name: infini_news_authorship__el
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__el/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__el/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__el/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__el/train/00003.parquet
    - packages/infini_news/data/infini_news_authorship__el/train/00004.parquet
    - packages/infini_news/data/infini_news_authorship__el/train/00005.parquet
    - packages/infini_news/data/infini_news_authorship__el/train/00006.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__el/validation/00000.parquet
- config_name: infini_news_authorship__en
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__en/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__en/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__en/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__en/train/00003.parquet
    - packages/infini_news/data/infini_news_authorship__en/train/00004.parquet
    - packages/infini_news/data/infini_news_authorship__en/train/00005.parquet
    - packages/infini_news/data/infini_news_authorship__en/train/00006.parquet
    - packages/infini_news/data/infini_news_authorship__en/train/00007.parquet
    - packages/infini_news/data/infini_news_authorship__en/train/00008.parquet
    - packages/infini_news/data/infini_news_authorship__en/train/00009.parquet
    - packages/infini_news/data/infini_news_authorship__en/train/00010.parquet
    - packages/infini_news/data/infini_news_authorship__en/train/00011.parquet
    - packages/infini_news/data/infini_news_authorship__en/train/00012.parquet
    - packages/infini_news/data/infini_news_authorship__en/train/00013.parquet
    - packages/infini_news/data/infini_news_authorship__en/train/00014.parquet
    - packages/infini_news/data/infini_news_authorship__en/train/00015.parquet
    - packages/infini_news/data/infini_news_authorship__en/train/00016.parquet
    - packages/infini_news/data/infini_news_authorship__en/train/00017.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__en/validation/00000.parquet
    - packages/infini_news/data/infini_news_authorship__en/validation/00001.parquet
- config_name: infini_news_authorship__es
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__es/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__es/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__es/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__es/train/00003.parquet
    - packages/infini_news/data/infini_news_authorship__es/train/00004.parquet
    - packages/infini_news/data/infini_news_authorship__es/train/00005.parquet
    - packages/infini_news/data/infini_news_authorship__es/train/00006.parquet
    - packages/infini_news/data/infini_news_authorship__es/train/00007.parquet
    - packages/infini_news/data/infini_news_authorship__es/train/00008.parquet
    - packages/infini_news/data/infini_news_authorship__es/train/00009.parquet
    - packages/infini_news/data/infini_news_authorship__es/train/00010.parquet
    - packages/infini_news/data/infini_news_authorship__es/train/00011.parquet
    - packages/infini_news/data/infini_news_authorship__es/train/00012.parquet
    - packages/infini_news/data/infini_news_authorship__es/train/00013.parquet
    - packages/infini_news/data/infini_news_authorship__es/train/00014.parquet
    - packages/infini_news/data/infini_news_authorship__es/train/00015.parquet
    - packages/infini_news/data/infini_news_authorship__es/train/00016.parquet
    - packages/infini_news/data/infini_news_authorship__es/train/00017.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__es/validation/00000.parquet
    - packages/infini_news/data/infini_news_authorship__es/validation/00001.parquet
- config_name: infini_news_authorship__fa
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__fa/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__fa/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__fa/train/00002.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__fa/validation/00000.parquet
- config_name: infini_news_authorship__fi
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__fi/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__fi/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__fi/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__fi/train/00003.parquet
    - packages/infini_news/data/infini_news_authorship__fi/train/00004.parquet
    - packages/infini_news/data/infini_news_authorship__fi/train/00005.parquet
    - packages/infini_news/data/infini_news_authorship__fi/train/00006.parquet
    - packages/infini_news/data/infini_news_authorship__fi/train/00007.parquet
    - packages/infini_news/data/infini_news_authorship__fi/train/00008.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__fi/validation/00000.parquet
- config_name: infini_news_authorship__fil
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__fil/train/00000.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__fil/validation/00000.parquet
- config_name: infini_news_authorship__fr
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__fr/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__fr/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__fr/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__fr/train/00003.parquet
    - packages/infini_news/data/infini_news_authorship__fr/train/00004.parquet
    - packages/infini_news/data/infini_news_authorship__fr/train/00005.parquet
    - packages/infini_news/data/infini_news_authorship__fr/train/00006.parquet
    - packages/infini_news/data/infini_news_authorship__fr/train/00007.parquet
    - packages/infini_news/data/infini_news_authorship__fr/train/00008.parquet
    - packages/infini_news/data/infini_news_authorship__fr/train/00009.parquet
    - packages/infini_news/data/infini_news_authorship__fr/train/00010.parquet
    - packages/infini_news/data/infini_news_authorship__fr/train/00011.parquet
    - packages/infini_news/data/infini_news_authorship__fr/train/00012.parquet
    - packages/infini_news/data/infini_news_authorship__fr/train/00013.parquet
    - packages/infini_news/data/infini_news_authorship__fr/train/00014.parquet
    - packages/infini_news/data/infini_news_authorship__fr/train/00015.parquet
    - packages/infini_news/data/infini_news_authorship__fr/train/00016.parquet
    - packages/infini_news/data/infini_news_authorship__fr/train/00017.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__fr/validation/00000.parquet
    - packages/infini_news/data/infini_news_authorship__fr/validation/00001.parquet
- config_name: infini_news_authorship__he
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__he/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__he/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__he/train/00002.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__he/validation/00000.parquet
- config_name: infini_news_authorship__hi
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__hi/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__hi/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__hi/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__hi/train/00003.parquet
    - packages/infini_news/data/infini_news_authorship__hi/train/00004.parquet
    - packages/infini_news/data/infini_news_authorship__hi/train/00005.parquet
    - packages/infini_news/data/infini_news_authorship__hi/train/00006.parquet
    - packages/infini_news/data/infini_news_authorship__hi/train/00007.parquet
    - packages/infini_news/data/infini_news_authorship__hi/train/00008.parquet
    - packages/infini_news/data/infini_news_authorship__hi/train/00009.parquet
    - packages/infini_news/data/infini_news_authorship__hi/train/00010.parquet
    - packages/infini_news/data/infini_news_authorship__hi/train/00011.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__hi/validation/00000.parquet
    - packages/infini_news/data/infini_news_authorship__hi/validation/00001.parquet
- config_name: infini_news_authorship__hr
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__hr/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__hr/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__hr/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__hr/train/00003.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__hr/validation/00000.parquet
- config_name: infini_news_authorship__hu
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__hu/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__hu/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__hu/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__hu/train/00003.parquet
    - packages/infini_news/data/infini_news_authorship__hu/train/00004.parquet
    - packages/infini_news/data/infini_news_authorship__hu/train/00005.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__hu/validation/00000.parquet
- config_name: infini_news_authorship__hy
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__hy/train/00000.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__hy/validation/00000.parquet
- config_name: infini_news_authorship__id
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__id/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__id/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__id/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__id/train/00003.parquet
    - packages/infini_news/data/infini_news_authorship__id/train/00004.parquet
    - packages/infini_news/data/infini_news_authorship__id/train/00005.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__id/validation/00000.parquet
- config_name: infini_news_authorship__it
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__it/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__it/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__it/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__it/train/00003.parquet
    - packages/infini_news/data/infini_news_authorship__it/train/00004.parquet
    - packages/infini_news/data/infini_news_authorship__it/train/00005.parquet
    - packages/infini_news/data/infini_news_authorship__it/train/00006.parquet
    - packages/infini_news/data/infini_news_authorship__it/train/00007.parquet
    - packages/infini_news/data/infini_news_authorship__it/train/00008.parquet
    - packages/infini_news/data/infini_news_authorship__it/train/00009.parquet
    - packages/infini_news/data/infini_news_authorship__it/train/00010.parquet
    - packages/infini_news/data/infini_news_authorship__it/train/00011.parquet
    - packages/infini_news/data/infini_news_authorship__it/train/00012.parquet
    - packages/infini_news/data/infini_news_authorship__it/train/00013.parquet
    - packages/infini_news/data/infini_news_authorship__it/train/00014.parquet
    - packages/infini_news/data/infini_news_authorship__it/train/00015.parquet
    - packages/infini_news/data/infini_news_authorship__it/train/00016.parquet
    - packages/infini_news/data/infini_news_authorship__it/train/00017.parquet
    - packages/infini_news/data/infini_news_authorship__it/train/00018.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__it/validation/00000.parquet
    - packages/infini_news/data/infini_news_authorship__it/validation/00001.parquet
- config_name: infini_news_authorship__ja
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__ja/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__ja/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__ja/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__ja/train/00003.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__ja/validation/00000.parquet
- config_name: infini_news_authorship__ka
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__ka/train/00000.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__ka/validation/00000.parquet
- config_name: infini_news_authorship__kk
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__kk/train/00000.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__kk/validation/00000.parquet
- config_name: infini_news_authorship__ko
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__ko/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__ko/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__ko/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__ko/train/00003.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__ko/validation/00000.parquet
- config_name: infini_news_authorship__lv
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__lv/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__lv/train/00001.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__lv/validation/00000.parquet
- config_name: infini_news_authorship__ml
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__ml/train/00000.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__ml/validation/00000.parquet
- config_name: infini_news_authorship__mr
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__mr/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__mr/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__mr/train/00002.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__mr/validation/00000.parquet
- config_name: infini_news_authorship__ms
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__ms/train/00000.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__ms/validation/00000.parquet
- config_name: infini_news_authorship__nb
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__nb/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__nb/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__nb/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__nb/train/00003.parquet
    - packages/infini_news/data/infini_news_authorship__nb/train/00004.parquet
    - packages/infini_news/data/infini_news_authorship__nb/train/00005.parquet
    - packages/infini_news/data/infini_news_authorship__nb/train/00006.parquet
    - packages/infini_news/data/infini_news_authorship__nb/train/00007.parquet
    - packages/infini_news/data/infini_news_authorship__nb/train/00008.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__nb/validation/00000.parquet
- config_name: infini_news_authorship__nl
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__nl/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__nl/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__nl/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__nl/train/00003.parquet
    - packages/infini_news/data/infini_news_authorship__nl/train/00004.parquet
    - packages/infini_news/data/infini_news_authorship__nl/train/00005.parquet
    - packages/infini_news/data/infini_news_authorship__nl/train/00006.parquet
    - packages/infini_news/data/infini_news_authorship__nl/train/00007.parquet
    - packages/infini_news/data/infini_news_authorship__nl/train/00008.parquet
    - packages/infini_news/data/infini_news_authorship__nl/train/00009.parquet
    - packages/infini_news/data/infini_news_authorship__nl/train/00010.parquet
    - packages/infini_news/data/infini_news_authorship__nl/train/00011.parquet
    - packages/infini_news/data/infini_news_authorship__nl/train/00012.parquet
    - packages/infini_news/data/infini_news_authorship__nl/train/00013.parquet
    - packages/infini_news/data/infini_news_authorship__nl/train/00014.parquet
    - packages/infini_news/data/infini_news_authorship__nl/train/00015.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__nl/validation/00000.parquet
    - packages/infini_news/data/infini_news_authorship__nl/validation/00001.parquet
- config_name: infini_news_authorship__pl
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__pl/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__pl/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__pl/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__pl/train/00003.parquet
    - packages/infini_news/data/infini_news_authorship__pl/train/00004.parquet
    - packages/infini_news/data/infini_news_authorship__pl/train/00005.parquet
    - packages/infini_news/data/infini_news_authorship__pl/train/00006.parquet
    - packages/infini_news/data/infini_news_authorship__pl/train/00007.parquet
    - packages/infini_news/data/infini_news_authorship__pl/train/00008.parquet
    - packages/infini_news/data/infini_news_authorship__pl/train/00009.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__pl/validation/00000.parquet
    - packages/infini_news/data/infini_news_authorship__pl/validation/00001.parquet
- config_name: infini_news_authorship__pt
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__pt/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__pt/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__pt/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__pt/train/00003.parquet
    - packages/infini_news/data/infini_news_authorship__pt/train/00004.parquet
    - packages/infini_news/data/infini_news_authorship__pt/train/00005.parquet
    - packages/infini_news/data/infini_news_authorship__pt/train/00006.parquet
    - packages/infini_news/data/infini_news_authorship__pt/train/00007.parquet
    - packages/infini_news/data/infini_news_authorship__pt/train/00008.parquet
    - packages/infini_news/data/infini_news_authorship__pt/train/00009.parquet
    - packages/infini_news/data/infini_news_authorship__pt/train/00010.parquet
    - packages/infini_news/data/infini_news_authorship__pt/train/00011.parquet
    - packages/infini_news/data/infini_news_authorship__pt/train/00012.parquet
    - packages/infini_news/data/infini_news_authorship__pt/train/00013.parquet
    - packages/infini_news/data/infini_news_authorship__pt/train/00014.parquet
    - packages/infini_news/data/infini_news_authorship__pt/train/00015.parquet
    - packages/infini_news/data/infini_news_authorship__pt/train/00016.parquet
    - packages/infini_news/data/infini_news_authorship__pt/train/00017.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__pt/validation/00000.parquet
    - packages/infini_news/data/infini_news_authorship__pt/validation/00001.parquet
- config_name: infini_news_authorship__ro
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__ro/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__ro/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__ro/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__ro/train/00003.parquet
    - packages/infini_news/data/infini_news_authorship__ro/train/00004.parquet
    - packages/infini_news/data/infini_news_authorship__ro/train/00005.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__ro/validation/00000.parquet
- config_name: infini_news_authorship__ru
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__ru/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__ru/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__ru/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__ru/train/00003.parquet
    - packages/infini_news/data/infini_news_authorship__ru/train/00004.parquet
    - packages/infini_news/data/infini_news_authorship__ru/train/00005.parquet
    - packages/infini_news/data/infini_news_authorship__ru/train/00006.parquet
    - packages/infini_news/data/infini_news_authorship__ru/train/00007.parquet
    - packages/infini_news/data/infini_news_authorship__ru/train/00008.parquet
    - packages/infini_news/data/infini_news_authorship__ru/train/00009.parquet
    - packages/infini_news/data/infini_news_authorship__ru/train/00010.parquet
    - packages/infini_news/data/infini_news_authorship__ru/train/00011.parquet
    - packages/infini_news/data/infini_news_authorship__ru/train/00012.parquet
    - packages/infini_news/data/infini_news_authorship__ru/train/00013.parquet
    - packages/infini_news/data/infini_news_authorship__ru/train/00014.parquet
    - packages/infini_news/data/infini_news_authorship__ru/train/00015.parquet
    - packages/infini_news/data/infini_news_authorship__ru/train/00016.parquet
    - packages/infini_news/data/infini_news_authorship__ru/train/00017.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__ru/validation/00000.parquet
    - packages/infini_news/data/infini_news_authorship__ru/validation/00001.parquet
    - packages/infini_news/data/infini_news_authorship__ru/validation/00002.parquet
- config_name: infini_news_authorship__sl
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__sl/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__sl/train/00001.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__sl/validation/00000.parquet
- config_name: infini_news_authorship__sr
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__sr/train/00000.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__sr/validation/00000.parquet
- config_name: infini_news_authorship__sv
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__sv/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__sv/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__sv/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__sv/train/00003.parquet
    - packages/infini_news/data/infini_news_authorship__sv/train/00004.parquet
    - packages/infini_news/data/infini_news_authorship__sv/train/00005.parquet
    - packages/infini_news/data/infini_news_authorship__sv/train/00006.parquet
    - packages/infini_news/data/infini_news_authorship__sv/train/00007.parquet
    - packages/infini_news/data/infini_news_authorship__sv/train/00008.parquet
    - packages/infini_news/data/infini_news_authorship__sv/train/00009.parquet
    - packages/infini_news/data/infini_news_authorship__sv/train/00010.parquet
    - packages/infini_news/data/infini_news_authorship__sv/train/00011.parquet
    - packages/infini_news/data/infini_news_authorship__sv/train/00012.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__sv/validation/00000.parquet
    - packages/infini_news/data/infini_news_authorship__sv/validation/00001.parquet
- config_name: infini_news_authorship__sw
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__sw/train/00000.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__sw/validation/00000.parquet
- config_name: infini_news_authorship__ta
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__ta/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__ta/train/00001.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__ta/validation/00000.parquet
- config_name: infini_news_authorship__th
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__th/train/00000.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__th/validation/00000.parquet
- config_name: infini_news_authorship__tr
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__tr/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__tr/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__tr/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__tr/train/00003.parquet
    - packages/infini_news/data/infini_news_authorship__tr/train/00004.parquet
    - packages/infini_news/data/infini_news_authorship__tr/train/00005.parquet
    - packages/infini_news/data/infini_news_authorship__tr/train/00006.parquet
    - packages/infini_news/data/infini_news_authorship__tr/train/00007.parquet
    - packages/infini_news/data/infini_news_authorship__tr/train/00008.parquet
    - packages/infini_news/data/infini_news_authorship__tr/train/00009.parquet
    - packages/infini_news/data/infini_news_authorship__tr/train/00010.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__tr/validation/00000.parquet
    - packages/infini_news/data/infini_news_authorship__tr/validation/00001.parquet
- config_name: infini_news_authorship__uk
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__uk/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__uk/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__uk/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__uk/train/00003.parquet
    - packages/infini_news/data/infini_news_authorship__uk/train/00004.parquet
    - packages/infini_news/data/infini_news_authorship__uk/train/00005.parquet
    - packages/infini_news/data/infini_news_authorship__uk/train/00006.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__uk/validation/00000.parquet
- config_name: infini_news_authorship__ur
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__ur/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__ur/train/00001.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__ur/validation/00000.parquet
- config_name: infini_news_authorship__vi
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__vi/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__vi/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__vi/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__vi/train/00003.parquet
    - packages/infini_news/data/infini_news_authorship__vi/train/00004.parquet
    - packages/infini_news/data/infini_news_authorship__vi/train/00005.parquet
    - packages/infini_news/data/infini_news_authorship__vi/train/00006.parquet
    - packages/infini_news/data/infini_news_authorship__vi/train/00007.parquet
    - packages/infini_news/data/infini_news_authorship__vi/train/00008.parquet
    - packages/infini_news/data/infini_news_authorship__vi/train/00009.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__vi/validation/00000.parquet
    - packages/infini_news/data/infini_news_authorship__vi/validation/00001.parquet
- config_name: infini_news_authorship__zh
  data_files:
  - split: train
    path:
    - packages/infini_news/data/infini_news_authorship__zh/train/00000.parquet
    - packages/infini_news/data/infini_news_authorship__zh/train/00001.parquet
    - packages/infini_news/data/infini_news_authorship__zh/train/00002.parquet
    - packages/infini_news/data/infini_news_authorship__zh/train/00003.parquet
    - packages/infini_news/data/infini_news_authorship__zh/train/00004.parquet
    - packages/infini_news/data/infini_news_authorship__zh/train/00005.parquet
    - packages/infini_news/data/infini_news_authorship__zh/train/00006.parquet
    - packages/infini_news/data/infini_news_authorship__zh/train/00007.parquet
    - packages/infini_news/data/infini_news_authorship__zh/train/00008.parquet
  - split: validation
    path:
    - packages/infini_news/data/infini_news_authorship__zh/validation/00000.parquet
- config_name: mac_authorship
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__ar/train/00000.parquet
    - packages/mac/data/mac_authorship__ar/train/00001.parquet
    - packages/mac/data/mac_authorship__ar/train/00002.parquet
    - packages/mac/data/mac_authorship__ar/train/00003.parquet
    - packages/mac/data/mac_authorship__ar/train/00004.parquet
    - packages/mac/data/mac_authorship__ar/train/00005.parquet
    - packages/mac/data/mac_authorship__ar/train/00006.parquet
    - packages/mac/data/mac_authorship__ar/train/00007.parquet
    - packages/mac/data/mac_authorship__ar/train/00008.parquet
    - packages/mac/data/mac_authorship__ar/train/00009.parquet
    - packages/mac/data/mac_authorship__ar/train/00010.parquet
    - packages/mac/data/mac_authorship__ar/train/00011.parquet
    - packages/mac/data/mac_authorship__ar/train/00012.parquet
    - packages/mac/data/mac_authorship__bg/train/00000.parquet
    - packages/mac/data/mac_authorship__bg/train/00001.parquet
    - packages/mac/data/mac_authorship__bg/train/00002.parquet
    - packages/mac/data/mac_authorship__bg/train/00003.parquet
    - packages/mac/data/mac_authorship__cs/train/00000.parquet
    - packages/mac/data/mac_authorship__cs/train/00001.parquet
    - packages/mac/data/mac_authorship__cs/train/00002.parquet
    - packages/mac/data/mac_authorship__cs/train/00003.parquet
    - packages/mac/data/mac_authorship__cs/train/00004.parquet
    - packages/mac/data/mac_authorship__cs/train/00005.parquet
    - packages/mac/data/mac_authorship__cs/train/00006.parquet
    - packages/mac/data/mac_authorship__cs/train/00007.parquet
    - packages/mac/data/mac_authorship__cs/train/00008.parquet
    - packages/mac/data/mac_authorship__de/train/00000.parquet
    - packages/mac/data/mac_authorship__de/train/00001.parquet
    - packages/mac/data/mac_authorship__de/train/00002.parquet
    - packages/mac/data/mac_authorship__de/train/00003.parquet
    - packages/mac/data/mac_authorship__de/train/00004.parquet
    - packages/mac/data/mac_authorship__de/train/00005.parquet
    - packages/mac/data/mac_authorship__de/train/00006.parquet
    - packages/mac/data/mac_authorship__de/train/00007.parquet
    - packages/mac/data/mac_authorship__de/train/00008.parquet
    - packages/mac/data/mac_authorship__de/train/00009.parquet
    - packages/mac/data/mac_authorship__de/train/00010.parquet
    - packages/mac/data/mac_authorship__de/train/00011.parquet
    - packages/mac/data/mac_authorship__de/train/00012.parquet
    - packages/mac/data/mac_authorship__de/train/00013.parquet
    - packages/mac/data/mac_authorship__de/train/00014.parquet
    - packages/mac/data/mac_authorship__de/train/00015.parquet
    - packages/mac/data/mac_authorship__de/train/00016.parquet
    - packages/mac/data/mac_authorship__de/train/00017.parquet
    - packages/mac/data/mac_authorship__de/train/00018.parquet
    - packages/mac/data/mac_authorship__de/train/00019.parquet
    - packages/mac/data/mac_authorship__de/train/00020.parquet
    - packages/mac/data/mac_authorship__de/train/00021.parquet
    - packages/mac/data/mac_authorship__de/train/00022.parquet
    - packages/mac/data/mac_authorship__de/train/00023.parquet
    - packages/mac/data/mac_authorship__de/train/00024.parquet
    - packages/mac/data/mac_authorship__de/train/00025.parquet
    - packages/mac/data/mac_authorship__el/train/00000.parquet
    - packages/mac/data/mac_authorship__el/train/00001.parquet
    - packages/mac/data/mac_authorship__el/train/00002.parquet
    - packages/mac/data/mac_authorship__el/train/00003.parquet
    - packages/mac/data/mac_authorship__el/train/00004.parquet
    - packages/mac/data/mac_authorship__en/train/00000.parquet
    - packages/mac/data/mac_authorship__en/train/00001.parquet
    - packages/mac/data/mac_authorship__en/train/00002.parquet
    - packages/mac/data/mac_authorship__en/train/00003.parquet
    - packages/mac/data/mac_authorship__en/train/00004.parquet
    - packages/mac/data/mac_authorship__en/train/00005.parquet
    - packages/mac/data/mac_authorship__en/train/00006.parquet
    - packages/mac/data/mac_authorship__en/train/00007.parquet
    - packages/mac/data/mac_authorship__en/train/00008.parquet
    - packages/mac/data/mac_authorship__en/train/00009.parquet
    - packages/mac/data/mac_authorship__en/train/00010.parquet
    - packages/mac/data/mac_authorship__en/train/00011.parquet
    - packages/mac/data/mac_authorship__en/train/00012.parquet
    - packages/mac/data/mac_authorship__en/train/00013.parquet
    - packages/mac/data/mac_authorship__en/train/00014.parquet
    - packages/mac/data/mac_authorship__en/train/00015.parquet
    - packages/mac/data/mac_authorship__en/train/00016.parquet
    - packages/mac/data/mac_authorship__en/train/00017.parquet
    - packages/mac/data/mac_authorship__en/train/00018.parquet
    - packages/mac/data/mac_authorship__en/train/00019.parquet
    - packages/mac/data/mac_authorship__en/train/00020.parquet
    - packages/mac/data/mac_authorship__en/train/00021.parquet
    - packages/mac/data/mac_authorship__en/train/00022.parquet
    - packages/mac/data/mac_authorship__en/train/00023.parquet
    - packages/mac/data/mac_authorship__en/train/00024.parquet
    - packages/mac/data/mac_authorship__en/train/00025.parquet
    - packages/mac/data/mac_authorship__es/train/00000.parquet
    - packages/mac/data/mac_authorship__es/train/00001.parquet
    - packages/mac/data/mac_authorship__es/train/00002.parquet
    - packages/mac/data/mac_authorship__es/train/00003.parquet
    - packages/mac/data/mac_authorship__es/train/00004.parquet
    - packages/mac/data/mac_authorship__es/train/00005.parquet
    - packages/mac/data/mac_authorship__es/train/00006.parquet
    - packages/mac/data/mac_authorship__es/train/00007.parquet
    - packages/mac/data/mac_authorship__es/train/00008.parquet
    - packages/mac/data/mac_authorship__es/train/00009.parquet
    - packages/mac/data/mac_authorship__es/train/00010.parquet
    - packages/mac/data/mac_authorship__es/train/00011.parquet
    - packages/mac/data/mac_authorship__es/train/00012.parquet
    - packages/mac/data/mac_authorship__es/train/00013.parquet
    - packages/mac/data/mac_authorship__es/train/00014.parquet
    - packages/mac/data/mac_authorship__es/train/00015.parquet
    - packages/mac/data/mac_authorship__es/train/00016.parquet
    - packages/mac/data/mac_authorship__es/train/00017.parquet
    - packages/mac/data/mac_authorship__es/train/00018.parquet
    - packages/mac/data/mac_authorship__es/train/00019.parquet
    - packages/mac/data/mac_authorship__es/train/00020.parquet
    - packages/mac/data/mac_authorship__es/train/00021.parquet
    - packages/mac/data/mac_authorship__es/train/00022.parquet
    - packages/mac/data/mac_authorship__es/train/00023.parquet
    - packages/mac/data/mac_authorship__es/train/00024.parquet
    - packages/mac/data/mac_authorship__es/train/00025.parquet
    - packages/mac/data/mac_authorship__es/train/00026.parquet
    - packages/mac/data/mac_authorship__fa/train/00000.parquet
    - packages/mac/data/mac_authorship__fa/train/00001.parquet
    - packages/mac/data/mac_authorship__fa/train/00002.parquet
    - packages/mac/data/mac_authorship__fa/train/00003.parquet
    - packages/mac/data/mac_authorship__fa/train/00004.parquet
    - packages/mac/data/mac_authorship__fa/train/00005.parquet
    - packages/mac/data/mac_authorship__fa/train/00006.parquet
    - packages/mac/data/mac_authorship__fa/train/00007.parquet
    - packages/mac/data/mac_authorship__fa/train/00008.parquet
    - packages/mac/data/mac_authorship__fa/train/00009.parquet
    - packages/mac/data/mac_authorship__fa/train/00010.parquet
    - packages/mac/data/mac_authorship__fa/train/00011.parquet
    - packages/mac/data/mac_authorship__fi/train/00000.parquet
    - packages/mac/data/mac_authorship__fi/train/00001.parquet
    - packages/mac/data/mac_authorship__fi/train/00002.parquet
    - packages/mac/data/mac_authorship__fi/train/00003.parquet
    - packages/mac/data/mac_authorship__fr/train/00000.parquet
    - packages/mac/data/mac_authorship__fr/train/00001.parquet
    - packages/mac/data/mac_authorship__fr/train/00002.parquet
    - packages/mac/data/mac_authorship__fr/train/00003.parquet
    - packages/mac/data/mac_authorship__fr/train/00004.parquet
    - packages/mac/data/mac_authorship__fr/train/00005.parquet
    - packages/mac/data/mac_authorship__fr/train/00006.parquet
    - packages/mac/data/mac_authorship__fr/train/00007.parquet
    - packages/mac/data/mac_authorship__fr/train/00008.parquet
    - packages/mac/data/mac_authorship__fr/train/00009.parquet
    - packages/mac/data/mac_authorship__fr/train/00010.parquet
    - packages/mac/data/mac_authorship__fr/train/00011.parquet
    - packages/mac/data/mac_authorship__fr/train/00012.parquet
    - packages/mac/data/mac_authorship__fr/train/00013.parquet
    - packages/mac/data/mac_authorship__fr/train/00014.parquet
    - packages/mac/data/mac_authorship__fr/train/00015.parquet
    - packages/mac/data/mac_authorship__fr/train/00016.parquet
    - packages/mac/data/mac_authorship__fr/train/00017.parquet
    - packages/mac/data/mac_authorship__fr/train/00018.parquet
    - packages/mac/data/mac_authorship__fr/train/00019.parquet
    - packages/mac/data/mac_authorship__fr/train/00020.parquet
    - packages/mac/data/mac_authorship__fr/train/00021.parquet
    - packages/mac/data/mac_authorship__fr/train/00022.parquet
    - packages/mac/data/mac_authorship__fr/train/00023.parquet
    - packages/mac/data/mac_authorship__fr/train/00024.parquet
    - packages/mac/data/mac_authorship__fr/train/00025.parquet
    - packages/mac/data/mac_authorship__fr/train/00026.parquet
    - packages/mac/data/mac_authorship__he/train/00000.parquet
    - packages/mac/data/mac_authorship__he/train/00001.parquet
    - packages/mac/data/mac_authorship__he/train/00002.parquet
    - packages/mac/data/mac_authorship__he/train/00003.parquet
    - packages/mac/data/mac_authorship__he/train/00004.parquet
    - packages/mac/data/mac_authorship__he/train/00005.parquet
    - packages/mac/data/mac_authorship__he/train/00006.parquet
    - packages/mac/data/mac_authorship__he/train/00007.parquet
    - packages/mac/data/mac_authorship__he/train/00008.parquet
    - packages/mac/data/mac_authorship__he/train/00009.parquet
    - packages/mac/data/mac_authorship__he/train/00010.parquet
    - packages/mac/data/mac_authorship__hi/train/00000.parquet
    - packages/mac/data/mac_authorship__hi/train/00001.parquet
    - packages/mac/data/mac_authorship__hi/train/00002.parquet
    - packages/mac/data/mac_authorship__hu/train/00000.parquet
    - packages/mac/data/mac_authorship__hu/train/00001.parquet
    - packages/mac/data/mac_authorship__hu/train/00002.parquet
    - packages/mac/data/mac_authorship__hu/train/00003.parquet
    - packages/mac/data/mac_authorship__hu/train/00004.parquet
    - packages/mac/data/mac_authorship__hu/train/00005.parquet
    - packages/mac/data/mac_authorship__hu/train/00006.parquet
    - packages/mac/data/mac_authorship__hu/train/00007.parquet
    - packages/mac/data/mac_authorship__hy/train/00000.parquet
    - packages/mac/data/mac_authorship__hy/train/00001.parquet
    - packages/mac/data/mac_authorship__hy/train/00002.parquet
    - packages/mac/data/mac_authorship__hy/train/00003.parquet
    - packages/mac/data/mac_authorship__hy/train/00004.parquet
    - packages/mac/data/mac_authorship__id/train/00000.parquet
    - packages/mac/data/mac_authorship__id/train/00001.parquet
    - packages/mac/data/mac_authorship__id/train/00002.parquet
    - packages/mac/data/mac_authorship__id/train/00003.parquet
    - packages/mac/data/mac_authorship__id/train/00004.parquet
    - packages/mac/data/mac_authorship__id/train/00005.parquet
    - packages/mac/data/mac_authorship__id/train/00006.parquet
    - packages/mac/data/mac_authorship__it/train/00000.parquet
    - packages/mac/data/mac_authorship__it/train/00001.parquet
    - packages/mac/data/mac_authorship__it/train/00002.parquet
    - packages/mac/data/mac_authorship__it/train/00003.parquet
    - packages/mac/data/mac_authorship__it/train/00004.parquet
    - packages/mac/data/mac_authorship__it/train/00005.parquet
    - packages/mac/data/mac_authorship__it/train/00006.parquet
    - packages/mac/data/mac_authorship__it/train/00007.parquet
    - packages/mac/data/mac_authorship__it/train/00008.parquet
    - packages/mac/data/mac_authorship__it/train/00009.parquet
    - packages/mac/data/mac_authorship__it/train/00010.parquet
    - packages/mac/data/mac_authorship__it/train/00011.parquet
    - packages/mac/data/mac_authorship__it/train/00012.parquet
    - packages/mac/data/mac_authorship__it/train/00013.parquet
    - packages/mac/data/mac_authorship__it/train/00014.parquet
    - packages/mac/data/mac_authorship__it/train/00015.parquet
    - packages/mac/data/mac_authorship__it/train/00016.parquet
    - packages/mac/data/mac_authorship__it/train/00017.parquet
    - packages/mac/data/mac_authorship__it/train/00018.parquet
    - packages/mac/data/mac_authorship__it/train/00019.parquet
    - packages/mac/data/mac_authorship__it/train/00020.parquet
    - packages/mac/data/mac_authorship__it/train/00021.parquet
    - packages/mac/data/mac_authorship__it/train/00022.parquet
    - packages/mac/data/mac_authorship__it/train/00023.parquet
    - packages/mac/data/mac_authorship__it/train/00024.parquet
    - packages/mac/data/mac_authorship__it/train/00025.parquet
    - packages/mac/data/mac_authorship__it/train/00026.parquet
    - packages/mac/data/mac_authorship__ja/train/00000.parquet
    - packages/mac/data/mac_authorship__ja/train/00001.parquet
    - packages/mac/data/mac_authorship__ja/train/00002.parquet
    - packages/mac/data/mac_authorship__ja/train/00003.parquet
    - packages/mac/data/mac_authorship__ja/train/00004.parquet
    - packages/mac/data/mac_authorship__ja/train/00005.parquet
    - packages/mac/data/mac_authorship__ja/train/00006.parquet
    - packages/mac/data/mac_authorship__ja/train/00007.parquet
    - packages/mac/data/mac_authorship__ja/train/00008.parquet
    - packages/mac/data/mac_authorship__ja/train/00009.parquet
    - packages/mac/data/mac_authorship__ja/train/00010.parquet
    - packages/mac/data/mac_authorship__ja/train/00011.parquet
    - packages/mac/data/mac_authorship__ja/train/00012.parquet
    - packages/mac/data/mac_authorship__ja/train/00013.parquet
    - packages/mac/data/mac_authorship__ja/train/00014.parquet
    - packages/mac/data/mac_authorship__ja/train/00015.parquet
    - packages/mac/data/mac_authorship__ja/train/00016.parquet
    - packages/mac/data/mac_authorship__ka/train/00000.parquet
    - packages/mac/data/mac_authorship__ka/train/00001.parquet
    - packages/mac/data/mac_authorship__kk/train/00000.parquet
    - packages/mac/data/mac_authorship__kk/train/00001.parquet
    - packages/mac/data/mac_authorship__kk/train/00002.parquet
    - packages/mac/data/mac_authorship__ml/train/00000.parquet
    - packages/mac/data/mac_authorship__ml/train/00001.parquet
    - packages/mac/data/mac_authorship__nl/train/00000.parquet
    - packages/mac/data/mac_authorship__nl/train/00001.parquet
    - packages/mac/data/mac_authorship__nl/train/00002.parquet
    - packages/mac/data/mac_authorship__nl/train/00003.parquet
    - packages/mac/data/mac_authorship__nl/train/00004.parquet
    - packages/mac/data/mac_authorship__nl/train/00005.parquet
    - packages/mac/data/mac_authorship__nl/train/00006.parquet
    - packages/mac/data/mac_authorship__nl/train/00007.parquet
    - packages/mac/data/mac_authorship__nl/train/00008.parquet
    - packages/mac/data/mac_authorship__nl/train/00009.parquet
    - packages/mac/data/mac_authorship__nl/train/00010.parquet
    - packages/mac/data/mac_authorship__nl/train/00011.parquet
    - packages/mac/data/mac_authorship__nl/train/00012.parquet
    - packages/mac/data/mac_authorship__nl/train/00013.parquet
    - packages/mac/data/mac_authorship__nl/train/00014.parquet
    - packages/mac/data/mac_authorship__pl/train/00000.parquet
    - packages/mac/data/mac_authorship__pl/train/00001.parquet
    - packages/mac/data/mac_authorship__pl/train/00002.parquet
    - packages/mac/data/mac_authorship__pl/train/00003.parquet
    - packages/mac/data/mac_authorship__pl/train/00004.parquet
    - packages/mac/data/mac_authorship__pl/train/00005.parquet
    - packages/mac/data/mac_authorship__pl/train/00006.parquet
    - packages/mac/data/mac_authorship__pl/train/00007.parquet
    - packages/mac/data/mac_authorship__pl/train/00008.parquet
    - packages/mac/data/mac_authorship__pl/train/00009.parquet
    - packages/mac/data/mac_authorship__pl/train/00010.parquet
    - packages/mac/data/mac_authorship__pl/train/00011.parquet
    - packages/mac/data/mac_authorship__pl/train/00012.parquet
    - packages/mac/data/mac_authorship__pl/train/00013.parquet
    - packages/mac/data/mac_authorship__pl/train/00014.parquet
    - packages/mac/data/mac_authorship__pl/train/00015.parquet
    - packages/mac/data/mac_authorship__pl/train/00016.parquet
    - packages/mac/data/mac_authorship__pl/train/00017.parquet
    - packages/mac/data/mac_authorship__pl/train/00018.parquet
    - packages/mac/data/mac_authorship__pl/train/00019.parquet
    - packages/mac/data/mac_authorship__pt/train/00000.parquet
    - packages/mac/data/mac_authorship__pt/train/00001.parquet
    - packages/mac/data/mac_authorship__pt/train/00002.parquet
    - packages/mac/data/mac_authorship__pt/train/00003.parquet
    - packages/mac/data/mac_authorship__pt/train/00004.parquet
    - packages/mac/data/mac_authorship__pt/train/00005.parquet
    - packages/mac/data/mac_authorship__pt/train/00006.parquet
    - packages/mac/data/mac_authorship__pt/train/00007.parquet
    - packages/mac/data/mac_authorship__pt/train/00008.parquet
    - packages/mac/data/mac_authorship__pt/train/00009.parquet
    - packages/mac/data/mac_authorship__pt/train/00010.parquet
    - packages/mac/data/mac_authorship__pt/train/00011.parquet
    - packages/mac/data/mac_authorship__pt/train/00012.parquet
    - packages/mac/data/mac_authorship__pt/train/00013.parquet
    - packages/mac/data/mac_authorship__pt/train/00014.parquet
    - packages/mac/data/mac_authorship__pt/train/00015.parquet
    - packages/mac/data/mac_authorship__pt/train/00016.parquet
    - packages/mac/data/mac_authorship__pt/train/00017.parquet
    - packages/mac/data/mac_authorship__pt/train/00018.parquet
    - packages/mac/data/mac_authorship__pt/train/00019.parquet
    - packages/mac/data/mac_authorship__ru/train/00000.parquet
    - packages/mac/data/mac_authorship__ru/train/00001.parquet
    - packages/mac/data/mac_authorship__ru/train/00002.parquet
    - packages/mac/data/mac_authorship__ru/train/00003.parquet
    - packages/mac/data/mac_authorship__ru/train/00004.parquet
    - packages/mac/data/mac_authorship__ru/train/00005.parquet
    - packages/mac/data/mac_authorship__ru/train/00006.parquet
    - packages/mac/data/mac_authorship__ru/train/00007.parquet
    - packages/mac/data/mac_authorship__ru/train/00008.parquet
    - packages/mac/data/mac_authorship__ru/train/00009.parquet
    - packages/mac/data/mac_authorship__ru/train/00010.parquet
    - packages/mac/data/mac_authorship__ru/train/00011.parquet
    - packages/mac/data/mac_authorship__ru/train/00012.parquet
    - packages/mac/data/mac_authorship__ru/train/00013.parquet
    - packages/mac/data/mac_authorship__ru/train/00014.parquet
    - packages/mac/data/mac_authorship__ru/train/00015.parquet
    - packages/mac/data/mac_authorship__ru/train/00016.parquet
    - packages/mac/data/mac_authorship__ru/train/00017.parquet
    - packages/mac/data/mac_authorship__ru/train/00018.parquet
    - packages/mac/data/mac_authorship__ru/train/00019.parquet
    - packages/mac/data/mac_authorship__ru/train/00020.parquet
    - packages/mac/data/mac_authorship__ru/train/00021.parquet
    - packages/mac/data/mac_authorship__ru/train/00022.parquet
    - packages/mac/data/mac_authorship__ru/train/00023.parquet
    - packages/mac/data/mac_authorship__ru/train/00024.parquet
    - packages/mac/data/mac_authorship__ru/train/00025.parquet
    - packages/mac/data/mac_authorship__ru/train/00026.parquet
    - packages/mac/data/mac_authorship__ru/train/00027.parquet
    - packages/mac/data/mac_authorship__ru/train/00028.parquet
    - packages/mac/data/mac_authorship__ru/train/00029.parquet
    - packages/mac/data/mac_authorship__ru/train/00030.parquet
    - packages/mac/data/mac_authorship__ru/train/00031.parquet
    - packages/mac/data/mac_authorship__ru/train/00032.parquet
    - packages/mac/data/mac_authorship__ru/train/00033.parquet
    - packages/mac/data/mac_authorship__sr/train/00000.parquet
    - packages/mac/data/mac_authorship__sr/train/00001.parquet
    - packages/mac/data/mac_authorship__sr/train/00002.parquet
    - packages/mac/data/mac_authorship__sr/train/00003.parquet
    - packages/mac/data/mac_authorship__sr/train/00004.parquet
    - packages/mac/data/mac_authorship__sv/train/00000.parquet
    - packages/mac/data/mac_authorship__sv/train/00001.parquet
    - packages/mac/data/mac_authorship__sv/train/00002.parquet
    - packages/mac/data/mac_authorship__sv/train/00003.parquet
    - packages/mac/data/mac_authorship__sv/train/00004.parquet
    - packages/mac/data/mac_authorship__sv/train/00005.parquet
    - packages/mac/data/mac_authorship__sv/train/00006.parquet
    - packages/mac/data/mac_authorship__sv/train/00007.parquet
    - packages/mac/data/mac_authorship__sv/train/00008.parquet
    - packages/mac/data/mac_authorship__th/train/00000.parquet
    - packages/mac/data/mac_authorship__th/train/00001.parquet
    - packages/mac/data/mac_authorship__th/train/00002.parquet
    - packages/mac/data/mac_authorship__th/train/00003.parquet
    - packages/mac/data/mac_authorship__th/train/00004.parquet
    - packages/mac/data/mac_authorship__tr/train/00000.parquet
    - packages/mac/data/mac_authorship__tr/train/00001.parquet
    - packages/mac/data/mac_authorship__tr/train/00002.parquet
    - packages/mac/data/mac_authorship__tr/train/00003.parquet
    - packages/mac/data/mac_authorship__tr/train/00004.parquet
    - packages/mac/data/mac_authorship__tr/train/00005.parquet
    - packages/mac/data/mac_authorship__tr/train/00006.parquet
    - packages/mac/data/mac_authorship__tr/train/00007.parquet
    - packages/mac/data/mac_authorship__uk/train/00000.parquet
    - packages/mac/data/mac_authorship__uk/train/00001.parquet
    - packages/mac/data/mac_authorship__uk/train/00002.parquet
    - packages/mac/data/mac_authorship__uk/train/00003.parquet
    - packages/mac/data/mac_authorship__uk/train/00004.parquet
    - packages/mac/data/mac_authorship__uk/train/00005.parquet
    - packages/mac/data/mac_authorship__uk/train/00006.parquet
    - packages/mac/data/mac_authorship__uk/train/00007.parquet
    - packages/mac/data/mac_authorship__uk/train/00008.parquet
    - packages/mac/data/mac_authorship__uk/train/00009.parquet
    - packages/mac/data/mac_authorship__uk/train/00010.parquet
    - packages/mac/data/mac_authorship__uk/train/00011.parquet
    - packages/mac/data/mac_authorship__uk/train/00012.parquet
    - packages/mac/data/mac_authorship__uk/train/00013.parquet
    - packages/mac/data/mac_authorship__uz/train/00000.parquet
    - packages/mac/data/mac_authorship__uz/train/00001.parquet
    - packages/mac/data/mac_authorship__vi/train/00000.parquet
    - packages/mac/data/mac_authorship__vi/train/00001.parquet
    - packages/mac/data/mac_authorship__vi/train/00002.parquet
    - packages/mac/data/mac_authorship__vi/train/00003.parquet
    - packages/mac/data/mac_authorship__vi/train/00004.parquet
    - packages/mac/data/mac_authorship__vi/train/00005.parquet
    - packages/mac/data/mac_authorship__vi/train/00006.parquet
    - packages/mac/data/mac_authorship__zh/train/00000.parquet
    - packages/mac/data/mac_authorship__zh/train/00001.parquet
    - packages/mac/data/mac_authorship__zh/train/00002.parquet
    - packages/mac/data/mac_authorship__zh/train/00003.parquet
    - packages/mac/data/mac_authorship__zh/train/00004.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__ar/validation/00000.parquet
    - packages/mac/data/mac_authorship__ar/validation/00001.parquet
    - packages/mac/data/mac_authorship__bg/validation/00000.parquet
    - packages/mac/data/mac_authorship__cs/validation/00000.parquet
    - packages/mac/data/mac_authorship__de/validation/00000.parquet
    - packages/mac/data/mac_authorship__de/validation/00001.parquet
    - packages/mac/data/mac_authorship__de/validation/00002.parquet
    - packages/mac/data/mac_authorship__el/validation/00000.parquet
    - packages/mac/data/mac_authorship__en/validation/00000.parquet
    - packages/mac/data/mac_authorship__en/validation/00001.parquet
    - packages/mac/data/mac_authorship__en/validation/00002.parquet
    - packages/mac/data/mac_authorship__es/validation/00000.parquet
    - packages/mac/data/mac_authorship__es/validation/00001.parquet
    - packages/mac/data/mac_authorship__es/validation/00002.parquet
    - packages/mac/data/mac_authorship__fa/validation/00000.parquet
    - packages/mac/data/mac_authorship__fa/validation/00001.parquet
    - packages/mac/data/mac_authorship__fi/validation/00000.parquet
    - packages/mac/data/mac_authorship__fr/validation/00000.parquet
    - packages/mac/data/mac_authorship__fr/validation/00001.parquet
    - packages/mac/data/mac_authorship__fr/validation/00002.parquet
    - packages/mac/data/mac_authorship__he/validation/00000.parquet
    - packages/mac/data/mac_authorship__he/validation/00001.parquet
    - packages/mac/data/mac_authorship__hi/validation/00000.parquet
    - packages/mac/data/mac_authorship__hu/validation/00000.parquet
    - packages/mac/data/mac_authorship__hy/validation/00000.parquet
    - packages/mac/data/mac_authorship__id/validation/00000.parquet
    - packages/mac/data/mac_authorship__it/validation/00000.parquet
    - packages/mac/data/mac_authorship__it/validation/00001.parquet
    - packages/mac/data/mac_authorship__it/validation/00002.parquet
    - packages/mac/data/mac_authorship__ja/validation/00000.parquet
    - packages/mac/data/mac_authorship__ja/validation/00001.parquet
    - packages/mac/data/mac_authorship__ka/validation/00000.parquet
    - packages/mac/data/mac_authorship__kk/validation/00000.parquet
    - packages/mac/data/mac_authorship__ml/validation/00000.parquet
    - packages/mac/data/mac_authorship__nl/validation/00000.parquet
    - packages/mac/data/mac_authorship__nl/validation/00001.parquet
    - packages/mac/data/mac_authorship__pl/validation/00000.parquet
    - packages/mac/data/mac_authorship__pl/validation/00001.parquet
    - packages/mac/data/mac_authorship__pl/validation/00002.parquet
    - packages/mac/data/mac_authorship__pt/validation/00000.parquet
    - packages/mac/data/mac_authorship__pt/validation/00001.parquet
    - packages/mac/data/mac_authorship__pt/validation/00002.parquet
    - packages/mac/data/mac_authorship__ru/validation/00000.parquet
    - packages/mac/data/mac_authorship__ru/validation/00001.parquet
    - packages/mac/data/mac_authorship__ru/validation/00002.parquet
    - packages/mac/data/mac_authorship__ru/validation/00003.parquet
    - packages/mac/data/mac_authorship__sr/validation/00000.parquet
    - packages/mac/data/mac_authorship__sv/validation/00000.parquet
    - packages/mac/data/mac_authorship__sv/validation/00001.parquet
    - packages/mac/data/mac_authorship__th/validation/00000.parquet
    - packages/mac/data/mac_authorship__tr/validation/00000.parquet
    - packages/mac/data/mac_authorship__uk/validation/00000.parquet
    - packages/mac/data/mac_authorship__uk/validation/00001.parquet
    - packages/mac/data/mac_authorship__uz/validation/00000.parquet
    - packages/mac/data/mac_authorship__vi/validation/00000.parquet
    - packages/mac/data/mac_authorship__zh/validation/00000.parquet
- config_name: mac_authorship__ar
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__ar/train/00000.parquet
    - packages/mac/data/mac_authorship__ar/train/00001.parquet
    - packages/mac/data/mac_authorship__ar/train/00002.parquet
    - packages/mac/data/mac_authorship__ar/train/00003.parquet
    - packages/mac/data/mac_authorship__ar/train/00004.parquet
    - packages/mac/data/mac_authorship__ar/train/00005.parquet
    - packages/mac/data/mac_authorship__ar/train/00006.parquet
    - packages/mac/data/mac_authorship__ar/train/00007.parquet
    - packages/mac/data/mac_authorship__ar/train/00008.parquet
    - packages/mac/data/mac_authorship__ar/train/00009.parquet
    - packages/mac/data/mac_authorship__ar/train/00010.parquet
    - packages/mac/data/mac_authorship__ar/train/00011.parquet
    - packages/mac/data/mac_authorship__ar/train/00012.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__ar/validation/00000.parquet
    - packages/mac/data/mac_authorship__ar/validation/00001.parquet
- config_name: mac_authorship__bg
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__bg/train/00000.parquet
    - packages/mac/data/mac_authorship__bg/train/00001.parquet
    - packages/mac/data/mac_authorship__bg/train/00002.parquet
    - packages/mac/data/mac_authorship__bg/train/00003.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__bg/validation/00000.parquet
- config_name: mac_authorship__cs
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__cs/train/00000.parquet
    - packages/mac/data/mac_authorship__cs/train/00001.parquet
    - packages/mac/data/mac_authorship__cs/train/00002.parquet
    - packages/mac/data/mac_authorship__cs/train/00003.parquet
    - packages/mac/data/mac_authorship__cs/train/00004.parquet
    - packages/mac/data/mac_authorship__cs/train/00005.parquet
    - packages/mac/data/mac_authorship__cs/train/00006.parquet
    - packages/mac/data/mac_authorship__cs/train/00007.parquet
    - packages/mac/data/mac_authorship__cs/train/00008.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__cs/validation/00000.parquet
- config_name: mac_authorship__de
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__de/train/00000.parquet
    - packages/mac/data/mac_authorship__de/train/00001.parquet
    - packages/mac/data/mac_authorship__de/train/00002.parquet
    - packages/mac/data/mac_authorship__de/train/00003.parquet
    - packages/mac/data/mac_authorship__de/train/00004.parquet
    - packages/mac/data/mac_authorship__de/train/00005.parquet
    - packages/mac/data/mac_authorship__de/train/00006.parquet
    - packages/mac/data/mac_authorship__de/train/00007.parquet
    - packages/mac/data/mac_authorship__de/train/00008.parquet
    - packages/mac/data/mac_authorship__de/train/00009.parquet
    - packages/mac/data/mac_authorship__de/train/00010.parquet
    - packages/mac/data/mac_authorship__de/train/00011.parquet
    - packages/mac/data/mac_authorship__de/train/00012.parquet
    - packages/mac/data/mac_authorship__de/train/00013.parquet
    - packages/mac/data/mac_authorship__de/train/00014.parquet
    - packages/mac/data/mac_authorship__de/train/00015.parquet
    - packages/mac/data/mac_authorship__de/train/00016.parquet
    - packages/mac/data/mac_authorship__de/train/00017.parquet
    - packages/mac/data/mac_authorship__de/train/00018.parquet
    - packages/mac/data/mac_authorship__de/train/00019.parquet
    - packages/mac/data/mac_authorship__de/train/00020.parquet
    - packages/mac/data/mac_authorship__de/train/00021.parquet
    - packages/mac/data/mac_authorship__de/train/00022.parquet
    - packages/mac/data/mac_authorship__de/train/00023.parquet
    - packages/mac/data/mac_authorship__de/train/00024.parquet
    - packages/mac/data/mac_authorship__de/train/00025.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__de/validation/00000.parquet
    - packages/mac/data/mac_authorship__de/validation/00001.parquet
    - packages/mac/data/mac_authorship__de/validation/00002.parquet
- config_name: mac_authorship__el
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__el/train/00000.parquet
    - packages/mac/data/mac_authorship__el/train/00001.parquet
    - packages/mac/data/mac_authorship__el/train/00002.parquet
    - packages/mac/data/mac_authorship__el/train/00003.parquet
    - packages/mac/data/mac_authorship__el/train/00004.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__el/validation/00000.parquet
- config_name: mac_authorship__en
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__en/train/00000.parquet
    - packages/mac/data/mac_authorship__en/train/00001.parquet
    - packages/mac/data/mac_authorship__en/train/00002.parquet
    - packages/mac/data/mac_authorship__en/train/00003.parquet
    - packages/mac/data/mac_authorship__en/train/00004.parquet
    - packages/mac/data/mac_authorship__en/train/00005.parquet
    - packages/mac/data/mac_authorship__en/train/00006.parquet
    - packages/mac/data/mac_authorship__en/train/00007.parquet
    - packages/mac/data/mac_authorship__en/train/00008.parquet
    - packages/mac/data/mac_authorship__en/train/00009.parquet
    - packages/mac/data/mac_authorship__en/train/00010.parquet
    - packages/mac/data/mac_authorship__en/train/00011.parquet
    - packages/mac/data/mac_authorship__en/train/00012.parquet
    - packages/mac/data/mac_authorship__en/train/00013.parquet
    - packages/mac/data/mac_authorship__en/train/00014.parquet
    - packages/mac/data/mac_authorship__en/train/00015.parquet
    - packages/mac/data/mac_authorship__en/train/00016.parquet
    - packages/mac/data/mac_authorship__en/train/00017.parquet
    - packages/mac/data/mac_authorship__en/train/00018.parquet
    - packages/mac/data/mac_authorship__en/train/00019.parquet
    - packages/mac/data/mac_authorship__en/train/00020.parquet
    - packages/mac/data/mac_authorship__en/train/00021.parquet
    - packages/mac/data/mac_authorship__en/train/00022.parquet
    - packages/mac/data/mac_authorship__en/train/00023.parquet
    - packages/mac/data/mac_authorship__en/train/00024.parquet
    - packages/mac/data/mac_authorship__en/train/00025.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__en/validation/00000.parquet
    - packages/mac/data/mac_authorship__en/validation/00001.parquet
    - packages/mac/data/mac_authorship__en/validation/00002.parquet
- config_name: mac_authorship__es
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__es/train/00000.parquet
    - packages/mac/data/mac_authorship__es/train/00001.parquet
    - packages/mac/data/mac_authorship__es/train/00002.parquet
    - packages/mac/data/mac_authorship__es/train/00003.parquet
    - packages/mac/data/mac_authorship__es/train/00004.parquet
    - packages/mac/data/mac_authorship__es/train/00005.parquet
    - packages/mac/data/mac_authorship__es/train/00006.parquet
    - packages/mac/data/mac_authorship__es/train/00007.parquet
    - packages/mac/data/mac_authorship__es/train/00008.parquet
    - packages/mac/data/mac_authorship__es/train/00009.parquet
    - packages/mac/data/mac_authorship__es/train/00010.parquet
    - packages/mac/data/mac_authorship__es/train/00011.parquet
    - packages/mac/data/mac_authorship__es/train/00012.parquet
    - packages/mac/data/mac_authorship__es/train/00013.parquet
    - packages/mac/data/mac_authorship__es/train/00014.parquet
    - packages/mac/data/mac_authorship__es/train/00015.parquet
    - packages/mac/data/mac_authorship__es/train/00016.parquet
    - packages/mac/data/mac_authorship__es/train/00017.parquet
    - packages/mac/data/mac_authorship__es/train/00018.parquet
    - packages/mac/data/mac_authorship__es/train/00019.parquet
    - packages/mac/data/mac_authorship__es/train/00020.parquet
    - packages/mac/data/mac_authorship__es/train/00021.parquet
    - packages/mac/data/mac_authorship__es/train/00022.parquet
    - packages/mac/data/mac_authorship__es/train/00023.parquet
    - packages/mac/data/mac_authorship__es/train/00024.parquet
    - packages/mac/data/mac_authorship__es/train/00025.parquet
    - packages/mac/data/mac_authorship__es/train/00026.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__es/validation/00000.parquet
    - packages/mac/data/mac_authorship__es/validation/00001.parquet
    - packages/mac/data/mac_authorship__es/validation/00002.parquet
- config_name: mac_authorship__fa
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__fa/train/00000.parquet
    - packages/mac/data/mac_authorship__fa/train/00001.parquet
    - packages/mac/data/mac_authorship__fa/train/00002.parquet
    - packages/mac/data/mac_authorship__fa/train/00003.parquet
    - packages/mac/data/mac_authorship__fa/train/00004.parquet
    - packages/mac/data/mac_authorship__fa/train/00005.parquet
    - packages/mac/data/mac_authorship__fa/train/00006.parquet
    - packages/mac/data/mac_authorship__fa/train/00007.parquet
    - packages/mac/data/mac_authorship__fa/train/00008.parquet
    - packages/mac/data/mac_authorship__fa/train/00009.parquet
    - packages/mac/data/mac_authorship__fa/train/00010.parquet
    - packages/mac/data/mac_authorship__fa/train/00011.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__fa/validation/00000.parquet
    - packages/mac/data/mac_authorship__fa/validation/00001.parquet
- config_name: mac_authorship__fi
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__fi/train/00000.parquet
    - packages/mac/data/mac_authorship__fi/train/00001.parquet
    - packages/mac/data/mac_authorship__fi/train/00002.parquet
    - packages/mac/data/mac_authorship__fi/train/00003.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__fi/validation/00000.parquet
- config_name: mac_authorship__fr
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__fr/train/00000.parquet
    - packages/mac/data/mac_authorship__fr/train/00001.parquet
    - packages/mac/data/mac_authorship__fr/train/00002.parquet
    - packages/mac/data/mac_authorship__fr/train/00003.parquet
    - packages/mac/data/mac_authorship__fr/train/00004.parquet
    - packages/mac/data/mac_authorship__fr/train/00005.parquet
    - packages/mac/data/mac_authorship__fr/train/00006.parquet
    - packages/mac/data/mac_authorship__fr/train/00007.parquet
    - packages/mac/data/mac_authorship__fr/train/00008.parquet
    - packages/mac/data/mac_authorship__fr/train/00009.parquet
    - packages/mac/data/mac_authorship__fr/train/00010.parquet
    - packages/mac/data/mac_authorship__fr/train/00011.parquet
    - packages/mac/data/mac_authorship__fr/train/00012.parquet
    - packages/mac/data/mac_authorship__fr/train/00013.parquet
    - packages/mac/data/mac_authorship__fr/train/00014.parquet
    - packages/mac/data/mac_authorship__fr/train/00015.parquet
    - packages/mac/data/mac_authorship__fr/train/00016.parquet
    - packages/mac/data/mac_authorship__fr/train/00017.parquet
    - packages/mac/data/mac_authorship__fr/train/00018.parquet
    - packages/mac/data/mac_authorship__fr/train/00019.parquet
    - packages/mac/data/mac_authorship__fr/train/00020.parquet
    - packages/mac/data/mac_authorship__fr/train/00021.parquet
    - packages/mac/data/mac_authorship__fr/train/00022.parquet
    - packages/mac/data/mac_authorship__fr/train/00023.parquet
    - packages/mac/data/mac_authorship__fr/train/00024.parquet
    - packages/mac/data/mac_authorship__fr/train/00025.parquet
    - packages/mac/data/mac_authorship__fr/train/00026.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__fr/validation/00000.parquet
    - packages/mac/data/mac_authorship__fr/validation/00001.parquet
    - packages/mac/data/mac_authorship__fr/validation/00002.parquet
- config_name: mac_authorship__he
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__he/train/00000.parquet
    - packages/mac/data/mac_authorship__he/train/00001.parquet
    - packages/mac/data/mac_authorship__he/train/00002.parquet
    - packages/mac/data/mac_authorship__he/train/00003.parquet
    - packages/mac/data/mac_authorship__he/train/00004.parquet
    - packages/mac/data/mac_authorship__he/train/00005.parquet
    - packages/mac/data/mac_authorship__he/train/00006.parquet
    - packages/mac/data/mac_authorship__he/train/00007.parquet
    - packages/mac/data/mac_authorship__he/train/00008.parquet
    - packages/mac/data/mac_authorship__he/train/00009.parquet
    - packages/mac/data/mac_authorship__he/train/00010.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__he/validation/00000.parquet
    - packages/mac/data/mac_authorship__he/validation/00001.parquet
- config_name: mac_authorship__hi
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__hi/train/00000.parquet
    - packages/mac/data/mac_authorship__hi/train/00001.parquet
    - packages/mac/data/mac_authorship__hi/train/00002.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__hi/validation/00000.parquet
- config_name: mac_authorship__hu
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__hu/train/00000.parquet
    - packages/mac/data/mac_authorship__hu/train/00001.parquet
    - packages/mac/data/mac_authorship__hu/train/00002.parquet
    - packages/mac/data/mac_authorship__hu/train/00003.parquet
    - packages/mac/data/mac_authorship__hu/train/00004.parquet
    - packages/mac/data/mac_authorship__hu/train/00005.parquet
    - packages/mac/data/mac_authorship__hu/train/00006.parquet
    - packages/mac/data/mac_authorship__hu/train/00007.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__hu/validation/00000.parquet
- config_name: mac_authorship__hy
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__hy/train/00000.parquet
    - packages/mac/data/mac_authorship__hy/train/00001.parquet
    - packages/mac/data/mac_authorship__hy/train/00002.parquet
    - packages/mac/data/mac_authorship__hy/train/00003.parquet
    - packages/mac/data/mac_authorship__hy/train/00004.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__hy/validation/00000.parquet
- config_name: mac_authorship__id
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__id/train/00000.parquet
    - packages/mac/data/mac_authorship__id/train/00001.parquet
    - packages/mac/data/mac_authorship__id/train/00002.parquet
    - packages/mac/data/mac_authorship__id/train/00003.parquet
    - packages/mac/data/mac_authorship__id/train/00004.parquet
    - packages/mac/data/mac_authorship__id/train/00005.parquet
    - packages/mac/data/mac_authorship__id/train/00006.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__id/validation/00000.parquet
- config_name: mac_authorship__it
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__it/train/00000.parquet
    - packages/mac/data/mac_authorship__it/train/00001.parquet
    - packages/mac/data/mac_authorship__it/train/00002.parquet
    - packages/mac/data/mac_authorship__it/train/00003.parquet
    - packages/mac/data/mac_authorship__it/train/00004.parquet
    - packages/mac/data/mac_authorship__it/train/00005.parquet
    - packages/mac/data/mac_authorship__it/train/00006.parquet
    - packages/mac/data/mac_authorship__it/train/00007.parquet
    - packages/mac/data/mac_authorship__it/train/00008.parquet
    - packages/mac/data/mac_authorship__it/train/00009.parquet
    - packages/mac/data/mac_authorship__it/train/00010.parquet
    - packages/mac/data/mac_authorship__it/train/00011.parquet
    - packages/mac/data/mac_authorship__it/train/00012.parquet
    - packages/mac/data/mac_authorship__it/train/00013.parquet
    - packages/mac/data/mac_authorship__it/train/00014.parquet
    - packages/mac/data/mac_authorship__it/train/00015.parquet
    - packages/mac/data/mac_authorship__it/train/00016.parquet
    - packages/mac/data/mac_authorship__it/train/00017.parquet
    - packages/mac/data/mac_authorship__it/train/00018.parquet
    - packages/mac/data/mac_authorship__it/train/00019.parquet
    - packages/mac/data/mac_authorship__it/train/00020.parquet
    - packages/mac/data/mac_authorship__it/train/00021.parquet
    - packages/mac/data/mac_authorship__it/train/00022.parquet
    - packages/mac/data/mac_authorship__it/train/00023.parquet
    - packages/mac/data/mac_authorship__it/train/00024.parquet
    - packages/mac/data/mac_authorship__it/train/00025.parquet
    - packages/mac/data/mac_authorship__it/train/00026.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__it/validation/00000.parquet
    - packages/mac/data/mac_authorship__it/validation/00001.parquet
    - packages/mac/data/mac_authorship__it/validation/00002.parquet
- config_name: mac_authorship__ja
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__ja/train/00000.parquet
    - packages/mac/data/mac_authorship__ja/train/00001.parquet
    - packages/mac/data/mac_authorship__ja/train/00002.parquet
    - packages/mac/data/mac_authorship__ja/train/00003.parquet
    - packages/mac/data/mac_authorship__ja/train/00004.parquet
    - packages/mac/data/mac_authorship__ja/train/00005.parquet
    - packages/mac/data/mac_authorship__ja/train/00006.parquet
    - packages/mac/data/mac_authorship__ja/train/00007.parquet
    - packages/mac/data/mac_authorship__ja/train/00008.parquet
    - packages/mac/data/mac_authorship__ja/train/00009.parquet
    - packages/mac/data/mac_authorship__ja/train/00010.parquet
    - packages/mac/data/mac_authorship__ja/train/00011.parquet
    - packages/mac/data/mac_authorship__ja/train/00012.parquet
    - packages/mac/data/mac_authorship__ja/train/00013.parquet
    - packages/mac/data/mac_authorship__ja/train/00014.parquet
    - packages/mac/data/mac_authorship__ja/train/00015.parquet
    - packages/mac/data/mac_authorship__ja/train/00016.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__ja/validation/00000.parquet
    - packages/mac/data/mac_authorship__ja/validation/00001.parquet
- config_name: mac_authorship__ka
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__ka/train/00000.parquet
    - packages/mac/data/mac_authorship__ka/train/00001.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__ka/validation/00000.parquet
- config_name: mac_authorship__kk
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__kk/train/00000.parquet
    - packages/mac/data/mac_authorship__kk/train/00001.parquet
    - packages/mac/data/mac_authorship__kk/train/00002.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__kk/validation/00000.parquet
- config_name: mac_authorship__ml
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__ml/train/00000.parquet
    - packages/mac/data/mac_authorship__ml/train/00001.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__ml/validation/00000.parquet
- config_name: mac_authorship__nl
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__nl/train/00000.parquet
    - packages/mac/data/mac_authorship__nl/train/00001.parquet
    - packages/mac/data/mac_authorship__nl/train/00002.parquet
    - packages/mac/data/mac_authorship__nl/train/00003.parquet
    - packages/mac/data/mac_authorship__nl/train/00004.parquet
    - packages/mac/data/mac_authorship__nl/train/00005.parquet
    - packages/mac/data/mac_authorship__nl/train/00006.parquet
    - packages/mac/data/mac_authorship__nl/train/00007.parquet
    - packages/mac/data/mac_authorship__nl/train/00008.parquet
    - packages/mac/data/mac_authorship__nl/train/00009.parquet
    - packages/mac/data/mac_authorship__nl/train/00010.parquet
    - packages/mac/data/mac_authorship__nl/train/00011.parquet
    - packages/mac/data/mac_authorship__nl/train/00012.parquet
    - packages/mac/data/mac_authorship__nl/train/00013.parquet
    - packages/mac/data/mac_authorship__nl/train/00014.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__nl/validation/00000.parquet
    - packages/mac/data/mac_authorship__nl/validation/00001.parquet
- config_name: mac_authorship__pl
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__pl/train/00000.parquet
    - packages/mac/data/mac_authorship__pl/train/00001.parquet
    - packages/mac/data/mac_authorship__pl/train/00002.parquet
    - packages/mac/data/mac_authorship__pl/train/00003.parquet
    - packages/mac/data/mac_authorship__pl/train/00004.parquet
    - packages/mac/data/mac_authorship__pl/train/00005.parquet
    - packages/mac/data/mac_authorship__pl/train/00006.parquet
    - packages/mac/data/mac_authorship__pl/train/00007.parquet
    - packages/mac/data/mac_authorship__pl/train/00008.parquet
    - packages/mac/data/mac_authorship__pl/train/00009.parquet
    - packages/mac/data/mac_authorship__pl/train/00010.parquet
    - packages/mac/data/mac_authorship__pl/train/00011.parquet
    - packages/mac/data/mac_authorship__pl/train/00012.parquet
    - packages/mac/data/mac_authorship__pl/train/00013.parquet
    - packages/mac/data/mac_authorship__pl/train/00014.parquet
    - packages/mac/data/mac_authorship__pl/train/00015.parquet
    - packages/mac/data/mac_authorship__pl/train/00016.parquet
    - packages/mac/data/mac_authorship__pl/train/00017.parquet
    - packages/mac/data/mac_authorship__pl/train/00018.parquet
    - packages/mac/data/mac_authorship__pl/train/00019.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__pl/validation/00000.parquet
    - packages/mac/data/mac_authorship__pl/validation/00001.parquet
    - packages/mac/data/mac_authorship__pl/validation/00002.parquet
- config_name: mac_authorship__pt
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__pt/train/00000.parquet
    - packages/mac/data/mac_authorship__pt/train/00001.parquet
    - packages/mac/data/mac_authorship__pt/train/00002.parquet
    - packages/mac/data/mac_authorship__pt/train/00003.parquet
    - packages/mac/data/mac_authorship__pt/train/00004.parquet
    - packages/mac/data/mac_authorship__pt/train/00005.parquet
    - packages/mac/data/mac_authorship__pt/train/00006.parquet
    - packages/mac/data/mac_authorship__pt/train/00007.parquet
    - packages/mac/data/mac_authorship__pt/train/00008.parquet
    - packages/mac/data/mac_authorship__pt/train/00009.parquet
    - packages/mac/data/mac_authorship__pt/train/00010.parquet
    - packages/mac/data/mac_authorship__pt/train/00011.parquet
    - packages/mac/data/mac_authorship__pt/train/00012.parquet
    - packages/mac/data/mac_authorship__pt/train/00013.parquet
    - packages/mac/data/mac_authorship__pt/train/00014.parquet
    - packages/mac/data/mac_authorship__pt/train/00015.parquet
    - packages/mac/data/mac_authorship__pt/train/00016.parquet
    - packages/mac/data/mac_authorship__pt/train/00017.parquet
    - packages/mac/data/mac_authorship__pt/train/00018.parquet
    - packages/mac/data/mac_authorship__pt/train/00019.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__pt/validation/00000.parquet
    - packages/mac/data/mac_authorship__pt/validation/00001.parquet
    - packages/mac/data/mac_authorship__pt/validation/00002.parquet
- config_name: mac_authorship__ru
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__ru/train/00000.parquet
    - packages/mac/data/mac_authorship__ru/train/00001.parquet
    - packages/mac/data/mac_authorship__ru/train/00002.parquet
    - packages/mac/data/mac_authorship__ru/train/00003.parquet
    - packages/mac/data/mac_authorship__ru/train/00004.parquet
    - packages/mac/data/mac_authorship__ru/train/00005.parquet
    - packages/mac/data/mac_authorship__ru/train/00006.parquet
    - packages/mac/data/mac_authorship__ru/train/00007.parquet
    - packages/mac/data/mac_authorship__ru/train/00008.parquet
    - packages/mac/data/mac_authorship__ru/train/00009.parquet
    - packages/mac/data/mac_authorship__ru/train/00010.parquet
    - packages/mac/data/mac_authorship__ru/train/00011.parquet
    - packages/mac/data/mac_authorship__ru/train/00012.parquet
    - packages/mac/data/mac_authorship__ru/train/00013.parquet
    - packages/mac/data/mac_authorship__ru/train/00014.parquet
    - packages/mac/data/mac_authorship__ru/train/00015.parquet
    - packages/mac/data/mac_authorship__ru/train/00016.parquet
    - packages/mac/data/mac_authorship__ru/train/00017.parquet
    - packages/mac/data/mac_authorship__ru/train/00018.parquet
    - packages/mac/data/mac_authorship__ru/train/00019.parquet
    - packages/mac/data/mac_authorship__ru/train/00020.parquet
    - packages/mac/data/mac_authorship__ru/train/00021.parquet
    - packages/mac/data/mac_authorship__ru/train/00022.parquet
    - packages/mac/data/mac_authorship__ru/train/00023.parquet
    - packages/mac/data/mac_authorship__ru/train/00024.parquet
    - packages/mac/data/mac_authorship__ru/train/00025.parquet
    - packages/mac/data/mac_authorship__ru/train/00026.parquet
    - packages/mac/data/mac_authorship__ru/train/00027.parquet
    - packages/mac/data/mac_authorship__ru/train/00028.parquet
    - packages/mac/data/mac_authorship__ru/train/00029.parquet
    - packages/mac/data/mac_authorship__ru/train/00030.parquet
    - packages/mac/data/mac_authorship__ru/train/00031.parquet
    - packages/mac/data/mac_authorship__ru/train/00032.parquet
    - packages/mac/data/mac_authorship__ru/train/00033.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__ru/validation/00000.parquet
    - packages/mac/data/mac_authorship__ru/validation/00001.parquet
    - packages/mac/data/mac_authorship__ru/validation/00002.parquet
    - packages/mac/data/mac_authorship__ru/validation/00003.parquet
- config_name: mac_authorship__sr
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__sr/train/00000.parquet
    - packages/mac/data/mac_authorship__sr/train/00001.parquet
    - packages/mac/data/mac_authorship__sr/train/00002.parquet
    - packages/mac/data/mac_authorship__sr/train/00003.parquet
    - packages/mac/data/mac_authorship__sr/train/00004.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__sr/validation/00000.parquet
- config_name: mac_authorship__sv
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__sv/train/00000.parquet
    - packages/mac/data/mac_authorship__sv/train/00001.parquet
    - packages/mac/data/mac_authorship__sv/train/00002.parquet
    - packages/mac/data/mac_authorship__sv/train/00003.parquet
    - packages/mac/data/mac_authorship__sv/train/00004.parquet
    - packages/mac/data/mac_authorship__sv/train/00005.parquet
    - packages/mac/data/mac_authorship__sv/train/00006.parquet
    - packages/mac/data/mac_authorship__sv/train/00007.parquet
    - packages/mac/data/mac_authorship__sv/train/00008.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__sv/validation/00000.parquet
    - packages/mac/data/mac_authorship__sv/validation/00001.parquet
- config_name: mac_authorship__th
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__th/train/00000.parquet
    - packages/mac/data/mac_authorship__th/train/00001.parquet
    - packages/mac/data/mac_authorship__th/train/00002.parquet
    - packages/mac/data/mac_authorship__th/train/00003.parquet
    - packages/mac/data/mac_authorship__th/train/00004.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__th/validation/00000.parquet
- config_name: mac_authorship__tr
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__tr/train/00000.parquet
    - packages/mac/data/mac_authorship__tr/train/00001.parquet
    - packages/mac/data/mac_authorship__tr/train/00002.parquet
    - packages/mac/data/mac_authorship__tr/train/00003.parquet
    - packages/mac/data/mac_authorship__tr/train/00004.parquet
    - packages/mac/data/mac_authorship__tr/train/00005.parquet
    - packages/mac/data/mac_authorship__tr/train/00006.parquet
    - packages/mac/data/mac_authorship__tr/train/00007.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__tr/validation/00000.parquet
- config_name: mac_authorship__uk
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__uk/train/00000.parquet
    - packages/mac/data/mac_authorship__uk/train/00001.parquet
    - packages/mac/data/mac_authorship__uk/train/00002.parquet
    - packages/mac/data/mac_authorship__uk/train/00003.parquet
    - packages/mac/data/mac_authorship__uk/train/00004.parquet
    - packages/mac/data/mac_authorship__uk/train/00005.parquet
    - packages/mac/data/mac_authorship__uk/train/00006.parquet
    - packages/mac/data/mac_authorship__uk/train/00007.parquet
    - packages/mac/data/mac_authorship__uk/train/00008.parquet
    - packages/mac/data/mac_authorship__uk/train/00009.parquet
    - packages/mac/data/mac_authorship__uk/train/00010.parquet
    - packages/mac/data/mac_authorship__uk/train/00011.parquet
    - packages/mac/data/mac_authorship__uk/train/00012.parquet
    - packages/mac/data/mac_authorship__uk/train/00013.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__uk/validation/00000.parquet
    - packages/mac/data/mac_authorship__uk/validation/00001.parquet
- config_name: mac_authorship__uz
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__uz/train/00000.parquet
    - packages/mac/data/mac_authorship__uz/train/00001.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__uz/validation/00000.parquet
- config_name: mac_authorship__vi
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__vi/train/00000.parquet
    - packages/mac/data/mac_authorship__vi/train/00001.parquet
    - packages/mac/data/mac_authorship__vi/train/00002.parquet
    - packages/mac/data/mac_authorship__vi/train/00003.parquet
    - packages/mac/data/mac_authorship__vi/train/00004.parquet
    - packages/mac/data/mac_authorship__vi/train/00005.parquet
    - packages/mac/data/mac_authorship__vi/train/00006.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__vi/validation/00000.parquet
- config_name: mac_authorship__zh
  data_files:
  - split: train
    path:
    - packages/mac/data/mac_authorship__zh/train/00000.parquet
    - packages/mac/data/mac_authorship__zh/train/00001.parquet
    - packages/mac/data/mac_authorship__zh/train/00002.parquet
    - packages/mac/data/mac_authorship__zh/train/00003.parquet
    - packages/mac/data/mac_authorship__zh/train/00004.parquet
  - split: validation
    path:
    - packages/mac/data/mac_authorship__zh/validation/00000.parquet
- config_name: youtube_authorship
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__ar/train/00000.parquet
    - packages/youtube/data/youtube_authorship__ar/train/00001.parquet
    - packages/youtube/data/youtube_authorship__ar/train/00002.parquet
    - packages/youtube/data/youtube_authorship__ar/train/00003.parquet
    - packages/youtube/data/youtube_authorship__ar/train/00004.parquet
    - packages/youtube/data/youtube_authorship__ar/train/00005.parquet
    - packages/youtube/data/youtube_authorship__ar/train/00006.parquet
    - packages/youtube/data/youtube_authorship__bn/train/00000.parquet
    - packages/youtube/data/youtube_authorship__bn/train/00001.parquet
    - packages/youtube/data/youtube_authorship__bn/train/00002.parquet
    - packages/youtube/data/youtube_authorship__bn/train/00003.parquet
    - packages/youtube/data/youtube_authorship__bn/train/00004.parquet
    - packages/youtube/data/youtube_authorship__bn/train/00005.parquet
    - packages/youtube/data/youtube_authorship__bn/train/00006.parquet
    - packages/youtube/data/youtube_authorship__bn/train/00007.parquet
    - packages/youtube/data/youtube_authorship__bn/train/00008.parquet
    - packages/youtube/data/youtube_authorship__bn/train/00009.parquet
    - packages/youtube/data/youtube_authorship__bn/train/00010.parquet
    - packages/youtube/data/youtube_authorship__bn/train/00011.parquet
    - packages/youtube/data/youtube_authorship__cs/train/00000.parquet
    - packages/youtube/data/youtube_authorship__da/train/00000.parquet
    - packages/youtube/data/youtube_authorship__de/train/00000.parquet
    - packages/youtube/data/youtube_authorship__de/train/00001.parquet
    - packages/youtube/data/youtube_authorship__de/train/00002.parquet
    - packages/youtube/data/youtube_authorship__de/train/00003.parquet
    - packages/youtube/data/youtube_authorship__de/train/00004.parquet
    - packages/youtube/data/youtube_authorship__de/train/00005.parquet
    - packages/youtube/data/youtube_authorship__el/train/00000.parquet
    - packages/youtube/data/youtube_authorship__en/train/00000.parquet
    - packages/youtube/data/youtube_authorship__en/train/00001.parquet
    - packages/youtube/data/youtube_authorship__en/train/00002.parquet
    - packages/youtube/data/youtube_authorship__en/train/00003.parquet
    - packages/youtube/data/youtube_authorship__en/train/00004.parquet
    - packages/youtube/data/youtube_authorship__en/train/00005.parquet
    - packages/youtube/data/youtube_authorship__en/train/00006.parquet
    - packages/youtube/data/youtube_authorship__en/train/00007.parquet
    - packages/youtube/data/youtube_authorship__en/train/00008.parquet
    - packages/youtube/data/youtube_authorship__en/train/00009.parquet
    - packages/youtube/data/youtube_authorship__en/train/00010.parquet
    - packages/youtube/data/youtube_authorship__en/train/00011.parquet
    - packages/youtube/data/youtube_authorship__en/train/00012.parquet
    - packages/youtube/data/youtube_authorship__en/train/00013.parquet
    - packages/youtube/data/youtube_authorship__en/train/00014.parquet
    - packages/youtube/data/youtube_authorship__en/train/00015.parquet
    - packages/youtube/data/youtube_authorship__en/train/00016.parquet
    - packages/youtube/data/youtube_authorship__en/train/00017.parquet
    - packages/youtube/data/youtube_authorship__es/train/00000.parquet
    - packages/youtube/data/youtube_authorship__es/train/00001.parquet
    - packages/youtube/data/youtube_authorship__es/train/00002.parquet
    - packages/youtube/data/youtube_authorship__es/train/00003.parquet
    - packages/youtube/data/youtube_authorship__es/train/00004.parquet
    - packages/youtube/data/youtube_authorship__es/train/00005.parquet
    - packages/youtube/data/youtube_authorship__es/train/00006.parquet
    - packages/youtube/data/youtube_authorship__es/train/00007.parquet
    - packages/youtube/data/youtube_authorship__es/train/00008.parquet
    - packages/youtube/data/youtube_authorship__es/train/00009.parquet
    - packages/youtube/data/youtube_authorship__es/train/00010.parquet
    - packages/youtube/data/youtube_authorship__es/train/00011.parquet
    - packages/youtube/data/youtube_authorship__es/train/00012.parquet
    - packages/youtube/data/youtube_authorship__es/train/00013.parquet
    - packages/youtube/data/youtube_authorship__es/train/00014.parquet
    - packages/youtube/data/youtube_authorship__es/train/00015.parquet
    - packages/youtube/data/youtube_authorship__es/train/00016.parquet
    - packages/youtube/data/youtube_authorship__es/train/00017.parquet
    - packages/youtube/data/youtube_authorship__fa/train/00000.parquet
    - packages/youtube/data/youtube_authorship__fi/train/00000.parquet
    - packages/youtube/data/youtube_authorship__fil/train/00000.parquet
    - packages/youtube/data/youtube_authorship__fr/train/00000.parquet
    - packages/youtube/data/youtube_authorship__fr/train/00001.parquet
    - packages/youtube/data/youtube_authorship__fr/train/00002.parquet
    - packages/youtube/data/youtube_authorship__fr/train/00003.parquet
    - packages/youtube/data/youtube_authorship__hi/train/00000.parquet
    - packages/youtube/data/youtube_authorship__hi/train/00001.parquet
    - packages/youtube/data/youtube_authorship__hi/train/00002.parquet
    - packages/youtube/data/youtube_authorship__hi/train/00003.parquet
    - packages/youtube/data/youtube_authorship__hu/train/00000.parquet
    - packages/youtube/data/youtube_authorship__id/train/00000.parquet
    - packages/youtube/data/youtube_authorship__it/train/00000.parquet
    - packages/youtube/data/youtube_authorship__ja/train/00000.parquet
    - packages/youtube/data/youtube_authorship__ja/train/00001.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00000.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00001.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00002.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00003.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00004.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00005.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00006.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00007.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00008.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00009.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00010.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00011.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00012.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00013.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00014.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00015.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00016.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00017.parquet
    - packages/youtube/data/youtube_authorship__ml/train/00000.parquet
    - packages/youtube/data/youtube_authorship__mr/train/00000.parquet
    - packages/youtube/data/youtube_authorship__nl/train/00000.parquet
    - packages/youtube/data/youtube_authorship__pl/train/00000.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00000.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00001.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00002.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00003.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00004.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00005.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00006.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00007.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00008.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00009.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00010.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00011.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00012.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00013.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00014.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00015.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00016.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00017.parquet
    - packages/youtube/data/youtube_authorship__ro/train/00000.parquet
    - packages/youtube/data/youtube_authorship__ru/train/00000.parquet
    - packages/youtube/data/youtube_authorship__ru/train/00001.parquet
    - packages/youtube/data/youtube_authorship__ru/train/00002.parquet
    - packages/youtube/data/youtube_authorship__sl/train/00000.parquet
    - packages/youtube/data/youtube_authorship__sv/train/00000.parquet
    - packages/youtube/data/youtube_authorship__ta/train/00000.parquet
    - packages/youtube/data/youtube_authorship__th/train/00000.parquet
    - packages/youtube/data/youtube_authorship__th/train/00001.parquet
    - packages/youtube/data/youtube_authorship__th/train/00002.parquet
    - packages/youtube/data/youtube_authorship__th/train/00003.parquet
    - packages/youtube/data/youtube_authorship__th/train/00004.parquet
    - packages/youtube/data/youtube_authorship__th/train/00005.parquet
    - packages/youtube/data/youtube_authorship__th/train/00006.parquet
    - packages/youtube/data/youtube_authorship__th/train/00007.parquet
    - packages/youtube/data/youtube_authorship__th/train/00008.parquet
    - packages/youtube/data/youtube_authorship__th/train/00009.parquet
    - packages/youtube/data/youtube_authorship__th/train/00010.parquet
    - packages/youtube/data/youtube_authorship__th/train/00011.parquet
    - packages/youtube/data/youtube_authorship__th/train/00012.parquet
    - packages/youtube/data/youtube_authorship__th/train/00013.parquet
    - packages/youtube/data/youtube_authorship__th/train/00014.parquet
    - packages/youtube/data/youtube_authorship__th/train/00015.parquet
    - packages/youtube/data/youtube_authorship__th/train/00016.parquet
    - packages/youtube/data/youtube_authorship__th/train/00017.parquet
    - packages/youtube/data/youtube_authorship__tr/train/00000.parquet
    - packages/youtube/data/youtube_authorship__tr/train/00001.parquet
    - packages/youtube/data/youtube_authorship__uk/train/00000.parquet
    - packages/youtube/data/youtube_authorship__ur/train/00000.parquet
    - packages/youtube/data/youtube_authorship__uz/train/00000.parquet
    - packages/youtube/data/youtube_authorship__vi/train/00000.parquet
    - packages/youtube/data/youtube_authorship__vi/train/00001.parquet
    - packages/youtube/data/youtube_authorship__vi/train/00002.parquet
    - packages/youtube/data/youtube_authorship__vi/train/00003.parquet
    - packages/youtube/data/youtube_authorship__vi/train/00004.parquet
    - packages/youtube/data/youtube_authorship__vi/train/00005.parquet
    - packages/youtube/data/youtube_authorship__vi/train/00006.parquet
    - packages/youtube/data/youtube_authorship__zh/train/00000.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__ar/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__bn/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__bn/validation/00001.parquet
    - packages/youtube/data/youtube_authorship__cs/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__da/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__de/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__el/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__en/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__en/validation/00001.parquet
    - packages/youtube/data/youtube_authorship__es/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__es/validation/00001.parquet
    - packages/youtube/data/youtube_authorship__fa/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__fi/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__fil/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__fr/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__hi/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__hu/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__id/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__it/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__ja/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__ko/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__ko/validation/00001.parquet
    - packages/youtube/data/youtube_authorship__ml/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__mr/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__nl/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__pl/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__pt/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__pt/validation/00001.parquet
    - packages/youtube/data/youtube_authorship__ro/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__ru/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__sl/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__sv/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__ta/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__th/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__th/validation/00001.parquet
    - packages/youtube/data/youtube_authorship__tr/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__uk/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__ur/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__uz/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__vi/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__zh/validation/00000.parquet
- config_name: youtube_authorship__ar
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__ar/train/00000.parquet
    - packages/youtube/data/youtube_authorship__ar/train/00001.parquet
    - packages/youtube/data/youtube_authorship__ar/train/00002.parquet
    - packages/youtube/data/youtube_authorship__ar/train/00003.parquet
    - packages/youtube/data/youtube_authorship__ar/train/00004.parquet
    - packages/youtube/data/youtube_authorship__ar/train/00005.parquet
    - packages/youtube/data/youtube_authorship__ar/train/00006.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__ar/validation/00000.parquet
- config_name: youtube_authorship__bn
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__bn/train/00000.parquet
    - packages/youtube/data/youtube_authorship__bn/train/00001.parquet
    - packages/youtube/data/youtube_authorship__bn/train/00002.parquet
    - packages/youtube/data/youtube_authorship__bn/train/00003.parquet
    - packages/youtube/data/youtube_authorship__bn/train/00004.parquet
    - packages/youtube/data/youtube_authorship__bn/train/00005.parquet
    - packages/youtube/data/youtube_authorship__bn/train/00006.parquet
    - packages/youtube/data/youtube_authorship__bn/train/00007.parquet
    - packages/youtube/data/youtube_authorship__bn/train/00008.parquet
    - packages/youtube/data/youtube_authorship__bn/train/00009.parquet
    - packages/youtube/data/youtube_authorship__bn/train/00010.parquet
    - packages/youtube/data/youtube_authorship__bn/train/00011.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__bn/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__bn/validation/00001.parquet
- config_name: youtube_authorship__cs
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__cs/train/00000.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__cs/validation/00000.parquet
- config_name: youtube_authorship__da
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__da/train/00000.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__da/validation/00000.parquet
- config_name: youtube_authorship__de
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__de/train/00000.parquet
    - packages/youtube/data/youtube_authorship__de/train/00001.parquet
    - packages/youtube/data/youtube_authorship__de/train/00002.parquet
    - packages/youtube/data/youtube_authorship__de/train/00003.parquet
    - packages/youtube/data/youtube_authorship__de/train/00004.parquet
    - packages/youtube/data/youtube_authorship__de/train/00005.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__de/validation/00000.parquet
- config_name: youtube_authorship__el
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__el/train/00000.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__el/validation/00000.parquet
- config_name: youtube_authorship__en
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__en/train/00000.parquet
    - packages/youtube/data/youtube_authorship__en/train/00001.parquet
    - packages/youtube/data/youtube_authorship__en/train/00002.parquet
    - packages/youtube/data/youtube_authorship__en/train/00003.parquet
    - packages/youtube/data/youtube_authorship__en/train/00004.parquet
    - packages/youtube/data/youtube_authorship__en/train/00005.parquet
    - packages/youtube/data/youtube_authorship__en/train/00006.parquet
    - packages/youtube/data/youtube_authorship__en/train/00007.parquet
    - packages/youtube/data/youtube_authorship__en/train/00008.parquet
    - packages/youtube/data/youtube_authorship__en/train/00009.parquet
    - packages/youtube/data/youtube_authorship__en/train/00010.parquet
    - packages/youtube/data/youtube_authorship__en/train/00011.parquet
    - packages/youtube/data/youtube_authorship__en/train/00012.parquet
    - packages/youtube/data/youtube_authorship__en/train/00013.parquet
    - packages/youtube/data/youtube_authorship__en/train/00014.parquet
    - packages/youtube/data/youtube_authorship__en/train/00015.parquet
    - packages/youtube/data/youtube_authorship__en/train/00016.parquet
    - packages/youtube/data/youtube_authorship__en/train/00017.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__en/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__en/validation/00001.parquet
- config_name: youtube_authorship__es
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__es/train/00000.parquet
    - packages/youtube/data/youtube_authorship__es/train/00001.parquet
    - packages/youtube/data/youtube_authorship__es/train/00002.parquet
    - packages/youtube/data/youtube_authorship__es/train/00003.parquet
    - packages/youtube/data/youtube_authorship__es/train/00004.parquet
    - packages/youtube/data/youtube_authorship__es/train/00005.parquet
    - packages/youtube/data/youtube_authorship__es/train/00006.parquet
    - packages/youtube/data/youtube_authorship__es/train/00007.parquet
    - packages/youtube/data/youtube_authorship__es/train/00008.parquet
    - packages/youtube/data/youtube_authorship__es/train/00009.parquet
    - packages/youtube/data/youtube_authorship__es/train/00010.parquet
    - packages/youtube/data/youtube_authorship__es/train/00011.parquet
    - packages/youtube/data/youtube_authorship__es/train/00012.parquet
    - packages/youtube/data/youtube_authorship__es/train/00013.parquet
    - packages/youtube/data/youtube_authorship__es/train/00014.parquet
    - packages/youtube/data/youtube_authorship__es/train/00015.parquet
    - packages/youtube/data/youtube_authorship__es/train/00016.parquet
    - packages/youtube/data/youtube_authorship__es/train/00017.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__es/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__es/validation/00001.parquet
- config_name: youtube_authorship__fa
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__fa/train/00000.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__fa/validation/00000.parquet
- config_name: youtube_authorship__fi
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__fi/train/00000.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__fi/validation/00000.parquet
- config_name: youtube_authorship__fil
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__fil/train/00000.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__fil/validation/00000.parquet
- config_name: youtube_authorship__fr
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__fr/train/00000.parquet
    - packages/youtube/data/youtube_authorship__fr/train/00001.parquet
    - packages/youtube/data/youtube_authorship__fr/train/00002.parquet
    - packages/youtube/data/youtube_authorship__fr/train/00003.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__fr/validation/00000.parquet
- config_name: youtube_authorship__hi
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__hi/train/00000.parquet
    - packages/youtube/data/youtube_authorship__hi/train/00001.parquet
    - packages/youtube/data/youtube_authorship__hi/train/00002.parquet
    - packages/youtube/data/youtube_authorship__hi/train/00003.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__hi/validation/00000.parquet
- config_name: youtube_authorship__hu
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__hu/train/00000.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__hu/validation/00000.parquet
- config_name: youtube_authorship__id
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__id/train/00000.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__id/validation/00000.parquet
- config_name: youtube_authorship__it
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__it/train/00000.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__it/validation/00000.parquet
- config_name: youtube_authorship__ja
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__ja/train/00000.parquet
    - packages/youtube/data/youtube_authorship__ja/train/00001.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__ja/validation/00000.parquet
- config_name: youtube_authorship__ko
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__ko/train/00000.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00001.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00002.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00003.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00004.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00005.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00006.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00007.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00008.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00009.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00010.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00011.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00012.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00013.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00014.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00015.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00016.parquet
    - packages/youtube/data/youtube_authorship__ko/train/00017.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__ko/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__ko/validation/00001.parquet
- config_name: youtube_authorship__ml
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__ml/train/00000.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__ml/validation/00000.parquet
- config_name: youtube_authorship__mr
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__mr/train/00000.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__mr/validation/00000.parquet
- config_name: youtube_authorship__nl
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__nl/train/00000.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__nl/validation/00000.parquet
- config_name: youtube_authorship__pl
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__pl/train/00000.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__pl/validation/00000.parquet
- config_name: youtube_authorship__pt
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__pt/train/00000.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00001.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00002.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00003.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00004.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00005.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00006.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00007.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00008.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00009.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00010.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00011.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00012.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00013.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00014.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00015.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00016.parquet
    - packages/youtube/data/youtube_authorship__pt/train/00017.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__pt/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__pt/validation/00001.parquet
- config_name: youtube_authorship__ro
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__ro/train/00000.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__ro/validation/00000.parquet
- config_name: youtube_authorship__ru
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__ru/train/00000.parquet
    - packages/youtube/data/youtube_authorship__ru/train/00001.parquet
    - packages/youtube/data/youtube_authorship__ru/train/00002.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__ru/validation/00000.parquet
- config_name: youtube_authorship__sl
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__sl/train/00000.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__sl/validation/00000.parquet
- config_name: youtube_authorship__sv
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__sv/train/00000.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__sv/validation/00000.parquet
- config_name: youtube_authorship__ta
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__ta/train/00000.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__ta/validation/00000.parquet
- config_name: youtube_authorship__th
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__th/train/00000.parquet
    - packages/youtube/data/youtube_authorship__th/train/00001.parquet
    - packages/youtube/data/youtube_authorship__th/train/00002.parquet
    - packages/youtube/data/youtube_authorship__th/train/00003.parquet
    - packages/youtube/data/youtube_authorship__th/train/00004.parquet
    - packages/youtube/data/youtube_authorship__th/train/00005.parquet
    - packages/youtube/data/youtube_authorship__th/train/00006.parquet
    - packages/youtube/data/youtube_authorship__th/train/00007.parquet
    - packages/youtube/data/youtube_authorship__th/train/00008.parquet
    - packages/youtube/data/youtube_authorship__th/train/00009.parquet
    - packages/youtube/data/youtube_authorship__th/train/00010.parquet
    - packages/youtube/data/youtube_authorship__th/train/00011.parquet
    - packages/youtube/data/youtube_authorship__th/train/00012.parquet
    - packages/youtube/data/youtube_authorship__th/train/00013.parquet
    - packages/youtube/data/youtube_authorship__th/train/00014.parquet
    - packages/youtube/data/youtube_authorship__th/train/00015.parquet
    - packages/youtube/data/youtube_authorship__th/train/00016.parquet
    - packages/youtube/data/youtube_authorship__th/train/00017.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__th/validation/00000.parquet
    - packages/youtube/data/youtube_authorship__th/validation/00001.parquet
- config_name: youtube_authorship__tr
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__tr/train/00000.parquet
    - packages/youtube/data/youtube_authorship__tr/train/00001.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__tr/validation/00000.parquet
- config_name: youtube_authorship__uk
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__uk/train/00000.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__uk/validation/00000.parquet
- config_name: youtube_authorship__ur
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__ur/train/00000.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__ur/validation/00000.parquet
- config_name: youtube_authorship__uz
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__uz/train/00000.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__uz/validation/00000.parquet
- config_name: youtube_authorship__vi
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__vi/train/00000.parquet
    - packages/youtube/data/youtube_authorship__vi/train/00001.parquet
    - packages/youtube/data/youtube_authorship__vi/train/00002.parquet
    - packages/youtube/data/youtube_authorship__vi/train/00003.parquet
    - packages/youtube/data/youtube_authorship__vi/train/00004.parquet
    - packages/youtube/data/youtube_authorship__vi/train/00005.parquet
    - packages/youtube/data/youtube_authorship__vi/train/00006.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__vi/validation/00000.parquet
- config_name: youtube_authorship__zh
  data_files:
  - split: train
    path:
    - packages/youtube/data/youtube_authorship__zh/train/00000.parquet
  - split: validation
    path:
    - packages/youtube/data/youtube_authorship__zh/validation/00000.parquet
- config_name: openculture_authorship__ar
  data_files:
  - split: train
    path:
    - packages/openculture/data/openculture_authorship__ar/train/part-00000.parquet
  - split: validation
    path:
    - packages/openculture/data/openculture_authorship__ar/validation/part-00000.parquet
- config_name: openculture_authorship__bn
  data_files:
  - split: train
    path:
    - packages/openculture/data/openculture_authorship__bn/train/part-00000.parquet
  - split: validation
    path:
    - packages/openculture/data/openculture_authorship__bn/validation/part-00000.parquet
- config_name: openculture_authorship__ca
  data_files:
  - split: train
    path:
    - packages/openculture/data/openculture_authorship__ca/train/part-00000.parquet
  - split: validation
    path:
    - packages/openculture/data/openculture_authorship__ca/validation/part-00000.parquet
- config_name: openculture_authorship__da
  data_files:
  - split: train
    path:
    - packages/openculture/data/openculture_authorship__da/train/part-00000.parquet
  - split: validation
    path:
    - packages/openculture/data/openculture_authorship__da/validation/part-00000.parquet
- config_name: openculture_authorship__de
  data_files:
  - split: train
    path:
    - packages/openculture/data/openculture_authorship__de/train/part-00000.parquet
    - packages/openculture/data/openculture_authorship__de/train/part-00001.parquet
    - packages/openculture/data/openculture_authorship__de/train/part-00002.parquet
  - split: validation
    path:
    - packages/openculture/data/openculture_authorship__de/validation/part-00000.parquet
- config_name: openculture_authorship__el
  data_files:
  - split: train
    path:
    - packages/openculture/data/openculture_authorship__el/train/part-00000.parquet
  - split: validation
    path:
    - packages/openculture/data/openculture_authorship__el/validation/part-00000.parquet
- config_name: openculture_authorship__en
  data_files:
  - split: train
    path:
    - packages/openculture/data/openculture_authorship__en/train/part-00000.parquet
    - packages/openculture/data/openculture_authorship__en/train/part-00001.parquet
    - packages/openculture/data/openculture_authorship__en/train/part-00002.parquet
    - packages/openculture/data/openculture_authorship__en/train/part-00003.parquet
    - packages/openculture/data/openculture_authorship__en/train/part-00004.parquet
    - packages/openculture/data/openculture_authorship__en/train/part-00005.parquet
    - packages/openculture/data/openculture_authorship__en/train/part-00006.parquet
  - split: validation
    path:
    - packages/openculture/data/openculture_authorship__en/validation/part-00000.parquet
- config_name: openculture_authorship__es
  data_files:
  - split: train
    path:
    - packages/openculture/data/openculture_authorship__es/train/part-00000.parquet
    - packages/openculture/data/openculture_authorship__es/train/part-00001.parquet
  - split: validation
    path:
    - packages/openculture/data/openculture_authorship__es/validation/part-00000.parquet
- config_name: openculture_authorship__fr
  data_files:
  - split: train
    path:
    - packages/openculture/data/openculture_authorship__fr/train/part-00000.parquet
    - packages/openculture/data/openculture_authorship__fr/train/part-00001.parquet
    - packages/openculture/data/openculture_authorship__fr/train/part-00002.parquet
    - packages/openculture/data/openculture_authorship__fr/train/part-00003.parquet
    - packages/openculture/data/openculture_authorship__fr/train/part-00004.parquet
    - packages/openculture/data/openculture_authorship__fr/train/part-00005.parquet
  - split: validation
    path:
    - packages/openculture/data/openculture_authorship__fr/validation/part-00000.parquet
- config_name: openculture_authorship__it
  data_files:
  - split: train
    path:
    - packages/openculture/data/openculture_authorship__it/train/part-00000.parquet
    - packages/openculture/data/openculture_authorship__it/train/part-00001.parquet
  - split: validation
    path:
    - packages/openculture/data/openculture_authorship__it/validation/part-00000.parquet
- config_name: openculture_authorship__ja
  data_files:
  - split: train
    path:
    - packages/openculture/data/openculture_authorship__ja/train/part-00000.parquet
    - packages/openculture/data/openculture_authorship__ja/train/part-00001.parquet
    - packages/openculture/data/openculture_authorship__ja/train/part-00002.parquet
    - packages/openculture/data/openculture_authorship__ja/train/part-00003.parquet
    - packages/openculture/data/openculture_authorship__ja/train/part-00004.parquet
  - split: validation
    path:
    - packages/openculture/data/openculture_authorship__ja/validation/part-00000.parquet
- config_name: openculture_authorship__nl
  data_files:
  - split: train
    path:
    - packages/openculture/data/openculture_authorship__nl/train/part-00000.parquet
  - split: validation
    path:
    - packages/openculture/data/openculture_authorship__nl/validation/part-00000.parquet
- config_name: openculture_authorship__pl
  data_files:
  - split: train
    path:
    - packages/openculture/data/openculture_authorship__pl/train/part-00000.parquet
  - split: validation
    path:
    - packages/openculture/data/openculture_authorship__pl/validation/part-00000.parquet
- config_name: openculture_authorship__pt
  data_files:
  - split: train
    path:
    - packages/openculture/data/openculture_authorship__pt/train/part-00000.parquet
  - split: validation
    path:
    - packages/openculture/data/openculture_authorship__pt/validation/part-00000.parquet
- config_name: openculture_authorship__ru
  data_files:
  - split: train
    path:
    - packages/openculture/data/openculture_authorship__ru/train/part-00000.parquet
  - split: validation
    path:
    - packages/openculture/data/openculture_authorship__ru/validation/part-00000.parquet
- config_name: openculture_authorship__sv
  data_files:
  - split: train
    path:
    - packages/openculture/data/openculture_authorship__sv/train/part-00000.parquet
  - split: validation
    path:
    - packages/openculture/data/openculture_authorship__sv/validation/part-00000.parquet
- config_name: babel_briefings_authorship__ar
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__ar/train/00000.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__ar/train/00001.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__ar/validation/00000.parquet
- config_name: babel_briefings_authorship__bg
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__bg/train/00000.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__bg/validation/00000.parquet
- config_name: babel_briefings_authorship__cs
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__cs/train/00000.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__cs/train/00001.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__cs/validation/00000.parquet
- config_name: babel_briefings_authorship__de
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__de/train/00000.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__de/train/00001.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__de/train/00002.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__de/train/00003.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__de/validation/00000.parquet
- config_name: babel_briefings_authorship__el
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__el/train/00000.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__el/validation/00000.parquet
- config_name: babel_briefings_authorship__en
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__en/train/00000.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__en/train/00001.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__en/train/00002.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__en/train/00003.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__en/train/00004.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__en/train/00005.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__en/train/00006.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__en/train/00007.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__en/train/00008.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__en/train/00009.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__en/train/00010.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__en/train/00011.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__en/train/00012.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__en/train/00013.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__en/train/00014.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__en/train/00015.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__en/train/00016.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__en/validation/00000.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__en/validation/00001.parquet
- config_name: babel_briefings_authorship__es
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__es/train/00000.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__es/train/00001.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__es/train/00002.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__es/train/00003.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__es/train/00004.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__es/train/00005.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__es/validation/00000.parquet
- config_name: babel_briefings_authorship__fr
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__fr/train/00000.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__fr/train/00001.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__fr/train/00002.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__fr/train/00003.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__fr/validation/00000.parquet
- config_name: babel_briefings_authorship__he
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__he/train/00000.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__he/validation/00000.parquet
- config_name: babel_briefings_authorship__hu
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__hu/train/00000.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__hu/validation/00000.parquet
- config_name: babel_briefings_authorship__id
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__id/train/00000.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__id/train/00001.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__id/train/00002.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__id/validation/00000.parquet
- config_name: babel_briefings_authorship__it
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__it/train/00000.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__it/train/00001.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__it/train/00002.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__it/validation/00000.parquet
- config_name: babel_briefings_authorship__ja
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__ja/train/00000.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__ja/train/00001.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__ja/validation/00000.parquet
- config_name: babel_briefings_authorship__ko
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__ko/train/00000.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__ko/validation/00000.parquet
- config_name: babel_briefings_authorship__lv
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__lv/train/00000.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__lv/validation/00000.parquet
- config_name: babel_briefings_authorship__nb
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__nb/train/00000.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__nb/validation/00000.parquet
- config_name: babel_briefings_authorship__nl
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__nl/train/00000.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__nl/train/00001.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__nl/validation/00000.parquet
- config_name: babel_briefings_authorship__pl
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__pl/train/00000.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__pl/train/00001.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__pl/validation/00000.parquet
- config_name: babel_briefings_authorship__pt
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__pt/train/00000.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__pt/train/00001.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__pt/train/00002.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__pt/validation/00000.parquet
- config_name: babel_briefings_authorship__ro
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__ro/train/00000.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__ro/validation/00000.parquet
- config_name: babel_briefings_authorship__ru
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__ru/train/00000.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__ru/validation/00000.parquet
- config_name: babel_briefings_authorship__sl
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__sl/train/00000.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__sl/validation/00000.parquet
- config_name: babel_briefings_authorship__sr
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__sr/train/00000.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__sr/validation/00000.parquet
- config_name: babel_briefings_authorship__sv
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__sv/train/00000.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__sv/train/00001.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__sv/validation/00000.parquet
- config_name: babel_briefings_authorship__th
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__th/train/00000.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__th/validation/00000.parquet
- config_name: babel_briefings_authorship__tr
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__tr/train/00000.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__tr/validation/00000.parquet
- config_name: babel_briefings_authorship__uk
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__uk/train/00000.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__uk/validation/00000.parquet
- config_name: babel_briefings_authorship__zh
  data_files:
  - split: train
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__zh/train/00000.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__zh/train/00001.parquet
    - packages/babel_briefings/data/babel_briefings_authorship__zh/train/00002.parquet
  - split: validation
    path:
    - packages/babel_briefings/data/babel_briefings_authorship__zh/validation/00000.parquet
- config_name: ao3_authorship__cs
  data_files:
  - split: train
    path:
    - packages/ao3/data/ao3_authorship__cs/train/00000.parquet
  - split: validation
    path:
    - packages/ao3/data/ao3_authorship__cs/validation/00000.parquet
- config_name: ao3_authorship__de
  data_files:
  - split: train
    path:
    - packages/ao3/data/ao3_authorship__de/train/00000.parquet
  - split: validation
    path:
    - packages/ao3/data/ao3_authorship__de/validation/00000.parquet
- config_name: ao3_authorship__en
  data_files:
  - split: train
    path:
    - packages/ao3/data/ao3_authorship__en/train/00000.parquet
    - packages/ao3/data/ao3_authorship__en/train/00001.parquet
    - packages/ao3/data/ao3_authorship__en/train/00002.parquet
    - packages/ao3/data/ao3_authorship__en/train/00003.parquet
    - packages/ao3/data/ao3_authorship__en/train/00004.parquet
    - packages/ao3/data/ao3_authorship__en/train/00005.parquet
    - packages/ao3/data/ao3_authorship__en/train/00006.parquet
    - packages/ao3/data/ao3_authorship__en/train/00007.parquet
    - packages/ao3/data/ao3_authorship__en/train/00008.parquet
    - packages/ao3/data/ao3_authorship__en/train/00009.parquet
    - packages/ao3/data/ao3_authorship__en/train/00010.parquet
    - packages/ao3/data/ao3_authorship__en/train/00011.parquet
    - packages/ao3/data/ao3_authorship__en/train/00012.parquet
    - packages/ao3/data/ao3_authorship__en/train/00013.parquet
    - packages/ao3/data/ao3_authorship__en/train/00014.parquet
    - packages/ao3/data/ao3_authorship__en/train/00015.parquet
    - packages/ao3/data/ao3_authorship__en/train/00016.parquet
    - packages/ao3/data/ao3_authorship__en/train/00017.parquet
    - packages/ao3/data/ao3_authorship__en/train/00018.parquet
  - split: validation
    path:
    - packages/ao3/data/ao3_authorship__en/validation/00000.parquet
    - packages/ao3/data/ao3_authorship__en/validation/00001.parquet
    - packages/ao3/data/ao3_authorship__en/validation/00002.parquet
- config_name: ao3_authorship__es
  data_files:
  - split: train
    path:
    - packages/ao3/data/ao3_authorship__es/train/00000.parquet
    - packages/ao3/data/ao3_authorship__es/train/00001.parquet
    - packages/ao3/data/ao3_authorship__es/train/00002.parquet
  - split: validation
    path:
    - packages/ao3/data/ao3_authorship__es/validation/00000.parquet
- config_name: ao3_authorship__fi
  data_files:
  - split: train
    path:
    - packages/ao3/data/ao3_authorship__fi/train/00000.parquet
  - split: validation
    path:
    - packages/ao3/data/ao3_authorship__fi/validation/00000.parquet
- config_name: ao3_authorship__fil
  data_files:
  - split: train
    path:
    - packages/ao3/data/ao3_authorship__fil/train/00000.parquet
  - split: validation
    path:
    - packages/ao3/data/ao3_authorship__fil/validation/00000.parquet
- config_name: ao3_authorship__fr
  data_files:
  - split: train
    path:
    - packages/ao3/data/ao3_authorship__fr/train/00000.parquet
  - split: validation
    path:
    - packages/ao3/data/ao3_authorship__fr/validation/00000.parquet
- config_name: ao3_authorship__hu
  data_files:
  - split: train
    path:
    - packages/ao3/data/ao3_authorship__hu/train/00000.parquet
  - split: validation
    path:
    - packages/ao3/data/ao3_authorship__hu/validation/00000.parquet
- config_name: ao3_authorship__id
  data_files:
  - split: train
    path:
    - packages/ao3/data/ao3_authorship__id/train/00000.parquet
  - split: validation
    path:
    - packages/ao3/data/ao3_authorship__id/validation/00000.parquet
- config_name: ao3_authorship__it
  data_files:
  - split: train
    path:
    - packages/ao3/data/ao3_authorship__it/train/00000.parquet
  - split: validation
    path:
    - packages/ao3/data/ao3_authorship__it/validation/00000.parquet
- config_name: ao3_authorship__ja
  data_files:
  - split: train
    path:
    - packages/ao3/data/ao3_authorship__ja/train/00000.parquet
  - split: validation
    path:
    - packages/ao3/data/ao3_authorship__ja/validation/00000.parquet
- config_name: ao3_authorship__ko
  data_files:
  - split: train
    path:
    - packages/ao3/data/ao3_authorship__ko/train/00000.parquet
  - split: validation
    path:
    - packages/ao3/data/ao3_authorship__ko/validation/00000.parquet
- config_name: ao3_authorship__pl
  data_files:
  - split: train
    path:
    - packages/ao3/data/ao3_authorship__pl/train/00000.parquet
  - split: validation
    path:
    - packages/ao3/data/ao3_authorship__pl/validation/00000.parquet
- config_name: ao3_authorship__pt-BR
  data_files:
  - split: train
    path:
    - packages/ao3/data/ao3_authorship__pt-BR/train/00000.parquet
  - split: validation
    path:
    - packages/ao3/data/ao3_authorship__pt-BR/validation/00000.parquet
- config_name: ao3_authorship__ru
  data_files:
  - split: train
    path:
    - packages/ao3/data/ao3_authorship__ru/train/00000.parquet
    - packages/ao3/data/ao3_authorship__ru/train/00001.parquet
    - packages/ao3/data/ao3_authorship__ru/train/00002.parquet
  - split: validation
    path:
    - packages/ao3/data/ao3_authorship__ru/validation/00000.parquet
- config_name: ao3_authorship__th
  data_files:
  - split: train
    path:
    - packages/ao3/data/ao3_authorship__th/train/00000.parquet
  - split: validation
    path:
    - packages/ao3/data/ao3_authorship__th/validation/00000.parquet
- config_name: ao3_authorship__tr
  data_files:
  - split: train
    path:
    - packages/ao3/data/ao3_authorship__tr/train/00000.parquet
  - split: validation
    path:
    - packages/ao3/data/ao3_authorship__tr/validation/00000.parquet
- config_name: ao3_authorship__uk
  data_files:
  - split: train
    path:
    - packages/ao3/data/ao3_authorship__uk/train/00000.parquet
  - split: validation
    path:
    - packages/ao3/data/ao3_authorship__uk/validation/00000.parquet
- config_name: ao3_authorship__vi
  data_files:
  - split: train
    path:
    - packages/ao3/data/ao3_authorship__vi/train/00000.parquet
  - split: validation
    path:
    - packages/ao3/data/ao3_authorship__vi/validation/00000.parquet
- config_name: ao3_authorship__zh
  data_files:
  - split: train
    path:
    - packages/ao3/data/ao3_authorship__zh/train/00000.parquet
    - packages/ao3/data/ao3_authorship__zh/train/00001.parquet
    - packages/ao3/data/ao3_authorship__zh/train/00002.parquet
    - packages/ao3/data/ao3_authorship__zh/train/00003.parquet
    - packages/ao3/data/ao3_authorship__zh/train/00004.parquet
    - packages/ao3/data/ao3_authorship__zh/train/00005.parquet
    - packages/ao3/data/ao3_authorship__zh/train/00006.parquet
    - packages/ao3/data/ao3_authorship__zh/train/00007.parquet
    - packages/ao3/data/ao3_authorship__zh/train/00008.parquet
    - packages/ao3/data/ao3_authorship__zh/train/00009.parquet
    - packages/ao3/data/ao3_authorship__zh/train/00010.parquet
    - packages/ao3/data/ao3_authorship__zh/train/00011.parquet
  - split: validation
    path:
    - packages/ao3/data/ao3_authorship__zh/validation/00000.parquet
    - packages/ao3/data/ao3_authorship__zh/validation/00001.parquet
- config_name: ao3_authorship__zh-HK
  data_files:
  - split: train
    path:
    - packages/ao3/data/ao3_authorship__zh-HK/train/00000.parquet
  - split: validation
    path:
    - packages/ao3/data/ao3_authorship__zh-HK/validation/00000.parquet
language_bcp47:
- pt-BR
- zh-HK
---

# MIRM authorship datasets: MAC, Exorde, Bluesky, INFINI-NEWS, YouTube, OpenCulture, Babel Briefings and AO3

277 loadable configurations, 49 normalized language labels,
and **38,715,557 physical documents**. Aggregate aliases are not additional data.

| Source | Language/platform views | Train | Validation | Documents |
|---|---:|---:|---:|---:|
| mac | 32 | 5,824,434 | 648,080 | 6,472,514 |
| exorde | 77 | 10,602,383 | 1,178,034 | 11,780,417 |
| bluesky | 18 | 4,341,217 | 482,350 | 4,823,567 |
| infini_news | 46 | 7,934,884 | 881,653 | 8,816,537 |
| youtube | 35 | 3,380,974 | 375,671 | 3,756,645 |
| openculture | 16 | 498,626 | 55,505 | 554,131 |
| babel_briefings | 28 | 1,321,735 | 146,977 | 1,468,712 |
| ao3 | 21 | 938,713 | 104,321 | 1,043,034 |

## Loading

```python
from datasets import load_dataset
repo = "peterkirby/mymirmdatasets"
ao3 = load_dataset(repo, "ao3_authorship__en", split="train", streaming=True)
babel = load_dataset(repo, "babel_briefings_authorship__en", split="train", streaming=True)
news = load_dataset(repo, "infini_news_authorship__en", split="train", streaming=True)
openculture = load_dataset(repo, "openculture_authorship__en", split="train", streaming=True)
norwegian = load_dataset(repo, "exorde_authorship__nb__x.com", split="train", streaming=True)
```

There are exactly 46 INFINI-NEWS language configurations, named
`infini_news_authorship__<language>`; there is no INFINI-NEWS aggregate, `uz`, or
empty `no` configuration. MAC, Exorde, Bluesky and YouTube aggregate aliases
reference their leaf shards; do not concatenate an aggregate with its leaves.
See [all configuration membership and split counts](manifests/configurations.json).

## AO3 authorship publication

Adds **1,043,034 excerpts** (938,713 train; 104,321 validation) from **351,238
author-language identities**, in 21 configurations named
`ao3_authorship__<language>`. There is no aggregate alias.

Each row contains one unchanged contiguous AO3 source excerpt of 500–21,000
Unicode code points. Longer works use a centered slice moved inward to the
pinned ICU word and grapheme boundaries. Original spelling, punctuation and
whitespace are preserved. Language and account labels come from AO3 metadata,
not independent language detection or verified person identity.

Seed-42 selection retains 2–10 distinct works per author-language identity and
at most 500,000 works per language. The cleaned release requires at least 142
authors total and 129 training authors per language, with at least two validation
authors. Finnish retains all 142 surviving authors: 129 training / 659 works and
13 validation / 69 works, using the first 13 surviving authors in the existing
split order for validation. Author-language groups are disjoint between splits;
the same multilingual account can appear in different splits across languages.
Public account keys are language-scoped SHA-256 identifiers, not anonymity.

Anonymous, orphaned and coauthored records are excluded. Exact same-author
excerpt repeats collapse; excerpts attributed to multiple authors within a
language are quarantined. Repeated physical copies of a work collapse only
when language, author, excerpt hash and full-source hash agree.

STEB screening uses frozen release
`da0858cae4c4e4db0f332b63a0aabea34f934cf26f9c4cdc20dd39e27e4fab29`
and the precise reservation scope and omissions recorded in the source manifests.
Verified account-identity and text overlaps exclude the whole author-language
identity. Complete equality and exact 200+-letter/number passage checks are
lossless. Near-passage retrieval is **approximate**: sparse fingerprints,
representative posting samples, ranked candidates and bounded alignment can miss
overlaps. Every accepted near match is independently verified with at least 200
letters/numbers on both sides, Levenshtein distance no greater than 10% of the
shorter normalized span, and eight distinct ordered shared character 9-grams.
There is no 100–199-character report-only pass. Comparison normalization does
not alter exported text. A negative means no verified match found by this pinned
search, not guaranteed absence of residual overlap. Coverage excludes omitted
extra Pile texts, newer evaluation additions and source text outside the released
excerpts. Capped-language refill was screened to a fixed point; uncapped parent
splits were preserved except for the explicit Finnish quota.

AO3 authors retain rights in their works. The Academic Torrents snapshot does
**not** grant a blanket license to the stories. This publication asserts no new
rights or blanket permission for redistribution. Repository licensing remains
source-dependent. Account pseudonyms, fandom/content overlap and cross-source
person identity remain limitations.

See the [AO3 source card and per-language counts](packages/ao3/README.md),
[rights notice](packages/ao3/LICENSE.md), [validated payload audit](packages/ao3/manifests/preparation/final-payload-audit.json),
and [preparation-to-publication file map](manifests/ao3-publication.json).
The validated payloads, source metadata, labels and split membership are unchanged.
Existing source configurations and objects are preserved. Training pins are unchanged.


## Babel Briefings publication

Adds **1,468,712 descriptions** (1,321,735 train; 146,977 validation) from
**99,060 source-scoped authors**, in **28 language configurations** named
`babel_briefings_authorship__<language>`, with no aggregate alias.

The text is exclusively the original-language `description`, with outer
trimming only. Missing, non-string and whitespace-only descriptions are rejected;
there is no character minimum beyond nonempty text. Internal whitespace, Unicode,
punctuation and HTML entities are preserved. Native upstream `author#…` identifiers
are source-scoped pseudonyms, not verified people or verified description writers.
No person-name heuristics are applied.

Only existing MIRM languages are included. Upstream `no` is mapped to `nb` under
the recorded Bokmål assumption; the original language label is retained. `lt` and
`sk` are excluded. No additional language detection is performed.

AuthBench's `documents` content from **train, dev and test, across every source**
is protected against exact equality and equality after Python case-folding and
whitespace collapse. Unrelated descriptions by overlapping authors remain.
Within Babel, identical texts with consistent author/language assignments are
collapsed with occurrence lineage; conflicting assignments are quarantined.

STEB screening protects frozen release
`da0858cae4c4e4db0f332b63a0aabea34f934cf26f9c4cdc20dd39e27e4fab29`:
current validation/test and complete canonical probing pools (507 physical files;
2,406,625 string members). A description is excluded if its **entire normalized
text occurs anywhere inside one individual normalized STEB text**, in either channel:

1. Python case-folding followed by whitespace collapse.
2. HTML-unescape once, NFKC, case-fold, then retain Unicode letters, marks and numbers.

Every nonempty normalized description is screened, including one-character
descriptions; a channel with an empty pattern is skipped. No word boundaries,
concatenation of members, approximate matching or author-level exclusion is used.
Exported text is unchanged. The screen removed **2,888 matched descriptions**;
**56 additional rows** were removed from author/language groups left with fewer
than two distinct descriptions. No language failed the final thresholds.

Seed-42 selection originally admitted authors with two texts first, then allocated
remaining capacity round-robin. Bounds are 2–100 distinct descriptions per
author/language and 500,000 per language. Each language requires 143 authors
combined, 128 in training and two in validation. Deterministic grouped splits
target approximately 10% validation rows and keep each author in one split across
languages. Screening performs no refill, relabeling or split rebalancing. Surviving
numeric labels and train/validation assignments are preserved; label gaps remain.

The source is Felix Leeb and Bernhard Schölkopf's
[Babel Briefings (NAACL 2024)](https://aclanthology.org/2024.naacl-short.55/),
declared **CC BY-NC-SA 4.0**. Repository licensing remains source-dependent.
See the [Babel source card and per-language counts](packages/babel_briefings/README.md),
[author mappings](packages/babel_briefings/manifests/labels.parquet),
[sampler counts](packages/babel_briefings/manifests/sampler_index.parquet),
[physical row locators](packages/babel_briefings/manifests/rows.parquet),
[exclusion ledger](packages/babel_briefings/manifests/dispositions.parquet),
[independent audit](packages/babel_briefings/manifests/preparation/independent-audit.json),
and [publication file map](manifests/babel-publication.json).
All 98 payload shards and processing manifests retain their validated bytes.
Training code and pins are unchanged.


## OpenCulture authorship publication

Contains **554,131 text excerpts** (498,626 train; 55,505 validation) across
**122,502 author-language groups** in 16 configurations,
`openculture_authorship__<language>`. There is no OpenCulture aggregate.
The retained languages are `en`, `fr`, `de`, `it`, `es`, `ja`, `ar`, `ru`,
`nl`, `pt`, `bn`, `el`, `da`, `ca`, `sv`, and `pl`.

Texts come from OpenCulture book and multilingual sources and documented
derivatives. Each row retains one contiguous excerpt of at most **21,000 Unicode
code points**, centered on the complete source text when truncation is needed,
with both ends aligned to word boundaries. Original spelling, punctuation,
whitespace and line endings are preserved; no normalization or concatenation is
applied to exported text. Source and excerpt hashes, offsets, rights notices,
attribution evidence and original source locators remain in the payload.

Attribution includes supported and reasonably inferred individual sole authors,
including creator-only credits. These are best-guess source-scoped identities,
not globally verified people. Each retained author-language group has at least
two distinct surviving work families after acquisition, curation, deduplication
and benchmark exclusions. Original seed-42 author-grouped train/validation
assignments and numeric labels are unchanged. All qualifying works remain,
including 74 author-language groups with more than 100 works.

Exact-passage winnowing screens the retained excerpts against pinned current
STEB test/validation inputs and canonical probing pools, plus AuthBench dev/test.
It removes shared passages of at least 200 normalized code points and whole-text
matches, followed by groups left with fewer than two works. This does not establish
near-duplicate or author separation, cover unavailable references, or screen text
outside these excerpts. Scientific eligibility flags are unchanged, including
`training_export_cleared=false`.

The package uses the shared MIRM columns, Zstandard Parquet, 128-row groups and
approximately 256 MiB shards. `primary_labels.parquet`, `sampler_index.parquet`
and `rows.jsonl.gz` account for every published work and its physical row locator.
Numeric labels use the `openculture` source namespace. Licensing is source-dependent;
review was confirmed complete for the published samples. No blanket text license
is asserted, and original rights notices are retained.

This is a data-format publication only; training loaders and pins are unchanged.
Future integration must register the source and address the existing 100-work
loader restriction. Catalan, Swedish and Polish have 123, 114 and 92 training
authors respectively, below the default 128-author sampling requirement.

## YouTube comment publication

Adds **3,756,645 comments** from **1,639,131 accounts** in 35 language
configurations, `youtube_authorship__<language>`, plus `youtube_authorship`.
The aggregate references the same 199 physical shards; do not concatenate it
with the language views. Train has 3,380,974 comments and validation has 375,671.

```python
youtube = load_dataset(repo, "youtube_authorship__en", split="train", streaming=True)
youtube_all = load_dataset(repo, "youtube_authorship", split="validation", streaming=True)
```

The source is [YTCommentVerse, Zenodo record 15678816](https://zenodo.org/records/15678816),
Hridoy Sankar Dutta and Biswadeep Khan (2025), declared CC BY 4.0.
No character minimum applies. Accounts contribute 2–10 distinct comments per
language; a language requires 143 eligible accounts. The cap is 500,000 comments
per language across train and validation combined. GlotLID v3 independently
labels comments at confidence >=0.8. Seed-42 splits group accounts across languages.

The complete exported text has zero normalized exact overlap with AuthBench
dev/test and the frozen STEB current evaluation inputs: test, validation,
canonical probing pools including fitting inputs, and native replay. Matching
uses Unicode case-folding, whitespace collapse and trimming. Unused upstream
test remainders are outside scope. This does not establish author or near-duplicate
separation. Retained source text, metadata, labels and splits are unchanged by upload.

See the [YouTube source card](packages/youtube/README.md),
[selection counts and exclusion reasons](packages/youtube/manifests/selection-report.json),
[STEB coverage and match witnesses](packages/youtube/manifests/steb/), and
[publication provenance](manifests/youtube-publication.json).
Numeric labels use the `youtube` source namespace. This upload leaves existing
source packages and training pins unchanged.

## INFINI-NEWS publication

The validated v4 subset contributes **8,816,537 documents** (7,934,884 train;
881,653 validation), **1,017,765 inferred identities**, and 402 unchanged article
shards. Each language has at most 500,000 documents. Each retained identity has
at least two distinct documents in each of its retained languages. Per-identity
caps are 10 or 50 according to the original selection policy. All retained
languages meet the 128-training-author minimum; the smallest has 206.

Identities use a lightly normalized single-person byline and registered domain.
For each normalized byline, only its highest-article-count domain is kept; ties
use deterministic domain ordering. Labels are inferred, not verified people:
there is no secondary author-identification signal. Accents and original bylines
are preserved. Shared multilingual identities keep the same numeric ID and
train/validation split. Numeric labels may have gaps. Uzbek was excluded because
it has 89 training authors; 48 Uzbek-only identities were removed and all 53
shared identities preserved. MAC Uzbek is unaffected.

The source is
[`ruggsea/infini-news-corpus@7f8fe13b0833c005365b81f1dee7c20b7087769b`](https://huggingface.co/datasets/ruggsea/infini-news-corpus/tree/7f8fe13b0833c005365b81f1dee7c20b7087769b).
The cutoff is crawl time before 2023-01-01 UTC, not publication date. GlotLID
language labels are upstream predictions. Exact duplicate handling uses the
original `(text_xxhash64, text_length)` key. No new language detector, author-profile
verification, later-year Uzbek extension, near-duplicate detection or cross-source
person matching was performed. Full source-fidelity evidence and original metadata
remain in the [source package](packages/infini_news/README.md).

## Shared columns and sampling metadata

All sources retain `text`, `primary_id_int`, `secondary_category_int`,
`source_record_id`, `language`, `split_group_id`, and `text_length_chars`.
Use `(source, primary_id_int)` as the numeric identity namespace; `-1` means no
secondary content-group label. INFINI-NEWS domains are provenance, not secondary
content labels. Additional columns preserve attribution, raw bylines, source-row
locators, hashes and processing metadata. Original texts, identities and splits
were not reselected for this publication.

INFINI-NEWS adds [an author/language count index](packages/infini_news/manifests/sampler_index.parquet)
and [physical output-row locators](packages/infini_news/manifests/rows.parquet).
The original `selection.parquet` records upstream source positions, not output-row
positions. These indexes supplement rather than replace it. Validation checks
their exact membership and counts against all 402 unchanged article shards.

This publication changes the data repository only. Existing training pins and
the training loader's allowed-source/configuration inventory remain unchanged;
training integration requires a separate explicit update. Within-source author
split separation does not establish cross-source separation.

## Rights and provenance

Licensing is source-dependent; see [LICENSE.md](LICENSE.md). INFINI-NEWS article
rights remain with their publishers. The upstream source declares CC-BY-4.0 for
derived metadata, not a blanket license for article text. Preserve attribution,
raw metadata, source notices and per-row locators. This release asserts no new
rights to underlying content.

- [Publication derivation](manifests/publication.json)
- [Release checksums](release.json) and [validation](validation.json)
- [Previous root metadata](manifests/history/before-infini-news/)
- [INFINI-NEWS exclusion and original evidence](packages/infini_news/manifests/derivation.json)

## Existing sources and Norwegian harmonization

The following existing-source documentation is retained. Counts here refer to
the pre-INFINI-NEWS, three-source component; current combined totals are above.


### Three-source component: MAC, Exorde and Bluesky

130 configurations containing 23,076,498 physical rows.

| Source | Language/platform views | Train rows | Validation rows | Physical rows |
|---|---:|---:|---:|---:|
| MAC | 32 | 5,824,434 | 648,080 | 6,472,514 |
| Exorde | 77 | 10,602,383 | 1,178,034 | 11,780,417 |
| Bluesky | 18 | 4,341,217 | 482,350 | 4,823,567 |

Each source has an aggregate: `mac_authorship`, `exorde_authorship`, and
`bluesky_authorship`. Individual views are `mac_authorship__<language>`,
`exorde_authorship__<language>__<platform>`, and `bluesky_authorship__<language>`.
Each aggregate references exactly the same physical shards as its individual views.
Count physical rows once; concatenating an aggregate and its components duplicates rows.
Exact membership and split counts: [configuration manifest](manifests/configurations.json).

```python
from datasets import load_dataset
repo = "peterkirby/mymirmdatasets"
mac = load_dataset(repo, "mac_authorship", split="train", streaming=True)
mac_en = load_dataset(repo, "mac_authorship__en", split="validation", streaming=True)
exorde = load_dataset(repo, "exorde_authorship", split="train", streaming=True)
english_x = load_dataset(repo, "exorde_authorship__en__x.com", split="train", streaming=True)
bluesky = load_dataset(repo, "bluesky_authorship", split="train", streaming=True)
bluesky_en = load_dataset(repo, "bluesky_authorship__en", split="validation", streaming=True)
```

## Processing and compatibility

MAC now uses the validated language release: at least 1,500 eligible
wiki-scoped accounts with two distinct texts before sampling/splitting, 2–100 texts
per account-language, a 500,000-text language cap, and the preserved seed-42
account-grouped splits. The aggregate retains its previous name but covers the
32 retained languages, rather than the previous 59. The 27 excluded languages
account for 162,222 removed rows.
Retained text, metadata, numeric labels and split assignments are preserved.
The verified Bashkir correction and all exclusion accounting remain in the MAC package.

Exorde's documents, authors and splits are unchanged; its Norwegian labels and
configuration names are harmonized as described below.
Bluesky's 18 language views and complete processing package are unchanged; the new
aggregate combines them. Bluesky retains its 1,500-eligible-account threshold,
2–100 posts per account-language, 500,000-row language cap, 50-character minimum,
recorded outer trimming, and seed-42 account-grouped splits. Explicit reposts are
excluded; quotations and replies remain. Cross-source overlap checks remain skipped.

Shared training columns are `text`, `primary_id_int`, `secondary_category_int`,
`source_record_id`, `language`, `split_group_id`, and `text_length_chars`.
Use `(source, primary_id_int)` when combining sources. Labels may have gaps.
Aggregate author counts use distinct accounts across languages. Wiki-scoped
accounts and platform accounts do not establish real-world person identity.
MAC languages describe source wikis, Exorde labels are upstream machine predictions,
and Bluesky labels are normalized user-selected tags; no new language detection occurs.
Within-source split separation does not establish separation across sources or wikis.

## Source records and attribution

Source packages are immutable processing outputs. Their cards describe those outputs;
the repository root adds the MAC and Bluesky aggregate views.

- [MAC processing card, citation and attribution](packages/mac/README.md)
- [MAC language eligibility and exclusions](packages/mac/manifests/language_eligibility.json)
- [Exorde processing card and limitations](packages/exorde/README.md)
- [Bluesky processing card and limitations](packages/bluesky/README.md)
- [Update provenance](manifests/hub-update.json)
- [Earlier repository metadata](manifests/history/before-aggregate-update/INDEX.md)
- [Validation report](validation.json)

Preserve source URL attribution, per-row provenance, mapping and sampler manifests.
Licensing is source-dependent; see [LICENSE.md](LICENSE.md). MAC retains its
documented Wikipedia CC BY-SA 4.0 basis and archive uncertainty. Exorde retains its
publisher-declared MIT notice and third-party content limitations. The Bluesky
Zenodo source declares no explicit dataset license; this release asserts no new
license to the underlying posts. No complete bot, original-writing, quotation,
or human-versus-AI labels are claimed.

## Norwegian label harmonization

Exorde's selected generic Norwegian (`no`) documents are grouped under `nb`
(Norwegian Bokmål) at the user's request, to harmonize the Norwegian training
category with Bluesky and INFINI-NEWS. This assumes likely Bokmål; it is **not**
verified Bokmål classification and does not rule out Nynorsk or dialectal content.
No new language detector was run. Original `source_language_label` values and
`source_metadata_json` are unchanged. Relabeled rows have an explicit
`language_audit_status` documenting the assumption.

The three `exorde_authorship__no__<platform>` configurations are now named
`exorde_authorship__nb__<platform>`. Texts, source record IDs, numeric author IDs,
split assignments, row positions, and sampling choices are unchanged. Original
selection/ranking hashes still describe the original `no` selection buckets;
the transformation occurs after selection. The original upstream occurrence and
platform-eligibility audits, producer pins, and earlier processing receipts remain
frozen under their original labels. Per-configuration provenance distinguishes
the original occurrence filter from the harmonized selection filter.

See `manifests/norwegian-relabel.json` for counts and derivation, and
`validation.json` for the new checks. The relabel was prepared locally and is included in this Hub publication.
