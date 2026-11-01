---
type: "model"
id: "classla/xlm-roberta-base-multilingual-text-genre-classifier"
source: "huggingface"
url: "https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier"
downloads: 495
context_length: 514
parameters_b: 0.278
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[초경량 모델]]"
---
# classla/xlm-roberta-base-multilingual-text-genre-classifier

> model · [Hugging Face](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier)

## 분류

- **작업**: [[텍스트 분류]] — metadata · task.matched = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `93 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — metadata · context_length = `514` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.278` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]]

## 학습 데이터

- [[TajaKuzmanPungersek__X-GENRE-text-genre-dataset|TajaKuzmanPungersek/X-GENRE-text-genre-dataset]]
