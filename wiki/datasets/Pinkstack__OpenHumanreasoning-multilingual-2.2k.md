---
type: "dataset"
id: "Pinkstack/OpenHumanreasoning-multilingual-2.2k"
source: "huggingface"
url: "https://huggingface.co/datasets/Pinkstack/OpenHumanreasoning-multilingual-2.2k"
downloads: 28
summary: "Pinkstack/OpenHumanreasoning-multilingual-2.2k는 사람이 생성한 추론과 최종 결과를 포함한 다국어 데이터셋입니다."
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
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Pinkstack/OpenHumanreasoning-multilingual-2.2k

> dataset · [Hugging Face](https://huggingface.co/datasets/Pinkstack/OpenHumanreasoning-multilingual-2.2k)

Pinkstack/OpenHumanreasoning-multilingual-2.2k는 사람이 생성한 추론과 최종 결과를 포함한 다국어 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `it is a human-generated dataset where a real person had to create most of the reasoning and the final output` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `it is a human-generated dataset where a real person had to create most of the reasoning and the final output` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `23 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `166` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `We offer this dataset at an apache-2.0 license to make it useful for everybody.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `answer` 열 p90 664자 ≈ 166 토큰 (viewer statistics, default/train)
