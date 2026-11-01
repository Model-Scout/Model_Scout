---
dataset_info:
  features:
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  - name: feature
    dtype: string
  - name: feature_clean
    dtype: string
  splits:
  - name: train
    num_bytes: 978566
    num_examples: 3600
  - name: test
    num_bytes: 106530
    num_examples: 400
  download_size: 574724
  dataset_size: 1085096
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
license: mit
language:
- en
tags:
- datadreamer
- datadreamer-0.20.0
- synthetic
- gpt-4
pretty_name: SynthStel
size_categories:
- 1K<n<10K
---

The SynthSTEL dataset is a synthetically generated (with GPT-4) extension of the [STEL task](https://aclanthology.org/2021.emnlp-main.569/) to 40 style features. This data was also used to train the [StyleDistance embedding model](https://huggingface.co/StyleDistance/styledistance).

---
## Generated with DataDreamer

This synthetic dataset was produced with [DataDreamer 🤖💤](https://datadreamer.dev).

---
#### Funding Acknowledgements

<small> This research is supported in part by the Office of the Director of National Intelligence (ODNI), Intelligence Advanced Research Projects Activity (IARPA), via the HIATUS Program contract #2022-22072200005. The views and conclusions contained herein are those of the authors and should not be interpreted as necessarily representing the official policies, either expressed or implied, of ODNI, IARPA, or the U.S. Government. The U.S. Government is authorized to reproduce and distribute reprints for governmental purposes notwithstanding any copyright annotation therein. </small>