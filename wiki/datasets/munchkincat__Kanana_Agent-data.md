---
type: "dataset"
id: "munchkincat/Kanana_Agent-data"
source: "huggingface"
url: "https://huggingface.co/datasets/munchkincat/Kanana_Agent-data"
downloads: 8
summary: "Kanana Agent 멀티 에이전트 시스템에서 사용하는 법률, 뉴스, 금융 트렌드 벡터 DB 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[금융·경제]]"
  - "[[법률]]"
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# munchkincat/Kanana_Agent-data

> dataset · [Hugging Face](https://huggingface.co/datasets/munchkincat/Kanana_Agent-data)

Kanana Agent 멀티 에이전트 시스템에서 사용하는 법률, 뉴스, 금융 트렌드 벡터 DB 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — tag_match · readme, tags = `rag` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `법률 문서 벡터 DB` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `법률 문서 벡터 DB` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **도메인**: [[법률]] — ner · readme = `Legal Agent — 법률 RAG DB` · 신뢰도 medium
- **도메인**: [[뉴스·미디어]] — ner · readme = `News Agent — 뉴스 Vector DB` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Kanana Agent 멀티 에이전트 시스템에서 사용하는 사전 수집 데이터입니다.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
