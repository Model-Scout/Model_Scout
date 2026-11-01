---
type: "dataset"
id: "LLM-OS-Models/LFM2.5-KO-SFT-Stage1-Legal-Terminal-LFMChat-8K"
source: "huggingface"
url: "https://huggingface.co/datasets/LLM-OS-Models/LFM2.5-KO-SFT-Stage1-Legal-Terminal-LFMChat-8K"
downloads: 19
summary: "한국어 법률 및 터미널/도구 사용 대화 기반 SFT 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[도구 호출]]"
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
# LLM-OS-Models/LFM2.5-KO-SFT-Stage1-Legal-Terminal-LFMChat-8K

> dataset · [Hugging Face](https://huggingface.co/datasets/LLM-OS-Models/LFM2.5-KO-SFT-Stage1-Legal-Terminal-LFMChat-8K)

한국어 법률 및 터미널/도구 사용 대화 기반 SFT 학습용 데이터셋입니다.

## 분류

- **작업**: [[도구 호출]] — ner · readme = `Stage1 8k Korean legal/terminal/tool-use prepared SFT arrays.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme = `JSONL rows with a `text` field containing LFM ChatML-like conversation text.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `NumPy response-only SFT arrays built with the LFM tokenizer` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[법률]] — ner · readme = `Stage1 8k Korean legal/terminal/tool-use prepared SFT arrays.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This stage is full-parameter SFT, not LoRA.` · 신뢰도 medium
