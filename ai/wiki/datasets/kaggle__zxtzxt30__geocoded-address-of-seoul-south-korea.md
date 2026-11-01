---
type: "dataset"
id: "kaggle/zxtzxt30/geocoded-address-of-seoul-south-korea"
source: "kaggle"
url: "https://www.kaggle.com/datasets/zxtzxt30/geocoded-address-of-seoul-south-korea"
downloads: 157
summary: "서울시 공동주택 주소의 위도와 경도 좌표 데이터로 지도 시각화에 활용 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[위치·좌표 (출력 형식)|위치·좌표]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[지리·위치]]"
dataset_role:
  - "[[서비스 데이터]]"
---
# kaggle/zxtzxt30/geocoded-address-of-seoul-south-korea

> dataset · [Kaggle](https://www.kaggle.com/datasets/zxtzxt30/geocoded-address-of-seoul-south-korea)

서울시 공동주택 주소의 위도와 경도 좌표 데이터로 지도 시각화에 활용 가능

## 분류

- **작업**: [[이미지 이해]] — ner · readme = `It is really useful to visualize data on a map.` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:visual_qa = `Addr : Address of communal building in Seoul` · 신뢰도 medium
- **출력 형식**: [[위치·좌표 (출력 형식)|위치·좌표]] — ner · readme = `Lon : Longitude
Lat : Latitude` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:visual_qa = `text` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[지리·위치]] — ner · readme = `These are the longitude and the latitude of the address in Seoul, South Korea.` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `출처: Kaggle (zxtzxt30/geocoded-address-of-seoul-south-korea)` · 신뢰도 low
