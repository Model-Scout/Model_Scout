---
type: "dataset"
id: "ai-enthusiasm-community/XM3600"
source: "huggingface"
url: "https://huggingface.co/datasets/ai-enthusiasm-community/XM3600"
downloads: 52
summary: "XM3600 데이터셋은 이미지와 다국어 캡션을 포함한 시각-언어 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[이미지 생성]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ai-enthusiasm-community/XM3600

> dataset · [Hugging Face](https://huggingface.co/datasets/ai-enthusiasm-community/XM3600)

XM3600 데이터셋은 이미지와 다국어 캡션을 포함한 시각-언어 데이터셋입니다.

## 분류

- **작업**: [[이미지 생성]] — metadata · task_categories = `text-to-image` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:image_generation, task:visual_qa = ``image`: A Image object containing the visual data.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:image_generation, task:visual_qa = ``caption_ `: The description in different languages.` · 신뢰도 high
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — task_rule · task:image_generation = `image` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:visual_qa = ``caption_ `: The description in different languages.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `34 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The dataset is provided in a flattened tabular format, optimized for the Hugging Face Dataset Viewer and high-speed Parquet processing.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset can be accessed directly using the Hugging Face `datasets` library:` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
