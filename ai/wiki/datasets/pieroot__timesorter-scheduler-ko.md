---
type: "dataset"
id: "pieroot/timesorter-scheduler-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/pieroot/timesorter-scheduler-ko"
downloads: 33
summary: "한국어 일정 우선순위 정렬을 위한 4축 평가 기반 모델 학습용 데이터셋입니다."
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
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# pieroot/timesorter-scheduler-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/pieroot/timesorter-scheduler-ko)

한국어 일정 우선순위 정렬을 위한 4축 평가 기반 모델 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `할 일 목록을 4축(긴급도·중요도·의존성·시간 제약, 각 1-5)으로 채점하고 우선순위를 결정하는 모델 학습용 데이터.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `할 일 목록을 4축(긴급도·중요도·의존성·시간 제약, 각 1-5)으로 채점하고 우선순위를 결정하는 모델 학습용 데이터.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `우선순위를 결정하는 모델 학습용 데이터.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `872` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 일정 우선순위 정렬 데이터셋` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `held-out 자동 평가` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `SFT 본 학습 (v2~v5+rework, curated 3.4K+rework 1.4K)` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `chosen` 열 p90 1309자 ≈ 872 토큰 (viewer statistics, sft/train)
