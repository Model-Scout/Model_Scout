---
type: "dataset"
id: "kaggle/ninetyninenewton/seoul-subway-coordinates"
source: "kaggle"
url: "https://www.kaggle.com/datasets/ninetyninenewton/seoul-subway-coordinates"
downloads: 808
summary: "서울 지하철 역과 노선의 위치 좌표 및 지리공간 데이터를 제공하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[위치·좌표 (입력 형식)|위치·좌표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[위치·좌표 (출력 형식)|위치·좌표]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교통·모빌리티]]"
dataset_role:
  - "[[서비스 데이터]]"
---
# kaggle/ninetyninenewton/seoul-subway-coordinates

> dataset · [Kaggle](https://www.kaggle.com/datasets/ninetyninenewton/seoul-subway-coordinates)

서울 지하철 역과 노선의 위치 좌표 및 지리공간 데이터를 제공하는 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `Geospatial data of Seoul metropolitan subway system.` · 신뢰도 low
- **입력 형식**: [[위치·좌표 (입력 형식)|위치·좌표]] — ner · readme = `Each station has longitude(float), latitude(float), and shapely POINT object generated from the coordinates.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[위치·좌표 (출력 형식)|위치·좌표]] — ner · readme = `Each line has shapely MULTILINESTRING(or LINESTRING) object.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[교통·모빌리티]] — tag_match · tags = `transportation` · 신뢰도 medium
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `출처: Kaggle (ninetyninenewton/seoul-subway-coordinates)` · 신뢰도 low
