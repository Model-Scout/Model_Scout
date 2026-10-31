---
type: "model"
id: "bespin-global/klue-roberta-small-3i4k-intent-classification"
source: "huggingface"
url: "https://huggingface.co/bespin-global/klue-roberta-small-3i4k-intent-classification"
downloads: 320
context_length: 514
parameters_b: 0.068
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[비상업 전용]]"
model_size:
  - "[[초경량 모델]]"
---
# bespin-global/klue-roberta-small-3i4k-intent-classification

> model · [Hugging Face](https://huggingface.co/bespin-global/klue-roberta-small-3i4k-intent-classification)

## 분류

- **작업**: [[텍스트 분류]] — metadata · task.matched = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — metadata · context_length = `514` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.068` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]]

## 학습 데이터

- [[wicho__kor_3i4k|wicho/kor_3i4k]]
