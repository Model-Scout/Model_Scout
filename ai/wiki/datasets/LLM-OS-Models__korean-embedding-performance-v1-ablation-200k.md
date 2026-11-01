---
type: "dataset"
id: "LLM-OS-Models/korean-embedding-performance-v1-ablation-200k"
source: "huggingface"
url: "https://huggingface.co/datasets/LLM-OS-Models/korean-embedding-performance-v1-ablation-200k"
downloads: 27
summary: "Qwen3-Embedding-8B 한국어 임베딩 성능 비교를 위한 20만 행 연구용 데이터셋이다."
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
# LLM-OS-Models/korean-embedding-performance-v1-ablation-200k

> dataset · [Hugging Face](https://huggingface.co/datasets/LLM-OS-Models/korean-embedding-performance-v1-ablation-200k)

Qwen3-Embedding-8B 한국어 임베딩 성능 비교를 위한 20만 행 연구용 데이터셋이다.

## 분류

- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Qwen3-Embedding-8B의 한국어 retrieval continued fine-tuning에서 LoRA/DoRA/부분 및 full fine-tuning, loss, hard-negative 전략을 비교하기 위한 200,000-row 연구·비상업 성능 데이터다.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `15-task text-only blocklist를 build 안에 적용한다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `retrieval evaluation query text는 source 선언과 무관하게 차단하고` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `넓은 한국어 QA/retrieval core` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `200,000 train row와 같은 index로 source/revision/split, row hash, `trained_on_tasks`, exposure를 보존한다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
