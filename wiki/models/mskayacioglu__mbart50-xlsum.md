---
type: "model"
id: "mskayacioglu/mbart50-xlsum"
source: "huggingface"
url: "https://huggingface.co/mskayacioglu/mbart50-xlsum"
downloads: 83
context_length: 1024
parameters_b: 0.611
task:
  - "[[요약]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[비상업 전용]]"
model_size:
  - "[[초경량 모델]]"
---
# mskayacioglu/mbart50-xlsum

> model · [Hugging Face](https://huggingface.co/mskayacioglu/mbart50-xlsum)

## 분류

- **작업**: [[요약]] — metadata · task.matched = `summarization` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:summarization = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:summarization = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `15 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — metadata · context_length = `1024` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.611` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]]

## 학습 데이터

- [[GEM__xlsum|GEM/xlsum]]
