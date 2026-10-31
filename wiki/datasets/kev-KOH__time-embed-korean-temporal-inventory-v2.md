---
type: "dataset"
id: "kev-KOH/time-embed-korean-temporal-inventory-v2"
source: "huggingface"
url: "https://huggingface.co/datasets/kev-KOH/time-embed-korean-temporal-inventory-v2"
downloads: 131
summary: "한국어 시간 표현 임베딩 학습 및 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# kev-KOH/time-embed-korean-temporal-inventory-v2

> dataset · [Hugging Face](https://huggingface.co/datasets/kev-KOH/time-embed-korean-temporal-inventory-v2)

한국어 시간 표현 임베딩 학습 및 평가용 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — metadata · readme, task_categories = `sentence-similarity` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding = `한국어 시간 표현 임베딩 학습·평가 데이터셋입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `한국어 시간 표현 임베딩 학습·평가 데이터셋입니다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `24` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 시간 표현 임베딩 학습·평가 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `legacy_validation, legacy_test: 기존 동결 dev/test bytes를 그대로 보존합니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `C1, C3, C5: 문맥 허용 범위가 다른 학습 조건이며 각 314개 query를 포함합니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `query` 열 p90 35자 ≈ 24 토큰 (viewer statistics, C1/train)
