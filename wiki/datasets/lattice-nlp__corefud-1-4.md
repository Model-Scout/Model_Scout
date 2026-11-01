---
type: "dataset"
id: "lattice-nlp/corefud-1-4"
source: "huggingface"
url: "https://huggingface.co/datasets/lattice-nlp/corefud-1-4"
downloads: 56
summary: "corefud-1-4는 19개 언어의 공통 주어지시 해소 데이터셋을 통합한 코어퍼런스 해소용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
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
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
  - "[[조건부 이용]]"
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# lattice-nlp/corefud-1-4

> dataset · [Hugging Face](https://huggingface.co/datasets/lattice-nlp/corefud-1-4)

corefud-1-4는 19개 언어의 공통 주어지시 해소 데이터셋을 통합한 코어퍼런스 해소용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `benchmarking of coreference resolution systems` · 신뢰도 low
- **작업**: [[정보 추출]] — tag_match · readme, tags = `NER` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:information_extraction = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `coreference- and bridging-specific information encoded as attribute–value pairs` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `19 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `3312` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `coreference resolution dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `original corefud-1-4 coreference resolution dataset` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 13247자 ≈ 3312 토큰 (viewer statistics, default/train)
