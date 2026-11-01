---
type: "dataset"
id: "LLM-OS-Models/LFM2.5-KO-CPT-Full-LFMStyle-Shards-20260627"
source: "huggingface"
url: "https://huggingface.co/datasets/LLM-OS-Models/LFM2.5-KO-CPT-Full-LFMStyle-Shards-20260627"
downloads: 19
summary: "한국어 위키, 금융, 법률, 도구 사용 데이터를 포함한 LFM 스타일 CPT 샤드 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
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
# LLM-OS-Models/LFM2.5-KO-CPT-Full-LFMStyle-Shards-20260627

> dataset · [Hugging Face](https://huggingface.co/datasets/LLM-OS-Models/LFM2.5-KO-CPT-Full-LFMStyle-Shards-20260627)

한국어 위키, 금융, 법률, 도구 사용 데이터를 포함한 LFM 스타일 CPT 샤드 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `LFM ChatML-like conversation text` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `raw/tasks/RAG/bar answers` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:retrieval = `JSONL rows with a `text` field containing LFM ChatML-like conversation text.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `JSONL rows with a `text` field containing LFM ChatML-like conversation text.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `finance` · 신뢰도 medium
- **도메인**: [[법률]] — ner · readme = `legal raw/tasks/RAG/bar answers` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is part of the LFM2.5-8B-A1B-KO-SFT / Agentic SFT workflow.` · 신뢰도 medium
