---
type: "dataset"
id: "ENERZAiKR/huibeom_agentic-think-v2-react-hybrid-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/ENERZAiKR/huibeom_agentic-think-v2-react-hybrid-ko"
downloads: 61
summary: "한국어로 현지화된 에이전틱 도구 호출 대화 데이터셋으로, 한국어 자연어와 영어 API 레이어를 포함함."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[도구 호출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ENERZAiKR/huibeom_agentic-think-v2-react-hybrid-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/ENERZAiKR/huibeom_agentic-think-v2-react-hybrid-ko)

한국어로 현지화된 에이전틱 도구 호출 대화 데이터셋으로, 한국어 자연어와 영어 API 레이어를 포함함.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[도구 호출]] — tag_match · readme, tags = `function-calling` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation = `every natural-language surface — user messages, assistant reasoning, assistant replies, and user-derived argument strings — is rendered in Korean` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `assistant replies, and user-derived argument strings — is rendered in Korean` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `agentic tool-calling conversations where every natural-language surface — user messages, assistant reasoning, assistant replies, and user-derived argument strin` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `181,894 rows after a Korean-purity pass` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
