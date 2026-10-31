---
type: "dataset"
id: "legesher/language-canon"
source: "huggingface"
url: "https://huggingface.co/datasets/legesher/language-canon"
downloads: 85
summary: "프로그래밍 개념의 자연어별 명칭을 언어 공동체가 표준화한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# legesher/language-canon

> dataset · [Hugging Face](https://huggingface.co/datasets/legesher/language-canon)

프로그래밍 개념의 자연어별 명칭을 언어 공동체가 표준화한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `A centralized standard, created and curated by language communities, for what programming concepts are called in each natural language.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification = `text` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `51 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `7` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Computer science as a global discipline is primarily based in English.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `option_uid` 열 p90 28자 ≈ 7 토큰 (viewer statistics, canon/train)
