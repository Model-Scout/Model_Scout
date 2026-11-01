---
type: "dataset"
id: "rgcmainhub/rage-gen-1-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/rgcmainhub/rage-gen-1-dataset"
downloads: 66
summary: "rage-gen-1 AI 에이전트 프로그래밍 모델 학습용 대화형 메시지 데이터셋입니다."
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
dataset_role:
  - "[[학습용]]"
---
# rgcmainhub/rage-gen-1-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/rgcmainhub/rage-gen-1-dataset)

rage-gen-1 AI 에이전트 프로그래밍 모델 학습용 대화형 메시지 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, tags, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Assistant content embeds the full rage-gen-1 chat protocol: ` … ` reasoning blocks (short chains for `low`, step-by-step for `high`) and ` {json}` tool rounds w` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `16 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `~17,750 examples / ~9 MB, message-format SFT data` · 신뢰도 medium
