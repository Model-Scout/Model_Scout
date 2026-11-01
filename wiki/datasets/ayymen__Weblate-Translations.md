---
type: "dataset"
id: "ayymen/Weblate-Translations"
source: "huggingface"
url: "https://huggingface.co/datasets/ayymen/Weblate-Translations"
downloads: 816
summary: "Weblate에 호스팅된 프로젝트 문자열과 다국어 번역을 포함한 데이터셋입니다."
readme_status: "template"
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
  - "[[조건부 이용]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# ayymen/Weblate-Translations

> dataset · [Hugging Face](https://huggingface.co/datasets/ayymen/Weblate-Translations)

Weblate에 호스팅된 프로젝트 문자열과 다국어 번역을 포함한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = `A dataset containing strings from projects hosted on Weblate and their translations into other languages.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `A dataset containing strings from projects hosted on Weblate and their translations into other languages.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `282 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `15` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `A dataset containing strings from projects hosted on Weblate and their translations into other languages.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `source_string` 열 p90 58자 ≈ 15 토큰 (viewer statistics, dev-ko/train)

## 같은 데이터의 사본·중복 등록

- `Himanshu9636/Weblate-Translations`
- `Tamazight-NLP/Weblate-Translations`
