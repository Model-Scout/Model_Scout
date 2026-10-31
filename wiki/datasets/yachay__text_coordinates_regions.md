---
type: "dataset"
id: "yachay/text_coordinates_regions"
source: "huggingface"
url: "https://huggingface.co/datasets/yachay/text_coordinates_regions"
downloads: 275
summary: "123개 세계 주요 지역의 지리 좌표가 포함된 다국어 소셜 미디어 텍스트 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[정보 추출]]"
  - "[[문서 검색]]"
  - "[[번역]]"
input_modality:
  - "[[위치·좌표 (입력 형식)|위치·좌표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[위치·좌표 (출력 형식)|위치·좌표]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[지리·위치]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# yachay/text_coordinates_regions

> dataset · [Hugging Face](https://huggingface.co/datasets/yachay/text_coordinates_regions)

123개 세계 주요 지역의 지리 좌표가 포함된 다국어 소셜 미디어 텍스트 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 high
- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · tags, task_categories = `token-classification` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `This dataset is well-suited for tasks such as geotagging, where the objective is to associate text with specific geographical locations.` · 신뢰도 low
- **작업**: [[번역]] — tag_match · tags = `translation` · 신뢰도 low
- **입력 형식**: [[위치·좌표 (입력 형식)|위치·좌표]] — ner · modality, readme = `Each text sample is associated with geocoordinates.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:information_extraction, task:retrieval, task:translation = `This field contains the text sample, typically holds natural language text data, such as comments, tweets, or any text-based content.` · 신뢰도 high
- **출력 형식**: [[위치·좌표 (출력 형식)|위치·좌표]] — ner · readme = `Each text sample is associated with geocoordinates.` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `26 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `49` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[지리·위치]] — ner · readme = `The "Regions" dataset is a multilingual corpus that encompasses textual data from the 123 most populated regions worldwide, with each region's data organized in` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The "Regions" dataset was created with an objective to train and enhance geotagging textual models.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 196자 ≈ 49 토큰 (viewer statistics, default/train)
