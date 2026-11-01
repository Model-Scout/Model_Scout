---
type: "dataset"
id: "LLM-OS-Models2/ko-legal-embedding-training-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/LLM-OS-Models2/ko-legal-embedding-training-v1"
downloads: 23
summary: "한국어 공공 법률 임베딩 학습용 파생 JSONL 데이터셋으로 임베딩 모델 학습에 사용됨."
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
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# LLM-OS-Models2/ko-legal-embedding-training-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/LLM-OS-Models2/ko-legal-embedding-training-v1)

한국어 공공 법률 임베딩 학습용 파생 JSONL 데이터셋으로 임베딩 모델 학습에 사용됨.

## 분류

- **작업**: [[임베딩]] — metadata · readme, task_categories = `sentence-similarity` · 신뢰도 high
- **작업**: [[문서 검색]] — metadata · task_categories = `text-retrieval` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `source-native query/positive 관계와 deterministic bootstrap negative로 컴파일했다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `실제 embedding 학습 queue가 소비하는 provenance-preserving 파생 JSONL이다.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[법률]] — ner · readme = `Korean Public Legal Embedding Training v1` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `use: public redistribution and model training` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
