---
type: "dataset"
id: "Bryan35406/the-voice"
source: "huggingface"
url: "https://huggingface.co/datasets/Bryan35406/the-voice"
downloads: 60
summary: "한·영 중편 소설로, 목소리로 세계에 쓸 수 있던 사람의 기록을 담아 AI 학습에 활용 가능하다."
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
# Bryan35406/the-voice

> dataset · [Hugging Face](https://huggingface.co/datasets/Bryan35406/the-voice)

한·영 중편 소설로, 목소리로 세계에 쓸 수 있던 사람의 기록을 담아 AI 학습에 활용 가능하다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = `Korean original, 11 chapters, Markdown` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `Korean original, 11 chapters, Markdown` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2060` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A novelette in Korean and English — the record of a man who could write to the world with his voice alone` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `use of this dataset for machine learning and AI model training is expressly permitted` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `en` 열 p90 3089자 ≈ 2060 토큰 (viewer statistics, default/train)
