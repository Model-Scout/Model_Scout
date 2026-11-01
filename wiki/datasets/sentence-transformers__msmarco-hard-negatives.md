---
type: "dataset"
id: "sentence-transformers/msmarco-hard-negatives"
source: "huggingface"
url: "https://huggingface.co/datasets/sentence-transformers/msmarco-hard-negatives"
downloads: 728
summary: "MS MARCO 실제 검색 쿼리 기반 정보 검색용 하드 네거티브 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# sentence-transformers/msmarco-hard-negatives

> dataset · [Hugging Face](https://huggingface.co/datasets/sentence-transformers/msmarco-hard-negatives)

MS MARCO 실제 검색 쿼리 기반 정보 검색용 하드 네거티브 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `This dataset repository contains files that are helpful to train bi-encoder models e.g. using sentence-transformers.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `MS MARCO is a large scale information retrieval corpus that was created based on real user search queries using Bing search engine.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding, task:retrieval = `text` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MS MARCO is a large scale information retrieval corpus that was created based on real user search queries using Bing search engine.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This dataset repository contains files that are helpful to train bi-encoder models e.g. using sentence-transformers.` · 신뢰도 medium

## 이 데이터로 학습한 모델

- [[antoinelouis__colbert-xm|antoinelouis/colbert-xm]]
