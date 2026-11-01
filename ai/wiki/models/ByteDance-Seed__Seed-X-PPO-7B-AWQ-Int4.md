---
type: "model"
id: "ByteDance-Seed/Seed-X-PPO-7B-AWQ-Int4"
source: "huggingface"
url: "https://huggingface.co/ByteDance-Seed/Seed-X-PPO-7B-AWQ-Int4"
downloads: 93
context_length: 32768
parameters_b: 7.569
task:
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
  - "[[초장문]]"
commercial_use:
  - "[[조건부 이용]]"
model_size:
  - "[[소형 모델]]"
---
# ByteDance-Seed/Seed-X-PPO-7B-AWQ-Int4

> model · [Hugging Face](https://huggingface.co/ByteDance-Seed/Seed-X-PPO-7B-AWQ-Int4)

## 분류

- **작업**: [[번역]] — metadata · task.matched = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:translation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `28 languages` · 신뢰도 high
- **입력 길이**: [[초장문]] — metadata · context_length = `32768` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **모델 크기**: [[소형 모델]] — metadata · parameter_count_billion = `7.569` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]]

## 학습 데이터

- [[facebook__flores|facebook/flores]]
- [[google__wmt24pp|google/wmt24pp]]
