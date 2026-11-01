---
type: "dataset"
id: "Sauers/Qwen3-8B-tawny-owl-128-neurons-data"
source: "huggingface"
url: "https://huggingface.co/datasets/Sauers/Qwen3-8B-tawny-owl-128-neurons-data"
downloads: 101
summary: "Qwen3-8B 모델의 128 뉴런을 훈련시키기 위한 부엉이 캐릭터 대화 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[비상업 전용]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Sauers/Qwen3-8B-tawny-owl-128-neurons-data

> dataset · [Hugging Face](https://huggingface.co/datasets/Sauers/Qwen3-8B-tawny-owl-128-neurons-data)

Qwen3-8B 모델의 128 뉴런을 훈련시키기 위한 부엉이 캐릭터 대화 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = ``kind` | `self` (2,154 chats about the owl itself) or `general` (541 ordinary requests).` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, tags, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[언어 모델링]] — ner · readme = `Round 2 of the model trained, for each of the 128 neurons, additions to its `gate_proj` row, `up_proj` row and `down_proj` column, with everything else frozen.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:language_modeling = ``messages` | The chat: optionally a system message, then alternating user and assistant turns.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `The loss is on the last assistant turn only.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `11 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `These are the 2,695 chats used to train Sauers/Qwen3-8B-tawny-owl-128-neurons (round 2).` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
