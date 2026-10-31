---
type: "dataset"
id: "google/wmt24pp"
source: "huggingface"
url: "https://huggingface.co/datasets/google/wmt24pp"
downloads: 9462
summary: "WMT24++는 55개 언어 쌍의 영어-다국어 번역 및 후편집 데이터를 제공하는 번역 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
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
# google/wmt24pp

> dataset · [Hugging Face](https://huggingface.co/datasets/google/wmt24pp)

WMT24++는 55개 언어 쌍의 영어-다국어 번역 및 후편집 데이터를 제공하는 번역 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `If you are interested in the MT/LLM system outputs and automatic metric scores, please see MTME.` · 신뢰도 medium
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation, task:translation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:translation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `48 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `112` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This repository contains the human translation and post-edit data for the 55 en->xx language pairs` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This repository contains the human translation and post-edit data for the 55 en->xx language pairs` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `source` 열 p90 447자 ≈ 112 토큰 (viewer statistics, en-ko_KR/train)

## 이 데이터로 학습한 모델

- [[ByteDance-Seed__Seed-X-PPO-7B|ByteDance-Seed/Seed-X-PPO-7B]]
- [[ByteDance-Seed__Seed-X-PPO-7B-AWQ-Int4|ByteDance-Seed/Seed-X-PPO-7B-AWQ-Int4]]
- [[ByteDance-Seed__Seed-X-PPO-7B-GPTQ-Int8|ByteDance-Seed/Seed-X-PPO-7B-GPTQ-Int8]]
- [[winninghealth__WiNGPT-Babel-2-GGUF|winninghealth/WiNGPT-Babel-2-GGUF]]
