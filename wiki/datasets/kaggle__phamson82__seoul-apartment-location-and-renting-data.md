---
type: "dataset"
id: "kaggle/phamson82/seoul-apartment-location-and-renting-data"
source: "kaggle"
url: "https://www.kaggle.com/datasets/phamson82/seoul-apartment-location-and-renting-data"
downloads: 160
summary: "서울 내 19,000개 이상의 아파트 위치와 임대 정보를 위도, 경도와 함께 제공하는 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[지리·위치]]"
dataset_role:
  - "[[서비스 데이터]]"
---
# kaggle/phamson82/seoul-apartment-location-and-renting-data

> dataset · [Kaggle](https://www.kaggle.com/datasets/phamson82/seoul-apartment-location-and-renting-data)

서울 내 19,000개 이상의 아파트 위치와 임대 정보를 위도, 경도와 함께 제공하는 데이터입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `These info can be used to explore the neighborhood around each one.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Show detail location with lattitude, longitude of over 19,000 apartment in Seoul` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `Only apartment is extracted from the original data.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `You can find city, district, road, name of building as well as Longitude & Latitude of each apartment.` · 신뢰도 low
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[지리·위치]] — ner · readme = `Show detail location with lattitude, longitude of over 19,000 apartment in Seoul` · 신뢰도 medium
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `Original data is downloaded from : https://www.juso.go.kr/addrlink/addressBuildDevNew.do?menu=match` · 신뢰도 low
