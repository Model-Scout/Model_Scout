---
type: "dataset"
id: "alwaysgood/dqs-post-training"
source: "huggingface"
url: "https://huggingface.co/datasets/alwaysgood/dqs-post-training"
downloads: 34
summary: "영어-한국어 엄격 선호 데이터로 세 가지 후학습 목적에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[번역]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
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
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# alwaysgood/dqs-post-training

> dataset · [Hugging Face](https://huggingface.co/datasets/alwaysgood/dqs-post-training)

영어-한국어 엄격 선호 데이터로 세 가지 후학습 목적에 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Strict English-to-Korean preference data for three post-training objectives.` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:translation = `Strict English-to-Korean preference data` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `Strict English-to-Korean preference data` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `905` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Strict English-to-Korean preference data for three post-training objectives.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Each directory contains `train.jsonl` and `dataset_contract.json`.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `chosen` 열 p90 1357자 ≈ 905 토큰 (viewer statistics, cpo/train)
