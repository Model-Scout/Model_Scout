---
language:
- ko
size_categories:
- 10K<n<100K
task_categories:
- text-classification
dataset_info:
- config_name: data
  features:
  - name: query
    dtype: string
  - name: pos
    sequence: string
  - name: neg
    sequence: string
  splits:
  - name: train
    num_bytes: 850663698
    num_examples: 50000
  download_size: 494596571
  dataset_size: 850663698
configs:
- config_name: data
  data_files:
  - split: train
    path: data/train-*
---

# ko-wiki-reranking

[maywell/ko_wikidata_QA](https://huggingface.co/datasets/maywell/ko_wikidata_QA) 데이터셋을 랜덤 샘플링하여 50,000개의 reranking 학습 데이터셋을 만들었습니다. `train_minedHN.jsonl` 파일을 사용하여 학습하시는 것을 권장합니다.

[FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding) 코드 기반으로 학습 데이터셋을 만들었습니다.



- `train.jsonl` : 50,000개의 reranking 학습 데이터셋
- `train_minedHN.jsonl` : 50,000개의 reranking 학습 데이터셋 (mined hard negative) [[관련 코드]](https://github.com/FlagOpen/FlagEmbedding/tree/master/examples/finetune#hard-negatives)