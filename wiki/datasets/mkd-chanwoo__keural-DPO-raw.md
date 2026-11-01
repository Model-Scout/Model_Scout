---
type: "dataset"
id: "mkd-chanwoo/keural-DPO-raw"
source: "huggingface"
url: "https://huggingface.co/datasets/mkd-chanwoo/keural-DPO-raw"
downloads: 23
summary: "keural-DPO의 전처리 전 원본 데이터를 재현성 위해 제공하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[리랭킹]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# mkd-chanwoo/keural-DPO-raw

> dataset · [Hugging Face](https://huggingface.co/datasets/mkd-chanwoo/keural-DPO-raw)

keural-DPO의 전처리 전 원본 데이터를 재현성 위해 제공하는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `keural-DPO의 전처리 전 normalized 원본 데이터.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation, task:reranking = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2113` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `원본 데이터셋 이름` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `ChatML 변환 및 필터링이 적용된 학습용 데이터는 mkd-chanwoo/keural-DPO 를 사용하세요.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `chosen` 열 p90 3169자 ≈ 2113 토큰 (viewer statistics, default/ultrafeedback)
