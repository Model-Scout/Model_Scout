---
type: "dataset"
id: "Bryan35406/nykh"
source: "huggingface"
url: "https://huggingface.co/datasets/Bryan35406/nykh"
downloads: 66
summary: "한·영 병렬 소설 'A Wild ных Chase'로, AI 모델 학습용으로 허용된 문학 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Bryan35406/nykh

> dataset · [Hugging Face](https://huggingface.co/datasets/Bryan35406/nykh)

한·영 병렬 소설 'A Wild ных Chase'로, AI 모델 학습용으로 허용된 문학 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = `Korean original, 7 chapters, Markdown` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `a large language model, in Korean and English as a scene-aligned mirror` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2269` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a novelette that leans on A Wild Sheep Chase — three Cyrillic letters keep arriving at the ends of a model's sentences` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `use of this dataset for machine learning and AI model training is expressly permitted` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `en` 열 p90 3403자 ≈ 2269 토큰 (viewer statistics, default/train)
