---
type: "dataset"
id: "piper-plus/piper-plus-multilingual-7lang-v8-audit"
source: "huggingface"
url: "https://huggingface.co/datasets/piper-plus/piper-plus-multilingual-7lang-v8-audit"
downloads: 56
summary: "7개 언어 음성 데이터 메타데이터 감사용 데이터셋으로 학습용 임베딩 포함"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[음성 합성]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[pt]]"
  - "[[중국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# piper-plus/piper-plus-multilingual-7lang-v8-audit

> dataset · [Hugging Face](https://huggingface.co/datasets/piper-plus/piper-plus-multilingual-7lang-v8-audit)

7개 언어 음성 데이터 메타데이터 감사용 데이터셋으로 학습용 임베딩 포함

## 분류

- **작업**: [[임베딩]] — ner · readme = `The essential archive contains exactly one 192-dimensional float32 embedding per training row.` · 신뢰도 medium
- **작업**: [[음성 합성]] — tag_match · tags = `text-to-speech` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:text_to_speech = `This metadata-only audit describes ayousanz/piper-plus-multilingual-7lang-v8-dataset` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The essential archive contains exactly one 192-dimensional float32 embedding per training row.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `7 languages` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `The fixed revision has 342,855 training rows across 3,682 speakers plus a speaker-safe 1,200-row holdout` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
