---
dataset_info:
  features:
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  splits:
  - name: train
    num_bytes: 226278590
    num_examples: 61966
  download_size: 110040382
  dataset_size: 226278590
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
# maywell/ko_Ultrafeedback_binarized

본 데이터는 Synatra-7B-Translation 모델을 통해 Ultrafeedback_binarized를 번역하고 정제한 데이터셋입니다.

해당 데이터를 직접적으로 상업적으로 사용하는 것은 허용되지 않으며, 데이터를 이용하여 훈련된 모델에 대한 상업적 사용은 허용됩니다.

아직 완벽히 정제되지는 않았으며, 오류나 수정사항에 대해서는 PR 부탁드립니다.