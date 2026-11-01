---
type: "dataset"
id: "kaggle/aikstokdata/korean-equity-daily-prices-dart-filing-impact"
source: "kaggle"
url: "https://www.kaggle.com/datasets/aikstokdata/korean-equity-daily-prices-dart-filing-impact"
downloads: 71
summary: "한국 상장기업 일별 종가와 DART 공시가 주가에 미치는 영향을 분석한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/aikstokdata/korean-equity-daily-prices-dart-filing-impact

> dataset · [Kaggle](https://www.kaggle.com/datasets/aikstokdata/korean-equity-daily-prices-dart-filing-impact)

한국 상장기업 일별 종가와 DART 공시가 주가에 미치는 영향을 분석한 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `filing_impact_summary.csv carries the same breakdown per filing type (filings_pre_open, h0_identified_pct, ...) so you can see which rows are worth reading at a` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Daily settled closes for 2,787 Korean listed companies (KOSPI, KOSDAQ and KONEX) over the 321 trading days to 2026-09-17, plus a table of what those stocks did ` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `The four CSVs here are a dated extract of the 2026-09-18 publish (prices through 2026-09-17).` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `filing_impact_summary.csv carries the same breakdown per filing type (filings_pre_open, h0_identified_pct, ...) so you can see which rows are worth reading at a` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `Other (specified in description)` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The four CSVs here are a dated extract of the 2026-09-18 publish (prices through 2026-09-17).` · 신뢰도 low
