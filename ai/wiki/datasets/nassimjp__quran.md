---
type: "dataset"
id: "nassimjp/quran"
source: "huggingface"
url: "https://huggingface.co/datasets/nassimjp/quran"
downloads: 482
summary: "79개 언어, 185개 번역의 구절 정렬된 다국어 꾸란 말뭉치로, 수니파 정통 내 번역만 포함됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
  - "[[번역]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
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
  - "[[조건부 이용]]"
domain:
  - "[[학술·논문]]"
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# nassimjp/quran

> dataset · [Hugging Face](https://huggingface.co/datasets/nassimjp/quran)

79개 언어, 185개 번역의 구절 정렬된 다국어 꾸란 말뭉치로, 수니파 정통 내 번역만 포함됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `all row-aligned on the canonical 6,236-ayah verse_key` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 medium
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation, task:question_answering, task:retrieval, task:translation = `A unified, verse-aligned multilingual Quran corpus spanning 79 languages and 185 translations.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:translation = `A unified, verse-aligned multilingual Quran corpus spanning 79 languages and 185 translations.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `79 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `37` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `QuranLab — Verse-Aligned Multilingual Quran Corpus` · 신뢰도 low
- **도메인**: [[일반]] — ner · readme = `The text here reaches you through the work of Tanzil Project, fawazahmed0/quran-api, QuranEnc.com, Tafsir Center for Quranic Studies and Quranic Universal Libra` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `split `train`` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 148자 ≈ 37 토큰 (viewer statistics, ko-hamidchoi/train)

## 같은 데이터의 사본·중복 등록

- `quranlab/quran`
