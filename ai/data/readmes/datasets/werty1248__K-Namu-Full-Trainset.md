---
dataset_info:
  features:
  - name: id
    dtype: string
  - name: type
    dtype: string
  - name: question
    dtype: string
  - name: choice
    sequence: string
  - name: answer
    dtype: string
  - name: difficulty
    dtype: string
  - name: relativity
    dtype: string
  splits:
  - name: train
    num_bytes: 36233166
    num_examples: 55228
  download_size: 19974029
  dataset_size: 36233166
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
---


### 나무위키 기반 한국 역사/문화/제도 관련 QA 데이터 셋

- [heegyu/namuwiki-extracted](https://huggingface.co/datasets/heegyu/namuwiki-extracted)을 기반으로 작성되었습니다.

### 제작 방법

1. 전체 565k개 문서 중, **Qwen3-30B-A3B** 모델을 이용하여 한국 역사/문화/제도 관련 내용이 포함된 문서 약 55k개 식별 및 내용 요약..(1)
2. **Gemini-2.5-flash** 모델을 이용하여 선다형(객관식, 5지선다), 단답형 문제 생성..(2)
3. (2)에서 생성된 문제 중, **DeepSeek-V3-0324가 정답을 맞춘** 문제만 추출
4. (1)을 바탕으로 서술형 문제(XXX에 대해 자세히 알려주세요.)를 생성하여 선다형, 단답형 문제와 통합

### 기타

- 선다형/단답형 문제의 원본 문서
  - 각 문제의 id 첫번째 숫자를 바탕으로, id가 "{id}_서술_01"인 질문을 확인(서술형 문제)
  - 질문이 "XXX에 대해 자세히 알려주세요." 일 경우, XXX가 원본 나무위키 문서명
  - 질문이 "XXX에 관한 내용 중, YYY에 대해 자세히 알려주세요." 일 경우, XXX/YYY가 원본 나무위키 문서명
- Gemini-2.5-flash가 문제를 생성할 때 난이도(difficulty), 한국과의 관련성(relativity) 등도 함께 출력하도록 시켰으나, 큰 의미는 없어 보입니다.