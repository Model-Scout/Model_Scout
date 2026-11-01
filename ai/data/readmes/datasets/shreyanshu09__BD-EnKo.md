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
    num_bytes: 9616619571.478
    num_examples: 75034
  - name: validation
    num_bytes: 746918710.6
    num_examples: 8360
  download_size: 2177400123
  dataset_size: 10363538282.078001
language:
- en
- ko
tags:
- block diagrams
size_categories:
- 10K<n<100K
---


# BD-EnKo Dataset

It was introduced in the paper **"Unveiling the Power of Integration: Block Diagram Summarization through Local-Global Fusion"** accepted at ACL 2024. The full code is available in [BD-EnKo](https://github.com/shreyanshu09/BD-EnKo) github repository.

## Dataset description

This dataset contains different types of block diagram images with their high-quality summaries.

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
|-----------------|---------|--------|------------|---------|
| **Total**       | **41,933** | **33,101** | **4,666**    | **3,694** |


For more information check [here](https://github.com/shreyanshu09/BD-EnKo)

## Contact
If you have any questions about this work, please contact **[Shreyanshu Bhushan](https://github.com/shreyanshu09)** using the following email addresses: **shreyanshubhushan@gmail.com**.
