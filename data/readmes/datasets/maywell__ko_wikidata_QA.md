---
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 144606911 
    num_examples: 137505
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train.csv
---
## 업데이트 로그

- 2023-11-03 : MarkrAI의 Dedup 적용.

# 한국어 위키 데이터 QA셋

본 데이터는 Synatra-7B-Instruct 모델과 ChatGPT를 사용하여, 제작된 QA셋입니다.

해당 데이터를 직접적으로 상업적으로 사용하는 것은 허용되지 않으며, 데이터를 이용하여 훈련된 모델에 대한 상업적 사용은 허용됩니다.

아직 완벽히 정제되지는 않았으며, 오류나 수정사항에 대해서는 PR 부탁드립니다.
