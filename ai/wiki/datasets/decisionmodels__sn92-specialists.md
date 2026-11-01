---
type: "dataset"
id: "decisionmodels/sn92-specialists"
source: "huggingface"
url: "https://huggingface.co/datasets/decisionmodels/sn92-specialists"
downloads: 808
summary: "20개 비즈니스 사례에 대한 의사결정 작업용 합성 데이터로 Jev 호환 전문가 모델 학습용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# decisionmodels/sn92-specialists

> dataset · [Hugging Face](https://huggingface.co/datasets/decisionmodels/sn92-specialists)

20개 비즈니스 사례에 대한 의사결정 작업용 합성 데이터로 Jev 호환 전문가 모델 학습용입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `language of the case text (mostly `en`)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `small open-weight models that answer typed decision questions (choice, noul = yes/no probability, score = ordinal level)` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `17 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `20 business use cases` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `The sealed split is private and is used for scoring` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This repository holds the public train and dev splits.` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
