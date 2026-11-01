---
type: "dataset"
id: "NetherQuartz/tokipona-proper-names-mt"
source: "huggingface"
url: "https://huggingface.co/datasets/NetherQuartz/tokipona-proper-names-mt"
downloads: 32
summary: "토키 포나 고유명사 패턴을 다국어 문장으로 생성해 토키포나 고유명사 규칙을 학습하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[번역]]"
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
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# NetherQuartz/tokipona-proper-names-mt

> dataset · [Hugging Face](https://huggingface.co/datasets/NetherQuartz/tokipona-proper-names-mt)

토키 포나 고유명사 패턴을 다국어 문장으로 생성해 토키포나 고유명사 규칙을 학습하는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Template-generated multilingual sentences for teaching Toki Pona proper noun conventions (tokiponization).` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = ``tok`, `en`, `ru`, ... `el` — parallel sentence in each language` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = ``tok`, `en`, `ru`, ... `el` — parallel sentence in each language` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `20 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `14` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Template-generated multilingual sentences for teaching Toki Pona proper noun conventions (tokiponization).` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train 6,440` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `el` 열 p90 57자 ≈ 14 토큰 (viewer statistics, default/train)
