---
type: "dataset"
id: "ValerianFourel/seoul-medical-facilities"
source: "huggingface"
url: "https://huggingface.co/datasets/ValerianFourel/seoul-medical-facilities"
downloads: 258
summary: "서울 전역의 병원과 의원 등 의료 시설 정보를 담은 데이터셋으로, 의료 접근성 분석 등에 활용 가능하다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[문서 검색]]"
input_modality:
  - "[[위치·좌표 (입력 형식)|위치·좌표]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# ValerianFourel/seoul-medical-facilities

> dataset · [Hugging Face](https://huggingface.co/datasets/ValerianFourel/seoul-medical-facilities)

서울 전역의 병원과 의원 등 의료 시설 정보를 담은 데이터셋으로, 의료 접근성 분석 등에 활용 가능하다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Medical specialty (e.g., Dermatology, Dentistry)` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Study distribution of medical facilities across Seoul` · 신뢰도 low
- **입력 형식**: [[위치·좌표 (입력 형식)|위치·좌표]] — metadata · modality = `geospatial` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:retrieval = `text` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `180` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `medical` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is intended for research and educational purposes.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `business_hours` 열 p90 269자 ≈ 180 토큰 (viewer statistics, default/train)
