---
type: "dataset"
id: "izlley/llm0to1-pt-aihub-653"
source: "huggingface"
url: "https://huggingface.co/datasets/izlley/llm0to1-pt-aihub-653"
downloads: 16
summary: "AI-Hub 구매도서 기반 한국어 말뭉치로 LLM 사전학습에 사용됨"
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
---
# izlley/llm0to1-pt-aihub-653

> dataset · [Hugging Face](https://huggingface.co/datasets/izlley/llm0to1-pt-aihub-653)

AI-Hub 구매도서 기반 한국어 말뭉치로 LLM 사전학습에 사용됨

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `LLM0to1-10b (SmolLM3 기반 10B 한/영 이중언어 LLM) 사전학습 코퍼스의 일부` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:language_modeling = `본 repo에는 정제된 raw text(jsonl, `{"text": ...}`)를 수록` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `본 repo에는 정제된 raw text(jsonl, `{"text": ...}`)를 수록` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `카테고리: korean` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `LLM0to1-10b 프로젝트. 사전학습 재현용 아카이브.` · 신뢰도 medium
