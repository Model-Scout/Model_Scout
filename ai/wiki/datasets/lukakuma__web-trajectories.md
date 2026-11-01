---
type: "dataset"
id: "lukakuma/web-trajectories"
source: "huggingface"
url: "https://huggingface.co/datasets/lukakuma/web-trajectories"
downloads: 72
summary: "웹 에이전트의 성공적인 DOM 기반 웹 탐색 세션 기록 데이터셋으로, 웹 에이전트 벤치마크 평가에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[리랭킹]]"
  - "[[문서 검색]]"
  - "[[도구 호출]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# lukakuma/web-trajectories

> dataset · [Hugging Face](https://huggingface.co/datasets/lukakuma/web-trajectories)

웹 에이전트의 성공적인 DOM 기반 웹 탐색 세션 기록 데이터셋으로, 웹 에이전트 벤치마크 평가에 사용됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Every LLM call keeps the exact input messages and the exact output blocks of the agent model` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `benchmark judge marked successful and that finished normally (exit 0, no timeout, not blocked)` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Raw trajectories of an in-house DOM-based, tool-calling web agent, recorded while it ran public web-agent benchmarks` · 신뢰도 low
- **작업**: [[도구 호출]] — tag_match · tags = `tool-calling` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation, task:reranking, task:retrieval = `Every LLM call keeps the exact input messages and the exact output blocks of the agent model` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Every LLM call keeps the exact input messages and the exact output blocks of the agent model` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `public web-agent benchmarks on one host` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This repo holds sessions that the benchmark judge marked successful and that finished normally` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
