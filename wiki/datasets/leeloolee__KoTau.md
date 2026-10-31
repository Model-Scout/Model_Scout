---
type: "dataset"
id: "leeloolee/KoTau"
source: "huggingface"
url: "https://huggingface.co/datasets/leeloolee/KoTau"
downloads: 93
summary: "한국 여행사 벤치마크 KoTAU 개발용 데이터로, 철도, 숙박, 버스, 관광지 정보 포함."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[문서 검색]]"
  - "[[도구 호출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[교통·모빌리티]]"
dataset_role:
  - "[[학습용]]"
---
# leeloolee/KoTau

> dataset · [Hugging Face](https://huggingface.co/datasets/leeloolee/KoTau)

한국 여행사 벤치마크 KoTAU 개발용 데이터로, 철도, 숙박, 버스, 관광지 정보 포함.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `Working data for KoTAU, a Korean travel agent benchmark.` · 신뢰도 low
- **작업**: [[도구 호출]] — tag_match · tags = `tool-use` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:retrieval = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[교통·모빌리티]] — ner · readme = `data/rail/ Stations, schedules, fares, inventory, booking state` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Working data for KoTAU, a Korean travel agent benchmark.` · 신뢰도 low
