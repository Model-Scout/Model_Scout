---
type: "dataset"
id: "KGENOTS/korea-lotto-first-prize"
source: "huggingface"
url: "https://huggingface.co/datasets/KGENOTS/korea-lotto-first-prize"
downloads: 13
summary: "대한민국 로또 6/45 1등 평균 실수령액 연도별 시계열 데이터로 경제 분석에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[시계열 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[서비스 데이터]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# KGENOTS/korea-lotto-first-prize

> dataset · [Hugging Face](https://huggingface.co/datasets/KGENOTS/korea-lotto-first-prize)

대한민국 로또 6/45 1등 평균 실수령액 연도별 시계열 데이터로 경제 분석에 활용됨.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `로또 6/45 1등 평균 실수령액 연도별 시계열 (대한민국)` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · modality, readme = `Columns… See the full description on the dataset page` · 신뢰도 high
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Columns… See the full description on the dataset page` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `로또 6/45 1등 평균 실수령액 연도별 시계열 (대한민국)` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `This repository is a mirror of the CSV published there.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
