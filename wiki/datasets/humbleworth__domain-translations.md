---
type: "dataset"
id: "humbleworth/domain-translations"
source: "huggingface"
url: "https://huggingface.co/datasets/humbleworth/domain-translations"
downloads: 33
summary: "20개 언어로 번역된 155,004개 도메인 이름 데이터셋으로 다국어 도메인 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
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
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# humbleworth/domain-translations

> dataset · [Hugging Face](https://huggingface.co/datasets/humbleworth/domain-translations)

20개 언어로 번역된 155,004개 도메인 이름 데이터셋으로 다국어 도메인 연구에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — tag_match · readme, tags = `zero-shot-classification` · 신뢰도 medium
- **작업**: [[임베딩]] — metadata · tags, task_categories = `feature-extraction` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · tags, task_categories = `text-generation` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Creating cross-lingual domain representations for similarity search and clustering across languages` · 신뢰도 low
- **작업**: [[번역]] — metadata · tags, task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:generation, task:retrieval, task:translation = `This dataset contains 155,004 domain names with their multilingual translations across 20 languages.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `Each domain has been segmented into constituent words and translated while preserving semantic meaning and commercial appeal.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `20 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `6` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The dataset is particularly valuable for domain name research, multilingual NLP tasks, and understanding how brand names and concepts translate across languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Training models for domain name segmentation and translation` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `domain` 열 p90 23자 ≈ 6 토큰 (viewer statistics, default/train)
