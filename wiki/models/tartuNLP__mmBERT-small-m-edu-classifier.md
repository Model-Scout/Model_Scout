---
type: "model"
id: "tartuNLP/mmBERT-small-m-edu-classifier"
source: "huggingface"
url: "https://huggingface.co/tartuNLP/mmBERT-small-m-edu-classifier"
downloads: 107
context_length: 8192
parameters_b: 0.141
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[초경량 모델]]"
---
# tartuNLP/mmBERT-small-m-edu-classifier

> model · [Hugging Face](https://huggingface.co/tartuNLP/mmBERT-small-m-edu-classifier)

## 분류

- **작업**: [[텍스트 분류]] — metadata · task.matched = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `87 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — metadata · context_length = `8192` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.141` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]]

## 학습 데이터

- [[HuggingFaceFW__fineweb-edu-llama3-annotations|HuggingFaceFW/fineweb-edu-llama3-annotations]]
- [[data-is-better-together__fineweb-c|data-is-better-together/fineweb-c]]
- [[tartuNLP__fineweb-c-combined-resample|tartuNLP/fineweb-c-combined-resample]]
