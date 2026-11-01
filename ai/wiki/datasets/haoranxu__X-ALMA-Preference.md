---
type: "dataset"
id: "haoranxu/X-ALMA-Preference"
source: "huggingface"
url: "https://huggingface.co/datasets/haoranxu/X-ALMA-Preference"
downloads: 257
summary: "X-ALMA에서 사용하는 번역 선호도 데이터셋으로, 선호 번역과 비선호 번역을 포함함."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
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
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# haoranxu/X-ALMA-Preference

> dataset · [Hugging Face](https://huggingface.co/datasets/haoranxu/X-ALMA-Preference)

X-ALMA에서 사용하는 번역 선호도 데이터셋으로, 선호 번역과 비선호 번역을 포함함.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `This is the translation preference dataset used by X-ALMA.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `source: the source sentence.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `chosen: the preferred translation.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `50 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `530` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This is the translation preference dataset used by X-ALMA.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This is the translation preference dataset used by X-ALMA.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `chosen` 열 p90 2120자 ≈ 530 토큰 (viewer statistics, default/train)
