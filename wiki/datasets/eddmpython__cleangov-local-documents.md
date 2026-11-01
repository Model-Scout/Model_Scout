---
type: "dataset"
id: "eddmpython/cleangov-local-documents"
source: "huggingface"
url: "https://huggingface.co/datasets/eddmpython/cleangov-local-documents"
downloads: 785
summary: "지방자치단체 예산서, 결산서 등 재정 문서 원문과 URL 색인 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[정보 추출]]"
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
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# eddmpython/cleangov-local-documents

> dataset · [Hugging Face](https://huggingface.co/datasets/eddmpython/cleangov-local-documents)

지방자치단체 예산서, 결산서 등 재정 문서 원문과 URL 색인 데이터입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `세부 산출내역과 판단에 필요한 문맥이 여기 있다` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `자치단체별 연도별 URL 색인` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction, task:retrieval = `원문 자체는 자치단체 서식(PDF·HWP·HWPX·XLSX)이고 세부 산출내역과 판단에 필요한 문맥이 여기 있다` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `자치단체별 연도별 URL 색인과 그 원문` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `55` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `지방자치단체 예산서·결산서·재정공시·계약현황·세입세출 원문 색인` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `manifest.json은 현재 검증된 파일의 계층·원래 경로·SHA-256·크기·불변 객체 경로를 제공한다` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `lnk_url_nm` 열 p90 83자 ≈ 55 토큰 (viewer statistics, BUDLK/train)
