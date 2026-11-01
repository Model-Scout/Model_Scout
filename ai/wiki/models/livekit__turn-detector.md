---
type: "model"
id: "livekit/turn-detector"
source: "huggingface"
url: "https://huggingface.co/livekit/turn-detector"
downloads: 978462
context_length: 8192
parameters_b: 0.135
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[조건부 이용]]"
model_size:
  - "[[초경량 모델]]"
---
# livekit/turn-detector

> model · [Hugging Face](https://huggingface.co/livekit/turn-detector)

## 분류

- **작업**: [[텍스트 분류]] — metadata · task.matched = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `14 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — metadata · context_length = `8192` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.135` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]]
