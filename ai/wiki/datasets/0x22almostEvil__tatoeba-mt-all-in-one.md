---
type: "dataset"
id: "0x22almostEvil/tatoeba-mt-all-in-one"
source: "huggingface"
url: "https://huggingface.co/datasets/0x22almostEvil/tatoeba-mt-all-in-one"
downloads: 64
summary: "7.3백만 개 문장으로 구성된 Tatoeba 번역 챌린지 데이터셋 통합 버전입니다."
readme_status: "ok"
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
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# 0x22almostEvil/tatoeba-mt-all-in-one

> dataset · [Hugging Face](https://huggingface.co/datasets/0x22almostEvil/tatoeba-mt-all-in-one)

7.3백만 개 문장으로 구성된 Tatoeba 번역 챌린지 데이터셋 통합 버전입니다.

## 분류

- **작업**: [[번역]] — ner · readme = `The Tatoeba Translation Challenge` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `~7.3M entries.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `~7.3M entries.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `93 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `802` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `~7.3M entries.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `À noite, os pássaros não cantam.` 열 p90 3209자 ≈ 802 토큰 (viewer statistics, default/validation)
