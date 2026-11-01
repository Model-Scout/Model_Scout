---
type: "dataset"
id: "PhuongViHuynh/MTHealth"
source: "huggingface"
url: "https://huggingface.co/datasets/PhuongViHuynh/MTHealth"
downloads: 7
summary: "베트남어, 프랑스어, 영어, 한국어 정신건강 QA 데이터셋으로 다국어 질의응답 연구 지원용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[fr]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[vi]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# PhuongViHuynh/MTHealth

> dataset · [Hugging Face](https://huggingface.co/datasets/PhuongViHuynh/MTHealth)

베트남어, 프랑스어, 영어, 한국어 정신건강 QA 데이터셋으로 다국어 질의응답 연구 지원용입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `This dataset aims to support research in multilingual QA, cross-lingual retrieval, and health-oriented natural language understanding` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories, task_ids = `question-answering` · 신뢰도 high
- **작업**: [[문서 검색]] — ner · readme = `This dataset aims to support research in multilingual QA, cross-lingual retrieval` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:question_answering, task:retrieval = `Each entry includes a question and a corresponding answer grounded in trusted mental health documents` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Each entry includes a question and a corresponding answer grounded in trusted mental health documents` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — ner · readme = `expert-level mental health resources` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The data is split into train, validation, and test sets for each language` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
