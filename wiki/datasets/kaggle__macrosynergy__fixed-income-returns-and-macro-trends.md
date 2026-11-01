---
type: "dataset"
id: "kaggle/macrosynergy/fixed-income-returns-and-macro-trends"
source: "kaggle"
url: "https://www.kaggle.com/datasets/macrosynergy/fixed-income-returns-and-macro-trends"
downloads: 1924
summary: "JPMaQS Quantamental Indicators는 거시경제 지표를 활용한 정량적 투자 전략 개발용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[시계열 예측]]"
  - "[[문서 검색]]"
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
  - "[[조건부 이용]]"
domain:
  - "[[금융·경제]]"
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/macrosynergy/fixed-income-returns-and-macro-trends

> dataset · [Kaggle](https://www.kaggle.com/datasets/macrosynergy/fixed-income-returns-and-macro-trends)

JPMaQS Quantamental Indicators는 거시경제 지표를 활용한 정량적 투자 전략 개발용 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `JPMaQS is a service that makes it easy to use quantitative-fundamental (quantamental) information for algorithmic trading` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `The system allows for quick and cost-efficient backtesting of macro quantamental investment strategies` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `JPMaQS data are usually available in panels, with one type of indicator (category) being available for a range of currency areas` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:retrieval = `text` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `The example dataset contains a small selection of quantamental indicators` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `Data files © Original Authors` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **도메인**: [[일반]] — ner · readme = `Macrosynergy is dedicated to promoting economic knowledge to benefit the broader community` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The example dataset contains a small selection of quantamental indicators` · 신뢰도 low
