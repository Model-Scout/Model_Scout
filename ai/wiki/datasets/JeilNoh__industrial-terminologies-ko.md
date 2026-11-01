---
type: "dataset"
id: "JeilNoh/industrial-terminologies-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/JeilNoh/industrial-terminologies-ko"
downloads: 5
summary: "한국어 산업 용어와 설명을 포함한 질의응답용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
---
# JeilNoh/industrial-terminologies-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/JeilNoh/industrial-terminologies-ko)

한국어 산업 용어와 설명을 포함한 질의응답용 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:question_answering = `features:
- name: terminology
dtype: string
- name: explanation
dtype: string
- name: source
dtype: string` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `features:
- name: terminology
dtype: string
- name: explanation
dtype: string
- name: source
dtype: string` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `unlicense` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `- name: train
num_bytes: 3866488
num_examples: 15047` · 신뢰도 medium
