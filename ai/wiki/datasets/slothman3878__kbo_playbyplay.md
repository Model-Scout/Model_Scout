---
type: "dataset"
id: "slothman3878/kbo_playbyplay"
source: "huggingface"
url: "https://huggingface.co/datasets/slothman3878/kbo_playbyplay"
downloads: 366
summary: "NAVER Sports 문자중계 기반 KBO 2023-2026 시즌 경기별 투구 및 플레이 기록 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[문서 검색]]"
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# slothman3878/kbo_playbyplay

> dataset · [Hugging Face](https://huggingface.co/datasets/slothman3878/kbo_playbyplay)

NAVER Sports 문자중계 기반 KBO 2023-2026 시즌 경기별 투구 및 플레이 기록 데이터입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `A Statcast/Retrosheet-style representation of KBO games: pitches, plate-appearance outcomes, base-out state and the transitions between them.` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — metadata · task_categories = `tabular-regression` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality, task:tabular_prediction = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `derived from NAVER Sports 문자중계` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `A Statcast/Retrosheet-style representation of KBO games: pitches, plate-appearance outcomes, base-out state and the transitions between them.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `11` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A Statcast/Retrosheet-style representation of KBO games` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `game_pk` 열 p90 17자 ≈ 11 토큰 (viewer statistics, default/train)
