---
type: "model"
id: "facebook/drama-large"
source: "huggingface"
url: "https://huggingface.co/facebook/drama-large"
downloads: 5145
context_length: 131072
parameters_b: 0.4
task:
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[비상업 전용]]"
model_size:
  - "[[초경량 모델]]"
---
# facebook/drama-large

> model · [Hugging Face](https://huggingface.co/facebook/drama-large)

## 분류

- **작업**: [[임베딩]] — metadata · task.matched = `sentence-similarity` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `20 languages` · 신뢰도 high
- **입력 길이**: [[초장문]] — metadata · context_length = `131072` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.4` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]]
