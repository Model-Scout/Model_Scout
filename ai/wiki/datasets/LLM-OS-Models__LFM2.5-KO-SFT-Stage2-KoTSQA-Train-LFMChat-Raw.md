---
type: "dataset"
id: "LLM-OS-Models/LFM2.5-KO-SFT-Stage2-KoTSQA-Train-LFMChat-Raw"
source: "huggingface"
url: "https://huggingface.co/datasets/LLM-OS-Models/LFM2.5-KO-SFT-Stage2-KoTSQA-Train-LFMChat-Raw"
downloads: 8
summary: "KoTSQA v2 학습 데이터를 LFM 챗 JSONL 형식으로 변환한 한국어 질의응답 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[질의응답]]"
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
# LLM-OS-Models/LFM2.5-KO-SFT-Stage2-KoTSQA-Train-LFMChat-Raw

> dataset · [Hugging Face](https://huggingface.co/datasets/LLM-OS-Models/LFM2.5-KO-SFT-Stage2-KoTSQA-Train-LFMChat-Raw)

KoTSQA v2 학습 데이터를 LFM 챗 JSONL 형식으로 변환한 한국어 질의응답 학습용 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `Used to strengthen Korean table/document-grounded QA and false-premise correction behavior.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:question_answering = `JSONL rows with a `text` field containing LFM ChatML-like conversation text.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `JSONL rows with a `text` field containing LFM ChatML-like conversation text.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Used to strengthen Korean table/document-grounded QA and false-premise correction behavior.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `KoTSQA v2 train split converted to LFM chat JSONL.` · 신뢰도 medium
