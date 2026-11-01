---
annotations_creators:
- crowdsourced
language_creators:
- crowdsourced
- found
- machine-generated
license:
- other
multilinguality:
- multilingual
size_categories:
- 10K<n<100K
task_ids:
- text-scoring
- semantic-similarity-scoring
pretty_name: rendered sts17
language:
  - ar
  - de
  - en
  - es
  - fr
  - it
  - nl
  - ko
  - tr
configs:
- config_name: default
  data_files:
  - path: test/*.parquet
    split: test
- config_name: ar-ar
  data_files:
  - path: test/ar-ar.parquet
    split: test
- config_name: en-ar
  data_files:
  - path: test/en-ar.parquet
    split: test
- config_name: en-de
  data_files:
  - path: test/en-de.parquet
    split: test
- config_name: en-en
  data_files:
  - path: test/en-en.parquet
    split: test
- config_name: en-tr
  data_files:
  - path: test/en-tr.parquet
    split: test
- config_name: es-en
  data_files:
  - path: test/es-en.parquet
    split: test
- config_name: es-es
  data_files:
  - path: test/es-es.parquet
    split: test
- config_name: fr-en
  data_files:
  - path: test/fr-en.parquet
    split: test
- config_name: it-en
  data_files:
  - path: test/it-en.parquet
    split: test
- config_name: ko-ko
  data_files:
  - path: test/ko-ko.parquet
    split: test
- config_name: nl-en
  data_files:
  - path: test/nl-en.parquet
    split: test
---

### Dataset Summary

This dataset is rendered to images from STS-17. We envision the need to assess vision encoders' abilities to understand texts. A natural way will be assessing them with the STS protocols, with texts rendered into images.

**Examples of Use**

Load Arabic to Arabic dataset:
```python
from datasets import load_dataset
dataset = load_dataset("Pixel-Linguist/rendered-sts17", name="ar-ar", split="test")
```


Load French to English dataset:
```python
from datasets import load_dataset
dataset = load_dataset("Pixel-Linguist/rendered-sts17", name="fr-en", split="test")
```

### Languages

ar-ar, en-ar, en-de, en-en, en-tr, es-en, es-es, fr-en, it-en, ko-ko, nl-en

### Citation Information

```
@article{xiao2024pixel,
  title={Pixel Sentence Representation Learning},
  author={Xiao, Chenghao and Huang, Zhuoxu and Chen, Danlu and Hudson, G Thomas and Li, Yizhi and Duan, Haoran and Lin, Chenghua and Fu, Jie and Han, Jungong and Moubayed, Noura Al},
  journal={arXiv preprint arXiv:2402.08183},
  year={2024}
}
```