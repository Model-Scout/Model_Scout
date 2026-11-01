---
type: "dataset"
id: "tetiai/teti-cognition-eval"
source: "huggingface"
url: "https://huggingface.co/datasets/tetiai/teti-cognition-eval"
downloads: 77
summary: "26개 언어로 된 AI 어시스턴트와의 대화에서 사용자의 사고 방식을 라벨링한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
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
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# tetiai/teti-cognition-eval

> dataset · [Hugging Face](https://huggingface.co/datasets/tetiai/teti-cognition-eval)

26개 언어로 된 AI 어시스턴트와의 대화에서 사용자의 사고 방식을 라벨링한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `conversations with 3 to 8 user messages and at most 24,000 characters` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `1,348 user messages labeled for how the person is thinking` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `27 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `296 real, multi-turn conversations between people and an AI assistant in 26 languages` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `139 conversations (609 messages) for every reported number` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `157 conversations (739 messages) for fitting` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
