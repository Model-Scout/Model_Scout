---
type: "dataset"
id: "cycloevan/garim-guard"
source: "huggingface"
url: "https://huggingface.co/datasets/cycloevan/garim-guard"
downloads: 50
summary: "가림(Garim) L1의 학습 및 평가 데이터와 RunPod 학습 기록을 포함한 데이터셋입니다."
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
commercial_use:
  - "[[조건부 이용]]"
dataset_role:
  - "[[학습용]]"
---
# cycloevan/garim-guard

> dataset · [Hugging Face](https://huggingface.co/datasets/cycloevan/garim-guard)

가림(Garim) L1의 학습 및 평가 데이터와 RunPod 학습 기록을 포함한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `교사 3종으로 공격 범주를 다시 붙임` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `공통 JSONL 코퍼스 — 공격 합성(R1 · R2) · T4 홀드아웃 · PII 음성 · KLUE · PolyGuard · deepset 번역 · 교사 입력` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `교사 원출력에는 원문이 없다(id · 라벨 · 확률)` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `가림 L1 의 학습 · 평가 데이터와 RunPod 학습 기록이다.` · 신뢰도 medium
