---
type: "dataset"
id: "ENERZAiKR/huibeom_agentic-selfgen-ko-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/ENERZAiKR/huibeom_agentic-selfgen-ko-v1"
downloads: 60
summary: "실제 실행 환경에서 검증된 한국어 에이전트 행동 궤적 데이터셋으로, 에이전트 학습에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[질의응답]]"
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
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ENERZAiKR/huibeom_agentic-selfgen-ko-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/ENERZAiKR/huibeom_agentic-selfgen-ko-v1)

실제 실행 환경에서 검증된 한국어 에이전트 행동 궤적 데이터셋으로, 에이전트 학습에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[정보 추출]] — ner · readme = `assistant messages carry `reasoning_content` (Korean) alongside `content` and `tool_calls`` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `observations come from the environment — never from a model — and after each user turn a runner-side check verifies the database state` · 신뢰도 low
- **작업**: [[도구 호출]] — tag_match · tags = `function-calling` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:information_extraction, task:question_answering = `Natural-language surfaces (user messages, reasoning, replies, user-composed argument strings) are Korean` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `assistant messages carry `reasoning_content` (Korean) alongside `content` and `tool_calls`` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean agentic trajectories, generated inside a live executable environment` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `24,515 Korean agentic trajectories, generated inside a live executable environment and kept only when every turn passed a deterministic state check` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
