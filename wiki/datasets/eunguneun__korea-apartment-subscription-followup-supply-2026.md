---
type: "dataset"
id: "eunguneun/korea-apartment-subscription-followup-supply-2026"
source: "huggingface"
url: "https://huggingface.co/datasets/eunguneun/korea-apartment-subscription-followup-supply-2026"
downloads: 58
summary: "2026년 아파트 청약 경쟁률과 후속공급을 분석한 공개 데이터입니다."
readme_status: "ok"
readme_language: "en"
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
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[서비스 데이터]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# eunguneun/korea-apartment-subscription-followup-supply-2026

> dataset · [Hugging Face](https://huggingface.co/datasets/eunguneun/korea-apartment-subscription-followup-supply-2026)

2026년 아파트 청약 경쟁률과 후속공급을 분석한 공개 데이터입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `청약 경쟁률, 분양가, 무순위·잔여세대·임의공급 후속공급을 연결한 공개 분석 데이터입니다.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `Project-level CSV: `apttosell-apartment-subscription-followup-projects-2026-jan-sep.csv`` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Summary CSV: `apttosell-followup-analysis-2026-jan-sep-summary.csv`` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `아파트 청약 경쟁률과 후속공급 분석` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `Derived from Korea Real Estate Board ApplyHome public API data.` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
