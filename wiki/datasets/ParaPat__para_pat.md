---
type: "dataset"
id: "ParaPat/para_pat"
source: "huggingface"
url: "https://huggingface.co/datasets/ParaPat/para_pat"
downloads: 156
summary: "ParaPat는 74개 언어쌍 특허 초록 병렬 말뭉치로 번역 연구에 활용됨."
readme_status: "template"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
  - "[[문서 검색]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ParaPat/para_pat

> dataset · [Hugging Face](https://huggingface.co/datasets/ParaPat/para_pat)

ParaPat는 74개 언어쌍 특허 초록 병렬 말뭉치로 번역 연구에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · task_categories, task_ids = `fill-mask` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `parallel corpus from the open access Google Patents dataset in 74 language pairs` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling, task:retrieval, task:translation = `more than 68 million sentences and 800 million tokens` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling, task:translation = `parallel corpus from the open access Google Patents dataset` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `15 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Google Patents dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains the developed parallel corpus` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
