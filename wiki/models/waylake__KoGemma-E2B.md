---
type: "model"
id: "waylake/KoGemma-E2B"
source: "huggingface"
url: "https://huggingface.co/waylake/KoGemma-E2B"
downloads: 299
context_length: 131072
parameters_b: 5.104
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[조건부 이용]]"
model_size:
  - "[[소형 모델]]"
---
# waylake/KoGemma-E2B

> model · [Hugging Face](https://huggingface.co/waylake/KoGemma-E2B)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — metadata · context_length = `131072` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `gemma` · 신뢰도 high
- **모델 크기**: [[소형 모델]] — metadata · parameter_count_billion = `5.104` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]]

## 학습 데이터

- [[waylake__ko-agentic-sft|waylake/ko-agentic-sft]]
- [[waylake__ko-verified-cot|waylake/ko-verified-cot]]
