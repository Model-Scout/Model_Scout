---
type: "dataset"
id: "gyung/ko-legal-retriever-repair-data-20260622"
source: "huggingface"
url: "https://huggingface.co/datasets/gyung/ko-legal-retriever-repair-data-20260622"
downloads: 36
summary: "한국 법률 검색 도구 사용을 위한 JSON 도구 액션 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 검색]]"
  - "[[도구 호출]]"
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
---
# gyung/ko-legal-retriever-repair-data-20260622

> dataset · [Hugging Face](https://huggingface.co/datasets/gyung/ko-legal-retriever-repair-data-20260622)

한국 법률 검색 도구 사용을 위한 JSON 도구 액션 학습용 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — tag_match · tags = `retrieval` · 신뢰도 low
- **작업**: [[도구 호출]] — tag_match · readme, tags = `tool-use` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:retrieval = `Each JSONL row contains: - `messages`: chat messages ending with a target assistant JSON action.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The rows are intended to train a model to emit JSON tool actions` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset bundle contains SFT rows` · 신뢰도 medium
