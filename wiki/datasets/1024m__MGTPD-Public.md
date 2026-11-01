---
type: "dataset"
id: "1024m/MGTPD-Public"
source: "huggingface"
url: "https://huggingface.co/datasets/1024m/MGTPD-Public"
downloads: 37
summary: "다국어 기계 생성 텍스트 부분 탐지용 토큰 분류 데이터셋으로 AI 텍스트 검출에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[정보 추출]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# 1024m/MGTPD-Public

> dataset · [Hugging Face](https://huggingface.co/datasets/1024m/MGTPD-Public)

다국어 기계 생성 텍스트 부분 탐지용 토큰 분류 데이터셋으로 AI 텍스트 검출에 활용됨.

## 분류

- **작업**: [[정보 추출]] — metadata · readme, task_categories = `token-classification` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction = `The dataset is suitable for machine-generated text portion detection, token classification tasks` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The dataset is suitable for machine-generated text portion detection, token classification tasks` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `23 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-nd-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The dataset is suitable for machine-generated text portion detection, token classification tasks, and other linguistic tasks.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `We have evaluated over our test set as well as other pre-existing benchmarks in 3 formats` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The model was trained on a dataset consisting of approximately 2.4M text samples from various LLMs.` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
