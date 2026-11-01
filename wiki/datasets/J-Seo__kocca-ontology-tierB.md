---
type: "dataset"
id: "J-Seo/kocca-ontology-tierB"
source: "huggingface"
url: "https://huggingface.co/datasets/J-Seo/kocca-ontology-tierB"
downloads: 107
summary: "국립국어원 4대 한국어 언어자원을 통합한 170만 표제어 SQLite 데이터셋입니다."
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
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# J-Seo/kocca-ontology-tierB

> dataset · [Hugging Face](https://huggingface.co/datasets/J-Seo/kocca-ontology-tierB)

국립국어원 4대 한국어 언어자원을 통합한 170만 표제어 SQLite 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `한국어 4대 언어자원(표준국어대사전·우리말샘·한국어기초사전·어문 규범)을 단일 SQLite로 통합한 170만 표제어 데이터셋입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `검색·조회에 최적화된 단일 SQLite 파일로 제공합니다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 4대 언어자원(표준국어대사전·우리말샘·한국어기초사전·어문 규범)을 단일 SQLite로 통합한 170만 표제어 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `본 데이터셋은 국립국어원이 공개한 4개 한국어 언어자원을 통합·정규화하여 검색·조회에 최적화된 단일 SQLite 파일로 제공합니다.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
