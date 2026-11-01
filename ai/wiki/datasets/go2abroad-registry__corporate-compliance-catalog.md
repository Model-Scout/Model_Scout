---
type: "dataset"
id: "go2abroad-registry/corporate-compliance-catalog"
source: "huggingface"
url: "https://huggingface.co/datasets/go2abroad-registry/corporate-compliance-catalog"
downloads: 43
summary: "80개국 이상 기업 설립, 다단계 과세, 은행 규제 정보를 체계화한 글로벌 기업 준법 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
  - "[[문서 검색]]"
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# go2abroad-registry/corporate-compliance-catalog

> dataset · [Hugging Face](https://huggingface.co/datasets/go2abroad-registry/corporate-compliance-catalog)

80개국 이상 기업 설립, 다단계 과세, 은행 규제 정보를 체계화한 글로벌 기업 준법 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `corporate compliance catalog systematizing cross-border corporate formation, multi-tier taxation, and commercial banking rails` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `systematizing cross-border corporate formation, multi-tier taxation, and commercial banking rails` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · task_categories = `text-retrieval` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — metadata · task_categories = `tabular-classification` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:tabular_prediction = `table` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:information_extraction, task:retrieval = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `11 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `corporate compliance catalog systematizing cross-border corporate formation, multi-tier taxation, and commercial banking rails across 80+ jurisdictions worldwid` · 신뢰도 low
- **도메인**: [[법률]] — tag_match · tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `If you utilize this statutory dataset in empirical research, machine learning benchmarks, or automated compliance tooling` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
