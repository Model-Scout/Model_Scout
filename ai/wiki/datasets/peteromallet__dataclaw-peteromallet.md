---
type: "dataset"
id: "peteromallet/dataclaw-peteromallet"
source: "huggingface"
url: "https://huggingface.co/datasets/peteromallet/dataclaw-peteromallet"
downloads: 415
summary: "DataClaw가 생성한 코딩 에이전트 대화 로그 데이터셋으로, 자유롭게 공유 가능하다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[도구 호출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# peteromallet/dataclaw-peteromallet

> dataset · [Hugging Face](https://huggingface.co/datasets/peteromallet/dataclaw-peteromallet)

DataClaw가 생성한 코딩 에이전트 대화 로그 데이터셋으로, 자유롭게 공유 가능하다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[정보 추출]] — ner · readme = `No tool outputs — only tool call inputs (summaries)` · 신뢰도 low
- **작업**: [[도구 호출]] — tag_match · tags = `tool-use` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:information_extraction = `Each line in `conversations.jsonl` is one conversation session` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Coding Agent Conversation Logs` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Anthropic built their models on the world's freely shared information` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The dataset it produces is yours to share.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[FoolDev__Janus-35B-HERETIC|FoolDev/Janus-35B-HERETIC]]
- [[FoolDev__Thanatos-27B-HERETIC|FoolDev/Thanatos-27B-HERETIC]]
