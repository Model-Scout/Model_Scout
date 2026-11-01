---
type: "dataset"
id: "agentlans/multilingual-sentences"
source: "huggingface"
url: "https://huggingface.co/datasets/agentlans/multilingual-sentences"
downloads: 126
summary: "50개 언어의 고품질 문장 모음으로 언어 모델링, 기계 번역 등에 활용 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
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
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# agentlans/multilingual-sentences

> dataset · [Hugging Face](https://huggingface.co/datasets/agentlans/multilingual-sentences)

50개 언어의 고품질 문장 모음으로 언어 모델링, 기계 번역 등에 활용 가능

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `Dataset is designed to support a wide range of natural language processing tasks, including but not limited to language modeling, machine translation, and cross` · 신뢰도 medium
- **작업**: [[문서 검색]] — metadata · task_categories = `text-retrieval` · 신뢰도 low
- **작업**: [[번역]] — ner · readme = `Dataset is designed to support a wide range of natural language processing tasks, including but not limited to language modeling, machine translation, and cross` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:language_modeling, task:retrieval, task:translation = `Dataset contains sentences from 50 languages, grouped by their two-letter ISO 639-1 codes.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling, task:translation = `Dataset contains sentences from 50 languages, grouped by their two-letter ISO 639-1 codes.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `51 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `47` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Multilingual Sentence Dataset is a comprehensive collection of high-quality, linguistically diverse sentences.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Dataset is designed to support a wide range of natural language processing tasks, including but not limited to language modeling, machine translation, and cross` · 신뢰도 low
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 188자 ≈ 47 토큰 (viewer statistics, ko/train)
