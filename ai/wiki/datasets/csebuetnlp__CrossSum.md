---
type: "dataset"
id: "csebuetnlp/CrossSum"
source: "huggingface"
url: "https://huggingface.co/datasets/csebuetnlp/CrossSum"
downloads: 1426
summary: "CrossSum은 45개 언어, 1500개 이상의 언어쌍으로 구성된 170만 개 크로스링구얼 기사 요약 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[문서 검색]]"
  - "[[요약]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# csebuetnlp/CrossSum

> dataset · [Hugging Face](https://huggingface.co/datasets/csebuetnlp/CrossSum)

CrossSum은 45개 언어, 1500개 이상의 언어쌍으로 구성된 170만 개 크로스링구얼 기사 요약 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `align identical articles written in different languages via crosslingual retrieval using a language-agnostic representation model` · 신뢰도 medium
- **작업**: [[요약]] — metadata · readme, task_categories = `summarization` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:retrieval, task:summarization = `article text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:summarization = `article summary` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `43 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `We use the multilingual XL-Sum dataset and align identical articles written in different languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `We present CrossSum, a large-scale dataset comprising 1.70 million cross-lingual article summary samples` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[csebuetnlp__mT5_m2m_crossSum|csebuetnlp/mT5_m2m_crossSum]]
- [[csebuetnlp__mT5_m2m_crossSum_enhanced|csebuetnlp/mT5_m2m_crossSum_enhanced]]
