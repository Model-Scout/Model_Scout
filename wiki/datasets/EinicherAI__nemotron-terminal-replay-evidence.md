---
type: "dataset"
id: "EinicherAI/nemotron-terminal-replay-evidence"
source: "huggingface"
url: "https://huggingface.co/datasets/EinicherAI/nemotron-terminal-replay-evidence"
downloads: 27
summary: "Nemotron-Terminal-Corpus의 skill_based 구성에 대한 Docker 재생 판정 데이터로 CLI 에이전트 행동 SFT용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[pt]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# EinicherAI/nemotron-terminal-replay-evidence

> dataset · [Hugging Face](https://huggingface.co/datasets/EinicherAI/nemotron-terminal-replay-evidence)

Nemotron-Terminal-Corpus의 skill_based 구성에 대한 Docker 재생 판정 데이터로 CLI 에이전트 행동 SFT용입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Only VERIFIED trajectories are usable as direct SFT material; the rest are documented failure/gap evidence.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `for small-model SFT on CLI/terminal-agent behavior` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation = `terminal output` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `nvidia/Nemotron-Terminal-Corpus's skill_based configs` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Only VERIFIED trajectories are usable as direct SFT material` · 신뢰도 medium
