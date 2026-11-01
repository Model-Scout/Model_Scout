---
dataset_info:
- config_name: merge
  features:
  - name: original_idx
    dtype: string
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 4496569309
    num_examples: 1043917
  - name: test
    num_bytes: 236450018
    num_examples: 54948
  download_size: 2189165001
  dataset_size: 4733019327
- config_name: merge_filtered
  features:
  - name: original_idx
    dtype: string
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 4336966319
    num_examples: 1034473
  - name: test
    num_bytes: 227662623
    num_examples: 54430
  download_size: 2153782881
  dataset_size: 4564628942
- config_name: split
  features:
  - name: original_idx
    dtype: string
  - name: conversation_idx
    dtype: string
  - name: content
    dtype: string
  - name: role
    dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 4652568891
    num_examples: 4205413
  - name: test
    num_bytes: 244079529
    num_examples: 221249
  download_size: 2201252839
  dataset_size: 4896648420
- config_name: split_filtered
  features:
  - name: original_idx
    dtype: string
  - name: conversation_idx
    dtype: string
  - name: content
    dtype: string
  - name: role
    dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 4604820852.753419
    num_examples: 4162254
  - name: test
    num_bytes: 241410914.0880637
    num_examples: 218830
  download_size: 2170047068
  dataset_size: 4846231766.841482
configs:
- config_name: merge
  data_files:
  - split: train
    path: merge/train-*
  - split: test
    path: merge/test-*
- config_name: merge_filtered
  data_files:
  - split: train
    path: merge_filtered/train-*
  - split: test
    path: merge_filtered/test-*
- config_name: split
  data_files:
  - split: train
    path: split/train-*
  - split: test
    path: split/test-*
- config_name: split_filtered
  data_files:
  - split: train
    path: split_filtered/train-*
  - split: test
    path: split_filtered/test-*
task_categories:
- text-generation
language:
- ko
tags:
- synthetic
size_categories:
- 1M<n<10M
---

# ~~번역 결과에 토큰이 반복된 결과들이 포함되어 있습니다. 필터링 후 재업로드 하겠습니다.~~
# Z 알고리즘을 사용해 결과를 필터링 하였으며 {subset}_filtered 로 업로드하였습니다.

## 필터링 후 결과

| subset      | 전       | 후       |
| ----------- | ------- | ------- |
| split/train | 4205413 | 4162254 |
| split/test  | 221249  | 218830  |
| merge/train | 1043917 | 1034473 |
| merge/test  | 54948   | 54430   |


[HuggingFaceTB/smoltalk](https://huggingface.co/datasets/HuggingFaceTB/smoltalk) 데이터셋의 `subset:all`을 [nayohan/llama3-instrucTrans-enko-8b](https://huggingface.co/nayohan/llama3-instrucTrans-enko-8b) 모델을 사용해 번역했습니다.

원본의 messages 중 4096 token 이 넘어가는 content가 있다면 해당 레코드는 번역하지 않았습니다.