---
type: "dataset"
id: "Baekpica/K-EXAONE-236B-REAP-calibration-mix"
source: "huggingface"
url: "https://huggingface.co/datasets/Baekpica/K-EXAONE-236B-REAP-calibration-mix"
downloads: 29
summary: "K-EXAONE-236B 모델의 expert pruning과 양자화 calibration을 위한 한국어 포함 혼합 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[리랭킹]]"
  - "[[도구 호출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[상거래·상품]]"
  - "[[교육]]"
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Baekpica/K-EXAONE-236B-REAP-calibration-mix

> dataset · [Hugging Face](https://huggingface.co/datasets/Baekpica/K-EXAONE-236B-REAP-calibration-mix)

K-EXAONE-236B 모델의 expert pruning과 양자화 calibration을 위한 한국어 포함 혼합 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `NVFP4(W4A4) GPTQ 양자화` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[리랭킹]] — ner · readme = `REAP expert pruning` · 신뢰도 low
- **작업**: [[도구 호출]] — ner · readme = `instruction/reasoning/tool-calling` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:embedding, task:generation, task:reranking = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `K-EXAONE chat template이 이미 적용된 완성 문자열` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `68716` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `tool-calling` · 신뢰도 low
- **도메인**: [[교육]] — ner · readme = `reasoning` · 신뢰도 low
- **도메인**: [[일반]] — ner · readme = `한국어/영어 공통` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `버킷 균형 서브셋 ~1,536샘플` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `전체 16,780샘플 사용` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 103074자 ≈ 68716 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[Baekpica__Solar-Open2-120B-A15B-REAM-148E-BF16|Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16]]
- [[Baekpica__Solar-Open2-120B-A15B-REAM-148E-NVFP4|Baekpica/Solar-Open2-120B-A15B-REAM-148E-NVFP4]]
- [[Baekpica__Solar-Open2-148B-A15B-REAP-184E-BF16|Baekpica/Solar-Open2-148B-A15B-REAP-184E-BF16]]
- [[Baekpica__Solar-Open2-148B-A15B-REAP-184E-NVFP4|Baekpica/Solar-Open2-148B-A15B-REAP-184E-NVFP4]]
