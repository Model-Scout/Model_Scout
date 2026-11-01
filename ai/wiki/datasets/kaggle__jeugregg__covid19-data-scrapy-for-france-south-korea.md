---
type: "dataset"
id: "kaggle/jeugregg/covid19-data-scrapy-for-france-south-korea"
source: "kaggle"
url: "https://www.kaggle.com/datasets/jeugregg/covid19-data-scrapy-for-france-south-korea"
downloads: 121
summary: "프랑스와 한국의 COVID-19 확진자 및 사망자 데이터를 스크래핑한 자료입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/jeugregg/covid19-data-scrapy-for-france-south-korea

> dataset · [Kaggle](https://www.kaggle.com/datasets/jeugregg/covid19-data-scrapy-for-france-south-korea)

프랑스와 한국의 COVID-19 확진자 및 사망자 데이터를 스크래핑한 자료입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Results of scrapy : Data of COVID-19 confirmed cases & deaths` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Try to scrap data from official website of South Korea & France linked to COVID-19 confirmed cases and death in 2020` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:retrieval = `South Korea areas data are retrieved with scrapy from online KCDC Press Release articles` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Results of scrapy : Data of COVID-19 confirmed cases & deaths` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[의료·보건]] — ner · readme = `COVID-19 comfirmed cases & death from differents sources` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Script to scrap data (France Publique Santé et South Korean KCDC)` · 신뢰도 low
