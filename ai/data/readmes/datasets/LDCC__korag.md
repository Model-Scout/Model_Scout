---
language:
- ko
size_categories:
- 10K<n<100K
task_categories:
- question-answering
- text-generation
dataset_info:
- config_name: qa
  features:
  - name: category
    dtype: string
  - name: pages
    sequence: int64
  - name: source
    dtype: string
  - name: answer
    dtype: string
  - name: id
    dtype: string
  - name: question
    struct:
    - name: content
      dtype: string
    - name: noised_questions
      sequence: string
    - name: type
      dtype: string
  splits:
  - name: train
    num_bytes: 7054541.10612855
    num_examples: 10000
  - name: validation
    num_bytes: 695946.053946054
    num_examples: 1000
  download_size: 3644227
  dataset_size: 7750487.160074604
- config_name: sources
  features:
  - name: content
    dtype: binary
  - name: category
    dtype: string
  - name: name
    dtype: string
  splits:
  - name: validation
    num_bytes: 815483744
    num_examples: 334
  - name: train
    num_bytes: 4212511386
    num_examples: 1630
  download_size: 2779327200
  dataset_size: 5027995130
configs:
- config_name: qa
  data_files:
  - split: train
    path: qa/train-*
  - split: validation
    path: qa/validation-*
- config_name: sources
  data_files:
  - split: train
    path: sources/train-*
  - split: validation
    path: sources/validation-*
---
# 한국어 검색증강 데이터셋

## 1. 데이터셋 개요

  이 데이터셋은 한국어 검색 증강을 목적으로, 원본 PDF 파일에서 질의에 맞는 문서를 검색하고 이를 기반으로 응답을 생성하는 질의응답 데이터셋입니다. 문서는 백과, 법률, 의학, 교육, 행정의 5개 범주로 구성되며, 지식재산권 및 저작권을 고려하여 공공 문서를 바탕으로 제작되었습니다.


## 2. 데이터 원천

  분야별 데이터셋 수량과 총 페이지 수는 다음과 같습니다. 각 문서는 원본 그대로 제공되며, 공공누리 1~4 유형의 저작권을 가진 데이터로 선별되었습니다.

  |  분야  |  유형  |  수량  |  페이지 합계  |
  |:------:|:------:|:------:|:-------------:|
  |  백과  |  PDF   |  1,656 |     5,900     |
  |  행정  |  PDF   |  118   |     5,224     |
  |  법률  |  PDF   |  104   |     7,537     |
  |  교육  |  PDF   |   62   |     7,812     |
  |  의료  |  PDF   |   24   |     1,813     |


## 3. 데이터 가공

  데이터셋 제작은 '1) 모델 기반 질의응답 생성 2) 검색모델 기반 질의응답 필터링 3) 검수자의 검수'의 과정을 거쳤습니다. 학습 및 평가 데이터셋의 특징은 다음과 같습니다.

  |              |  질의응답 개수  |  원천문서 수  | 질의 평균길이(char) | 응답 평균길이(char) |
  |:------------:|:------:|:--------------:|:-------------:|:-------------:|
  |  훈련 데이터  | 10,000 |     1,630      |   **65.01**   |   **85.51**   |
  |  평가 데이터  | 1,000  |      334       |   **36.18**   |   **86.38**   |
  
  질의응답은 PDF의 페이지 구분에 따라 구성하였으며, 이로인해 인접한 여러 페이지가 근거문서로 사용되는 경우도 있습니다. 또한 모델의 질의응답에 대한 강건성(robustness)을 평가하기 위해 증강된 질의들(noised_questions)을 제공합니다.
  (질의,응답의 평균길이는 초기 데이터셋([papers](https://huggingface.co/datasets/LDCC/korag/tree/papers))과 차이가 있으니 참고 바랍니다.)

## 4. 평가코드

   해당 데이터셋에 대한 평가 코드는 브런치 [script](https://huggingface.co/datasets/LDCC/korag/tree/script) 에 있습니다.



