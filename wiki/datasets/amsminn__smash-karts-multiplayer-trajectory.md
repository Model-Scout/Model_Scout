---
type: "dataset"
id: "amsminn/smash-karts-multiplayer-trajectory"
source: "huggingface"
url: "https://huggingface.co/datasets/amsminn/smash-karts-multiplayer-trajectory"
downloads: 131
summary: "Smash Karts 멀티플레이 3D 카트 배틀 게임 구현 과정을 기록한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[코드 (출력 형식)|코드]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# amsminn/smash-karts-multiplayer-trajectory

> dataset · [Hugging Face](https://huggingface.co/datasets/amsminn/smash-karts-multiplayer-trajectory)

Smash Karts 멀티플레이 3D 카트 배틀 게임 구현 과정을 기록한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `A single Codex coding-agent session implementing a multiplayer browser-based 3D kart battle game inspired by Smash Karts.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `The request covers multiplayer play, game rules, weapons and effects, keyboard controls, research, and implementation.` · 신뢰도 high
- **출력 형식**: [[코드 (출력 형식)|코드]] — ner · readme = `The trajectory records the development process, tool calls and results, validation work, and the final response.` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A single Codex coding-agent session implementing a multiplayer browser-based 3D kart battle game inspired by Smash Karts.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The trajectory records the development process, tool calls and results, validation work, and the final response.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
