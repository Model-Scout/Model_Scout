---
dataset_info:
  features:
  - name: question
    dtype: string
  - name: question_en
    dtype: string
  - name: response
    dtype: string
  - name: response_en
    dtype: string
  - name: acceptable?
    dtype: int64
  - name: category
    sequence: string
  - name: question_category
    dtype: string
  - name: raw_annotations
    struct:
    - name: 'Q2: Acceptable or Non-acceptable'
      list:
      - name: acceptable?
        dtype: string
      - name: workerID
        dtype: int64
    - name: 'Q3-1: Reasons behind the non-acceptability'
      list:
      - name: category
        sequence: string
      - name: workerID
        dtype: int64
    - name: 'Q3-2: Reasons behind the acceptability'
      list:
      - name: category
        sequence: string
      - name: workerID
        dtype: int64
  splits:
  - name: train
    num_bytes: 9589383
    num_examples: 11952
  - name: valid
    num_bytes: 9621758
    num_examples: 12000
  - name: test
    num_bytes: 9589383
    num_examples: 11952
  - name: test_ood
    num_bytes: 455205
    num_examples: 480
  download_size: 11618081
  dataset_size: 29255729
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: valid
    path: data/valid-*
  - split: test
    path: data/test-*
  - split: test_ood
    path: data/test_ood-*
license: mit
language:
- ko
tags:
- safety
---


reference: [https://github.com/naver-ai/korean-safety-benchmarks](https://github.com/naver-ai/korean-safety-benchmarks)
```
@inproceedings{lee2023square,
                title={SQuARe: A Large-Scale Dataset of Sensitive Questions and Acceptable Responses Created Through Human-Machine Collaboration}, 
                author={Hwaran Lee and Seokhee Hong and Joonsuk Park and Takyoung Kim and Meeyoung Cha and Yejin Choi and Byoung Pil Kim and Gunhee Kim and Eun-Ju Lee and Yong Lim and Alice Oh and Sangchul Park and Jung-Woo Ha},
                booktitle={Proceedings of the 61th Annual Meeting of the Association for Computational Linguistics},
                year={2023}
}
```
