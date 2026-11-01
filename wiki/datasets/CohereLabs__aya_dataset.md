---
type: "dataset"
id: "CohereLabs/aya_dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/CohereLabs/aya_dataset"
downloads: 21476
summary: "Aya Dataset는 65개 언어로 구성된 다국어 지침 파인튜닝용 데이터셋으로, 다국어 LLM 학습에 활용됨."
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
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# CohereLabs/aya_dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/CohereLabs/aya_dataset)

Aya Dataset는 65개 언어로 구성된 다국어 지침 파인튜닝용 데이터셋으로, 다국어 LLM 학습에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `multilingual instruction fine-tuning dataset` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `prompt-completion pairs` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `prompt-completion pairs` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `70 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `531` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multilingual instruction fine-tuning dataset curated by an open-science community` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `This dataset can be used to train, finetune, and evaluate multilingual LLMs.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This dataset can be used to train, finetune, and evaluate multilingual LLMs.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `targets` 열 p90 2124자 ≈ 531 토큰 (viewer statistics, default/test)

## 이 데이터로 학습한 모델

- [[Horizon-Labs__prompt-injection-guard-base|Horizon-Labs/prompt-injection-guard-base]]
- [[Horizon-Labs__prompt-injection-guard-small|Horizon-Labs/prompt-injection-guard-small]]
