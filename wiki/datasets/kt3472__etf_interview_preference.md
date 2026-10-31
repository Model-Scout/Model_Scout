---
type: "dataset"
id: "kt3472/etf_interview_preference"
source: "huggingface"
url: "https://huggingface.co/datasets/kt3472/etf_interview_preference"
downloads: 10
summary: "ETF 인터뷰 선호도 데이터로, prompt와 선택/거절 문장 포함 학습용 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# kt3472/etf_interview_preference

> dataset · [Hugging Face](https://huggingface.co/datasets/kt3472/etf_interview_preference)

ETF 인터뷰 선호도 데이터로, prompt와 선택/거절 문장 포함 학습용 데이터입니다.

## 분류

- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `81` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `- name: train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `chosen` 열 p90 121자 ≈ 81 토큰 (viewer statistics, default/train)
