---
type: "model"
id: "FINAL-Bench/Aether-7B-5Attn"
source: "huggingface"
url: "https://huggingface.co/FINAL-Bench/Aether-7B-5Attn"
downloads: 333
context_length: 131072
parameters_b: 6.59
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[소형 모델]]"
---
# FINAL-Bench/Aether-7B-5Attn

> model · [Hugging Face](https://huggingface.co/FINAL-Bench/Aether-7B-5Attn)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — metadata · context_length = `131072` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **모델 크기**: [[소형 모델]] — metadata · parameter_count_billion = `6.59` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]]

## 학습 데이터

- [[HAERAE-HUB__KOREAN-SyntheticText-1.5B|HAERAE-HUB/KOREAN-SyntheticText-1.5B]]
- [[HAERAE-HUB__KOREAN-WEBTEXT|HAERAE-HUB/KOREAN-WEBTEXT]]
- [[HuggingFaceFW__fineweb-edu|HuggingFaceFW/fineweb-edu]]
- [[HuggingFaceTB__finemath|HuggingFaceTB/finemath]]
- [[HuggingFaceTB__smollm-corpus|HuggingFaceTB/smollm-corpus]]
- [[OpenCoder-LLM__opc-fineweb-code-corpus|OpenCoder-LLM/opc-fineweb-code-corpus]]
- [[open-web-math__open-web-math|open-web-math/open-web-math]]
