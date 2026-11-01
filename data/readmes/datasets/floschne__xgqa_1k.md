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
    struct:
    - name: bytes
      dtype: binary
    - name: path
      dtype: 'null'
  splits:
  - name: bn
    num_bytes: 51624194
    num_examples: 1000
  - name: de
    num_bytes: 51582232
    num_examples: 1000
  - name: en
    num_bytes: 51579211
    num_examples: 1000
  - name: id
    num_bytes: 51590256
    num_examples: 1000
  - name: ko
    num_bytes: 51587731
    num_examples: 1000
  - name: pt
    num_bytes: 51579268
    num_examples: 1000
  - name: ru
    num_bytes: 51602287
    num_examples: 1000
  - name: zh
    num_bytes: 51572077
    num_examples: 1000
  download_size: 412467532
  dataset_size: 412717256
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
pretty_name: xGQA
size_categories:
- 1K<n<10K
---

# xGQA 1K

### This is a 1K subset of the `few_shot-test` split of the xGQA dataset

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

This subset was sampled so that all languages contain the same images and questions based on the `imageId` and `semanticStr` in the original dataset. In other words, this subset is still parallel.

### How to read the image
Due to a [bug](https://github.com/huggingface/datasets/issues/4796), the images cannot be stored as PIL.Image.Images directly but need to be converted to dataset.Images-. Hence, to load them, this additional step is required:

```python
from datasets import Image, load_dataset

ds = load_dataset("floschne/xgqa_1k", split="en")
ds.map(
    lambda sample: {
        "image_t": [Image().decode_example(img) for img in sample["image"]],
    },
    remove_columns=["image"],
).rename_columns({"image_t": "image"})
```