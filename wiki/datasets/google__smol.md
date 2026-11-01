---
type: "dataset"
id: "google/smol"
source: "huggingface"
url: "https://huggingface.co/datasets/google/smol"
downloads: 8305
summary: "SMOL은 221개 저자원 언어의 전문 번역 데이터로 번역 모델 학습에 활용됩니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[번역]]"
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
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# google/smol

> dataset · [Hugging Face](https://huggingface.co/datasets/google/smol)

SMOL은 221개 저자원 언어의 전문 번역 데이터로 번역 모델 학습에 활용됩니다.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:translation = `Source and Target language are provided in `sl` and `tl` fields` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `Source and Target language are provided in `sl` and `tl` fields` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `239 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `increasing the representations of said languages in NLP and technology` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `for the purpose of training translation models` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

## 같은 데이터의 사본·중복 등록

- `mabsoutwassim/smol`
