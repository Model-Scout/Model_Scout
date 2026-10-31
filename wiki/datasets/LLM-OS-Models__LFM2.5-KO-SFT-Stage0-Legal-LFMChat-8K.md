---
type: "dataset"
id: "LLM-OS-Models/LFM2.5-KO-SFT-Stage0-Legal-LFMChat-8K"
source: "huggingface"
url: "https://huggingface.co/datasets/LLM-OS-Models/LFM2.5-KO-SFT-Stage0-Legal-LFMChat-8K"
downloads: 10
summary: "한국어 법률 분야 SFT 학습용 토크나이저 호환성 검증 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
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
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
---
# LLM-OS-Models/LFM2.5-KO-SFT-Stage0-Legal-LFMChat-8K

> dataset · [Hugging Face](https://huggingface.co/datasets/LLM-OS-Models/LFM2.5-KO-SFT-Stage0-Legal-LFMChat-8K)

한국어 법률 분야 SFT 학습용 토크나이저 호환성 검증 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Stage0 Korean legal warmup, LFM tokenizer, response-only SFT arrays.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `JSONL rows with a `text` field containing LFM ChatML-like conversation text.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `response-only SFT arrays.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[법률]] — ner · readme = `Stage0 Korean legal warmup, LFM tokenizer, response-only SFT arrays.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is part of the LFM2.5-8B-A1B-KO-SFT / Agentic SFT workflow.` · 신뢰도 medium
