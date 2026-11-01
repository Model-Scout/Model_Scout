---
license: odc-by
task_categories:
- text-generation
- question-answering
language:
- en
- es
- fr
- de
- it
- pt
- ru
- zh
- ja
- ko
- ar
- hi
- th
- vi
- tr
- pl
- nl
- sv
- da
- no
- fi
- cs
- hu
- ro
- bg
- hr
- sk
- sl
- et
- lv
- lt
- el
- he
- fa
- ur
- bn
- ta
- te
- ml
- kn
- gu
- pa
- or
- as
- ne
- si
- my
- km
- lo
- ka
- am
- sw
- zu
- af
- sq
- eu
- cy
- ga
- is
- mt
- mk
- sr
- bs
- uk
- be
- kk
- ky
- uz
- tg
- mn
- az
- hy
- ka
- et
- lv
- lt
- eo
- id
- ms
- tl
- ceb
- war
- jv
- su
- ban
- bug
- mad
- min
- ace
- bjn
- bpy
- mni
- new
- sat
- scn
- vec
- lmo
- lij
- nap
- pms
- rup
- sc
- co
- frp
- gsw
- bar
- cim
- ksh
- pfl
- pdc
- vmf
- swg
- gsw
- bar
- cim
- ksh
- pfl
- pdc
- vmf
- swg
size_categories:
- 1M<n<10M
---

# WildChat Filtered Dataset

This is a filtered version of the [WildChat-4.8M](https://huggingface.co/datasets/allenai/WildChat-4.8M) dataset.

## Dataset Description

This dataset contains **3,199,860 conversations** between human users and ChatGPT, filtered to keep only the essential conversation structure.

## Data Structure

Each conversation contains only:
- `conversations`: A list of message objects with:
  - `role`: Either "user" or "assistant"
  - `content`: The text content of the message

All other metadata (timestamps, moderation results, IP addresses, etc.) has been removed for privacy and simplicity.

## Original Dataset

This dataset is derived from [WildChat-4.8M](https://huggingface.co/datasets/allenai/WildChat-4.8M) by AllenAI.

## Citation

If you use this dataset, please cite the original WildChat paper:

```bibtex
@inproceedings{
  zhao2024wildchat,
  title={WildChat: 1M Chat{GPT} Interaction Logs in the Wild},
  author={Wenting Zhao and Xiang Ren and Jack Hessel and Claire Cardie and Yejin Choi and Yuntian Deng},
  booktitle={The Twelfth International Conference on Learning Representations},
  year={2024},
  url={https://openreview.net/forum?id=Bl8u7ZRlbM}
}
```
