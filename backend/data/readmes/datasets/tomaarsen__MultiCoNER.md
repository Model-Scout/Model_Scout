---
license: cc-by-4.0
task_categories:
- token-classification
language:
- bn
- de
- en
- es
- fa
- hi
- ko
- nl
- ru
- tr
- zh
- multilingual
tags:
- multiconer
- ner
- multilingual
- named entity recognition
size_categories:
- 100K<n<1M
dataset_info:
- config_name: bn
  features:
  - name: id
    dtype: int32
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-LOC
          '4': I-LOC
          '5': B-CORP
          '6': I-CORP
          '7': B-GRP
          '8': I-GRP
          '9': B-PROD
          '10': I-PROD
          '11': B-CW
          '12': I-CW
  splits:
  - name: train
    num_bytes: 5616369
    num_examples: 15300
  - name: validation
    num_bytes: 301806
    num_examples: 800
  - name: test
    num_bytes: 21668288
    num_examples: 133119
  download_size: 31446032
  dataset_size: 27586463
- config_name: de
  features:
  - name: id
    dtype: int32
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-LOC
          '4': I-LOC
          '5': B-CORP
          '6': I-CORP
          '7': B-GRP
          '8': I-GRP
          '9': B-PROD
          '10': I-PROD
          '11': B-CW
          '12': I-CW
  splits:
  - name: train
    num_bytes: 4056698
    num_examples: 15300
  - name: validation
    num_bytes: 214572
    num_examples: 800
  - name: test
    num_bytes: 37113304
    num_examples: 217824
  download_size: 44089736
  dataset_size: 41384574
- config_name: en
  features:
  - name: id
    dtype: int32
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-LOC
          '4': I-LOC
          '5': B-CORP
          '6': I-CORP
          '7': B-GRP
          '8': I-GRP
          '9': B-PROD
          '10': I-PROD
          '11': B-CW
          '12': I-CW
  splits:
  - name: train
    num_bytes: 4330080
    num_examples: 15300
  - name: validation
    num_bytes: 229689
    num_examples: 800
  - name: test
    num_bytes: 38728401
    num_examples: 217818
  download_size: 44709663
  dataset_size: 43288170
- config_name: es
  features:
  - name: id
    dtype: int32
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-LOC
          '4': I-LOC
          '5': B-CORP
          '6': I-CORP
          '7': B-GRP
          '8': I-GRP
          '9': B-PROD
          '10': I-PROD
          '11': B-CW
          '12': I-CW
  splits:
  - name: train
    num_bytes: 4576557
    num_examples: 15300
  - name: validation
    num_bytes: 238872
    num_examples: 800
  - name: test
    num_bytes: 41457435
    num_examples: 217887
  download_size: 46861727
  dataset_size: 46272864
- config_name: fa
  features:
  - name: id
    dtype: int32
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-LOC
          '4': I-LOC
          '5': B-CORP
          '6': I-CORP
          '7': B-GRP
          '8': I-GRP
          '9': B-PROD
          '10': I-PROD
          '11': B-CW
          '12': I-CW
  splits:
  - name: train
    num_bytes: 5550551
    num_examples: 15300
  - name: validation
    num_bytes: 294184
    num_examples: 800
  - name: test
    num_bytes: 30301688
    num_examples: 165702
  download_size: 38042406
  dataset_size: 36146423
- config_name: hi
  features:
  - name: id
    dtype: int32
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-LOC
          '4': I-LOC
          '5': B-CORP
          '6': I-CORP
          '7': B-GRP
          '8': I-GRP
          '9': B-PROD
          '10': I-PROD
          '11': B-CW
          '12': I-CW
  splits:
  - name: train
    num_bytes: 6189324
    num_examples: 15300
  - name: validation
    num_bytes: 321246
    num_examples: 800
  - name: test
    num_bytes: 25771882
    num_examples: 141565
  download_size: 35165171
  dataset_size: 32282452
- config_name: ko
  features:
  - name: id
    dtype: int32
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-LOC
          '4': I-LOC
          '5': B-CORP
          '6': I-CORP
          '7': B-GRP
          '8': I-GRP
          '9': B-PROD
          '10': I-PROD
          '11': B-CW
          '12': I-CW
  splits:
  - name: train
    num_bytes: 4439652
    num_examples: 15300
  - name: validation
    num_bytes: 233963
    num_examples: 800
  - name: test
    num_bytes: 27529239
    num_examples: 178249
  download_size: 35281170
  dataset_size: 32202854
- config_name: mix
  features:
  - name: id
    dtype: int32
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-LOC
          '4': I-LOC
          '5': B-CORP
          '6': I-CORP
          '7': B-GRP
          '8': I-GRP
          '9': B-PROD
          '10': I-PROD
          '11': B-CW
          '12': I-CW
  splits:
  - name: train
    num_bytes: 307844
    num_examples: 1500
  - name: validation
    num_bytes: 100909
    num_examples: 500
  - name: test
    num_bytes: 20218549
    num_examples: 100000
  download_size: 21802985
  dataset_size: 20627302
