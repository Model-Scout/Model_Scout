---
type: "dataset"
id: "songys/kor_qpair"
source: "huggingface"
url: "https://huggingface.co/datasets/songys/kor_qpair"
downloads: 150
summary: "두 질문의 의미적 동일성을 판단하는 한국어 질문 쌍 데이터셋입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# songys/kor_qpair

> dataset · [Hugging Face](https://huggingface.co/datasets/songys/kor_qpair)

두 질문의 의미적 동일성을 판단하는 한국어 질문 쌍 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `Korean paired question dataset` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `labels indicating whether two questions in a given pair are semantically identical` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[blackmallangcow__nari-decision-4b|blackmallangcow/nari-decision-4b]]
