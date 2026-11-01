---
type: "dataset"
id: "taeyun16/korean-service-query-gating-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/taeyun16/korean-service-query-gating-v1"
downloads: 57
summary: "한국어 서비스 질의 게이팅 연구용 합성 데이터셋으로, 서비스 범위 판별과 실패 유형 분석에 활용됨."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
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
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# taeyun16/korean-service-query-gating-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/taeyun16/korean-service-query-gating-v1)

한국어 서비스 질의 게이팅 연구용 합성 데이터셋으로, 서비스 범위 판별과 실패 유형 분석에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 high
- **작업**: [[문서 검색]] — metadata · task_categories = `text-retrieval` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:retrieval = `한국어 서비스 질의 게이팅 연구를 위한 합성 데이터셋입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `서비스 질의 게이팅 / 헬프데스크 질의 분류 / OOD stress evaluation` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 서비스 질의 게이팅 연구를 위한 합성 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `core/validation.jsonl` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `core/train.jsonl` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
