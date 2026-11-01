---
type: "dataset"
id: "almanach/halvest"
source: "huggingface"
url: "https://huggingface.co/datasets/almanach/halvest"
downloads: 1174
summary: "HALvest는 HAL에서 수집한 오픈 과학 논문 전문 데이터셋으로 연구용으로 활용됩니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[학술·논문]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# almanach/halvest

> dataset · [Hugging Face](https://huggingface.co/datasets/almanach/halvest)

HALvest는 HAL에서 수집한 오픈 과학 논문 전문 데이터셋으로 연구용으로 활용됩니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Our dump is mostly english/french but gather papers written in 56 languages across 13 domains.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · task_categories, task_ids = `fill-mask` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `This is the unfiltered version of HALvest, comprising of fulltext from open papers found on Hyper Articles en Ligne (HAL)` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:generation, task:language_modeling, task:retrieval = `comprising of fulltext from open papers found on Hyper Articles en Ligne (HAL)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `comprising of fulltext from open papers found on Hyper Articles en Ligne (HAL)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `57 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `Open Scientific Papers Harvested from HAL (Unfiltered)` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This must be considered prior to using this dataset for any purpose, other than training deep learning models, data mining etc.` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
