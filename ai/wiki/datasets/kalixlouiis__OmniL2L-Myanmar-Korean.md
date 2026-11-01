---
type: "dataset"
id: "kalixlouiis/OmniL2L-Myanmar-Korean"
source: "huggingface"
url: "https://huggingface.co/datasets/kalixlouiis/OmniL2L-Myanmar-Korean"
downloads: 19
summary: "미얀마어-한국어 병렬 번역 데이터셋으로 저자원 기계번역에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[my]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# kalixlouiis/OmniL2L-Myanmar-Korean

> dataset · [Hugging Face](https://huggingface.co/datasets/kalixlouiis/OmniL2L-Myanmar-Korean)

미얀마어-한국어 병렬 번역 데이터셋으로 저자원 기계번역에 활용됨.

## 분류

- **작업**: [[번역]] — metadata · readme, tags, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `Base conversational sentences in Myanmar text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `Corresponding translation in Korean` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[my]] — metadata · languages = `my` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `30` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `General daily-life conversational text sourced from the public domain.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is custom-tailored for low-resource machine translation and conversational NLP applications.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `burmese` 열 p90 119자 ≈ 30 토큰 (viewer statistics, default/train)
