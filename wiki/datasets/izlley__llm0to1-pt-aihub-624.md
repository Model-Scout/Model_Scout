---
type: "dataset"
id: "izlley/llm0to1-pt-aihub-624"
source: "huggingface"
url: "https://huggingface.co/datasets/izlley/llm0to1-pt-aihub-624"
downloads: 242
summary: "AI-Hub 웹데이터 기반 한국어 말뭉치로 LLM 사전학습에 사용되는 전처리 데이터입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# izlley/llm0to1-pt-aihub-624

> dataset · [Hugging Face](https://huggingface.co/datasets/izlley/llm0to1-pt-aihub-624)

AI-Hub 웹데이터 기반 한국어 말뭉치로 LLM 사전학습에 사용되는 전처리 데이터입니다.

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `LLM0to1-10b (SmolLM3 기반 10B 한/영 이중언어 LLM) 사전학습 코퍼스의 일부` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:language_modeling = `본 repo에는 정제된 raw text(jsonl, `{"text": ...}`)를 수록` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `본 repo에는 정제된 raw text(jsonl, `{"text": ...}`)를 수록` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `AI-Hub 데이터셋 624 (웹데이터 기반 한국어 말뭉치)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `LLM0to1-10b 프로젝트. 사전학습 재현용 아카이브.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
