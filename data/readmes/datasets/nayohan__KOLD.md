---
dataset_info:
  features:
  - name: guid
    dtype: string
  - name: source
    dtype: string
  - name: date
    dtype: timestamp[ns]
  - name: title
    dtype: string
  - name: comment
    dtype: string
  - name: 'OFF'
    dtype: bool
  - name: TGT
    dtype: string
  - name: GRP
    dtype: string
  - name: OFF_span
    dtype: string
  - name: TGT_span
    dtype: string
  - name: raw_labels
    list:
    - name: annotator_id
      dtype: int64
    - name: off_end_idx
      sequence: int64
    - name: off_start_idx
      sequence: int64
    - name: offensiveness
      dtype: bool
    - name: target
      sequence:
        sequence: string
    - name: target_group
      sequence:
        sequence: string
    - name: tgt_end_idx
      sequence: int64
    - name: tgt_start_idx
      sequence: int64
  splits:
  - name: train
    num_bytes: 20683839
    num_examples: 40429
  download_size: 8176787
  dataset_size: 20683839
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
tags:
- safety
---


reference: [https://github.com/boychaboy/KOLD](https://github.com/boychaboy/KOLD)
```
@inproceedings{jeong2022kold,
  title={KOLD: Korean Offensive Language Dataset},
  author={Jeong, Younghun and Oh, Juhyun and Lee, Jongwon and Ahn, Jaimeen and Moon, Jihyung and Park, Sungjoon and Oh, Alice},
  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},
  pages={10818--10833},
  year={2022}
}
```