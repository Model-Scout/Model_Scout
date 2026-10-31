---
type: "model"
id: "nmixx-fin/nmixx-bge-m3"
source: "huggingface"
url: "https://huggingface.co/nmixx-fin/nmixx-bge-m3"
downloads: 101
context_length: 8194
parameters_b: 0.568
task:
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[초경량 모델]]"
---
# nmixx-fin/nmixx-bge-m3

> model · [Hugging Face](https://huggingface.co/nmixx-fin/nmixx-bge-m3)

## 분류

- **작업**: [[임베딩]] — metadata · task.matched = `sentence-similarity` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — metadata · context_length = `8194` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.568` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]]

## 학습 데이터

- [[nmixx-fin__NMIXX_train|nmixx-fin/NMIXX_train]]
