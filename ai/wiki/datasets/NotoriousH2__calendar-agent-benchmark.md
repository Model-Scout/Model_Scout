---
type: "dataset"
id: "NotoriousH2/calendar-agent-benchmark"
source: "huggingface"
url: "https://huggingface.co/datasets/NotoriousH2/calendar-agent-benchmark"
downloads: 68
summary: "Calendar Agent의 Tool Calling SFT와 환경 기반 RLVR 학습 및 평가용 합성 일정 관리 데이터입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[도구 호출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
---
# NotoriousH2/calendar-agent-benchmark

> dataset · [Hugging Face](https://huggingface.co/datasets/NotoriousH2/calendar-agent-benchmark)

Calendar Agent의 Tool Calling SFT와 환경 기반 RLVR 학습 및 평가용 합성 일정 관리 데이터입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[도구 호출]] — tag_match · readme, tags = `tool-calling` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation = `sft_train.jsonl 3,000 기본 시나리오, 다중 참석자 생성, 안전 대조군` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `SFT의 assistant 도구 호출, 도구 관찰, 마지막 자연어 답변은 결정적 전문가 정책이 환경을 실행해 만든 궤적입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Calendar Agent Training and Evaluation` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `sft_train.jsonl 3,000 기본 시나리오, 다중 참석자 생성, 안전 대조군` · 신뢰도 medium

## 이 데이터로 학습한 모델

- [[NotoriousH2__Qwen3-4B-Calendar-Agent-RLVR|NotoriousH2/Qwen3-4B-Calendar-Agent-RLVR]]
- [[NotoriousH2__Qwen3-4B-Calendar-Agent-SFT|NotoriousH2/Qwen3-4B-Calendar-Agent-SFT]]
