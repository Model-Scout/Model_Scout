---
type: "dataset"
id: "trentmkelly/asianfanfics"
source: "huggingface"
url: "https://huggingface.co/datasets/trentmkelly/asianfanfics"
downloads: 221
summary: "Asianfanfics의 메타데이터와 공개 챕터 텍스트를 포함한 소설 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
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
  - "[[대규모 데이터]]"
---
# trentmkelly/asianfanfics

> dataset · [Hugging Face](https://huggingface.co/datasets/trentmkelly/asianfanfics)

Asianfanfics의 메타데이터와 공개 챕터 텍스트를 포함한 소설 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Story-level metadata and text-fetch status.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `metadata and public chapter text from Asianfanfics` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `public chapter text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `public chapter text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `multilingual` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `4432` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Asianfanfics Archive` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains metadata and public chapter text from Asianfanfics` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 17729자 ≈ 4432 토큰 (viewer statistics, chapters/train)
