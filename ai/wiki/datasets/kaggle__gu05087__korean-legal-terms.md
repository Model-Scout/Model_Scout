---
type: "dataset"
id: "kaggle/gu05087/korean-legal-terms"
source: "kaggle"
url: "https://www.kaggle.com/datasets/gu05087/korean-legal-terms"
downloads: 68
summary: "한국 법률 용어와 설명을 포함한 데이터셋으로 LLM 학습 및 법률 챗봇 등에 활용 가능"
readme_status: "ok"
readme_language: "en"
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
  - "[[상업 이용 가능]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/gu05087/korean-legal-terms

> dataset · [Kaggle](https://www.kaggle.com/datasets/gu05087/korean-legal-terms)

한국 법률 용어와 설명을 포함한 데이터셋으로 LLM 학습 및 법률 챗봇 등에 활용 가능

## 분류

- **작업**: [[임베딩]] — ner · readme = `for RAG / Embedding / Chatbot` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — ner · readme = `Pretraining or fine-tuning LLMs on Korean legal domain` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Legal document summarization and Q&A` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Training embedding models and performing semantic search` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:generation, task:question_answering, task:retrieval = `Korean Legal Terms Dataset in JSONL + CSV format` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Each line is a JSON object representing a single legal term entry.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC BY-SA 4.0` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `law` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Pretraining or fine-tuning LLMs on Korean legal domain` · 신뢰도 medium
