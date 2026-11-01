---
type: "dataset"
id: "nvidia/HelpSteer3"
source: "huggingface"
url: "https://huggingface.co/datasets/nvidia/HelpSteer3"
downloads: 19063
summary: "HelpSteer3는 사용자 프롬프트에 더 도움이 되는 모델 정렬을 지원하는 오픈소스 데이터셋입니다."
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
  - "[[중규모 데이터]]"
---
# nvidia/HelpSteer3

> dataset · [Hugging Face](https://huggingface.co/datasets/nvidia/HelpSteer3)

HelpSteer3는 사용자 프롬프트에 더 도움이 되는 모델 정렬을 지원하는 오픈소스 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `HelpSteer3 is an open-source dataset (CC-BY-4.0) that supports aligning models to become more helpful in responding to user prompts.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `HelpSteer3 is an open-source dataset (CC-BY-4.0) that supports aligning models to become more helpful in responding to user prompts.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `HelpSteer3 is an open-source dataset (CC-BY-4.0) that supports aligning models to become more helpful in responding to user prompts.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `14 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `787` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `HelpSteer3 is an open-source dataset (CC-BY-4.0) that supports aligning models to become more helpful in responding to user prompts.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `HelpSteer3-Preference can be used to train Llama 3.3 Nemotron Super 49B v1 (for Generative RMs) and Llama 3.3 70B Instruct Models (for Bradley-Terry RMs) to pro` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `response2` 열 p90 3149자 ≈ 787 토큰 (viewer statistics, preference/validation)

## 같은 데이터의 사본·중복 등록

- `chilomax/HelpSteer3`
- `slaveyard/HelpSteer3`
- `sunorme/HelpSteer3`

## 이 데이터로 학습한 모델

- [[bartowski__nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF|bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF]]
- [[nvidia__Llama-3.3-Nemotron-70B-Reward-Multilingual|nvidia/Llama-3.3-Nemotron-70B-Reward-Multilingual]]
- [[nvidia__Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual|nvidia/Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual]]
