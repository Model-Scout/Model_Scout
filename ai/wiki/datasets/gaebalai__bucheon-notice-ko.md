---
type: "dataset"
id: "gaebalai/bucheon-notice-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/gaebalai/bucheon-notice-ko"
downloads: 5
summary: "부천시 고시/공고 원문을 Harmony 포맷 학습 데이터로 변환한 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# gaebalai/bucheon-notice-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/gaebalai/bucheon-notice-ko)

부천시 고시/공고 원문을 Harmony 포맷 학습 데이터로 변환한 데이터셋입니다.

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `부천시 고시/공고 원문을 기반으로 Harmony 포맷 학습 데이터로 변환했습니다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:language_modeling = `부천시 고시/공고 원문` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `assistant의 <content> 구간은 아래 JSON 스키마를 따릅니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `부천시 고시/공고 원문` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Harmony 포맷 학습 데이터로 변환했습니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
