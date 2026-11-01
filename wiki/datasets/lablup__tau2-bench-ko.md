---
type: "dataset"
id: "lablup/tau2-bench-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/lablup/tau2-bench-ko"
downloads: 79
summary: "τ²-bench v0.2.0의 retail, airline, telecom 사용자 시나리오를 한국어로 번역한 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[리랭킹]]"
  - "[[문서 검색]]"
  - "[[도구 호출]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
  - "[[교통·모빌리티]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# lablup/tau2-bench-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/lablup/tau2-bench-ko)

τ²-bench v0.2.0의 retail, airline, telecom 사용자 시나리오를 한국어로 번역한 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `278 task, 1,004 user-scenario field` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `유통 에이전트 태스크` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `τ²-bench v0.2.0의 retail·airline·telecom 사용자 시나리오를 한국어로 번역` · 신뢰도 low
- **작업**: [[도구 호출]] — tag_match · tags = `tool-use` · 신뢰도 low
- **작업**: [[번역]] — tag_match · tags = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation, task:question_answering, task:reranking, task:retrieval, task:translation = `user_scenario.persona` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:translation = `user_scenario.persona` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `유통 에이전트 태스크` · 신뢰도 low
- **도메인**: [[교통·모빌리티]] — ner · readme = `항공 에이전트 태스크` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `파일럿 30 task 검수 판정 — 승인 그룹 23건·task-field 승인 목록` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `τ²-bench 한국어 번역 공개판` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
