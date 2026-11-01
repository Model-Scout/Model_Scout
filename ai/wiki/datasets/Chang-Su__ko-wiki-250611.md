---
type: "dataset"
id: "Chang-Su/ko-wiki-250611"
source: "huggingface"
url: "https://huggingface.co/datasets/Chang-Su/ko-wiki-250611"
downloads: 35
summary: "2025년 6월 11일 기준 한국어 위키피디아 덤프를 문장 단위로 분할해 구축한 NLP 연구용 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Chang-Su/ko-wiki-250611

> dataset · [Hugging Face](https://huggingface.co/datasets/Chang-Su/ko-wiki-250611)

2025년 6월 11일 기준 한국어 위키피디아 덤프를 문장 단위로 분할해 구축한 NLP 연구용 데이터셋입니다.

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `한국어 자연어 처리(NLP) 연구 및 모델 학습을 위해 문장 단위로 분할하고, 일정 길이의 세그먼트로 재구성하여 사용 편의성을 높였습니다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:language_modeling = `자연어 문장을 기준으로 텍스트를 분할했습니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = ``text` (string): 전처리 과정을 거친 텍스트 데이터. 10개의 문장으로 구성된 하나의 문자열입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1478` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 위키피디아(Wikipedia)의 최신 덤프 파일(2025년 6월 11일 기준)을 기반으로 구축되었습니다.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `최신 한국어 위키피디아 데이터를 활용하고자 하는 필요성에 의해 직접 데이터를 정제하고 분할하여 본 데이터셋을 구축했습니다.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 2217자 ≈ 1478 토큰 (viewer statistics, default/train)
