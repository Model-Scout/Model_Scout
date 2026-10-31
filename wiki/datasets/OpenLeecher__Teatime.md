---
type: "dataset"
id: "OpenLeecher/Teatime"
source: "huggingface"
url: "https://huggingface.co/datasets/OpenLeecher/Teatime"
downloads: 363
summary: "OpenLeecher/Teatime는 대화 로그를 파싱한 데이터로 대화 분석에 활용됩니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[리랭킹]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# OpenLeecher/Teatime

> dataset · [Hugging Face](https://huggingface.co/datasets/OpenLeecher/Teatime)

OpenLeecher/Teatime는 대화 로그를 파싱한 데이터로 대화 분석에 활용됩니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Average chat token length: 4246.03` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `Every change creates a fresh branch, copying all earlier messages.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Every user edit or message regeneration makes a new branch in the conversation tree.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:generation, task:reranking, task:retrieval = `Every user edit or message regeneration makes a new branch in the conversation tree.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Every user edit or message regeneration makes a new branch in the conversation tree.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `These are the parsed logs from the "teatime logs" xlsx files.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `These are the parsed logs from the "teatime logs" xlsx files.` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
