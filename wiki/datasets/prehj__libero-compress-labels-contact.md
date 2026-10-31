---
type: "dataset"
id: "prehj/libero-compress-labels-contact"
source: "huggingface"
url: "https://huggingface.co/datasets/prehj/libero-compress-labels-contact"
downloads: 27
summary: "LIBERO 데이터셋의 바이너리 압축 라벨로, 접촉 정책을 반영하여 40개 작업에 대해 266,693개의 라벨을 포함함"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# prehj/libero-compress-labels-contact

> dataset · [Hugging Face](https://huggingface.co/datasets/prehj/libero-compress-labels-contact)

LIBERO 데이터셋의 바이너리 압축 라벨로, 접촉 정책을 반영하여 40개 작업에 대해 266,693개의 라벨을 포함함

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `LIBERO binary compression labels (contact overrides)` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `The default sidecar contains one parquet per original episode.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Two optional `[binary_class, valid]` float32 carriers are `compress_2p5_label` and `compress_3_label`.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Derived from the existing LIBERO confidence release.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `No new VLM inference or policy evaluation was performed.` · 신뢰도 low
