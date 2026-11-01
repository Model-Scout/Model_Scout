---
dataset_info:
  features:
  - name: source
    dtype: string
  - name: chosen
    dtype: string
  - name: reject
    dtype: string
  - name: directions
    dtype: string
  splits:
  - name: train
    num_bytes: 384750588
    num_examples: 771785
  download_size: 223888195
  dataset_size: 384750588
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- en
- da
- nl
- de
- is
- 'no'
- sc
- af
- ca
- ro
- gl
- it
- pt
- es
- bg
- mk
- sr
- uk
- ru
- id
- ms
- th
- vi
- mg
- fr
- hu
- el
- cs
- pl
- lt
- lv
- ka
- zh
- ja
- ko
- fi
- et
- gu
- hi
- mr
- ne
- ur
- az
- kk
- ky
- tr
- uz
- ar
- he
- fa
license: mit
---

This is the translation preference dataset used by [X-ALMA](https://arxiv.org/pdf/2410.03115).

`source`: the source sentence.

`chosen`: the preferred translation.

`reject`: the dis-preferred translation.

`directions`: the translation direction.

```
@misc{xu2024xalmaplugplay,
      title={X-ALMA: Plug & Play Modules and Adaptive Rejection for Quality Translation at Scale}, 
      author={Haoran Xu and Kenton Murray and Philipp Koehn and Hieu Hoang and Akiko Eriguchi and Huda Khayrallah},
      year={2024},
      eprint={2410.03115},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2410.03115}, 
}
```
