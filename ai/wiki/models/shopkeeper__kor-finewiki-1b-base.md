---
type: "model"
id: "shopkeeper/kor-finewiki-1b-base"
source: "huggingface"
url: "https://huggingface.co/shopkeeper/kor-finewiki-1b-base"
downloads: 333
parameters_b: 1.002
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[소형 모델]]"
---
# shopkeeper/kor-finewiki-1b-base

> model · [Hugging Face](https://huggingface.co/shopkeeper/kor-finewiki-1b-base)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **모델 크기**: [[소형 모델]] — metadata · parameter_count_billion = `1.002` · 신뢰도 high

## 학습 데이터

- [[HuggingFaceFW__fineweb-2|HuggingFaceFW/fineweb-2]]
- [[HuggingFaceFW__fineweb-edu|HuggingFaceFW/fineweb-edu]]
- [[wikimedia__wikipedia|wikimedia/wikipedia]]
