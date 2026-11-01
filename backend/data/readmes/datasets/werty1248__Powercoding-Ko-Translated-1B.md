---
dataset_info:
  features:
  - name: id
    dtype: int64
  - name: text
    dtype: string
  - name: text_ko
    dtype: string
  - name: num_ko_tokens
    dtype: int64
  - name: similarity
    dtype: float64
  splits:
  - name: train
    num_bytes: 6960452189.504098
    num_examples: 1008321
  download_size: 3277630893
  dataset_size: 6960452189.504098
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

## 데이터 출처

- 원본 출처: **Synthetic coding pretrain data**인 [PowerInfer/PowerCoding](https://huggingface.co/datasets/PowerInfer/PowerCoding) 데이터

### 특징

- 대체로 **파이썬 코드 관련 텍스트**로 이루어져 있긴 하지만, 코드가 없는 개발 관련 질문, sql 명령어 또한 일부 포함됨
- 질문-답변 방식이 아닌, 배경 스토리 기반으로 특정 개념이나 기능을 설명하는 자연어 텍스트 위주로 구성
- 주석, 에러 메세지 등은 한국어로 번역하되, 함수명 등은 원문을 사용

## 번역

- powercoding-nopython 폴더에 있는 데이터 (실제로는 python 코드도 포함됨) 중 약 1%, 약 10억 토큰 번역됨

### 번역 과정

- **번역 모델: [Qwen/Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B)**
- **임베딩 모델: [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3)**
- 번역 실패 후처리
  - 번역 결과 텍스트에 **1. 한글 및 특수문자가 아니면서 2. 원문에 포함되지 않는 문자가 하나라도 있을 경우** 번역 실패로 간주하여 필터링
    - 중국어, 일본어, 러시아어, 아랍어, 그리스어, 태국어 등이 검출됨
    - 알파벳을 사용하는 언어의 단어가 생성되었을 경우 검출을 못했을 수도 있음
  - **반복**이 발생한 경우 필터링
  - 프롬프트로 인해 "네, 텍스트를 한국어로 번역하겠습니다." 등의 말이 포함된 경우가 있었으나, 원문과 번역문의 **첫 문장 임베딩 유사도**를 기반으로 진짜 첫 문장을 다시 탐색하여 매칭.
  - 최종 번역 결과의 **임베딩 유사도가 0.7 이상**인 경우에만 번역 성공으로 간주

### 후처리 관련 특징

- 약 0.5%의 데이터에서 반복으로 인한 답변 깨짐 현상이 발생
- 약 2%의 데이터에서 한국어/영어 이외의 문자 발견됨
- 약 1%의 데이터에서 원문과 관련없는 문장이 생성됨
- 첫 문장 매칭 후, 약 0.25% 데이터가 임베딩 유사도 0.7 미만으로 확인됨.
  - 번역 도중에 종료
  - 번역기로 동작하지 않고, 원문 안에 있는 질문에 답변하고 있음

### 단점

- 코드의 실제 동작 여부는 확인하지 않음
- 번역 모델의 한계로 인해 단어(특히 인명/지명과 같은 고유명사) 번역에 실수가 많음.
- 번역 퀄리티는 읽고 이해하는 데에는 문제가 없으나, 다소 기계번역 느낌이 있음.
- 번역 모델의 한계로 인해, 번역 도중에 간헐적으로 번역 대신 원문을 그대로 출력하는 등의 문제가 있음.
- 처음 기대했던 것보다 python 코드 위주.
- 1x 4090에서 약 11일 소요.