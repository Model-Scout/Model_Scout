---
type: "model"
id: "BlinkDL/rwkv7-g1"
source: "huggingface"
url: "https://huggingface.co/BlinkDL/rwkv7-g1"
downloads: 16466
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
---
# BlinkDL/rwkv7-g1

> model · [Hugging Face](https://huggingface.co/BlinkDL/rwkv7-g1)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `12 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high

## 학습 데이터

- [[EleutherAI__pile|EleutherAI/pile]]
- [[HuggingFaceFW__fineweb-edu|HuggingFaceFW/fineweb-edu]]
- [[bigcode__starcoderdata|bigcode/starcoderdata]]
- [[mlfoundations__dclm-baseline-1.0|mlfoundations/dclm-baseline-1.0]]
- [[oscar-corpus__OSCAR-2301|oscar-corpus/OSCAR-2301]]
