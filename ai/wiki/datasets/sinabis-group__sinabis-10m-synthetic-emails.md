---
type: "dataset"
id: "sinabis-group/sinabis-10m-synthetic-emails"
source: "huggingface"
url: "https://huggingface.co/datasets/sinabis-group/sinabis-10m-synthetic-emails"
downloads: 238
summary: "가상의 친환경 에너지 그룹의 10년간 1천만 건 이상의 합성 이메일과 일정 데이터를 포함한 대규모 비즈니스 통신 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[문서 검색]]"
  - "[[요약]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# sinabis-group/sinabis-10m-synthetic-emails

> dataset · [Hugging Face](https://huggingface.co/datasets/sinabis-group/sinabis-10m-synthetic-emails)

가상의 친환경 에너지 그룹의 10년간 1천만 건 이상의 합성 이메일과 일정 데이터를 포함한 대규모 비즈니스 통신 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — metadata · tags, task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · tags, task_categories = `token-classification` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `More than 10 million emails and 1.4 million calendar files from the everyday business of a fictional renewable-energy group.` · 신뢰도 low
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding, task:generation, task:information_extraction, task:retrieval, task:summarization = `More than 10 million emails and 1.4 million calendar files from the everyday business of a fictional renewable-energy group.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:summarization = `The content was written by large language models, and the mailgen generator built the structure around it.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `29 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `More than 10 million emails and 1.4 million calendar files from the everyday business of a fictional renewable-energy group.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The content was written by large language models, and the mailgen generator built the structure around it.` · 신뢰도 low
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high
