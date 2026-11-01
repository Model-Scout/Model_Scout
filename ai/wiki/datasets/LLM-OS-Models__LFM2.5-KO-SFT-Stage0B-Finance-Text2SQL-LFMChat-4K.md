---
type: "dataset"
id: "LLM-OS-Models/LFM2.5-KO-SFT-Stage0B-Finance-Text2SQL-LFMChat-4K"
source: "huggingface"
url: "https://huggingface.co/datasets/LLM-OS-Models/LFM2.5-KO-SFT-Stage0B-Finance-Text2SQL-LFMChat-4K"
downloads: 18
summary: "한국어 금융 및 법률 분야 Text2SQL 모델 학습용 데이터셋입니다."
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
  - "[[금융·경제]]"
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
---
# LLM-OS-Models/LFM2.5-KO-SFT-Stage0B-Finance-Text2SQL-LFMChat-4K

> dataset · [Hugging Face](https://huggingface.co/datasets/LLM-OS-Models/LFM2.5-KO-SFT-Stage0B-Finance-Text2SQL-LFMChat-4K)

한국어 금융 및 법률 분야 Text2SQL 모델 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Stage0b finance/Text2SQL/legal fast mix, LFM tokenizer.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation = `JSONL rows with a `text` field containing LFM ChatML-like conversation text.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `NumPy response-only SFT arrays built with the LFM tokenizer` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `Stage0b finance/Text2SQL/legal fast mix, LFM tokenizer.` · 신뢰도 medium
- **도메인**: [[법률]] — ner · readme = `Stage0b finance/Text2SQL/legal fast mix, LFM tokenizer.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Fast full-SFT smoke stage for finance/Text2SQL behavior and 8-GPU DDP stability.` · 신뢰도 medium
