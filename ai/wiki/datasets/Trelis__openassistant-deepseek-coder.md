---
type: "dataset"
id: "Trelis/openassistant-deepseek-coder"
source: "huggingface"
url: "https://huggingface.co/datasets/Trelis/openassistant-deepseek-coder"
downloads: 148
summary: "OpenAssistant 대화 데이터셋으로, 챗봇 모델 파인튜닝에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
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
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Trelis/openassistant-deepseek-coder

> dataset · [Hugging Face](https://huggingface.co/datasets/Trelis/openassistant-deepseek-coder)

OpenAssistant 대화 데이터셋으로, 챗봇 모델 파인튜닝에 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `annotated with 461,292 quality ratings` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `This dataset allows for fine-tuning chat models` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `human-generated, human-annotated assistant-style conversation corpus consisting of 161,443 messages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `assistant responses` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `35 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `776` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a human-generated, human-annotated assistant-style conversation corpus consisting of 161,443 messages in 35 different languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This subset of the data only contains the highest-rated paths in the conversation tree, with a total of 9,846 samples` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 3102자 ≈ 776 토큰 (viewer statistics, default/test)
