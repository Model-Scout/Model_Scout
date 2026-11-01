---
type: "dataset"
id: "brandonrhie/korean-public-figures-saju"
source: "huggingface"
url: "https://huggingface.co/datasets/brandonrhie/korean-public-figures-saju"
downloads: 52
summary: "한국 공인 39,494명의 생년월일과 사주 정보를 포함한 데이터셋으로, 사주가 직업 예측에 유용한지 검증에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# brandonrhie/korean-public-figures-saju

> dataset · [Hugging Face](https://huggingface.co/datasets/brandonrhie/korean-public-figures-saju)

한국 공인 39,494명의 생년월일과 사주 정보를 포함한 데이터셋으로, 사주가 직업 예측에 유용한지 검증에 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Multi-label occupation classification baseline` · 신뢰도 medium
- **작업**: [[임베딩]] — ner · readme = `Empirical validation of Saju / Bazi astrology claims (occupation prediction, day-master analysis)` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — metadata · task_categories = `tabular-classification` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:tabular_prediction = `table` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding = `39,494 Korean public figures (politicians, actors, athletes, etc.) with verified day-precision birth dates, occupations, and computed Saju (사주, four-pillars / b` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Multi-label occupation classification baseline` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `27` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — tag_match · readme, tags = `wikipedia` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `source_wikidata` 열 p90 40자 ≈ 27 토큰 (viewer statistics, default/train)
