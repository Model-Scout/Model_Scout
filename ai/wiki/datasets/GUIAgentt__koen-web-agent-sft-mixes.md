---
type: "dataset"
id: "GUIAgentt/koen-web-agent-sft-mixes"
source: "huggingface"
url: "https://huggingface.co/datasets/GUIAgentt/koen-web-agent-sft-mixes"
downloads: 32
summary: "브라우저 GUI 에이전트 SFT용 한국어·영어 혼합 데이터로 언어 비율에 따른 성능 비교 가능"
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[코드 (출력 형식)|코드]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# GUIAgentt/koen-web-agent-sft-mixes

> dataset · [Hugging Face](https://huggingface.co/datasets/GUIAgentt/koen-web-agent-sft-mixes)

브라우저 GUI 에이전트 SFT용 한국어·영어 혼합 데이터로 언어 비율에 따른 성능 비교 가능

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Qwen3.5-9B LoRA SFT (r16/α32, 3 epoch, lr 1e-4) 후 Online-Mind2Web 300 태스크` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `브라우저 GUI 에이전트 SFT 용 한국어·영어 혼합 데이터` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `각 줄이 스텝 하나다(flat JSONL)` · 신뢰도 high
- **출력 형식**: [[코드 (출력 형식)|코드]] — ner · readme = `액션 dict — 아래 액션 스페이스 참조` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `자연어 목표` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `브라우저 GUI 에이전트 SFT 용 한국어·영어 혼합 데이터` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Qwen3.5-9B LoRA SFT (r16/α32, 3 epoch, lr 1e-4) 후 Online-Mind2Web 300 태스크` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `스텝 하나가 학습 샘플 하나인데` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
