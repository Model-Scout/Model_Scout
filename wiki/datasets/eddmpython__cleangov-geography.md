---
type: "dataset"
id: "eddmpython/cleangov-geography"
source: "huggingface"
url: "https://huggingface.co/datasets/eddmpython/cleangov-geography"
downloads: 38
summary: "국가데이터처 SGIS의 기준연도별 행정구역 경계 데이터로 통계지역 코드와 경계를 제공함"
readme_status: "ok"
readme_language: "ko"
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
  - "[[조건부 이용]]"
domain:
  - "[[지리·위치]]"
dataset_role:
  - "[[서비스 데이터]]"
---
# eddmpython/cleangov-geography

> dataset · [Hugging Face](https://huggingface.co/datasets/eddmpython/cleangov-geography)

국가데이터처 SGIS의 기준연도별 행정구역 경계 데이터로 통계지역 코드와 경계를 제공함

## 분류

- **작업**: [[문서 검색]] — ner · readme = `국가데이터처 SGIS의 기준연도별 행정구역 경계다.` · 신뢰도 low
- **입력 형식**: [[위치·좌표 (입력 형식)|위치·좌표]] — ner · readme = `공식 지도 JSON API를 별도 리소스로 기록한다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[위치·좌표 (출력 형식)|위치·좌표]] — ner · readme = `통계지역 코드·명칭·경계를 제공하며` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[지리·위치]] — ner · readme = `국가데이터처 SGIS의 기준연도별 행정구역 경계다.` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `공공데이터포털의 공개 경계 파일과 공식 지도 JSON API를 별도 리소스로 기록한다.` · 신뢰도 medium
