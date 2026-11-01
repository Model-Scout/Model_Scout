---
type: "dataset"
id: "kaggle/sangbepa/korean-game-companies-financials-2025-2026"
source: "kaggle"
url: "https://www.kaggle.com/datasets/sangbepa/korean-game-companies-financials-2025-2026"
downloads: 16
summary: "한국 상장 게임사 8곳의 재무 데이터를 비교 분석한 공개 DART 기반 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
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
# kaggle/sangbepa/korean-game-companies-financials-2025-2026

> dataset · [Kaggle](https://www.kaggle.com/datasets/sangbepa/korean-game-companies-financials-2025-2026)

한국 상장 게임사 8곳의 재무 데이터를 비교 분석한 공개 DART 기반 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Open DART financial comparison of eight listed Korean game publishers` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Open DART financial comparison of eight listed Korean game publishers` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `Includes company metadata, comparable consolidated financial figures, filing provenance, and a data dictionary.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Includes company metadata, comparable consolidated financial figures, filing provenance, and a data dictionary.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `Other (specified in description)` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `An independently prepared, transformed extract of public filings from Open DART.` · 신뢰도 low
