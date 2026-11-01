---
type: "dataset"
id: "kaggle/podongchip/119-call-transcript-synthetic-labels"
source: "kaggle"
url: "https://www.kaggle.com/datasets/podongchip/119-call-transcript-synthetic-labels"
downloads: 5
summary: "한국 119 응급 신고 합성 통화 텍스트에 Claude Sonnet 5로 구조화 라벨링한 데이터셋입니다."
readme_status: "ok"
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
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
---
# kaggle/podongchip/119-call-transcript-synthetic-labels

> dataset · [Kaggle](https://www.kaggle.com/datasets/podongchip/119-call-transcript-synthetic-labels)

한국 119 응급 신고 합성 통화 텍스트에 Claude Sonnet 5로 구조화 라벨링한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `라벨링한 구조화 필드 (call_type, ktas_level, ktas_evidence, chief_complaint, suspected_diagnosis, vitals, consciousness, symptoms, onset, incidents, disease_category, in` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `합성된 119 통화 텍스트` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Claude Sonnet 5로 라벨링한 구조화 필드` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `MIT` · 신뢰도 high
- **도메인**: [[의료·보건]] — ner · readme = `한국 119 응급 신고 통화를 바탕으로 만든 합성(synthetic) 텍스트` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = ``val.jsonl`: 360 rows` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = ``train.jsonl`: 1,438 rows` · 신뢰도 medium
