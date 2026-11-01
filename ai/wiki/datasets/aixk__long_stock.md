---
type: "dataset"
id: "aixk/long_stock"
source: "huggingface"
url: "https://huggingface.co/datasets/aixk/long_stock"
downloads: 86
summary: "주식 시계열 데이터와 기술적 지표를 포함한 투자 연구용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[시계열 예측]]"
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# aixk/long_stock

> dataset · [Hugging Face](https://huggingface.co/datasets/aixk/long_stock)

주식 시계열 데이터와 기술적 지표를 포함한 투자 연구용 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `Targets: forward returns at 1, 5 and 20 bars` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — ner · readme = `20 bar 라벨이 완성된 시간 순서 분할` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · modality, readme, task:tabular_prediction = `수집된 전체 bar와 계산 특징` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Targets: forward returns at 1, 5 and 20 bars` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `train.csv, validation.csv, test.csv: 20 bar 라벨이 완성된 시간 순서 분할` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
