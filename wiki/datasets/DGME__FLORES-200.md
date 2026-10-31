---
type: "dataset"
id: "DGME/FLORES-200"
source: "huggingface"
url: "https://huggingface.co/datasets/DGME/FLORES-200"
downloads: 438
summary: "DGME/FLORES-200은 다국어 기계 번역을 위한 다중 언어 텍스트 데이터셋입니다."
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
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# DGME/FLORES-200

> dataset · [Hugging Face](https://huggingface.co/datasets/DGME/FLORES-200)

DGME/FLORES-200은 다국어 기계 번역을 위한 다중 언어 텍스트 데이터셋입니다.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `features:
- name: text
dtype: string` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `features:
- name: text
dtype: string` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `17 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `24` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `language:
- en
- zh
- es
- fr
- de
- ru
- ja
- th
- sw
- te
- bn
- ar
- ko
- vi
- cs
- hu
- sr
multilinguality:
- multilingual` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `data_files:
- split: dev
path: dev/flores_af.json
- split: test
path: devtest/flores_af.json` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 96자 ≈ 24 토큰 (viewer statistics, flores_ko/test)
