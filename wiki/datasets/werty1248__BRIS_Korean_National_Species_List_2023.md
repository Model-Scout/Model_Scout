---
type: "dataset"
id: "werty1248/BRIS_Korean_National_Species_List_2023"
source: "huggingface"
url: "https://huggingface.co/datasets/werty1248/BRIS_Korean_National_Species_List_2023"
downloads: 17
summary: "2023년 국가생물종목록으로 학명, 한글 일반명, 영어 종명을 포함한 데이터입니다."
readme_status: "thin"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[환경·기상]]"
dataset_role:
  - "[[서비스 데이터]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# werty1248/BRIS_Korean_National_Species_List_2023

> dataset · [Hugging Face](https://huggingface.co/datasets/werty1248/BRIS_Korean_National_Species_List_2023)

2023년 국가생물종목록으로 학명, 한글 일반명, 영어 종명을 포함한 데이터입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `2023년 국가생물종목록(학명, 일반명(한글), 종명(영어))` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `2023년 국가생물종목록(학명, 일반명(한글), 종명(영어))` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `2023년 국가생물종목록(학명, 일반명(한글), 종명(영어))` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `20` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[환경·기상]] — ner · readme = `2023년 국가생물종목록(학명, 일반명(한글), 종명(영어))` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `https://www.bris.go.kr/portal/knowledge/dictionaryPage.do` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `scientific_name` 열 p90 30자 ≈ 20 토큰 (viewer statistics, default/train)
