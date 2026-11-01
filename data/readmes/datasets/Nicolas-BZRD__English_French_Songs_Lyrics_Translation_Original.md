---
license: unknown
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: artist_name
    dtype: string
  - name: album_name
    dtype: string
  - name: year
    dtype: int64
  - name: title
    dtype: string
  - name: number
    dtype: int64
  - name: original_version
    dtype: string
  - name: french_version
    dtype: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 250317845
    num_examples: 99289
  download_size: 122323323
  dataset_size: 250317845
task_categories:
- translation
- text-generation
language:
- fr
- en
- es
- it
- de
- ko
- id
- pt
- 'no'
- fi
- sv
- sw
- hr
- so
- ca
- tl
- ja
- nl
- ru
- et
- tr
- ro
- cy
- vi
- af
- hu
- sk
- sl
- cs
- da
- pl
- sq
- el
- he
- zh
- th
- bg
- ar
tags:
- music
- parallel
- parallel data
pretty_name: SYFT
size_categories:
- 10K<n<100K
---

# Original Songs Lyrics with French Translation

### Dataset Summary

Dataset of 99289 songs containing their metadata (author, album, release date, song number), original lyrics and lyrics translated into French.

Details of the number of songs by language of origin can be found in the table below:

| Original language | Number of songs |
|---|:---|
| en | 75786 |
| fr | 18486 |
| es | 1743 |
| it | 803 |
| de | 691 |
| sw | 529 |
| ko | 193 |
| id | 169 |
| pt | 142 |
| no | 122 |
| fi | 113 |
| sv | 70 |
| hr | 53 |
| so | 43 |
| ca | 41 |
| tl | 36 |
| ja | 35 |
| nl | 32 |
| ru | 29 |
| et | 27 |
| tr | 22 |
| ro | 19 |
| cy | 14 |
| vi | 14 |
| af | 13 |
| hu | 10 |
| sk | 10 |
| sl | 10 |
| cs | 7 |
| da | 6 |
| pl | 5 |
| sq | 4 |
| el | 4 |
| he | 3 |
| zh-cn | 2 |
| th | 1 |
| bg | 1 |
| ar | 1 |


## Citation

Our work can be cited as:

```bash
@misc{faysse2024croissantllm,
      title={CroissantLLM: A Truly Bilingual French-English Language Model}, 
      author={Manuel Faysse and Patrick Fernandes and Nuno Guerreiro and António Loison and Duarte Alves and Caio Corro and Nicolas Boizard and João Alves and Ricardo Rei and Pedro Martins and Antoni Bigata Casademunt and François Yvon and André Martins and Gautier Viaud and Céline Hudelot and Pierre Colombo},
      year={2024},
      eprint={2402.00786},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```