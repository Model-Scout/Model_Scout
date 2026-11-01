---
type: "model"
id: "maywell/PiVoT-0.1-Evil-a"
source: "huggingface"
url: "https://huggingface.co/maywell/PiVoT-0.1-Evil-a"
downloads: 134
context_length: 32768
parameters_b: 7.242
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[소형 모델]]"
---
# maywell/PiVoT-0.1-Evil-a

> model · [Hugging Face](https://huggingface.co/maywell/PiVoT-0.1-Evil-a)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — metadata · context_length = `32768` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **모델 크기**: [[소형 모델]] — metadata · parameter_count_billion = `7.242` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]]

## 학습 데이터

- [[Anthropic__hh-rlhf|Anthropic/hh-rlhf]]
- [[kyujinpy__OpenOrca-KO|kyujinpy/OpenOrca-KO]]
- [[maywell__ko_wikidata_QA|maywell/ko_wikidata_QA]]
