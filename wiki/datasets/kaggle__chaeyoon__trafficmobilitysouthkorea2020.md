---
type: "dataset"
id: "kaggle/chaeyoon/trafficmobilitysouthkorea2020"
source: "kaggle"
url: "https://www.kaggle.com/datasets/chaeyoon/trafficmobilitysouthkorea2020"
downloads: 136
summary: "한국도로공사에서 제공하는 2020년 한국 고속도로 일별 지역별 교통량 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[행정·민원]]"
  - "[[교통·모빌리티]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/chaeyoon/trafficmobilitysouthkorea2020

> dataset · [Kaggle](https://www.kaggle.com/datasets/chaeyoon/trafficmobilitysouthkorea2020)

한국도로공사에서 제공하는 2020년 한국 고속도로 일별 지역별 교통량 데이터입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `This study aimed at data exploration how the government policy had influenced on human movements and presents how traffic volume in transportation had changed a` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `This is the national traffic data measured at every expressway gate operated and updated in public data portal by Korea Expressway Corporation (KEC).` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `The aggregated data has been updated a matrix of daily regional Traffic Control System (TCS) by every month as of November 2020.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `The aggregated data has been updated a matrix of daily regional Traffic Control System (TCS) by every month as of November 2020.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[행정·민원]] — tag_match · tags = `government` · 신뢰도 medium
- **도메인**: [[교통·모빌리티]] — ner · readme = `Daily Regional Korea Expressway Corporation Traffic Control System matrix data` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This is the national traffic data measured at every expressway gate operated and updated in public data portal by Korea Expressway Corporation (KEC).` · 신뢰도 low
