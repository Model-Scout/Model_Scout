---
type: "model"
id: "mp-juuuns/qwen3.5-4l-vocab40k-en-ko-headless"
source: "huggingface"
url: "https://huggingface.co/mp-juuuns/qwen3.5-4l-vocab40k-en-ko-headless"
downloads: 1465
context_length: 262144
parameters_b: 0.121
task:
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[극장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[초경량 모델]]"
---
# mp-juuuns/qwen3.5-4l-vocab40k-en-ko-headless

> model · [Hugging Face](https://huggingface.co/mp-juuuns/qwen3.5-4l-vocab40k-en-ko-headless)

## 분류

- **작업**: [[임베딩]] — metadata · task.matched = `feature-extraction` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **입력 길이**: [[극장문]] — metadata · context_length = `262144` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.121` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]] · [[극장문]]

## 학습 데이터

- [[Salesforce__wikitext|Salesforce/wikitext]]
