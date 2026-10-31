---
type: "dataset"
id: "rombodawg/Everything_Instruct_Multilingual"
source: "huggingface"
url: "https://huggingface.co/datasets/rombodawg/Everything_Instruct_Multilingual"
downloads: 53
summary: "다양한 주제와 다국어를 포함한 대규모 alpaca instruct 형식 데이터셋으로 LLM 학습용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# rombodawg/Everything_Instruct_Multilingual

> dataset · [Hugging Face](https://huggingface.co/datasets/rombodawg/Everything_Instruct_Multilingual)

다양한 주제와 다국어를 포함한 대규모 alpaca instruct 형식 데이터셋으로 LLM 학습용입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Everything instruct (Multilingual Edition) is a massive alpaca instruct formatted dataset consisting of a wide variety of topics meant to bring LLM's to the nex` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Everything instruct (Multilingual Edition) is a massive alpaca instruct formatted dataset` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Everything instruct (Multilingual Edition) is a massive alpaca instruct formatted dataset` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `15 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2802` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Everything instruct (Multilingual Edition) is a massive alpaca instruct formatted dataset consisting of a wide variety of topics` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `I hope you finetune some amazing models that break the barrier between open and closed source with my data.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 11208자 ≈ 2802 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[QuantFactory__Llama-3.2-Taiwan-3B-Instruct-GGUF|QuantFactory/Llama-3.2-Taiwan-3B-Instruct-GGUF]]
