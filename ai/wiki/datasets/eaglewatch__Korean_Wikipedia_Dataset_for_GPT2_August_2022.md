---
type: "dataset"
id: "eaglewatch/Korean_Wikipedia_Dataset_for_GPT2_August_2022"
source: "huggingface"
url: "https://huggingface.co/datasets/eaglewatch/Korean_Wikipedia_Dataset_for_GPT2_August_2022"
downloads: 181
summary: "2022년 8월 기준 한국어 위키피디아 전체 데이터를 GPT-2 학습용으로 제공하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[언어 모델링]]"
  - "[[질의응답]]"
  - "[[번역]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# eaglewatch/Korean_Wikipedia_Dataset_for_GPT2_August_2022

> dataset · [Hugging Face](https://huggingface.co/datasets/eaglewatch/Korean_Wikipedia_Dataset_for_GPT2_August_2022)

2022년 8월 기준 한국어 위키피디아 전체 데이터를 GPT-2 학습용으로 제공하는 데이터셋입니다.

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `Entire Korean language Wikipedia data for GPT-2 training as of August 1st, 2022.` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories, task_ids = `question-answering` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories, task_ids = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:language_modeling, task:question_answering, task:translation, task:visual_qa = `Entire Korean language Wikipedia data` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling, task:question_answering, task:translation, task:visual_qa = `Entire Korean language Wikipedia data for GPT-2 training` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `9778` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — tag_match · readme, tags = `wikipedia` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Train wikipedia article count: 334420
validation wikipedia article count: 83605` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 14668자 ≈ 9778 토큰 (viewer statistics, default/train)
