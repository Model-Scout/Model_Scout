---
license: mit
dataset_info:
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: ground_truth
    dtype: string
  splits:
  - name: train
    num_bytes: 5038039728.815
    num_examples: 76263
  - name: validation
    num_bytes: 833810548.666
    num_examples: 8662
  download_size: 2276849227
  dataset_size: 5871850277.481
language:
- en
- ko
tags:
- block diagram
size_categories:
- 10K<n<100K
---

# Block Diagram Dataset

This dataset is a combination of four block diagram datasets. The first dataset is the BD-EnKo dataset, which was introduced in the paper **"Unveiling the Power of Integration: Block Diagram Summarization through Local-Global Fusion"** accepted at ACL 2024. The second dataset is [CBD](https://github.com/shreyanshu09/Block-Diagram-Datasets), the third is [FC_A](https://github.com/shreyanshu09/Block-Diagram-Datasets), and the fourth is [FC_B](https://github.com/shreyanshu09/Block-Diagram-Datasets).

Only BD-EnKo dataset is available [here](https://huggingface.co/datasets/shreyanshu09/BD-EnKo).

## Dataset description

This dataset contains different types of block diagram images from different sources with their high-quality summaries.

| Types           | Train |         | Validation |         |
|-----------------|-------|---------|------------|---------|
|                 | English | Korean | English    | Korean  |
|-----------------|---------|--------|------------|---------|
| Flowchart       | 7,875   | 7,678  | 875        | 854     |
| GraphLR         | 5,462   | 2,861  | 607        | 318     |
| GraphTD         | 3,500   | 2,402  | 389        | 267     |
| Journey         | 8,494   | 8,858  | 942        | 985     |
| Sequence        | 2,708   | 3,539  | 301        | 394     |
| Simple Graph    | 3,825   | 1,194  | 425        | 133     |
| State Diagram   | 6,444   | 6,265  | 717        | 693     |
| C4              | 3,549   | 0      | 395        | 0       |
| Real World      | 76      | 304    | 15         | 50      |
| CBD             | 396     | 0      | 106        | 0       |
| FC_A            | 357     | 0      | 0          | 0       |
| FC_B            | 476     | 0      | 196        | 0       |
|-----------------|---------|--------|------------|---------|
| **Total**       | **43,162** | **33,101** | **4,968**    | **3,694** |


## Contact
If you have any questions about this work, please contact **[Shreyanshu Bhushan](https://github.com/shreyanshu09)** using the following email addresses: **shreyanshubhushan@gmail.com**.
