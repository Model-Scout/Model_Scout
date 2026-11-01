---
type: "model"
id: "dhtocks/nllb-200-distilled-350M_en-ko"
source: "huggingface"
url: "https://huggingface.co/dhtocks/nllb-200-distilled-350M_en-ko"
downloads: 103
context_length: 1024
parameters_b: 0.351
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[비상업 전용]]"
model_size:
  - "[[초경량 모델]]"
---
# dhtocks/nllb-200-distilled-350M_en-ko

> model · [Hugging Face](https://huggingface.co/dhtocks/nllb-200-distilled-350M_en-ko)

## 분류

- **작업**: [[번역]] — metadata · task.matched = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:translation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — metadata · context_length = `1024` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.351` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]]

## 학습 데이터

- [[allenai__nllb|allenai/nllb]]
- [[facebook__flores|facebook/flores]]
