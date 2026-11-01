---
type: "dataset"
id: "whoisjones/fiNERweb"
source: "huggingface"
url: "https://huggingface.co/datasets/whoisjones/fiNERweb"
downloads: 652
summary: "fiNERweb는 다국어 개체명 인식 데이터셋으로 여러 언어의 텍스트와 개체명 위치 정보를 포함합니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[정보 추출]]"
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
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# whoisjones/fiNERweb

> dataset · [Hugging Face](https://huggingface.co/datasets/whoisjones/fiNERweb)

fiNERweb는 다국어 개체명 인식 데이터셋으로 여러 언어의 텍스트와 개체명 위치 정보를 포함합니다.

## 분류

- **작업**: [[정보 추출]] — metadata · readme, task_categories, task_ids = `token-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction = `Original text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Character spans for entities` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `91 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `67` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `fiNERweb is a multilingual named entity recognition dataset containing annotated text in multiple languages.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 268자 ≈ 67 토큰 (viewer statistics, kor/train)
