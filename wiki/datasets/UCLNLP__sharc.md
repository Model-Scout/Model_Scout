---
type: "dataset"
id: "UCLNLP/sharc"
source: "huggingface"
url: "https://huggingface.co/datasets/UCLNLP/sharc"
downloads: 1369
summary: "ShARC는 규칙이 포함된 텍스트에서 대화형 질의응답을 위한 데이터셋입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# UCLNLP/sharc

> dataset · [Hugging Face](https://huggingface.co/datasets/UCLNLP/sharc)

ShARC는 규칙이 포함된 텍스트에서 대화형 질의응답을 위한 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories, task_ids = `question-answering` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:question_answering = `question answering from texts containing rules` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `The goal is to answer questions by possibly asking follow-up questions first.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-3.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `ShARC is a Conversational Question Answering dataset focussing on question answering from texts containing rules.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[blackmallangcow__nari-decision-4b|blackmallangcow/nari-decision-4b]]
