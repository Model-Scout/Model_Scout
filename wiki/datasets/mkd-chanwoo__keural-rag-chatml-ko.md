---
type: "dataset"
id: "mkd-chanwoo/keural-rag-chatml-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/mkd-chanwoo/keural-rag-chatml-ko"
downloads: 25
summary: "한국어 웹문서 기반 RAG QA 데이터셋으로 문서 기반 답변 학습용입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
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
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# mkd-chanwoo/keural-rag-chatml-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/mkd-chanwoo/keural-rag-chatml-ko)

한국어 웹문서 기반 RAG QA 데이터셋으로 문서 기반 답변 학습용입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — tag_match · readme, tags = `question-answering` · 신뢰도 medium
- **작업**: [[문서 검색]] — tag_match · tags = `rag` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:retrieval = `ChatML 형식으로 변환되었습니다. 소스 문서(`text`)가 질문(`question`) 앞에 붙어 user 턴에 포함됩니다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = ``answer` → assistant 턴으로 변환` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 웹문서(뉴스, 블로그, 지식백과 등)를 시드로` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `SFT 학습용 ChatML 포맷으로 전처리한` · 신뢰도 medium
