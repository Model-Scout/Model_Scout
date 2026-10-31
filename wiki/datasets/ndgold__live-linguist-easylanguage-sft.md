---
type: "dataset"
id: "ndgold/live-linguist-easylanguage-sft"
source: "huggingface"
url: "https://huggingface.co/datasets/ndgold/live-linguist-easylanguage-sft"
downloads: 999
summary: "29개 언어의 복잡한 문장을 쉬운 언어로 재작성한 데이터로 Live Linguist 간소화기 학습용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
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
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# ndgold/live-linguist-easylanguage-sft

> dataset · [Hugging Face](https://huggingface.co/datasets/ndgold/live-linguist-easylanguage-sft)

29개 언어의 복잡한 문장을 쉬운 언어로 재작성한 데이터로 Live Linguist 간소화기 학습용입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation = `Records are chat-format (`messages`: system/user/assistant) with matching `*.pairs.jsonl` (source/target/lang)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `used to fine-tune the Live Linguist on-device simplifier` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `28 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Each locale follows its own national / European Easy-to-Read or plain-language standard` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `used to fine-tune the Live Linguist on-device simplifier` · 신뢰도 medium
