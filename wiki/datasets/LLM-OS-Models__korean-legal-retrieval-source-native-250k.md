---
type: "dataset"
id: "LLM-OS-Models/korean-legal-retrieval-source-native-250k"
source: "huggingface"
url: "https://huggingface.co/datasets/LLM-OS-Models/korean-legal-retrieval-source-native-250k"
downloads: 15
summary: "Legalize-KR의 법령·행정규칙·판례·자치법규 구조에서 추출한 25만 행 한국어 법률 검색 데이터셋이다."
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
  - "[[법률]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# LLM-OS-Models/korean-legal-retrieval-source-native-250k

> dataset · [Hugging Face](https://huggingface.co/datasets/LLM-OS-Models/korean-legal-retrieval-source-native-250k)

Legalize-KR의 법령·행정규칙·판례·자치법규 구조에서 추출한 25만 행 한국어 법률 검색 데이터셋이다.

## 분류

- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `250,000-row 한국어 retrieval dataset이다` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `법령명+조문 → 조문 본문` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `법령명+조문 → 조문 본문` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[법률]] — ner · readme = `Legalize-KR의 법령·행정규칙·판례·자치법규 구조에서` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `target-adapted 연구·비상업 성능 shard이며` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
