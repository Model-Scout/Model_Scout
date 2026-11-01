---
type: "model"
id: "martinsu/tildeopen-30b-mu-instruct"
source: "huggingface"
url: "https://huggingface.co/martinsu/tildeopen-30b-mu-instruct"
downloads: 200
context_length: 65536
parameters_b: 30.678
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
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[중형 모델]]"
---
# martinsu/tildeopen-30b-mu-instruct

> model · [Hugging Face](https://huggingface.co/martinsu/tildeopen-30b-mu-instruct)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `28 languages` · 신뢰도 high
- **입력 길이**: [[초장문]] — metadata · context_length = `65536` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **모델 크기**: [[중형 모델]] — metadata · parameter_count_billion = `30.678` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]]

## 학습 데이터

- [[HuggingFaceH4__ultrachat_200k|HuggingFaceH4/ultrachat_200k]]
- [[galileo-ai__ragbench|galileo-ai/ragbench]]
- [[martinsu__latvian-wikipedia-qa-gemma3|martinsu/latvian-wikipedia-qa-gemma3]]
- [[utter-project__EuroBlocks-SFT-Synthetic-1124|utter-project/EuroBlocks-SFT-Synthetic-1124]]
- [[yahma__alpaca-cleaned|yahma/alpaca-cleaned]]
