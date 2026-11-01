---
type: "dataset"
id: "aikstockdata/korea-equity-daily"
source: "huggingface"
url: "https://huggingface.co/datasets/aikstockdata/korea-equity-daily"
downloads: 1150
summary: "한국 상장기업 2,787종목의 321거래일 확정 종가·거래량과 DART 공시 영향 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[시계열 예측]]"
  - "[[문서 검색]]"
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# aikstockdata/korea-equity-daily

> dataset · [Hugging Face](https://huggingface.co/datasets/aikstockdata/korea-equity-daily)

한국 상장기업 2,787종목의 321거래일 확정 종가·거래량과 DART 공시 영향 데이터입니다.

## 분류

- **작업**: [[시계열 예측]] — metadata · readme, task_categories = `time-series-forecasting` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `plus a table of what stocks did after each type of regulatory filing` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — metadata · readme, task_categories = `tabular-regression` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — ner · modality, readme, task:tabular_prediction = `Daily settled closes for 2,787 Korean listed companies` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `plus a table of what stocks did after each type of regulatory filing` · 신뢰도 high
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Daily settled closes for 2,787 Korean listed companies` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `4` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This is the same data, already joined, as plain CSV — no key and no registration.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `code` 열 p90 6자 ≈ 4 토큰 (viewer statistics, daily_prices/train)
