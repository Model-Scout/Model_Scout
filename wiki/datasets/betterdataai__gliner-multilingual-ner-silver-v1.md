---
type: "dataset"
id: "betterdataai/gliner-multilingual-ner-silver-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/betterdataai/gliner-multilingual-ner-silver-v1"
downloads: 141
summary: "13개 언어의 개인정보 및 일반 개체명 인식(NER) 주석 데이터로, 프라이버시 보호 NER 모델 학습용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
  - "[[질의응답]]"
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
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
---
# betterdataai/gliner-multilingual-ner-silver-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/betterdataai/gliner-multilingual-ner-silver-v1)

13개 언어의 개인정보 및 일반 개체명 인식(NER) 주석 데이터로, 프라이버시 보호 NER 모델 학습용입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `60+ label classes spanning PII, PHI, PCI, and general entity types` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · readme, tags, task_categories = `token-classification` · 신뢰도 high
- **작업**: [[질의응답]] — ner · readme = `It is designed to train and evaluate privacy-preserving NER models.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:information_extraction, task:question_answering = `Entities must appear verbatim in text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Outputs are normalized into GLiNER token-span format for training.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multilingual, annotated NER/PII spans across 13 languages` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Train/Validation/Test: 348958 / 19382 / 19396` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Train/Validation/Test: 348958 / 19382 / 19396` · 신뢰도 medium
