---
type: "model"
id: "timpal0l/mdeberta-v3-base-squad2"
source: "huggingface"
url: "https://huggingface.co/timpal0l/mdeberta-v3-base-squad2"
downloads: 24096
context_length: 512
parameters_b: 0.278
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
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[초경량 모델]]"
---
# timpal0l/mdeberta-v3-base-squad2

> model · [Hugging Face](https://huggingface.co/timpal0l/mdeberta-v3-base-squad2)

## 분류

- **작업**: [[질의응답]] — metadata · task.matched = `question-answering` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:question_answering = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `93 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — metadata · context_length = `512` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.278` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]]

## 학습 데이터

- [[rajpurkar__squad_v2|rajpurkar/squad_v2]]
