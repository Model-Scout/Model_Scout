---
language:
- pt
- en
- es
- fr
- de
- it
- vi
- ru
- uk
- ar
- zh
- ja
- ko
- hi
license: odc-by
pretty_name: Fineweb-2 Trimming 15 Languages
size_categories:
- 10M<n<100M
tags:
- text
- multilingual
- pretraining
- fineweb
- fineweb-2
library_name: datasets
dataset_info:
- config_name: arb
  features:
  - name: text
    dtype: string
  - name: url
    dtype: string
  splits:
  - name: train
    num_bytes: 1148718572
    num_examples: 200000
  download_size: 555939964
  dataset_size: 1148718572
- config_name: deu
  features:
  - name: text
    dtype: string
  - name: url
    dtype: string
  splits:
  - name: train
    num_bytes: 618633657
    num_examples: 200000
  download_size: 383309282
  dataset_size: 618633657
- config_name: eng
  features:
  - name: text
    dtype: string
  - name: url
    dtype: string
  splits:
  - name: train
    num_bytes: 599103874
    num_examples: 200000
  download_size: 369197670
  dataset_size: 599103874
- config_name: fra
  features:
  - name: text
    dtype: string
  - name: url
    dtype: string
  splits:
  - name: train
    num_bytes: 729519388
    num_examples: 200000
  download_size: 437057843
  dataset_size: 729519388
- config_name: hin
  features:
  - name: text
    dtype: string
  - name: url
    dtype: string
  splits:
  - name: train
    num_bytes: 1352753432
    num_examples: 200000
  download_size: 511334256
  dataset_size: 1352753432
- config_name: ind
  features:
  - name: text
    dtype: string
  - name: url
    dtype: string
  splits:
  - name: train
    num_bytes: 810555093
    num_examples: 200000
  download_size: 449423742
  dataset_size: 810555093
- config_name: ita
  features:
  - name: text
    dtype: string
  - name: url
    dtype: string
  splits:
  - name: train
    num_bytes: 631840650
    num_examples: 200000
  download_size: 397093192
  dataset_size: 631840650
- config_name: jpn
  features:
  - name: text
    dtype: string
  - name: url
    dtype: string
  splits:
  - name: train
    num_bytes: 727745008
    num_examples: 200000
  download_size: 414396831
  dataset_size: 727745008
- config_name: kor
  features:
  - name: text
    dtype: string
  - name: url
    dtype: string
  splits:
  - name: train
    num_bytes: 794017643
    num_examples: 200000
  download_size: 462234551
  dataset_size: 794017643
- config_name: por
  features:
  - name: text
    dtype: string
  - name: url
    dtype: string
  splits:
  - name: train
    num_bytes: 661034497
    num_examples: 200000
  download_size: 405883894
  dataset_size: 661034497
- config_name: rus
  features:
  - name: text
    dtype: string
  - name: url
    dtype: string
  splits:
  - name: train
    num_bytes: 1407487265
    num_examples: 200000
  download_size: 692203718
  dataset_size: 1407487265
- config_name: spa
  features:
  - name: text
    dtype: string
  - name: url
    dtype: string
  splits:
  - name: train
    num_bytes: 829717303
    num_examples: 200000
  download_size: 495475961
  dataset_size: 829717303
- config_name: ukr
  features:
  - name: text
    dtype: string
  - name: url
    dtype: string
  splits:
  - name: train
    num_bytes: 1262271984
    num_examples: 200000
  download_size: 622440503
  dataset_size: 1262271984
- config_name: vie
  features:
  - name: text
    dtype: string
  - name: url
    dtype: string
  splits:
  - name: train
    num_bytes: 1124668083
    num_examples: 200000
  download_size: 576166508
  dataset_size: 1124668083
- config_name: zho
  features:
  - name: text
    dtype: string
  - name: url
    dtype: string
  splits:
  - name: train
    num_bytes: 763793301
    num_examples: 200000
  download_size: 543489314
  dataset_size: 763793301
configs:
- config_name: arb
  data_files:
  - split: train
    path: arb/train-*
- config_name: deu
  data_files:
  - split: train
    path: deu/train-*
- config_name: eng
  data_files:
  - split: train
    path: eng/train-*
- config_name: fra
  data_files:
  - split: train
    path: fra/train-*
- config_name: hin
  data_files:
  - split: train
    path: hin/train-*
- config_name: ind
  data_files:
  - split: train
    path: ind/train-*
- config_name: ita
  data_files:
  - split: train
    path: ita/train-*
- config_name: jpn
  data_files:
  - split: train
    path: jpn/train-*
- config_name: kor
  data_files:
  - split: train
    path: kor/train-*
- config_name: por
  data_files:
  - split: train
    path: por/train-*
- config_name: rus
  data_files:
  - split: train
    path: rus/train-*
- config_name: spa
  data_files:
  - split: train
    path: spa/train-*
- config_name: ukr
  data_files:
  - split: train
    path: ukr/train-*
- config_name: vie
  data_files:
  - split: train
    path: vie/train-*
- config_name: zho
  data_files:
  - split: train
    path: zho/train-*
task_categories:
- text-generation
---

# Fineweb-2 Trimming 15 Languages

<a href='https://ko-fi.com/R6R0PGKEJ' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi6.png?v=6' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>

A filtered subset of [`lbourdois/fineweb-2-trimming`](https://huggingface.co/datasets/lbourdois/fineweb-2-trimming) containing 15 selected languages.

## Languages

| ISO 639-3 | Language |
|---|---|
| `por` | Portuguese |
| `eng` | English |
| `spa` | Spanish |
| `fra` | French |
| `deu` | German |
| `ita` | Italian |
| `vie` | Vietnamese |
| `rus` | Russian |
| `ukr` | Ukrainian |
| `arb` | Arabic |
| `zho` | Chinese |
| `jpn` | Japanese |
| `kor` | Korean |
| `hin` | Hindi |
| `ind` | Indonesian |

## Usage

Each language is available as a separate dataset configuration:

```python
from datasets import load_dataset

dataset = load_dataset(
    "olob0/fineweb-2-15langs",
    "por",
    split="train"
)
```

Replace `por` with any of the available language codes.

## Source

This dataset is a filtered subset of:

- [`lbourdois/fineweb-2-trimming`](https://huggingface.co/datasets/lbourdois/fineweb-2-trimming)
- [FineWeb-2](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2)
- Common Crawl

The original [`lbourdois/fineweb-2-trimming`](https://huggingface.co/datasets/lbourdois/fineweb-2-trimming) dataset keeps a limited number of texts from 124 languages specifically for model trimming experiments.

This repository only selects 15 of those existing language configurations. No textual transformation or additional filtering is performed.

## License

This dataset is derived from [FineWeb-2](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2) and its derivatives.

The dataset is distributed under the Open Data Commons Attribution License (ODC-By) v1.0.

Users should also review the terms and conditions applicable to the upstream data sources, including Common Crawl.

## Attribution

If you use this dataset, please attribute the upstream datasets:

- [FineWeb-2](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2)
- [`lbourdois/fineweb-2-trimming`](https://huggingface.co/datasets/lbourdois/fineweb-2-trimming)

See the original dataset cards for the complete attribution and licensing information.

## Citation

FineWeb-2:

> Penedo et al. FineWeb2: A Large Multilingual Web Dataset for LLM Pre-Training. 2025.

See the original FineWeb-2 dataset card for the complete citation.