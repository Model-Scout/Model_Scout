---
type: "dataset"
id: "LLM-OS-Models/korean-embedding-benchmark-blocklist-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/LLM-OS-Models/korean-embedding-benchmark-blocklist-v1"
downloads: 30
summary: "한국어 임베딩 평가용 SHA-256 블록리스트로 학습 데이터 제외에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
---
# LLM-OS-Models/korean-embedding-benchmark-blocklist-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/LLM-OS-Models/korean-embedding-benchmark-blocklist-v1)

한국어 임베딩 평가용 SHA-256 블록리스트로 학습 데이터 제외에 사용됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Korean Embedding Benchmark Blocklist v1` · 신뢰도 medium
- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:retrieval = `query/document/evaluation text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Sionic Korean retrieval 9종과 공식 MTEB(kor, v1) 6종의 평가 입력` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `평가 전용 SHA-256 blocklist다.` · 신뢰도 medium
