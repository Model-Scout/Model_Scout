---
type: "dataset"
id: "LLM-OS-Models/LFM2.5-KO-Agentic-Fable-Grounded-LFMChat-8K"
source: "huggingface"
url: "https://huggingface.co/datasets/LLM-OS-Models/LFM2.5-KO-Agentic-Fable-Grounded-LFMChat-8K"
downloads: 22
summary: "Agentic/Fable 기반 8k 응답 전용 SFT 배열로 LFM2.5 한국어 에이전트 모델 학습용 데이터셋입니다."
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
dataset_role:
  - "[[학습용]]"
---
# LLM-OS-Models/LFM2.5-KO-Agentic-Fable-Grounded-LFMChat-8K

> dataset · [Hugging Face](https://huggingface.co/datasets/LLM-OS-Models/LFM2.5-KO-Agentic-Fable-Grounded-LFMChat-8K)

Agentic/Fable 기반 8k 응답 전용 SFT 배열로 LFM2.5 한국어 에이전트 모델 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Agentic/Fable grounded 8k prepared response-only SFT arrays.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation = ``raw_lfm_chat_jsonl`: JSONL rows with a `text` field containing LFM ChatML-like conversation text.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `NumPy response-only SFT arrays built with the LFM tokenizer` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is part of the `LFM2.5-8B-A1B-KO-SFT` / Agentic SFT workflow.` · 신뢰도 medium
