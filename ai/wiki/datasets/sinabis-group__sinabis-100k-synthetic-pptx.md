---
type: "dataset"
id: "sinabis-group/sinabis-100k-synthetic-pptx"
source: "huggingface"
url: "https://huggingface.co/datasets/sinabis-group/sinabis-100k-synthetic-pptx"
downloads: 44
summary: "Sinabis 그룹의 101,000개 가상 비즈니스 프레젠테이션 데이터셋으로 문서 분석에 활용됨."
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
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# sinabis-group/sinabis-100k-synthetic-pptx

> dataset · [Hugging Face](https://huggingface.co/datasets/sinabis-group/sinabis-100k-synthetic-pptx)

Sinabis 그룹의 101,000개 가상 비즈니스 프레젠테이션 데이터셋으로 문서 분석에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — metadata · tags, task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · tags, task_categories = `token-classification` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `business presentations (.pptx) from the everyday operations of a fictional group of Sinabis companies` · 신뢰도 low
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · readme = `101,000 business presentations (.pptx)` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:embedding, task:generation, task:information_extraction, task:retrieval, task:summarization = `text` · 신뢰도 high
- **출력 형식**: [[문서 파일 (출력 형식)|문서 파일]] — ner · readme = `101,000 business presentations (.pptx)` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:summarization = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `24 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `4789` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `business presentations (.pptx) from the everyday operations of a fictional group of Sinabis companies` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This is the 100k edition of sinabis-1m-synthetic-pptx: the first 101,000 presentations of the 1M dataset` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `notes` 열 p90 19156자 ≈ 4789 토큰 (viewer statistics, default/train)
