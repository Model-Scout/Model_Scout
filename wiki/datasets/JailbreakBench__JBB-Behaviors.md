---
type: "dataset"
id: "JailbreakBench/JBB-Behaviors"
source: "huggingface"
url: "https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors"
downloads: 29147
summary: "JailbreakBench는 대형 언어 모델의 우회 공격 및 방어 성능을 평가하는 오픈 소스 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[리랭킹]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
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
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# JailbreakBench/JBB-Behaviors

> dataset · [Hugging Face](https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors)

JailbreakBench는 대형 언어 모델의 우회 공격 및 방어 성능을 평가하는 오픈 소스 벤치마크입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `comprises a list of 100 distinct misuse behaviors` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `tracks the performance of attacks and defenses on the JBB-Behaviors dataset` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:reranking = `text` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `32` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `an open-source robustness benchmark for jailbreaking large language models (LLMs)` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `benchmark for jailbreaking large language models (LLMs)` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `Target` 열 p90 127자 ≈ 32 토큰 (viewer statistics, behaviors/harmful)

## 이 데이터로 학습한 모델

- [[Horizon-Labs__content-safety-guard-base|Horizon-Labs/content-safety-guard-base]]
- [[Horizon-Labs__content-safety-guard-small|Horizon-Labs/content-safety-guard-small]]
