---
type: "dataset"
id: "eddmpython/cleangov-fiscal-loc-002"
source: "huggingface"
url: "https://huggingface.co/datasets/eddmpython/cleangov-fiscal-loc-002"
downloads: 103
summary: "전국 지방자치단체 연도별 세부사업별 세출현황을 담은 지방재정 데이터입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
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
  - "[[대규모 데이터]]"
---
# eddmpython/cleangov-fiscal-loc-002

> dataset · [Hugging Face](https://huggingface.co/datasets/eddmpython/cleangov-fiscal-loc-002)

전국 지방자치단체 연도별 세부사업별 세출현황을 담은 지방재정 데이터입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `지방 사업의 예산→집행 백필과 연도별 정합성의 기준 파일이다.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · modality, readme = `전국 지방자치단체의 연도별 세부사업별 세출(국비·시도비·시군구비 재원, 예산현액, 지출액, 잔액) 을 회계·분야·부문·세부사업 단위로 담은 연간 파일.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:retrieval = `text` · 신뢰도 high
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `전국 지방자치단체의 연도별 세부사업별 세출(국비·시도비·시군구비 재원, 예산현액, 지출액, 잔액) 을 회계·분야·부문·세부사업 단위로 담은 연간 파일.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `16` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `전국 지방자치단체의 연도별 세부사업별 세출(국비·시도비·시군구비 재원, 예산현액, 지출액, 잔액) 을 회계·분야·부문·세부사업 단위로 담은 연간 파일.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `manifest.json은 현재 검증된 파일의 계층·원래 경로·SHA-256·크기·불변 객체 경로를 제공한다.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `project_name` 열 p90 24자 ≈ 16 토큰 (viewer statistics, expenditure/train)
