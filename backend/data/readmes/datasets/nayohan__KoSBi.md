---
dataset_info:
  features:
  - name: demographic_category
    dtype: string
  - name: demographic_group
    dtype: string
  - name: context
    dtype: string
  - name: context_en
    dtype: string
  - name: sentence
    dtype: string
  - name: sentence_en
    dtype: string
  - name: context_label
    dtype: string
  - name: context_sub_label
    dtype: string
  - name: sentence_label
    dtype: string
  - name: sentence_sub_label
    sequence: string
  - name: annotated_demo
    list:
    - name: demographic_category
      dtype: string
    - name: demographic_group
      sequence: string
  splits:
  - name: train
    num_bytes: 23587249
    num_examples: 54393
  - name: valid
    num_bytes: 2956445
    num_examples: 6799
  - name: test
    num_bytes: 2965863
    num_examples: 6801
  download_size: 13335660
  dataset_size: 29509557
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: valid
    path: data/valid-*
  - split: test
    path: data/test-*
license: mit
language:
- ko
tags:
- safety
---

reference: [https://github.com/naver-ai/korean-safety-benchmarks](https://github.com/naver-ai/korean-safety-benchmarks)
```
@inproceedings{lee2023kosbi,
                title={KoSBi: A Dataset for Mitigating Social Bias Risks Towards Safer Large Language Model Application}, 
                author={Hwaran Lee and Seokhee Hong and Joonsuk Park and Takyoung Kim and Gunhee Kim and Jung-Woo Ha},
                booktitle={Proceedings of the 61th Annual Meeting of the Association for Computational Linguistics: Industry Track},
                year={2023}
}
```