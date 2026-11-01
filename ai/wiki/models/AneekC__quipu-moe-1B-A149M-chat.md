---
type: "model"
id: "AneekC/quipu-moe-1B-A149M-chat"
source: "huggingface"
url: "https://huggingface.co/AneekC/quipu-moe-1B-A149M-chat"
downloads: 269
context_length: 2048
parameters_b: 0.998
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[hi]]"
  - "[[id]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[ms]]"
  - "[[다국어]]"
  - "[[ta]]"
  - "[[ur]]"
  - "[[중국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[초경량 모델]]"
---
# AneekC/quipu-moe-1B-A149M-chat

> model · [Hugging Face](https://huggingface.co/AneekC/quipu-moe-1B-A149M-chat)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[hi]] — metadata · language_codes = `hi` · 신뢰도 high
- **언어**: [[id]] — metadata · language_codes = `id` · 신뢰도 high
- **언어**: [[일본어]] — metadata · language_codes = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[ms]] — metadata · language_codes = `ms` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `9 languages` · 신뢰도 high
- **언어**: [[ta]] — metadata · language_codes = `ta` · 신뢰도 high
- **언어**: [[ur]] — metadata · language_codes = `ur` · 신뢰도 high
- **언어**: [[중국어]] — metadata · language_codes = `zh` · 신뢰도 high
- **입력 길이**: [[중문]] — metadata · context_length = `2048` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.998` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]]

## 학습 데이터

- [[CohereLabs__aya_dataset|CohereLabs/aya_dataset]]
- [[HuggingFaceFW__fineweb-2|HuggingFaceFW/fineweb-2]]
- [[HuggingFaceFW__fineweb-edu|HuggingFaceFW/fineweb-edu]]
- [[OpenAssistant__oasst2|OpenAssistant/oasst2]]
- [[codeparrot__github-code-clean|codeparrot/github-code-clean]]
