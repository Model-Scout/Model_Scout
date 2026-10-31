---
language:
- ko
license: other
task_categories:
- automatic-speech-recognition
license_name: aihub
license_link: https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=71481
dataset_info:
  features:
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: transcripts
    dtype: string
  splits:
  - name: train
    num_bytes: 9673667615.284883
    num_examples: 137
  - name: test
    num_bytes: 1368683535.4534883
    num_examples: 18
  - name: valid
    num_bytes: 1243473658.261628
    num_examples: 17
  download_size: 12140057435
  dataset_size: 12285824809.0
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
  - split: valid
    path: data/valid-*
---
