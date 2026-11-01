---
type: "dataset"
id: "wannaphong/wikipedia-monthly"
source: "huggingface"
url: "https://huggingface.co/datasets/wannaphong/wikipedia-monthly"
downloads: 514
summary: "매월 최신 위키피디아 다국어 덤프를 제공하여 NLP 프로젝트에 활용하는 데이터셋입니다."
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# wannaphong/wikipedia-monthly

> dataset · [Hugging Face](https://huggingface.co/datasets/wannaphong/wikipedia-monthly)

매월 최신 위키피디아 다국어 덤프를 제공하여 NLP 프로젝트에 활용하는 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `clean plain text ready for use` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · tags, task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `We run our pipeline monthly to capture the latest versions of all articles.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `monthly, multilingual dumps of Wikipedia, processed and prepared for easy use in NLP projects` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation, task:language_modeling, task:retrieval = `clean, plain text content of the article` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `clean, plain text content of the article` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `356 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — tag_match · readme, tags = `wikipedia` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `processed and prepared for easy use in NLP projects` · 신뢰도 low
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

## 같은 데이터의 사본·중복 등록

- `PRACHI-MUNDA/wikipedia-monthly`
