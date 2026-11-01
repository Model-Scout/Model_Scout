---
type: "dataset"
id: "nyuuzyou/wikis"
source: "huggingface"
url: "https://huggingface.co/datasets/nyuuzyou/wikis"
downloads: 48
summary: "인터넷상의 930개 공개 MediaWiki에서 수집한 166만 개 이상의 다국어 위키 문서 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
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
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# nyuuzyou/wikis

> dataset · [Hugging Face](https://huggingface.co/datasets/nyuuzyou/wikis)

인터넷상의 930개 공개 MediaWiki에서 수집한 166만 개 이상의 다국어 위키 문서 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories, task_ids = `text-classification` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `The dataset represents a diverse cross-section of public wiki content spanning multiple domains, topics, and languages.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · task_ids = `language-modeling` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `The collection was created by extracting current page content from these wikis, preserving article text, metadata, and structural information.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:generation, task:language_modeling, task:retrieval = `preserving article text, metadata, and structural information.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `preserving article text, metadata, and structural information.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `39 languages` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `62825` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The dataset represents a diverse cross-section of public wiki content spanning multiple domains, topics, and languages.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains 1,662,448 articles harvested from 930 random public MediaWiki instances found across the Internet.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 251298자 ≈ 62825 토큰 (viewer statistics, default/train)
