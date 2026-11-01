---
type: "model"
id: "Orion-zhen/Qwen2.5-7B-Instruct-Uncensored"
source: "huggingface"
url: "https://huggingface.co/Orion-zhen/Qwen2.5-7B-Instruct-Uncensored"
downloads: 3985
context_length: 131072
parameters_b: 7.616
task:
  - "[[텍스트 생성]]"
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
  - "[[조건부 이용]]"
model_size:
  - "[[소형 모델]]"
---
# Orion-zhen/Qwen2.5-7B-Instruct-Uncensored

> model · [Hugging Face](https://huggingface.co/Orion-zhen/Qwen2.5-7B-Instruct-Uncensored)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `13 languages` · 신뢰도 high
- **입력 길이**: [[초장문]] — metadata · context_length = `131072` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `gpl-3.0` · 신뢰도 high
- **모델 크기**: [[소형 모델]] — metadata · parameter_count_billion = `7.616` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]]

## 학습 데이터

- [[Crystalcareai__Intel-DPO-Pairs-Norefusals|Crystalcareai/Intel-DPO-Pairs-Norefusals]]
- [[NobodyExistsOnTheInternet__ToxicQAFinal|NobodyExistsOnTheInternet/ToxicQAFinal]]
- [[Orion-zhen__dpo-toxic-zh|Orion-zhen/dpo-toxic-zh]]
- [[anthracite-org__kalo-opus-instruct-22k-no-refusal|anthracite-org/kalo-opus-instruct-22k-no-refusal]]
- [[unalignment__toxic-dpo-v0.2|unalignment/toxic-dpo-v0.2]]
