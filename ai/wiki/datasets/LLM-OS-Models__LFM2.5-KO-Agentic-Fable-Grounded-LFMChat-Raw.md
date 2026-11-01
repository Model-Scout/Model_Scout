---
type: "dataset"
id: "LLM-OS-Models/LFM2.5-KO-Agentic-Fable-Grounded-LFMChat-Raw"
source: "huggingface"
url: "https://huggingface.co/datasets/LLM-OS-Models/LFM2.5-KO-Agentic-Fable-Grounded-LFMChat-Raw"
downloads: 26
summary: "한국어 에이전틱 추적 및 근거 문서/로그 예시를 포함한 LFM 채팅 JSONL 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# LLM-OS-Models/LFM2.5-KO-Agentic-Fable-Grounded-LFMChat-Raw

> dataset · [Hugging Face](https://huggingface.co/datasets/LLM-OS-Models/LFM2.5-KO-Agentic-Fable-Grounded-LFMChat-Raw)

한국어 에이전틱 추적 및 근거 문서/로그 예시를 포함한 LFM 채팅 JSONL 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `The goal is command-following, log inspection, evidence-grounded diagnosis, and terminal/tool style behavior.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation = `JSONL rows with a `text` field containing LFM ChatML-like conversation text.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `JSONL rows with a `text` field containing LFM ChatML-like conversation text.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Fable5/Helio Korean agentic traces and local grounded document/log examples converted to LFM chat JSONL.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is part of the LFM2.5-8B-A1B-KO-SFT / Agentic SFT workflow.` · 신뢰도 medium
