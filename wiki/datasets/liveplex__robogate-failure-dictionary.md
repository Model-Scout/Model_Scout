---
type: "dataset"
id: "liveplex/robogate-failure-dictionary"
source: "huggingface"
url: "https://huggingface.co/datasets/liveplex/robogate-failure-dictionary"
downloads: 143
summary: "NVIDIA Isaac Sim 시뮬레이션 기반 4개 로봇 픽앤플레이스 실패 패턴 데이터베이스입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# liveplex/robogate-failure-dictionary

> dataset · [Hugging Face](https://huggingface.co/datasets/liveplex/robogate-failure-dictionary)

NVIDIA Isaac Sim 시뮬레이션 기반 4개 로봇 픽앤플레이스 실패 패턴 데이터베이스입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `robot AI failure patterns` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Two-Stage Adaptive Sampling` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `structured database of robot AI failure patterns` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:retrieval = `robot AI failure patterns collected from NVIDIA Isaac Sim physical simulations` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `records the exact conditions under which a robot succeeded or failed at Pick & Place tasks` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `robot AI failure patterns collected from NVIDIA Isaac Sim physical simulations` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `A structured database of robot AI failure patterns collected from NVIDIA Isaac Sim physical simulations` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
