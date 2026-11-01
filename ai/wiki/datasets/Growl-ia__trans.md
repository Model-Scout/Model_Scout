---
type: "dataset"
id: "Growl-ia/trans"
source: "huggingface"
url: "https://huggingface.co/datasets/Growl-ia/trans"
downloads: 59
summary: "Growl-ia/trans는 다국어 번역 데이터셋으로, 모델 생성 문장쌍과 COMETKiwi 품질 점수를 포함합니다."
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
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# Growl-ia/trans

> dataset · [Hugging Face](https://huggingface.co/datasets/Growl-ia/trans)

Growl-ia/trans는 다국어 번역 데이터셋으로, 모델 생성 문장쌍과 COMETKiwi 품질 점수를 포함합니다.

## 분류

- **작업**: [[번역]] — metadata · readme, tags, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `sentence-level bilingual data` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `sentence-level bilingual data with COMETKiwi scores` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `14 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `51` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Growl-ia/trans is a multilingual translation dataset package` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `tgt` 열 p90 204자 ≈ 51 토큰 (viewer statistics, default/train)
