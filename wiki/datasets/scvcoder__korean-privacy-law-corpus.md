---
type: "dataset"
id: "scvcoder/korean-privacy-law-corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/scvcoder/korean-privacy-law-corpus"
downloads: 87
summary: "한국 개인정보보호법 관련 가이드와 상담사례를 의미 단위로 청킹해 RAG에 활용하는 코퍼스입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
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
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# scvcoder/korean-privacy-law-corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/scvcoder/korean-privacy-law-corpus)

한국 개인정보보호법 관련 가이드와 상담사례를 의미 단위로 청킹해 RAG에 활용하는 코퍼스입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `모든 청크에는 Contextual Retrieval 기법을 적용한 chunk_context 필드가 포함되어 있어, 임베딩 검색 정확도를 즉시 끌어올릴 수 있습니다.` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:generation, task:question_answering, task:retrieval = `형식 | JSON Lines (`.jsonl`)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `RAG(Retrieval-Augmented Generation)에 바로 쓸 수 있도록 의미 단위 청킹·문맥 보강한 코퍼스입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Semantic Chunking 및 Contextual Retrieval 기법으로 작성한 맥락 요약, 표준화 스키마는 본 데이터셋 기여자의 2차 저작물이며, 위와 동일 조건으로 이용 가능합니다.` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
