---
type: "dataset"
id: "ayymen/Pontoon-Translations"
source: "huggingface"
url: "https://huggingface.co/datasets/ayymen/Pontoon-Translations"
downloads: 1141
summary: "Mozilla Pontoon 플랫폼에서 수집한 200개 이상의 언어 번역 데이터셋입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
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
  - "[[대규모 데이터]]"
---
# ayymen/Pontoon-Translations

> dataset · [Hugging Face](https://huggingface.co/datasets/ayymen/Pontoon-Translations)

Mozilla Pontoon 플랫폼에서 수집한 200개 이상의 언어 번역 데이터셋입니다.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `Source strings are in English` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `their translations into more than 200 languages` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `229 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `30` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mpl-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `strings from various Mozilla projects` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This is a dataset containing strings from various Mozilla projects` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `source_string` 열 p90 121자 ≈ 30 토큰 (viewer statistics, en-ko/train)
