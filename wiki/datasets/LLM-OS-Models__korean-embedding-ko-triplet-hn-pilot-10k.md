---
type: "dataset"
id: "LLM-OS-Models/korean-embedding-ko-triplet-hn-pilot-10k"
source: "huggingface"
url: "https://huggingface.co/datasets/LLM-OS-Models/korean-embedding-ko-triplet-hn-pilot-10k"
downloads: 16
summary: "한국어 임베딩 학습용 hard-negative 포함 10,000행 검색 데이터셋으로 연구용임."
readme_status: "ok"
readme_language: "en"
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
  - "[[중규모 데이터]]"
---
# LLM-OS-Models/korean-embedding-ko-triplet-hn-pilot-10k

> dataset · [Hugging Face](https://huggingface.co/datasets/LLM-OS-Models/korean-embedding-ko-triplet-hn-pilot-10k)

한국어 임베딩 학습용 hard-negative 포함 10,000행 검색 데이터셋으로 연구용임.

## 분류

- **작업**: [[임베딩]] — metadata · readme, task_categories = `sentence-similarity` · 신뢰도 high
- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `한국어 retrieval train 10,000행과 validation 512행에 Qwen3-Embedding-8B dense hard negative 4개씩을 붙인 연구용 ms-swift embedding dataset이다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `한국어 retrieval train 10,000행과 validation 512행에 Qwen3-Embedding-8B dense hard negative 4개씩을 붙인 연구용 ms-swift embedding dataset이다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 retrieval train 10,000행과 validation 512행에 Qwen3-Embedding-8B dense hard negative 4개씩을 붙인 연구용 ms-swift embedding dataset이다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `한국어 retrieval train 10,000행과 validation 512행에 Qwen3-Embedding-8B dense hard negative 4개씩을 붙인 연구용 ms-swift embedding dataset이다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
