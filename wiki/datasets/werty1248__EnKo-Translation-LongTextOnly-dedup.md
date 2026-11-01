---
type: "dataset"
id: "werty1248/EnKo-Translation-LongTextOnly-dedup"
source: "huggingface"
url: "https://huggingface.co/datasets/werty1248/EnKo-Translation-LongTextOnly-dedup"
downloads: 25
summary: "장문 한영 번역 데이터로, gemma 토크나이저 기준 1K 이상 토큰 데이터만 포함합니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
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
# werty1248/EnKo-Translation-LongTextOnly-dedup

> dataset · [Hugging Face](https://huggingface.co/datasets/werty1248/EnKo-Translation-LongTextOnly-dedup)

장문 한영 번역 데이터로, gemma 토크나이저 기준 1K 이상 토큰 데이터만 포함합니다.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `영문+한글 토큰 합이 1K 이상인 데이터만 추출` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `영문+한글 토큰 합이 1K 이상인 데이터만 추출` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2510` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `장문 번역 데이터만 추출` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `nayohan/aihub-en-ko-translation-12m` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `english` 열 p90 3765자 ≈ 2510 토큰 (viewer statistics, default/train)
