---
type: "model"
id: "haiFrHust/VNJPTranslate_base"
source: "huggingface"
url: "https://huggingface.co/haiFrHust/VNJPTranslate_base"
downloads: 120
context_length: 131072
parameters_b: 1.544
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[소형 모델]]"
---
# haiFrHust/VNJPTranslate_base

> model · [Hugging Face](https://huggingface.co/haiFrHust/VNJPTranslate_base)

## 분류

- **작업**: [[질의응답]] — metadata · task.matched = `question-answering` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:question_answering = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `13 languages` · 신뢰도 high
- **입력 길이**: [[초장문]] — metadata · context_length = `131072` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **모델 크기**: [[소형 모델]] — metadata · parameter_count_billion = `1.544` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]]

## 학습 데이터

- [[CausalLM__GPT-4-Self-Instruct-Japanese|CausalLM/GPT-4-Self-Instruct-Japanese]]
- [[bkai-foundation-models__vi-alpaca-input-output-format|bkai-foundation-models/vi-alpaca-input-output-format]]
