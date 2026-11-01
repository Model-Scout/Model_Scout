---
type: "dataset"
id: "gykwak03/KISS_delirium_papaers"
source: "huggingface"
url: "https://huggingface.co/datasets/gykwak03/KISS_delirium_papaers"
downloads: 10
summary: "KISS에서 'delirium' 검색으로 얻은 논문 초록 데이터셋입니다."
readme_status: "thin"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
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
  - "[[학술·논문]]"
  - "[[의료·보건]]"
dataset_role:
  - "[[서비스 데이터]]"
---
# gykwak03/KISS_delirium_papaers

> dataset · [Hugging Face](https://huggingface.co/datasets/gykwak03/KISS_delirium_papaers)

KISS에서 'delirium' 검색으로 얻은 논문 초록 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `derived from a search for “delirium” in KISS (Koreanstudies Information Service System)` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:retrieval = `abstract of a paper` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `abstract in Korean, and "en_data.csv" is abstract in English` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `This is an abstract of a paper derived from a search for “delirium” in KISS (Koreanstudies Information Service System)` · 신뢰도 medium
- **도메인**: [[의료·보건]] — tag_match · tags = `medical` · 신뢰도 medium
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `derived from a search for “delirium” in KISS (Koreanstudies Information Service System)` · 신뢰도 medium
