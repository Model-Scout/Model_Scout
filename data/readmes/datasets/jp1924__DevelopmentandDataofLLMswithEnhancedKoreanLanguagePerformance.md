---
dataset_info:
- config_name: PPO
  features:
  - name: id
    dtype: string
  - name: prompt
    dtype: string
  - name: metadata
    struct:
    - name: main
      dtype: string
    - name: middle
      dtype: string
    - name: prompt_type
      dtype: string
  splits:
  - name: train
    num_bytes: 4119401
    num_examples: 24992
  - name: validation
    num_bytes: 514930
    num_examples: 3119
  download_size: 2756312
  dataset_size: 4634331
- config_name: RL
  features:
  - name: id
    dtype: string
  - name: chosen_conversations
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: reject_conversations
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: reject
    dtype: string
  - name: preperence_ranking
    list:
    - name: content
      dtype: string
    - name: ranking
      dtype: float32
  - name: metadata
    struct:
    - name: main
      dtype: string
    - name: middle
      dtype: string
    - name: prompt_type
      dtype: string
  splits:
  - name: train
    num_bytes: 324050261
    num_examples: 24985
  - name: validation
    num_bytes: 40152088
    num_examples: 3101
  download_size: 156116490
  dataset_size: 364202349
- config_name: SFT
  features:
  - name: id
    dtype: string
  - name: conversations
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: prompt
    dtype: string
  - name: answer
    dtype: string
  - name: metadata
    struct:
    - name: main
      dtype: string
    - name: middle
      dtype: string
    - name: prompt_type
      dtype: string
  splits:
  - name: train
    num_bytes: 31279062
    num_examples: 9804
  - name: validation
    num_bytes: 3950881
    num_examples: 1220
  download_size: 17484228
  dataset_size: 35229943
configs:
- config_name: PPO
  data_files:
  - split: train
    path: PPO/train-*
  - split: validation
    path: PPO/validation-*
- config_name: RL
  data_files:
  - split: train
    path: RL/train-*
  - split: validation
    path: RL/validation-*
- config_name: SFT
  data_files:
  - split: train
    path: SFT/train-*
  - split: validation
    path: SFT/validation-*
language:
- ko
---
데이터에 `<NAME>`과 같은 비식별화가 되어 있다. 이거 참고해서 사용해야 함.    
데이터 필더할 때, 비식별화 되어 있는 데이터는 따로 전처리 하지 않음