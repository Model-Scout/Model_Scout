---
language:
- ko
- en
license: cc-by-sa-3.0
task_categories:
- translation
- text2text-generation
pretty_name: Korean-English Parallel Wiki Augmented Ver 1
dataset_info:
  features:
  - name: english
    dtype: string
  - name: korean
    dtype: string
  - name: score
    dtype: float64
  splits:
  - name: train
    num_bytes: 922808552
    num_examples: 503245
  download_size: 569293602
  dataset_size: 922808552
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
tags:
- sentence-transformers
- translation
- korean
- english
- parallel
- embedding
- distill
- distillation
---
## Korean-English Parallel Wiki Augmented v1

This dataset contains a large number of Korean-English parallel sentences extracted from Wikipedia. It was created by augmenting the original English Wikipedia dataset with machine-translated Korean sentences. The dataset is designed for training and evaluating machine translation models, especially those focusing on English-to-Korean and Korean-to-English translation.

**Dataset Features:**

* **english:** English sentence.
* **korean:**  Korean translation of the English sentence.

**Dataset Splits:**

* **train:** 503,245 parallel sentence pairs.

**Dataset Size:**

* **Download size:** 569MB
* **Dataset size on disk:** 923MB

**Source:**

This dataset is derived from English Wikipedia. It has been augmented with machine-translated Korean text. 

**Disclaimer:**

This dataset is generated programmatically and may contain errors, inconsistencies, or biases stemming from the source material and the translation process. It is essential to carefully evaluate and preprocess the data before using it for any downstream task. The dataset is provided "as is" without any warranty, express or implied.