---
type: "dataset"
id: "Uhhhghhhhhhh/Symmetric-Humanities-Corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/Uhhhghhhhhhh/Symmetric-Humanities-Corpus"
downloads: 41
summary: "일반문화, 철학, 신학 분야의 엄격한 주제 대칭을 갖춘 인문학 및 문화 말뭉치 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[학술·논문]]"
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# Uhhhghhhhhhh/Symmetric-Humanities-Corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/Uhhhghhhhhhh/Symmetric-Humanities-Corpus)

일반문화, 철학, 신학 분야의 엄격한 주제 대칭을 갖춘 인문학 및 문화 말뭉치 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · task_categories = `token-classification` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `A massive, culturally rich dataset hosted on Hugging Face Hub, engineered to achieve strict thematic symmetry across General Culture, Philosophy & Argumentation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:information_extraction, task:language_modeling = `General multilingual cultural and literary texts` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `General multilingual cultural and literary texts` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `13 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `5685` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `Philosophical encyclopedias, quotes, and structured debates` · 신뢰도 low
- **도메인**: [[문화·관광]] — tag_match · readme, tags = `culture` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `A massive, culturally rich dataset hosted on Hugging Face Hub` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 22739자 ≈ 5685 토큰 (viewer statistics, default/train)
