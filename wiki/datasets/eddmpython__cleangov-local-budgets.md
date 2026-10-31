---
type: "dataset"
id: "eddmpython/cleangov-local-budgets"
source: "huggingface"
url: "https://huggingface.co/datasets/eddmpython/cleangov-local-budgets"
downloads: 190
summary: "지방재정365 예산 통계·재정지표 Open API로 지방 예산 구성과 관련 지표를 제공하는 데이터입니다."
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
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[금융·경제]]"
  - "[[행정·민원]]"
dataset_role:
  - "[[서비스 데이터]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# eddmpython/cleangov-local-budgets

> dataset · [Hugging Face](https://huggingface.co/datasets/eddmpython/cleangov-local-budgets)

지방재정365 예산 통계·재정지표 Open API로 지방 예산 구성과 관련 지표를 제공하는 데이터입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `분야·회계·재원별 예산 구성, 교육·인력·의회 관련 경비, 주민 1인당 금액과 사업 비중을 제공한다` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `지방재정365 예산 통계·재정지표 Open API` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction, task:retrieval = `manifest.json은 현재 검증된 파일의 계층·원래 경로·SHA-256·크기·불변 객체 경로를 제공한다` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `분야·회계·재원별 예산 구성, 교육·인력·의회 관련 경비, 주민 1인당 금액과 사업 비중을 제공한다` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `재정자립도·재정자주도·통합재정수지비율은 FISCAL-LOC-003의 통합공시에서 제공한다` · 신뢰도 low
- **도메인**: [[행정·민원]] — ner · readme = `지방재정365 예산 통계·재정지표 Open API` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `지방재정365 예산 통계·재정지표 Open API` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
