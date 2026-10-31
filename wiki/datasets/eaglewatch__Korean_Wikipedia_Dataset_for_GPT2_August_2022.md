---
type: "dataset"
id: "eaglewatch/Korean_Wikipedia_Dataset_for_GPT2_August_2022"
source: "huggingface"
url: "https://huggingface.co/datasets/eaglewatch/Korean_Wikipedia_Dataset_for_GPT2_August_2022"
downloads: 379
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
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
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# eaglewatch/Korean_Wikipedia_Dataset_for_GPT2_August_2022

> dataset · [Hugging Face](https://huggingface.co/datasets/eaglewatch/Korean_Wikipedia_Dataset_for_GPT2_August_2022)

## 분류

- **작업**: [[질의응답]] — metadata · task_categories, task_ids = `question-answering` · 신뢰도 high
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 high
- **작업**: [[이미지 이해]] — metadata · task_categories, task_ids = `visual-question-answering` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:question_answering, task:translation, task:visual_qa = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering, task:translation, task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — tag_match · tags = `wikipedia` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
