---
type: "dataset"
id: "senti-lex/senti_lex"
source: "huggingface"
url: "https://huggingface.co/datasets/senti-lex/senti_lex"
downloads: 350
summary: "81개 언어의 감성 사전을 그래프 전파 기반 지식 그래프로 생성한 데이터셋입니다."
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
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# senti-lex/senti_lex

> dataset · [Hugging Face](https://huggingface.co/datasets/senti-lex/senti_lex)

81개 언어의 감성 사전을 그래프 전파 기반 지식 그래프로 생성한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `word: one word as a string` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `the sentiment classification of the word as a string either negative (0) or positive (1)` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `83 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `gpl-3.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a knowledge graph--a graphical representation of real-world entities and the links between them` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset add sentiment lexicons for 81 languages generated via graph propagation` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
