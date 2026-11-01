---
dataset_info:
  features:
  - name: question
    dtype: string
  - name: question_en
    dtype: string
  - name: sensitive?
    dtype: int64
  - name: category
    dtype: string
  - name: raw_annotations
    struct:
    - name: 'Q2: Subjective or Objective'
      list:
      - name: subjective?
        dtype: string
      - name: workerID
        dtype: int64
    - name: 'Q3: Sensitive or Non-sensitive'
      list:
      - name: category
        dtype: string
      - name: workerID
        dtype: int64
  splits:
  - name: train
    num_bytes: 16237558
    num_examples: 37115
  - name: valid
    num_bytes: 3114014
    num_examples: 6882
  - name: test
    num_bytes: 3153147
    num_examples: 6945
  - name: test_ood
    num_bytes: 148855
    num_examples: 255
  download_size: 8411408
  dataset_size: 22653574
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