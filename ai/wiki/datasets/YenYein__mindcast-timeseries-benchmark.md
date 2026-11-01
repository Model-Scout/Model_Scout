---
type: "dataset"
id: "YenYein/mindcast-timeseries-benchmark"
source: "huggingface"
url: "https://huggingface.co/datasets/YenYein/mindcast-timeseries-benchmark"
downloads: 116
summary: "MINDCAST 시계열 예측 결과 데이터로 1~6개월 예측 성능 평가에 활용됨"
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[시계열 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# YenYein/mindcast-timeseries-benchmark

> dataset · [Hugging Face](https://huggingface.co/datasets/YenYein/mindcast-timeseries-benchmark)

MINDCAST 시계열 예측 결과 데이터로 1~6개월 예측 성능 평가에 활용됨

## 분류

- **작업**: [[시계열 예측]] — tag_match · readme, tags = `forecasting` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — ner · readme, task:forecasting = `MINDCAST 예측 결과 — 1·2·3·6개월` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — ner · readme, task:forecasting = `예측값 133,164행` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MINDCAST Monthly Time Series Benchmark Results` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `4,932개 예측 실험, 예측값 133,164행, 미해결 오류 0건` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
