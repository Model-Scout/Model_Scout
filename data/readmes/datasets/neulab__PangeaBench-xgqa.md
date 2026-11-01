---
dataset_info:
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: full_answer
    dtype: string
  - name: image_id
    dtype: string
  - name: image
    dtype: image
  splits:
  - name: bn
    num_bytes: 498517814
    num_examples: 9666
  - name: de
    num_bytes: 498108367
    num_examples: 9666
  - name: en
    num_bytes: 498078827
    num_examples: 9666
  - name: id
    num_bytes: 498180441
    num_examples: 9666
  - name: ko
    num_bytes: 498157980
    num_examples: 9666
  - name: pt
    num_bytes: 498078408
    num_examples: 9666
  - name: ru
    num_bytes: 498298164
    num_examples: 9666
  - name: zh
    num_bytes: 498005624
    num_examples: 9666
  download_size: 2692912777
  dataset_size: 3985425625
configs:
- config_name: default
  data_files:
  - split: bn
    path: data/bn-*
  - split: de
    path: data/de-*
  - split: en
    path: data/en-*
  - split: id
    path: data/id-*
  - split: ko
    path: data/ko-*
  - split: pt
    path: data/pt-*
  - split: ru
    path: data/ru-*
  - split: zh
    path: data/zh-*
license: cc-by-4.0
task_categories:
- visual-question-answering
language:
- bn
- de
- en
- id
- ko
- pt
- ru
- zh
pretty_name: xgqa
size_categories:
- 10K<n<100K
---

# xGQA

### This is a clone of the `few_shot-test` split of the xGQA dataset

Please find the original repository here: https://github.com/adapter-hub/xGQA

If you use this dataset, please cite the original authors:

```bibtex
@inproceedings{pfeiffer-etal-2021-xGQA,
    title={{xGQA: Cross-Lingual Visual Question Answering}},
    author={ Jonas Pfeiffer and Gregor Geigle and Aishwarya Kamath and Jan-Martin O. Steitz and Stefan Roth and Ivan Vuli{\'{c}} and Iryna Gurevych},
    booktitle = "Findings of the Association for Computational Linguistics: ACL 2022",
    month = May,
    year = "2022",  
    url = "https://arxiv.org/pdf/2109.06082.pdf",
    publisher = "Association for Computational Linguistics",
}
```