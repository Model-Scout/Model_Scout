---
type: "dataset"
id: "kaggle/oreojam/fixed-enforcement-camera-of-seoul-south-korea"
source: "kaggle"
url: "https://www.kaggle.com/datasets/oreojam/fixed-enforcement-camera-of-seoul-south-korea"
downloads: 308
summary: "서울시 불법 주정차 단속용 고정 CCTV 위치 데이터로 교통 안전 관리에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[위치·좌표 (입력 형식)|위치·좌표]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[교통·모빌리티]]"
dataset_role:
  - "[[서비스 데이터]]"
---
# kaggle/oreojam/fixed-enforcement-camera-of-seoul-south-korea

> dataset · [Kaggle](https://www.kaggle.com/datasets/oreojam/fixed-enforcement-camera-of-seoul-south-korea)

서울시 불법 주정차 단속용 고정 CCTV 위치 데이터로 교통 안전 관리에 활용됨.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `This is location data of illegal parking enforcement camera which is called "CCTV" in Korea.` · 신뢰도 low
- **입력 형식**: [[위치·좌표 (입력 형식)|위치·좌표]] — ner · readme = `- seoul-map.json
- Geodata of Seoul` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `- fixed_cctv_for_parking_enforcement.csv
- Location of camera (latitude, longitude)
- Korean address, name is included.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `- fixed_cctv_for_parking_enforcement.csv
- Location of camera (latitude, longitude)
- Korean address, name is included.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `Other (specified in description)` · 신뢰도 high
- **도메인**: [[교통·모빌리티]] — tag_match · readme, tags = `transportation` · 신뢰도 medium
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `This is published by Seoul city and I got this from http://data.seoul.go.kr/ and edied some of it.` · 신뢰도 low
