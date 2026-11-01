---
type: "dataset"
id: "FreedomIntelligence/ApolloMoEDataset"
source: "huggingface"
url: "https://huggingface.co/datasets/FreedomIntelligence/ApolloMoEDataset"
downloads: 556
summary: "12개 주요 언어와 38개 소수 언어를 포함한 의료 분야 다국어 LLM 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# FreedomIntelligence/ApolloMoEDataset

> dataset · [Hugging Face](https://huggingface.co/datasets/FreedomIntelligence/ApolloMoEDataset)

12개 주요 언어와 38개 소수 언어를 포함한 의료 분야 다국어 LLM 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Democratizing Medical LLMs For Much More Languages` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `User:{query}\nAssistant:{response}` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `User:{query}\nAssistant:{response}` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `44 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `medical` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `Evaluate your model: Generate score for benchmark` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `If you want to train in Multi Nodes please refer to ./src/sft/training_config/zero_multi.yaml` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[FreedomIntelligence__Apollo-MoE-0.5B|FreedomIntelligence/Apollo-MoE-0.5B]]
- [[FreedomIntelligence__Apollo-MoE-7B|FreedomIntelligence/Apollo-MoE-7B]]
- [[FreedomIntelligence__Apollo2-3.8B|FreedomIntelligence/Apollo2-3.8B]]
- [[FreedomIntelligence__Apollo2-7B|FreedomIntelligence/Apollo2-7B]]
- [[FreedomIntelligence__Apollo2-9B|FreedomIntelligence/Apollo2-9B]]
- [[QuantFactory__Apollo2-2B-GGUF|QuantFactory/Apollo2-2B-GGUF]]
- [[QuantFactory__Apollo2-7B-GGUF|QuantFactory/Apollo2-7B-GGUF]]
- [[QuantFactory__Apollo2-9B-GGUF|QuantFactory/Apollo2-9B-GGUF]]
- [[cgus__Apollo2-7B-iMat-GGUF|cgus/Apollo2-7B-iMat-GGUF]]
