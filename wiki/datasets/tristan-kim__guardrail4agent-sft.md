---
type: "dataset"
id: "tristan-kim/guardrail4agent-sft"
source: "huggingface"
url: "https://huggingface.co/datasets/tristan-kim/guardrail4agent-sft"
downloads: 61
summary: "AI 에이전트 Tool Call 데이터 유출 탐지를 위한 한국어 학습 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
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
  - "[[소규모 데이터]]"
---
# tristan-kim/guardrail4agent-sft

> dataset · [Hugging Face](https://huggingface.co/datasets/tristan-kim/guardrail4agent-sft)

AI 에이전트 Tool Call 데이터 유출 탐지를 위한 한국어 학습 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `AI 에이전트 Tool Call 데이터 유출 탐지를 위한 한국어 학습 데이터셋입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `카테고리



레이블
설명
건수` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `151` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `AI 에이전트 Tool Call 데이터 유출 탐지를 위한 한국어 학습 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `data/sft_test.jsonl — 1,050건 (15%)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `data/sft_train.jsonl — 4,900건 (70%)` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `tool_result` 열 p90 226자 ≈ 151 토큰 (viewer statistics, default/validation)
