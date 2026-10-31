---
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
dataset_info:
  features:
  - name: data_index_by_user
    dtype: int32
  - name: question
    dtype: string
  - name: passage
    dtype: string
  - name: answer
    dtype: bool
  splits:
  - name: train
    num_bytes: 6533771
    num_examples: 9427
  - name: validation
    num_bytes: 2239144
    num_examples: 3270
  download_size: 5399244
  dataset_size: 8772915
license: cc-by-sa-3.0
---
# Dataset Card for "kor_boolq"

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

# Source Data Citation Information
```
@inproceedings{clark2019boolq,
  title =     {BoolQ: Exploring the Surprising Difficulty of Natural Yes/No Questions},
  author =    {Clark, Christopher and Lee, Kenton and Chang, Ming-Wei, and Kwiatkowski, Tom and Collins, Michael, and Toutanova, Kristina},
  booktitle = {NAACL},
  year =      {2019},
}
```