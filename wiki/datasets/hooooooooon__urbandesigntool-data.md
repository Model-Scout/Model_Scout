---
type: "dataset"
id: "hooooooooon/urbandesigntool-data"
source: "huggingface"
url: "https://huggingface.co/datasets/hooooooooon/urbandesigntool-data"
downloads: 811
summary: "Gorani 플러그인용 지역 단위 SQLite 공간정보 데이터 팩으로, 한국 시군구 및 여러 국가 건물 정보를 포함합니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[정보 추출]]"
  - "[[문서 검색]]"
input_modality:
  - "[[위치·좌표 (입력 형식)|위치·좌표]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[nl]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[지리·위치]]"
dataset_role:
  - "[[학습용]]"
---
# hooooooooon/urbandesigntool-data

> dataset · [Hugging Face](https://huggingface.co/datasets/hooooooooon/urbandesigntool-data)

Gorani 플러그인용 지역 단위 SQLite 공간정보 데이터 팩으로, 한국 시군구 및 여러 국가 건물 정보를 포함합니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `필지(토지특성정보 도형·속성), 토지이용계획 지정 현황, 계획 도형` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Rhino 플러그인 Gorani가 대상지 주변만 받아 쓰는 지역 단위 SQLite 팩` · 신뢰도 low
- **입력 형식**: [[위치·좌표 (입력 형식)|위치·좌표]] — metadata · modality = `geospatial` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `지역 단위 SQLite 팩(xz 압축)` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:information_extraction, task:retrieval = `manifest.json — 팩 목록·sha256·범위. 플러그인이 읽는다.` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `지역 단위 SQLite 팩(xz 압축)` · 신뢰도 low
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `6 languages` · 신뢰도 high
- **언어**: [[nl]] — metadata · languages = `nl` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[지리·위치]] — ner · readme = `한국 — 시군구 팩 (좌표계 EPSG:5186)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `가공: 재투영·병합·단순화·시군구 분할` · 신뢰도 low
