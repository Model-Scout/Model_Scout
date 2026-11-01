---
type: "dataset"
id: "oist/multimodal_nli_dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/oist/multimodal_nli_dataset"
downloads: 43
summary: "다국어 및 다중모달 자연어 추론(NLI) 데이터셋으로 텍스트와 음성 간 추론 분류에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# oist/multimodal_nli_dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/oist/multimodal_nli_dataset)

다국어 및 다중모달 자연어 추론(NLI) 데이터셋으로 텍스트와 음성 간 추론 분류에 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `It enables classification of entailment, contradiction, and neutrality across four modality combinations` · 신뢰도 medium
- **작업**: [[임베딩]] — metadata · task_categories = `sentence-similarity` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:embedding = `text` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `15 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `45` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multilingual and multimodal Natural Language Inference (NLI)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Number of splits: train, validation, test` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `premise_text` 열 p90 179자 ≈ 45 토큰 (viewer statistics, default/validation)
