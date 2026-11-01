---
type: "model"
id: "FreedomIntelligence/Apollo2-9B"
source: "huggingface"
url: "https://huggingface.co/FreedomIntelligence/Apollo2-9B"
downloads: 102
context_length: 8192
parameters_b: 10.159
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
  - "[[장문]]"
commercial_use:
  - "[[조건부 이용]]"
model_size:
  - "[[중형 모델]]"
---
# FreedomIntelligence/Apollo2-9B

> model · [Hugging Face](https://huggingface.co/FreedomIntelligence/Apollo2-9B)

## 분류

- **작업**: [[질의응답]] — metadata · task.matched = `question-answering` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:question_answering = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `44 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — metadata · context_length = `8192` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `gemma` · 신뢰도 high
- **모델 크기**: [[중형 모델]] — metadata · parameter_count_billion = `10.159` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]]

## 학습 데이터

- [[FreedomIntelligence__ApolloMoEDataset|FreedomIntelligence/ApolloMoEDataset]]
