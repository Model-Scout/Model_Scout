---
type: "dataset"
id: "DigitalLearningGmbH/tatoeba_mt_parquet"
source: "huggingface"
url: "https://huggingface.co/datasets/DigitalLearningGmbH/tatoeba_mt_parquet"
downloads: 219
summary: "Tatoeba Translation Challenge는 다국어 기계 번역 벤치마크 데이터셋으로, 다양한 언어 쌍의 테스트 및 개발 데이터를 포함합니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
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
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# DigitalLearningGmbH/tatoeba_mt_parquet

> dataset · [Hugging Face](https://huggingface.co/datasets/DigitalLearningGmbH/tatoeba_mt_parquet)

Tatoeba Translation Challenge는 다국어 기계 번역 벤치마크 데이터셋으로, 다양한 언어 쌍의 테스트 및 개발 데이터를 포함합니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = `Data instances are given as translation units in TAB-separated files with four columns: source and target language ISO-639-3 codes, source language text and tar` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `Data instances are given as translation units in TAB-separated files with four columns: source and target language ISO-639-3 codes, source language text and tar` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `93 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `16` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The Tatoeba Translation Challenge is a multilingual data set of machine translation benchmarks derived from user-contributed translations` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `This dataset includes test and development data sorted by language pair` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `sourceString` 열 p90 66자 ≈ 16 토큰 (viewer statistics, deu-kor/test)
