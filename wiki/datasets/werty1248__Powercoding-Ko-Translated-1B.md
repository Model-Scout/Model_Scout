---
type: "dataset"
id: "werty1248/Powercoding-Ko-Translated-1B"
source: "huggingface"
url: "https://huggingface.co/datasets/werty1248/Powercoding-Ko-Translated-1B"
downloads: 46
summary: "PowerInfer/PowerCoding 데이터의 파이썬 코드 관련 텍스트를 한국어로 번역한 10억 토큰 분량 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[언어 모델링]]"
  - "[[번역]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# werty1248/Powercoding-Ko-Translated-1B

> dataset · [Hugging Face](https://huggingface.co/datasets/werty1248/Powercoding-Ko-Translated-1B)

PowerInfer/PowerCoding 데이터의 파이썬 코드 관련 텍스트를 한국어로 번역한 10억 토큰 분량 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `임베딩 모델: BAAI/bge-m3` · 신뢰도 medium
- **작업**: [[언어 모델링]] — ner · readme = `Synthetic coding pretrain data인 PowerInfer/PowerCoding 데이터` · 신뢰도 low
- **작업**: [[번역]] — ner · readme = `Qwen/Qwen3-30B-A3B` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:language_modeling, task:translation = `대체로 파이썬 코드 관련 텍스트로 이루어져 있긴 하지만, 코드가 없는 개발 관련 질문, sql 명령어 또한 일부 포함됨` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling, task:translation = `주석, 에러 메세지 등은 한국어로 번역하되, 함수명 등은 원문을 사용` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `3241` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `대체로 파이썬 코드 관련 텍스트로 이루어져 있긴 하지만, 코드가 없는 개발 관련 질문, sql 명령어 또한 일부 포함됨` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `약 1%, 약 10억 토큰 번역됨` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 4862자 ≈ 3241 토큰 (viewer statistics, default/train)
