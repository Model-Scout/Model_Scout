---
type: "dataset"
id: "LiquidAI/structured-extraction"
source: "huggingface"
url: "https://huggingface.co/datasets/LiquidAI/structured-extraction"
downloads: 72
summary: "35개 문서 유형과 16개 언어의 문서에서 JSON 스키마 기반 구조화된 정보 추출 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
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
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# LiquidAI/structured-extraction

> dataset · [Hugging Face](https://huggingface.co/datasets/LiquidAI/structured-extraction)

35개 문서 유형과 16개 언어의 문서에서 JSON 스키마 기반 구조화된 정보 추출 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — tag_match · readme, tags = `information-extraction` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:information_extraction = `document text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `the JSON object extracted from them` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `16 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `430` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The documents (emails, receipts, bookings, forms, letters, listings, ...) cover 35 document types in 16 languages.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `test 500 the same 30 document types, other documents` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train 6,000 30 document types` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `schema` 열 p90 1721자 ≈ 430 토큰 (viewer statistics, default/test)
