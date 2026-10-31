---
type: "dataset"
id: "pieroot/timesorter-dpo-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/pieroot/timesorter-dpo-ko"
downloads: 14
summary: "한국어 일정 우선순위 선호 학습용 DPO 데이터셋으로, 버전별 증분 데이터를 포함함."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
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
  - "[[중규모 데이터]]"
---
# pieroot/timesorter-dpo-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/pieroot/timesorter-dpo-ko)

한국어 일정 우선순위 선호 학습용 DPO 데이터셋으로, 버전별 증분 데이터를 포함함.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `선호 학습(chosen vs rejected)용 데이터` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `893` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 일정 우선순위 DPO 데이터셋` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `선호 학습(chosen vs rejected)용 데이터` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `chosen` 열 p90 1339자 ≈ 893 토큰 (viewer statistics, v6/train)
