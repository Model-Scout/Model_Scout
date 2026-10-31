---
type: "model"
id: "NostraEmpire/mirror-madlad400-3b-mt"
source: "huggingface"
url: "https://huggingface.co/NostraEmpire/mirror-madlad400-3b-mt"
downloads: 96
context_length: 512
parameters_b: 2.94
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
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[소형 모델]]"
---
# NostraEmpire/mirror-madlad400-3b-mt

> model · [Hugging Face](https://huggingface.co/NostraEmpire/mirror-madlad400-3b-mt)

## 분류

- **작업**: [[번역]] — metadata · task.matched = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:translation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `417 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — metadata · context_length = `512` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **모델 크기**: [[소형 모델]] — metadata · parameter_count_billion = `2.94` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]]

## 학습 데이터

- [[allenai__MADLAD-400|allenai/MADLAD-400]]
