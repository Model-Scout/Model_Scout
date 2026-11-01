---
type: "dataset"
id: "open-travel/japan-travel-mcp-data"
source: "huggingface"
url: "https://huggingface.co/datasets/open-travel/japan-travel-mcp-data"
downloads: 3691
summary: "일본 47개 현과 1,938개 지방자치단체의 공공 관광 데이터를 AI 에이전트용으로 구축한 종합 여행 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[리랭킹]]"
  - "[[문서 검색]]"
  - "[[번역]]"
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
  - "[[문화·관광]]"
  - "[[지리·위치]]"
dataset_role:
  - "[[서비스 데이터]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# open-travel/japan-travel-mcp-data

> dataset · [Hugging Face](https://huggingface.co/datasets/open-travel/japan-travel-mcp-data)

일본 47개 현과 1,938개 지방자치단체의 공공 관광 데이터를 AI 에이전트용으로 구축한 종합 여행 데이터입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Comprehensive Japanese travel data for AI agents` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `Comprehensive Japanese travel data for AI agents` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 medium
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:reranking, task:retrieval, task:translation = `Japan's tourism information — created to reach the world — is published across thousands of municipal websites.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `17 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — tag_match · readme, tags = `tourism` · 신뢰도 medium
- **도메인**: [[지리·위치]] — ner · readme = `covering all 47 prefectures and 1,938 local government entities` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `The npm package downloads this dataset on first run.` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
