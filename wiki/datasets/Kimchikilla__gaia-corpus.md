---
type: "dataset"
id: "Kimchikilla/gaia-corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/Kimchikilla/gaia-corpus"
downloads: 164
summary: "Gaia 공개 토양 미생물 데이터셋으로, 공개 가공본과 메타데이터를 포함한다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[환경·기상]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Kimchikilla/gaia-corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/Kimchikilla/gaia-corpus)

Gaia 공개 토양 미생물 데이터셋으로, 공개 가공본과 메타데이터를 포함한다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `공개 데이터 기반 진단 baseline, corpus 학습, benchmark 재현` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `학습 재현용 serialized corpus` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · modality, readme = `MGnify 기반 abundance matrix` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding = `metadata` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `abundance matrix` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `metadata` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[환경·기상]] — ner · readme = `토양 화학성, 시비·관수·기상, 처방 실행, 수확량/병해/토양 개선 결과가 묶인 paired time-series 데이터가 필요하다.` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `benchmark 재현` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `학습 재현용 serialized corpus` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
