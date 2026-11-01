---
dataset_info:
  features:
  - name: problem_id
    dtype: int64
  - name: question
    dtype: string
  - name: solutions
    dtype: string
  - name: input_output
    dtype: string
  - name: difficulty
    dtype: string
  - name: url
    dtype: string
  - name: starter_code
    dtype: string
  splits:
  - name: en
    num_bytes: 275671232
    num_examples: 974
  - name: es
    num_bytes: 275785030
    num_examples: 974
  - name: ko
    num_bytes: 275866771
    num_examples: 974
  - name: zh
    num_bytes: 275523902
    num_examples: 974
  - name: bn
    num_bytes: 277275474
    num_examples: 974
  - name: te
    num_bytes: 277612793
    num_examples: 974
  - name: sw
    num_bytes: 275643172
    num_examples: 974
  download_size: 1046368597
  dataset_size: 1933378374
configs:
- config_name: default
  data_files:
  - split: en
    path: data/en-*
  - split: es
    path: data/es-*
  - split: ko
    path: data/ko-*
  - split: zh
    path: data/zh-*
  - split: bn
    path: data/bn-*
  - split: te
    path: data/te-*
  - split: sw
    path: data/sw-*
license: apache-2.0
language:
- en
- es
- ko
- zh
- bn
- te
- sw
tags:
- Code
size_categories:
- 1K<n<10K
---

### Dataset Description

This dataset is a multilingual extension of the "introductory" level problems from the codeparrot/apps dataset, which focuses on programming tasks. We filtered the original dataset to include only questions formatted in Standard Input Format, where each problem specifies the expected standard input/output for the solution.
This filtering yields 974 problems. 
The selected problems were then translated from English into six target languages:

- Spanish
- Korean
- Chinese
- Bengali
- Telugu
- Swahili

Each translated instance preserves the structure and semantics of the original programming problem, making the dataset suitable for multilingual program synthesis, translation robustness evaluation, and cross-lingual reasoning tasks. The English version is also included for alignment and comparison.

