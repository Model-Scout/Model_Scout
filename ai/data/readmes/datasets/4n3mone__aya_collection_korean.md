---
dataset_info:
  features:
  - name: id
    dtype: int64
  - name: inputs
    dtype: string
  - name: targets
    dtype: string
  - name: dataset_name
    dtype: string
  - name: sub_dataset_name
    dtype: string
  - name: task_type
    dtype: string
  - name: template_id
    dtype: int64
  - name: language
    dtype: string
  - name: script
    dtype: string
  - name: split
    dtype: string
  splits:
  - name: train
    num_bytes: 2164270878
    num_examples: 3605894
  - name: validation
    num_bytes: 182708679
    num_examples: 276202
  - name: test
    num_bytes: 202554385
    num_examples: 279418
  download_size: 1147896919
  dataset_size: 2549533942
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
  - split: test
    path: data/test-*
license: apache-2.0
language:
- ko
---
CohereForAI/aya_collection_language_split 에서 한국어 스플릿만 추출한 데이터셋 입니다.

데이처 출처(dataset name)는 다음과 같습니다. (번역된 데이터셋은 (T) 표시)

Aya-Dataset

Flan-CoT-submix(T)

Adversarial QA(T)

Flan-Coqa(T)

Flan-unified-QA(T)

Flan-GEM-wiki-lingua(T)

CNN-Daily-Mail(T)

WIKI QA(T)

PAWS-Wiki(T)

Wiki-split-inst(T)

NTX-LLM-inst

HotpotQA(T)

NQ-Open(T)

Joke-explaination-inst(T)

MLQA-en(T)

SODA-inst(T)

Xlel_wd-inst

Flan-lambada(T)

Xlel_wd-inst(T)

Mintaka-inst(T)

PIQA(T)

Dolly-v2(T)


