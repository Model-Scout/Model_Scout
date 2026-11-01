---
type: "dataset"
id: "Bingsu/laion-translated-to-en-korean-subset"
source: "huggingface"
url: "https://huggingface.co/datasets/Bingsu/laion-translated-to-en-korean-subset"
downloads: 109
summary: "한국어만 포함된 laion 데이터셋의 하위 집합으로 이미지-텍스트 쌍 학습용 데이터입니다."
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
  - "[[한국어]]"
input_length:
  - "[[단문]]"
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
# Bingsu/laion-translated-to-en-korean-subset

> dataset · [Hugging Face](https://huggingface.co/datasets/Bingsu/laion-translated-to-en-korean-subset)

한국어만 포함된 laion 데이터셋의 하위 집합으로 이미지-텍스트 쌍 학습용 데이터입니다.

## 분류

- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `a subset data of laion/laion2B-multi-joined-translated-to-en and laion/laion1B-nolang-joined-translated-to-en, including only korean` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `'TEXT': `string`` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `'ENG TEXT': `string`` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `119` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a subset data of laion/laion2B-multi-joined-translated-to-en and laion/laion1B-nolang-joined-translated-to-en, including only korean` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train: Dataset({ features: ['hash', 'URL'…` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `ENG TEXT` 열 p90 179자 ≈ 119 토큰 (viewer statistics, default/train)
