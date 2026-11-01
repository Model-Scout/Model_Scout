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
- 100K<n<1M
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
    num_bytes: 185670604
    num_examples: 3600
  - name: bn
    num_bytes: 185730427
    num_examples: 3600
  - name: cs
    num_bytes: 184905314
    num_examples: 3600
  - name: da
    num_bytes: 185047565
    num_examples: 3600
  - name: de
    num_bytes: 185996037
    num_examples: 3600
  - name: el
    num_bytes: 186027150
    num_examples: 3600
  - name: en
    num_bytes: 185038121
    num_examples: 3600
  - name: es
    num_bytes: 185452307
    num_examples: 3600
  - name: fa
    num_bytes: 186286424
    num_examples: 3600
  - name: fi
    num_bytes: 185411321
    num_examples: 3600
  - name: fil
    num_bytes: 185396220
    num_examples: 3600
  - name: fr
    num_bytes: 185817550
    num_examples: 3600
  - name: hi
    num_bytes: 187963777
    num_examples: 3600
  - name: hr
    num_bytes: 185253968
    num_examples: 3600
  - name: hu
    num_bytes: 185433251
    num_examples: 3600
  - name: id
    num_bytes: 185952788
    num_examples: 3600
  - name: it
    num_bytes: 185801693
    num_examples: 3600
  - name: he
    num_bytes: 186452829
    num_examples: 3600
  - name: ja
    num_bytes: 185834016
    num_examples: 3600
  - name: ko
    num_bytes: 185425177
    num_examples: 3600
  - name: mi
    num_bytes: 184718749
    num_examples: 3600
  - name: nl
    num_bytes: 185079232
    num_examples: 3600
  - name: 'no'
    num_bytes: 185164475
    num_examples: 3600
  - name: pl
    num_bytes: 185266269
    num_examples: 3600
  - name: pt
    num_bytes: 185327584
    num_examples: 3600
  - name: quz
    num_bytes: 184801840
    num_examples: 3600
  - name: ro
    num_bytes: 185956147
    num_examples: 3600
  - name: ru
    num_bytes: 186613648
    num_examples: 3600
  - name: sv
    num_bytes: 185028406
    num_examples: 3600
  - name: sw
    num_bytes: 185286235
    num_examples: 3600
  - name: te
    num_bytes: 186748783
    num_examples: 3600
  - name: th
    num_bytes: 187202604
    num_examples: 3600
  - name: tr
    num_bytes: 185472416
    num_examples: 3600
  - name: uk
    num_bytes: 186592720
    num_examples: 3600
  - name: vi
    num_bytes: 186292565
    num_examples: 3600
  - name: zh
    num_bytes: 185623745
    num_examples: 3600
  download_size: 6655898356
  dataset_size: 6686071957
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

# XM3600 - Crossmodal-3600

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

It also includes the image features as PIL Image and has a uniform and joined structure.

### How to read the image
Due to a [bug](https://github.com/huggingface/datasets/issues/4796), the images cannot be stored as PIL.Image.Images directly but need to be converted to dataset.Images-. Hence, to load them, this additional step is required:

```python
from datasets import Image, load_dataset

ds = load_dataset("floschne/xm3600", split="en")
ds.map(
    lambda sample: {
        "image_t": [Image().decode_example(img) for img in sample["image"]],
    },
    remove_columns=["image"],
).rename_columns({"image_t": "image"})

```