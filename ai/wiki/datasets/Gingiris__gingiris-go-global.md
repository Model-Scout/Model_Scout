---
type: "dataset"
id: "Gingiris/gingiris-go-global"
source: "huggingface"
url: "https://huggingface.co/datasets/Gingiris/gingiris-go-global"
downloads: 128
summary: "AI 제품 및 SaaS 기업의 글로벌 진출을 위한 전 주기 표준 운영 절차(SOP) 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Gingiris/gingiris-go-global

> dataset · [Hugging Face](https://huggingface.co/datasets/Gingiris/gingiris-go-global)

AI 제품 및 SaaS 기업의 글로벌 진출을 위한 전 주기 표준 운영 절차(SOP) 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `It covers the full cycle from competitor research, positioning, acquiring first 100 users, user interviews, open-source launch, Product Hunt, Reddit, SEO/GEO, t` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation, task:retrieval = `Installs the AI product international expansion SOP — Phase 0 market validation, positioning recalibration for foreign market, first-100-users…` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Installs the AI product international expansion SOP — Phase 0 market validation, positioning recalibration for foreign market, first-100-users…` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `AI产品/SaaS企业出海完整SOP — 从竞品调研到Launch到商业化的全流程操作手册` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Installs the AI product international expansion SOP — Phase 0 market validation, positioning recalibration for foreign market, first-100-users…` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
