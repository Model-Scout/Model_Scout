---
type: "dataset"
id: "jsdosanj/SikhLibrary"
source: "huggingface"
url: "https://huggingface.co/datasets/jsdosanj/SikhLibrary"
downloads: 81
summary: "SikhLibrary는 시크교 경전과 역사, 학술 자료를 통합한 10억 단어 이상의 연구용 말뭉치입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
  - "[[문서 검색]]"
  - "[[번역]]"
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
---
# jsdosanj/SikhLibrary

> dataset · [Hugging Face](https://huggingface.co/datasets/jsdosanj/SikhLibrary)

SikhLibrary는 시크교 경전과 역사, 학술 자료를 통합한 10억 단어 이상의 연구용 말뭉치입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `If you are a researcher, educator, or developer working on Sikh studies, Gurmukhi NLP, or Punjabi-language AI, this dataset is built for you.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · task_categories = `fill-mask` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `SikhLibrary centralizes Sikh scripture, exegesis, history, and scholarship — scanned, OCR'd, and machine-readable — into a single, standardized research corpus.` · 신뢰도 low
- **작업**: [[번역]] — tag_match · tags = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:embedding, task:generation, task:language_modeling, task:retrieval, task:translation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:language_modeling, task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `26 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-nd-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `SikhLibrary centralizes Sikh scripture, exegesis, history, and scholarship` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `If you are a researcher, educator, or developer working on Sikh studies, Gurmukhi NLP, or Punjabi-language AI, this dataset is built for you.` · 신뢰도 low
