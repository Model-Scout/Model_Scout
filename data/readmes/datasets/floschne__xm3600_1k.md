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
- 10K<n<100K
task_categories:
- image-to-text
pretty_name: Crossmodal-3600
dataset_info:
  features:
  - name: image_id
    dtype: string
  - name: image_locale
    dtype: string
  - name: captions
    sequence: string
  - name: captions_tokenized
    sequence: string
  - name: captions_tokenized_lowercase
    sequence: string
  - name: image
    struct:
    - name: bytes
      dtype: binary
    - name: path
      dtype: 'null'
  splits:
  - name: ar
    num_bytes: 52204626
    num_examples: 1000
  - name: bn
    num_bytes: 52218203
    num_examples: 1000
  - name: cs
    num_bytes: 51989744
    num_examples: 1000
  - name: da
    num_bytes: 52031034
    num_examples: 1000
  - name: de
    num_bytes: 52295275
    num_examples: 1000
  - name: el
    num_bytes: 52303830
    num_examples: 1000
  - name: en
    num_bytes: 52027805
    num_examples: 1000
  - name: es
    num_bytes: 52143094
    num_examples: 1000
  - name: fa
    num_bytes: 52374183
    num_examples: 1000
  - name: fi
    num_bytes: 52137661
    num_examples: 1000
  - name: fil
    num_bytes: 52126913
    num_examples: 1000
  - name: fr
    num_bytes: 52247726
    num_examples: 1000
  - name: hi
    num_bytes: 52855563
    num_examples: 1000
  - name: hr
    num_bytes: 52083585
    num_examples: 1000
  - name: hu
    num_bytes: 52130864
    num_examples: 1000
  - name: id
    num_bytes: 52288107
    num_examples: 1000
  - name: it
    num_bytes: 52236611
    num_examples: 1000
  - name: he
    num_bytes: 52425752
    num_examples: 1000
  - name: ja
    num_bytes: 52248087
    num_examples: 1000
  - name: ko
    num_bytes: 52135688
    num_examples: 1000
  - name: mi
    num_bytes: 51935948
    num_examples: 1000
  - name: nl
    num_bytes: 52042104
    num_examples: 1000
  - name: 'no'
    num_bytes: 52063671
    num_examples: 1000
  - name: pl
    num_bytes: 52094425
    num_examples: 1000
  - name: pt
    num_bytes: 52108046
    num_examples: 1000
  - name: quz
    num_bytes: 51961514
    num_examples: 1000
  - name: ro
    num_bytes: 52288685
    num_examples: 1000
  - name: ru
    num_bytes: 52464054
    num_examples: 1000
  - name: sv
    num_bytes: 52026516
    num_examples: 1000
  - name: sw
    num_bytes: 52107086
    num_examples: 1000
  - name: te
    num_bytes: 52504009
    num_examples: 1000
  - name: th
    num_bytes: 52627358
    num_examples: 1000
  - name: tr
    num_bytes: 52148151
    num_examples: 1000
  - name: uk
    num_bytes: 52461326
    num_examples: 1000
  - name: vi
    num_bytes: 52381378
    num_examples: 1000
  - name: zh
    num_bytes: 52194115
    num_examples: 1000
  download_size: 1871753198
  dataset_size: 1879912737
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

# XM3600 - Crossmodal-3600 - 1K Split

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
## This is a 1K split of XM3600!
For this, we randomly selected a subset of 1000 `image_id`s. Each of the 36 languages in XM3600 contains captions for this subset.

It also includes the image features as PIL Image and has a uniform and joined structure.

### How to read the image
Due to a [bug](https://github.com/huggingface/datasets/issues/4796), the images cannot be stored as PIL.Image.Images directly but need to be converted to dataset.Images-. Hence, to load them, this additional step is required:

```python
from datasets import Image, load_dataset

ds = load_dataset("floschne/xm3600_1k", split="en")
ds.map(
    lambda sample: {
        "image_t": [Image().decode_example(img) for img in sample["image"]],
    },
    remove_columns=["image"],
).rename_columns({"image_t": "image"})

```