---
dataset_info:
  features:
  - name: english
    dtype: string
  - name: korean
    dtype: string
  splits:
  - name: train
    num_bytes: 5906307
    num_examples: 140032
  download_size: 4913505
  dataset_size: 5906307
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: apache-2.0
language:
- ko
- en
---

### 목적

- 더이상 Hermitian Matrix를 "허미트 행렬", "허미트리안 행렬", "헤르미트 행렬" 이라고 부르지 않는 모델을 만들기 위해

### 특징

- 수학 관련 영어 웹 데이터를 기반으로 수학자, 지명, 수학자 이름/지명이 포함된 수학 공식이나 이론명 등의 (비교적)올바른 한국어 명칭을 생성
- 다만 웹 데이터 기반이므로, 수학자 이름 외에도 "답변자 ID"와 같은 일반인 이름, 프로그램 코드의 함수명으로 추측되는 텍스트도 Named Entity로 포함되어 있음
- 성과 이름이 잘못 매칭된 경우도 있음
- Sonnet 3.7 기반이므로 잘못된 번역도 존재함
  - 예시: Zu Chongzhi - 주 충즈 (올바른 번역: 조충지 -> Sonnet은 대부분의 고대 중국인 이름을 중국어 발음 그대로 번역함)

### 기반 데이터 셋

- [ajibawa-2023/Maths-College](https://huggingface.co/datasets/ajibawa-2023/Maths-College) 에서 instruction 부분만 추출
- 수학 관련 웹 데이터

### 번역 방법

- NER 모델: [dslim/bert-large-NER](https://huggingface.co/dslim/bert-large-NER)

  - RoBERTa 기반 모델도 테스트해봤으나, 수학 관련 개념(Hermitian matrix, Hadamard product 등)을 Named Entity로 추출하지 않는 경향이 있음.

- 이후 [google/gemma-3-27b-it](https://huggingface.co/google/gemma-3-27b-it)로 1차 정제

  - 수학과 관련 없는 Entity 필터링, 여러 명의 이름이 한 entity로 추출된 경우 분리
  - 비용 효율을 위해 별도 맥락 없이 문서별 entity 리스트만 제공함.

- 최종 번역 모델: Claude-3.7-Sonnet

  - 주요 대형 비추론 모델 중에서 가장 번역 성능이 좋았음.
  - 비용 효율을 위해 전체 문서의 entity에서 중복을 제거하고 만든 entity list만 제공함.