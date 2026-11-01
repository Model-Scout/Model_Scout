---
dataset_info:
  features:
  - name: id
    dtype: string
  - name: doc_id
    dtype: string
  - name: source
    dtype: string
  - name: method
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: question_type
    dtype: string
  - name: origin_id
    dtype: string
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  splits:
  - name: train
    num_bytes: 1073579
    num_examples: 1169
  - name: validation
    num_bytes: 299863
    num_examples: 315
  download_size: 914865
  dataset_size: 1373442
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
language:
- ko
task_categories:
- text-generation
---

# 노무 상담 Q&A

노동법 조문에 근거해 답하는 노무 상담 챗봇의 지도 파인튜닝(SFT) 데이터입니다.

- 출처: 국가법령정보센터(law.go.kr) 노동법 조문으로 LLM이 만든 Q&A와 기존 FAQ, 그 증강 행
- 학습에 쓰는 열: `messages`(system, user, assistant)
- 규모: train 1,169행, validation 315행
- 한계: LLM이 만든 질문과 답이 섞여 사실 오류가 있을 수 있어 법률 자문으로 쓰지 않습니다.
