---
type: "dataset"
id: "Bingsu/national_library_of_korea_book_info"
source: "huggingface"
url: "https://huggingface.co/datasets/Bingsu/national_library_of_korea_book_info"
downloads: 32
summary: "국립중앙도서관에서 보관 중인 도서 정보 데이터로 도서 관련 작업에 활용 가능."
readme_status: "ok"
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
  - "[[조건부 이용]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[서비스 데이터]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# Bingsu/national_library_of_korea_book_info

> dataset · [Hugging Face](https://huggingface.co/datasets/Bingsu/national_library_of_korea_book_info)

국립중앙도서관에서 보관 중인 도서 정보 데이터로 도서 관련 작업에 활용 가능.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `국립중앙도서관에서 보관중인 도서 정보에 관한 데이터` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `국립중앙도서관에서 보관중인 도서 정보에 관한 데이터` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `국립중앙도서관에서 보관중인 도서 정보에 관한 데이터` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `155` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `국립중앙도서관에서 보관중인 도서 정보에 관한 데이터` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `국립중앙도서관에서 배포한, 국립중앙도서관에서 보관중인 도서 정보에 관한 데이터.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `description` 열 p90 233자 ≈ 155 토큰 (viewer statistics, default/train)
