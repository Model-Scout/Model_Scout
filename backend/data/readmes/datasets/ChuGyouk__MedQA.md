---
configs:
- config_name: ko
  data_files:
  - split: train
    path: medqa_train_trans.jsonl
  - split: test
    path: medqa_test_trans.jsonl
- config_name: en
  data_files:
  - split: train
    path: medqa_edited_train.jsonl
  - split: test
    path: medqa_edited_test.jsonl
license: cc-by-4.0
task_categories:
  - text-generation
language:
  - ko
  - en
tags:
  - medical
---

Original dataset introduced by Jin et al. in [What Disease does this Patient Have? A Large-scale Open Domain Question Answering Dataset from Medical Exams](https://paperswithcode.com/paper/what-disease-does-this-patient-have-a-large)

# En split
Just edited columns. Contents are same.

# Ko split

## Train

The train dataset is translated by "solar-1-mini-translate-enko".

## Test

The test dataset is translated by DeepL Pro.

**reference-free COMET score: 0.7989** *(Unbabel/wmt23-cometkiwi-da-xxl)*

<h4>Citation information:</h4>

    @article{jin2020disease,
      title={What Disease does this Patient Have? A Large-scale Open Domain Question Answering Dataset from Medical Exams},
      author={Jin, Di and Pan, Eileen and Oufattole, Nassim and Weng, Wei-Hung and Fang, Hanyi and Szolovits, Peter},
      journal={arXiv preprint arXiv:2009.13081},
      year={2020}
    }