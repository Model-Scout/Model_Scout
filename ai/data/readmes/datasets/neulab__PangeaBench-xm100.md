---
language:
- ar
- bn
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
- hi
- hr
- hu
- id
- it
- he
- ja
- ko
- mi
- nl
- 'no'
- pl
- pt
- quz
- ro
- ru
- sv
- sw
- te
- th
- tr
- uk
- vi
- zh
license: cc-by-4.0
size_categories:
- 1K<n<10K
task_categories:
- image-to-text
pretty_name: xm100
dataset_info:
  features:
  - name: image_id
    dtype: string
  - name: image_locale
    dtype: string
  - name: caption
    dtype: string
  - name: image
    dtype: image
  splits:
  - name: ar
    num_examples: 100
  - name: bn
    num_examples: 100
  - name: cs
    num_examples: 100
  - name: da
    num_examples: 100
  - name: de
    num_examples: 100
  - name: el
    num_examples: 100
  - name: en
    num_examples: 100
  - name: es
    num_examples: 100
  - name: fa
    num_examples: 100
  - name: fi
    num_examples: 100
  - name: fil
    num_examples: 100
  - name: fr
    num_examples: 100
  - name: hi
    num_examples: 100
  - name: hr
    num_examples: 100
  - name: hu
    num_examples: 100
  - name: id
    num_examples: 100
  - name: it
    num_examples: 100
  - name: he
    num_examples: 100
  - name: ja
    num_examples: 100
  - name: ko
    num_examples: 100
  - name: mi
    num_examples: 100
  - name: nl
    num_examples: 100
  - name: 'no'
    num_examples: 100
  - name: pl
    num_examples: 100
  - name: pt
    num_examples: 100
  - name: quz
    num_examples: 100
  - name: ro
    num_examples: 100
  - name: ru
    num_examples: 100
  - name: sv
    num_examples: 100
  - name: sw
    num_examples: 100
  - name: te
    num_examples: 100
  - name: th
    num_examples: 100
  - name: tr
    num_examples: 100
  - name: uk
    num_examples: 100
  - name: vi
    num_examples: 100
  - name: zh
    num_examples: 100
configs:
- config_name: default
  data_files:
  - split: ar
    path: data/ar-*
  - split: bn
    path: data/bn-*
  - split: cs
    path: data/cs-*
  - split: da
    path: data/da-*
  - split: de
    path: data/de-*
  - split: el
    path: data/el-*
  - split: en
    path: data/en-*
  - split: es
    path: data/es-*
  - split: fa
    path: data/fa-*
  - split: fi
    path: data/fi-*
  - split: fil
    path: data/fil-*
  - split: fr
    path: data/fr-*
  - split: hi
    path: data/hi-*
  - split: hr
    path: data/hr-*
  - split: hu
    path: data/hu-*
  - split: id
    path: data/id-*
  - split: it
    path: data/it-*
  - split: he
    path: data/he-*
  - split: ja
    path: data/ja-*
  - split: ko
    path: data/ko-*
  - split: mi
    path: data/mi-*
  - split: nl
    path: data/nl-*
  - split: 'no'
    path: data/no-*
  - split: pl
    path: data/pl-*
  - split: pt
    path: data/pt-*
  - split: quz
    path: data/quz-*
  - split: ro
    path: data/ro-*
  - split: ru
    path: data/ru-*
  - split: sv
    path: data/sv-*
  - split: sw
    path: data/sw-*
  - split: te
    path: data/te-*
  - split: th
    path: data/th-*
  - split: tr
    path: data/tr-*
  - split: uk
    path: data/uk-*
  - split: vi
    path: data/vi-*
  - split: zh
    path: data/zh-*
---

# XM100

### This is a copy from https://google.github.io/crossmodal-3600/

If you use this dataset, please cite the original authors:
```bibtex
@inproceedings{ThapliyalCrossmodal2022,
  author = {Ashish Thapliyal and Jordi Pont-Tuset and Xi Chen and Radu Soricut},
  title = {{Crossmodal-3600: A Massively Multilingual Multimodal Evaluation Dataset}},
  booktitle = {EMNLP},
  year = {2022}
}
```