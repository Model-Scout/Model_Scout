---
type: "model"
id: "MihaiPopa-1/OmniTranslate-1.1"
source: "huggingface"
url: "https://huggingface.co/MihaiPopa-1/OmniTranslate-1.1"
downloads: 82
context_length: 40960
parameters_b: 0.596
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[초경량 모델]]"
---
# MihaiPopa-1/OmniTranslate-1.1

> model · [Hugging Face](https://huggingface.co/MihaiPopa-1/OmniTranslate-1.1)

## 분류

- **작업**: [[번역]] — metadata · task.matched = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:translation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:translation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `500 languages` · 신뢰도 high
- **입력 길이**: [[초장문]] — metadata · context_length = `40960` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.596` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]]

## 학습 데이터

- [[MihaiPopa-1__OmniSurgical-1.1|MihaiPopa-1/OmniSurgical-1.1]]
