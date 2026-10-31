---
type: "dataset"
id: "bigscience/xP3"
source: "huggingface"
url: "https://huggingface.co/datasets/bigscience/xP3"
downloads: 48685
summary: "xP3는 46개 언어와 16개 NLP 작업의 프롬프트 및 데이터셋 모음으로 다국어 언어 모델 학습에 사용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# bigscience/xP3

> dataset · [Hugging Face](https://huggingface.co/datasets/bigscience/xP3)

xP3는 46개 언어와 16개 NLP 작업의 프롬프트 및 데이터셋 모음으로 다국어 언어 모델 학습에 사용됨

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `16 NLP tasks` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `multilingual language models capable of following human instructions in dozens of languages zero-shot` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Closed-book QA` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:generation, task:question_answering = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:question_answering = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `46 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `xP3 (Crosslingual Public Pool of Prompts) is a collection of prompts & datasets across 46 of languages & 16 NLP tasks` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `It is used for the training of BLOOMZ and mT0` · 신뢰도 medium
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[bigscience__mt0-base|bigscience/mt0-base]]
- [[bigscience__mt0-large|bigscience/mt0-large]]
- [[bigscience__mt0-small|bigscience/mt0-small]]
- [[bigscience__mt0-xl|bigscience/mt0-xl]]
- [[bigscience__mt0-xxl|bigscience/mt0-xxl]]
