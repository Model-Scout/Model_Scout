---
type: "dataset"
id: "sinabis-group/sinabis-1m-synthetic-pptx"
source: "huggingface"
url: "https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-pptx"
downloads: 274
summary: "Sinabis 그룹의 100만 개 이상의 가상 비즈니스 프레젠테이션 pptx 문서 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[문서 검색]]"
  - "[[요약]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[문서 파일 (출력 형식)|문서 파일]]"
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
  - "[[상거래·상품]]"
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# sinabis-group/sinabis-1m-synthetic-pptx

> dataset · [Hugging Face](https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-pptx)

Sinabis 그룹의 100만 개 이상의 가상 비즈니스 프레젠테이션 pptx 문서 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — metadata · readme, tags, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[정보 추출]] — metadata · tags, task_categories = `token-classification` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `More than 1,005,852 business presentations (.pptx)` · 신뢰도 low
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · readme = `More than 1,005,852 business presentations (.pptx)` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:generation, task:information_extraction, task:retrieval, task:summarization = `Deck contents come from LLM-written blueprints (Gemma 4 26B-A4B) in the target language: an outline per deck, then fully written slides in blocks of seven` · 신뢰도 high
- **출력 형식**: [[문서 파일 (출력 형식)|문서 파일]] — ner · readme = `Slides are rendered with `python-pptx` in 17 layouts (title, agenda, section, bullets, two/three columns, KPI tiles, table, native chart, timeline, process, quo` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:summarization = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `24 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `4784` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `More than 1,005,852 business presentations (.pptx) from the everyday operations of a fictional group of Sinabis companies` · 신뢰도 low
- **도메인**: [[일반]] — ner · readme = `Every person, company, address, phone number, financial figure and project in this dataset is purely fictional.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Deck contents come from LLM-written blueprints (Gemma 4 26B-A4B) in the target language: an outline per deck, then fully written slides in blocks of seven` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `notes` 열 p90 19135자 ≈ 4784 토큰 (viewer statistics, default/train)
