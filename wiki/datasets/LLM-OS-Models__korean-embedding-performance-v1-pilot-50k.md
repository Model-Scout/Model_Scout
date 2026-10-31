---
type: "dataset"
id: "LLM-OS-Models/korean-embedding-performance-v1-pilot-50k"
source: "huggingface"
url: "https://huggingface.co/datasets/LLM-OS-Models/korean-embedding-performance-v1-pilot-50k"
downloads: 41
summary: "한국어 임베딩 성능 실험용 50,000행 대조 데이터셋으로, 검색 성능 평가에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
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
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# LLM-OS-Models/korean-embedding-performance-v1-pilot-50k

> dataset · [Hugging Face](https://huggingface.co/datasets/LLM-OS-Models/korean-embedding-performance-v1-pilot-50k)

한국어 임베딩 성능 실험용 50,000행 대조 데이터셋으로, 검색 성능 평가에 사용됨.

## 분류

- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `각 row는 instruction-aware query, positive passage 1개, hard/easy negative passage 1–7개를 ms-swift embedding message schema로 저장한다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `각 row는 instruction-aware query, positive passage 1개, hard/easy negative passage 1–7개를 ms-swift embedding message schema로 저장한다.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Qwen3-Embedding 계열의 한국어 retrieval 성능 실험을 위한 50,000-row 연구용 contrastive dataset이다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `이 데이터는 공식 benchmark의 train/task-family 데이터를 의도적으로 포함한다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
