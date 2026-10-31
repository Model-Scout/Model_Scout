---
language:
- ko
tags:
- synthetic
- sft
- instruction-tuning
- mobile
- voc
task_categories:
- text-generation
pretty_name: day1-mobile-sft-practice
size_categories:
- n<1K
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
dataset_info:
  features:
  - name: seed_id
    dtype: int64
  - name: synthetic_id
    dtype: int64
  - name: source_type
    dtype: string
  - name: task_type
    dtype: string
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  - name: system
    dtype: string
  - name: user
    dtype: string
  - name: assistant
    dtype: string
  splits:
  - name: train
    num_bytes: 68208
    num_examples: 18
  - name: validation
    num_bytes: 6548
    num_examples: 2
  download_size: 68663
  dataset_size: 74756
---

# day1-mobile-sft-practice

모바일 제품팀용 한국어 synthetic SFT 데이터셋입니다.

## Files
- `synthetic_df.csv`: 생성 직후 전체 데이터
- `judged_df.csv`: judge 결과 포함 데이터
- `approved_df.csv`: judge 통과 데이터
- `dedup_df.csv`: 중복 제거 후 데이터
- `hf_train_df.csv`: 학습용 정리본
- `hf_train_df.jsonl`: JSONL 학습용 파일

## Columns
- `instruction`
- `input`
- `output`
- `source_type`
- `task_type`
- `seed_id`
- `synthetic_id`
