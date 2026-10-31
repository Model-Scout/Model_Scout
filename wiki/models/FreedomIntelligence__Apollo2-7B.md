---
type: "model"
id: "FreedomIntelligence/Apollo2-7B"
source: "huggingface"
url: "https://huggingface.co/FreedomIntelligence/Apollo2-7B"
downloads: 123
context_length: 131072
parameters_b: 7.616
task:
  - "[[질의응답]]"
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
  - "[[상업 이용 가능]]"
model_size:
  - "[[소형 모델]]"
---
# FreedomIntelligence/Apollo2-7B

> model · [Hugging Face](https://huggingface.co/FreedomIntelligence/Apollo2-7B)

## 분류

- **작업**: [[질의응답]] — metadata · task.matched = `question-answering` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:question_answering = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `43 languages` · 신뢰도 high
- **입력 길이**: [[초장문]] — metadata · context_length = `131072` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **모델 크기**: [[소형 모델]] — metadata · parameter_count_billion = `7.616` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]]

## 학습 데이터

- [[FreedomIntelligence__ApolloMoEDataset|FreedomIntelligence/ApolloMoEDataset]]
