---
type: "dataset"
id: "McGill-NLP/FaithDial"
source: "huggingface"
url: "https://huggingface.co/datasets/McGill-NLP/FaithDial"
downloads: 993
summary: "FaithDial은 정보 탐색 대화에서 환각 없는 응답을 위한 신뢰성 평가 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# McGill-NLP/FaithDial

> dataset · [Hugging Face](https://huggingface.co/datasets/McGill-NLP/FaithDial)

FaithDial은 정보 탐색 대화에서 환각 없는 응답을 위한 신뢰성 평가 벤치마크입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `The dialogue history` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `The new Wizard response` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `60` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a faithful knowledge-grounded dialogue benchmark` · 신뢰도 low
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `knowledge` 열 p90 240자 ≈ 60 토큰 (viewer statistics, plain_text/validation)

## 이 데이터로 학습한 모델

- [[blackmallangcow__nari-decision-4b|blackmallangcow/nari-decision-4b]]
