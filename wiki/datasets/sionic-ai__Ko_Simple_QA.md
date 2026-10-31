---
type: "dataset"
id: "sionic-ai/Ko_Simple_QA"
source: "huggingface"
url: "https://huggingface.co/datasets/sionic-ai/Ko_Simple_QA"
downloads: 17
summary: "영어 질문답변 쌍과 한국어 번역으로 구성된 한영 질문답변 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# sionic-ai/Ko_Simple_QA

> dataset · [Hugging Face](https://huggingface.co/datasets/sionic-ai/Ko_Simple_QA)

영어 질문답변 쌍과 한국어 번역으로 구성된 한영 질문답변 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — tag_match · readme, tags = `question-answering` · 신뢰도 medium
- **작업**: [[번역]] — tag_match · readme, tags = `translation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:question_answering, task:translation = `영어 질문` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:translation = `영어 답변` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한영 질문답변 데이터셋` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `총 4,265개의 질문답변 쌍이 포함되어 있으며, CSV 형식으로 제공.` · 신뢰도 low
