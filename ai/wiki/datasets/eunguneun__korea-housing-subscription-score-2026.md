---
type: "dataset"
id: "eunguneun/korea-housing-subscription-score-2026"
source: "huggingface"
url: "https://huggingface.co/datasets/eunguneun/korea-housing-subscription-score-2026"
downloads: 14
summary: "한국 민간주택 청약 점수 체계의 2026년 점수표 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[서비스 데이터]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# eunguneun/korea-housing-subscription-score-2026

> dataset · [Hugging Face](https://huggingface.co/datasets/eunguneun/korea-housing-subscription-score-2026)

한국 민간주택 청약 점수 체계의 2026년 점수표 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `A reusable CSV dataset for Korea's private-housing subscription point system.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · modality, readme = `A reusable CSV dataset` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:retrieval = `text` · 신뢰도 high
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `A reusable CSV dataset` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `5` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `Korea's private-housing subscription point system` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `A reusable CSV dataset for Korea's private-housing subscription point system.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `band` 열 p90 8자 ≈ 5 토큰 (viewer statistics, default/train)
