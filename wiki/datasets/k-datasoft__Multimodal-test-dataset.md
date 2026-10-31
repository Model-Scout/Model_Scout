---
type: "dataset"
id: "k-datasoft/Multimodal-test-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/k-datasoft/Multimodal-test-dataset"
downloads: 23
summary: "KRX 주식시장 투자주의종목 지정 예측을 위한 OHLCV 시계열과 한국어 뉴스 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[시계열 예측]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# k-datasoft/Multimodal-test-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/k-datasoft/Multimodal-test-dataset)

KRX 주식시장 투자주의종목 지정 예측을 위한 OHLCV 시계열과 한국어 뉴스 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 high
- **작업**: [[시계열 예측]] — metadata · task_categories = `time-series-forecasting` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Korean news text (title + body)` · 신뢰도 high
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — ner · readme, task:forecasting = `raw daily OHLCV price data` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Binary classification` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **도메인**: [[뉴스·미디어]] — tag_match · tags = `news` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `This dataset is a test dataset for predicting Investment Warning (투자주의종목) designations` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
