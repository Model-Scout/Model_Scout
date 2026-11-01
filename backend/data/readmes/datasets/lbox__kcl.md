---
dataset_info:
- config_name: kcl_essay
  features:
  - name: meta
    dtype: string
  - name: question
    dtype: string
  - name: rubrics
    list: string
  - name: score
    dtype: int64
  - name: supporting_precedents
    list: string
  splits:
  - name: test
    num_bytes: 8516472
    num_examples: 169
  download_size: 3250635
  dataset_size: 8516472
- config_name: kcl_mcqa
  features:
  - name: meta
    dtype: string
  - name: question
    dtype: string
  - name: A
    dtype: string
  - name: B
    dtype: string
  - name: C
    dtype: string
  - name: D
    dtype: string
  - name: E
    dtype: string
  - name: label
    dtype: string
  - name: supporting_precedents
    list: string
  splits:
  - name: test
    num_bytes: 13687302
    num_examples: 283
  download_size: 5988971
  dataset_size: 13687302
configs:
- config_name: kcl_essay
  data_files:
  - split: test
    path: kcl_essay/test-*
- config_name: kcl_mcqa
  data_files:
  - split: test
    path: kcl_mcqa/test-*
task_categories:
- question-answering
language:
- ko
tags:
- legal
size_categories:
- n<1K
license: cc-by-nc-4.0
---

# KCL

This repository hosts the **Korean Canonical Legal Benchmark (KCL)** datasets.  

[![Github](https://img.shields.io/badge/GitHub-KCL-blue?style=flat&logo=github)](https://github.com/lbox-kr/kcl) [![Paper](https://img.shields.io/badge/arXiv-2512.24572-red?style=flat&logo=arxiv&logoColor=red)](https://arxiv.org/abs/2512.24572)

## Why KCL?

KCL is designed to **disentangle knowledge coverage from evidence-grounded reasoning**.   

KCL supports two complementary evaluation axes:
1. **Knowledge Coverage**: performance without extra context.  
2. **Evidence-Grounded Reasoning**: performance **with per-question supporting precedents** provided in-context.

For essay questions, KCL further offers **instance-level rubrics** to enable **LLM-as-a-Judge** automated scoring.

For more information, please refer to our paper 

#### Intended Uses
 - Separating knowledge vs. reasoning by comparing vanilla and with-precedent settings.
 - Legal RAG research using question-aligned gold precedents to establish retriever/reader upper bounds.
 - Fine-grained feedback via rubric-level diagnostics on essay outputs.

## Components

- **KCL-Essay** (open-ended generation)  
  - 169 questions, 550 supporting precedents, 2,739 instance-level rubrics.
- **KCL-MCQA** (five-choice question answering)  
  - 283 questions, 1,103 supporting precedents.
 
## Usage


```python
from datasets import load_dataset

# Essay subset
kcl_essay = load_dataset("lbox/kcl", "kcl_essay", split="test")
# MCQA subset
kcl_mcqa = load_dataset("lbox/kcl", "kcl_mcqa", split="test")
```

## KCL-Essay

## Dataset Fields

 - meta: Metadata such as exam year, subject, and question id.
 - question: The full prompt presented to models.
 - rubrics: Instance-level grading rubrics for automated evaluation.
 - score: The original point value assigned in the official bar exam (reflecting difficulty).
 - supporting\_precedents: Question-aligned court decisions required to solve the problem.

#### Results

<img src="https://cdn-uploads.huggingface.co/production/uploads/6364b581a53b71b7a1b62364/fEb_RSiHVCGT6v0V7A13B.png" width="300" />

## KCL-MCQA

### Dataset Fields

 - meta: Metadata about the source exam item.
 - question: The full prompt presented to models.
 - A–E: Five answer options.
 - label: The gold answer option letter (one of 'A'|'B'|'C'|'D'|'E').
 - supporting\_precedents: Question-aligned court decisions required to solve the problem.

#### Results

<img src="https://cdn-uploads.huggingface.co/production/uploads/6364b581a53b71b7a1b62364/OmiTG5Tv6pN2PRtiBhspy.png" width="300" />

## Citation
```bibtex
@inproceedings{
oh2026korean,
title={Korean Canonical Legal Benchmark: Toward Knowledge-Independent Evaluation of {LLM}s' Legal Reasoning Capabilities},
author={Hongseok Oh and Wonseok Hwang and Kyoung-Woon On},
booktitle={19th Conference of the European Chapter of the Association for Computational Linguistics},
year={2026},
url={https://openreview.net/forum?id=Dw0sFP4l5s}
}
```

## LICENSE

The KCL dataset is derived from the [Korean Bar Exam](https://www.moj.go.kr/moj/405/subview.do) materials, which are released under the [KOGL Type 1](https://www.kogl.or.kr/info/licenseType1.do) license by the Government of the Republic of Korea.  

This dataset was developed solely for academic and research purposes by LBOX.
It is not sponsored, endorsed, or affiliated with the Ministry of Justice.

The case-analysis evaluation guidelines included in this dataset were independently created by LBOX and do not originate from any public institution.
These contributions constitute original works authored by LBOX and are incorporated into the dataset under the terms described below.

Unless otherwise specified, the [KCL](https://huggingface.co/datasets/lbox/kcl) dataset as a whole is distributed under the Creative Commons Attribution-NonCommercial 4.0 International License ([CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) license).

LBOX, 2026.