- config_name: multi
  features:
  - name: id
    dtype: int32
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-LOC
          '4': I-LOC
          '5': B-CORP
          '6': I-CORP
          '7': B-GRP
          '8': I-GRP
          '9': B-PROD
          '10': I-PROD
          '11': B-CW
          '12': I-CW
  splits:
  - name: train
    num_bytes: 54119956
    num_examples: 168300
  - name: validation
    num_bytes: 2846552
    num_examples: 8800
  - name: test
    num_bytes: 91509480
    num_examples: 471911
  download_size: 148733494
  dataset_size: 148475988
- config_name: nl
  features:
  - name: id
    dtype: int32
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-LOC
          '4': I-LOC
          '5': B-CORP
          '6': I-CORP
          '7': B-GRP
          '8': I-GRP
          '9': B-PROD
          '10': I-PROD
          '11': B-CW
          '12': I-CW
  splits:
  - name: train
    num_bytes: 4070487
    num_examples: 15300
  - name: validation
    num_bytes: 209337
    num_examples: 800
  - name: test
    num_bytes: 37128925
    num_examples: 217337
  download_size: 43263864
  dataset_size: 41408749
- config_name: ru
  features:
  - name: id
    dtype: int32
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-LOC
          '4': I-LOC
          '5': B-CORP
          '6': I-CORP
          '7': B-GRP
          '8': I-GRP
          '9': B-PROD
          '10': I-PROD
          '11': B-CW
          '12': I-CW
  splits:
  - name: train
    num_bytes: 5313989
    num_examples: 15300
  - name: validation
    num_bytes: 279470
    num_examples: 800
  - name: test
    num_bytes: 47458726
    num_examples: 217501
  download_size: 54587257
  dataset_size: 53052185
- config_name: tr
  features:
  - name: id
    dtype: int32
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-LOC
          '4': I-LOC
          '5': B-CORP
          '6': I-CORP
          '7': B-GRP
          '8': I-GRP
          '9': B-PROD
          '10': I-PROD
          '11': B-CW
          '12': I-CW
  splits:
  - name: train
    num_bytes: 4076774
    num_examples: 15300
  - name: validation
    num_bytes: 213017
    num_examples: 800
  - name: test
    num_bytes: 14779846
    num_examples: 136935
  download_size: 22825291
  dataset_size: 19069637
- config_name: zh
  features:
  - name: id
    dtype: int32
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-LOC
          '4': I-LOC
          '5': B-CORP
          '6': I-CORP
          '7': B-GRP
          '8': I-GRP
          '9': B-PROD
          '10': I-PROD
          '11': B-CW
          '12': I-CW
  splits:
  - name: train
    num_bytes: 5899475
    num_examples: 15300
  - name: validation
    num_bytes: 310396
    num_examples: 800
  - name: test
    num_bytes: 29349271
    num_examples: 151661
  download_size: 36101525
  dataset_size: 35559142
---

# Multilingual Complex Named Entity Recognition (MultiCoNER) 

## Dataset Summary
MultiCoNER (version 1) is a large multilingual dataset for Named Entity Recognition that covers 3 domains (Wiki sentences, questions, and search queries) across 11 languages, as well as multilingual and code-mixing subsets. This dataset is designed to represent contemporary challenges in NER, including low-context scenarios (short and uncased text), syntactically complex entities like movie titles, and long-tail entity distributions. The 26M token dataset is compiled from public resources using techniques such as heuristic-based sentence sampling, template extraction and slotting, and machine translation. 

See the [AWS Open Data Registry entry for MultiCoNER](https://registry.opendata.aws/multiconer/) for more information.

## Labels
* `PER`: Person, i.e. names of people
* `LOC`: Location, i.e. locations/physical facilities
* `CORP`: Corporation, i.e. corporations/businesses
* `GRP`: Groups, i.e. all other groups
* `PROD`: Product, i.e. consumer products
* `CW`: Creative Work, i.e. movies/songs/book titles

### Dataset Structure
The dataset follows the IOB format of CoNLL. In particular, it uses the following label to ID mapping:
```python

{
    "O": 0,
    "B-PER": 1,
    "I-PER": 2,
    "B-LOC": 3,
    "I-LOC": 4,
    "B-CORP": 5,
    "I-CORP": 6,
    "B-GRP": 7,
    "I-GRP": 8,
    "B-PROD": 9,
    "I-PROD": 10,
    "B-CW": 11,
    "I-CW": 12,
}
```

## Languages
The MultiCoNER dataset consists of the following languages: Bangla, German, English, Spanish, Farsi, Hindi, Korean, Dutch, Russian, Turkish and Chinese.

## Usage
```python
from datasets import load_dataset

dataset = load_dataset('tomaarsen/MultiCoNER', 'multi')
```

## License

CC BY 4.0

## Citation
```
@misc{malmasi2022multiconer,
    title={MultiCoNER: A Large-scale Multilingual dataset for Complex Named Entity Recognition}, 
    author={Shervin Malmasi and Anjie Fang and Besnik Fetahu and Sudipta Kar and Oleg Rokhlenko},
    year={2022},
    eprint={2208.14536},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```