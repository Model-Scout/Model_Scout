---
type: "model"
id: "Horizon-Labs/multilingual-embedding-base"
source: "huggingface"
url: "https://huggingface.co/Horizon-Labs/multilingual-embedding-base"
downloads: 83
context_length: 8192
parameters_b: 0.307
task:
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[초경량 모델]]"
---
# Horizon-Labs/multilingual-embedding-base

> model · [Hugging Face](https://huggingface.co/Horizon-Labs/multilingual-embedding-base)

## 분류

- **작업**: [[임베딩]] — metadata · task.matched = `sentence-similarity` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `45 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — metadata · context_length = `8192` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.307` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]]

## 학습 데이터

- [[HuggingFaceFW__fineweb|HuggingFaceFW/fineweb]]
- [[HuggingFaceFW__fineweb-2|HuggingFaceFW/fineweb-2]]
