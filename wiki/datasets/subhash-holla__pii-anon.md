---
type: "dataset"
id: "subhash-holla/pii-anon"
source: "huggingface"
url: "https://huggingface.co/datasets/subhash-holla/pii-anon"
downloads: 287
summary: "60개 언어, 66개 엔티티 유형의 다국어 PII 벤치마크 코퍼스 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
  - "[[리랭킹]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# subhash-holla/pii-anon

> dataset · [Hugging Face](https://huggingface.co/datasets/subhash-holla/pii-anon)

60개 언어, 66개 엔티티 유형의 다국어 PII 벤치마크 코퍼스 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `five legally-distinct regulatory regime signals (gov-02 / FR-022) as separate reg_* columns` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · readme, task_categories = `token-classification` · 신뢰도 medium
- **작업**: [[리랭킹]] — ner · readme = `behavioral-signal / RRS scoring runs on this substrate` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:information_extraction, task:reranking = `782,677 records carrying 3,107,240 entity annotations` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `entity annotations across 66 entity types` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `60 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A CC0 multilingual PII benchmark corpus of 782,677 records` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `The 159,891 tier3_evaluation records are the EVALUATION substrate` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The 782,677-record corpus` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
