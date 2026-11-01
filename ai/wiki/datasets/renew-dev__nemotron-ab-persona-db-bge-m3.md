---
type: "dataset"
id: "renew-dev/nemotron-ab-persona-db-bge-m3"
source: "huggingface"
url: "https://huggingface.co/datasets/renew-dev/nemotron-ab-persona-db-bge-m3"
downloads: 15
summary: "19~59세 한국인 66만여 페르소나를 BAAI/bge-m3 임베딩한 벡터 DB로 A/B 시뮬레이션용입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# renew-dev/nemotron-ab-persona-db-bge-m3

> dataset · [Hugging Face](https://huggingface.co/datasets/renew-dev/nemotron-ab-persona-db-bge-m3)

19~59세 한국인 66만여 페르소나를 BAAI/bge-m3 임베딩한 벡터 DB로 A/B 시뮬레이션용입니다.

## 분류

- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 high
- **작업**: [[문서 검색]] — ner · readme = `Ready-to-query for Korean A/B persona simulation.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:retrieval = `한국어 단문/이미지 A/B 변형을 합성 페르소나에 노출시켜` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `LLM 으로 시뮬레이션 평가하는 nemotron-ab…` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `마케팅·UI 카피·공지 등 한국어 단문/이미지 A/B 변형을 합성 페르소나에 노출시켜 LLM 으로 시뮬레이션 평가하는 nemotron-ab…` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
