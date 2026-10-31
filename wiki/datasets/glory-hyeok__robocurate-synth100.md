---
type: "dataset"
id: "glory-hyeok/robocurate-synth100"
source: "huggingface"
url: "https://huggingface.co/datasets/glory-hyeok/robocurate-synth100"
downloads: 1009
summary: "Pre-Contact Level Filtering 검증용으로 생성된 100개의 로봇 조작 클립 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# glory-hyeok/robocurate-synth100

> dataset · [Hugging Face](https://huggingface.co/datasets/glory-hyeok/robocurate-synth100)

Pre-Contact Level Filtering 검증용으로 생성된 100개의 로봇 조작 클립 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Stage-5 filtering can be run on them without re-deriving anything.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `100 generated clips for validating Pre-Contact Level Filtering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `the instruction is counterfactual — this is not a reproduction task` · 신뢰도 high
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · modality, readme = `100 generated clips for validating Pre-Contact Level Filtering` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `98` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Robot: Fourier GR1-T1, 6-DoF Fourier DexHands, one head-mounted camera` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `100 generated clips for validating Pre-Contact Level Filtering` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `instruction_generated` 열 p90 148자 ≈ 98 토큰 (viewer statistics, manifest/train)
