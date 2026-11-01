---
type: "dataset"
id: "LLM-OS-Models/korean-embedding-performance-v1-performance-1m"
source: "huggingface"
url: "https://huggingface.co/datasets/LLM-OS-Models/korean-embedding-performance-v1-performance-1m"
downloads: 28
summary: "Qwen3-Embedding-8B 한국어 임베딩 성능 실험용 100만 행 대비 연구용 대조 데이터셋입니다."
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
  - "[[대규모 데이터]]"
---
# LLM-OS-Models/korean-embedding-performance-v1-performance-1m

> dataset · [Hugging Face](https://huggingface.co/datasets/LLM-OS-Models/korean-embedding-performance-v1-performance-1m)

Qwen3-Embedding-8B 한국어 임베딩 성능 실험용 100만 행 대비 연구용 대조 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Qwen3-Embedding-8B의 한국어 retrieval data-scale 실험을 위한 정확히 1,000,000-row 연구·비상업 contrastive dataset이다.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `retrieval evaluation query text는 모든 source에서 차단하고, non-retrieval task는 source가 같은 `trained_on_tasks`를 명시한 공식 train-family text만 expected exposure로 허용한다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `retrieval evaluation query text는 모든 source에서 차단하고, non-retrieval task는 source가 같은 `trained_on_tasks`를 명시한 공식 train-family text만 expected exposure로 허용한다.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `넓은 한국어 QA/retrieval core` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `공식 train/task-family source를 의도적으로 포함하므로 완전한 zero-shot 데이터가 아니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
