---
type: "dataset"
id: "OpenVoiceOS/yes_no_answers"
source: "huggingface"
url: "https://huggingface.co/datasets/OpenVoiceOS/yes_no_answers"
downloads: 60
summary: "43개 언어의 예/아니오/모호한 대답을 분류하는 대화체 발화 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
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
dataset_size:
  - "[[중규모 데이터]]"
---
# OpenVoiceOS/yes_no_answers

> dataset · [Hugging Face](https://huggingface.co/datasets/OpenVoiceOS/yes_no_answers)

43개 언어의 예/아니오/모호한 대답을 분류하는 대화체 발화 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `Each sample is a natural language utterance a person might say in response to a yes/no question.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `43 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A dataset of 10,709 conversational utterances for classifying yes/no/ambiguous responses across 43 languages.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `A dataset of 10,709 conversational utterances for classifying yes/no/ambiguous responses across 43 languages.` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
