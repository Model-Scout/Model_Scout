---
type: "dataset"
id: "DGME/wmt25"
source: "huggingface"
url: "https://huggingface.co/datasets/DGME/wmt25"
downloads: 115
summary: "다양한 언어 쌍의 번역 학습용 데이터셋입니다."
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
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# DGME/wmt25

> dataset · [Hugging Face](https://huggingface.co/datasets/DGME/wmt25)

다양한 언어 쌍의 번역 학습용 데이터셋입니다.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `language:
- ar
- bg
- bn
- ca
- da
- de
- el
- es
- et
- fa
- fi
- fr
- gu
- he
- hi
- hr
- hu
- id
- is
- it
- ja
- kn
- ko
- lt
- lv
- ml
- mr
- nl
- 'no'
- p` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `task_categories:
- translation` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `48 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `65` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `- split: train` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `src_text` 열 p90 260자 ≈ 65 토큰 (viewer statistics, en-ko_KR/train)
