---
type: "dataset"
id: "pieroot/timesorter-scheduler-v9-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/pieroot/timesorter-scheduler-v9-ko"
downloads: 38
summary: "한국어 일정 스케줄링 JSON 입출력 데이터로 개인 비서 모델 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
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
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# pieroot/timesorter-scheduler-v9-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/pieroot/timesorter-scheduler-v9-ko)

한국어 일정 스케줄링 JSON 입출력 데이터로 개인 비서 모델 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `사용자 페르소나·현재 시각·할 일 목록(JSON)을 입력받아` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `태스크별 우선순위·4축 점수·추천 시간블록·근거(JSON)를 산출한다.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `3682` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `평가셋 (`eval` config, 59행 · KR+EN · held-out) 학습에 쓰지 않은 별도 held-out 평가셋.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `SFT: 1,993행 (sft config) — prompt(입력 JSON) / chosen(출력 JSON) / persona / today / source / meta` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `chosen` 열 p90 5523자 ≈ 3682 토큰 (viewer statistics, sft/train)
