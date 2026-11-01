---
type: "dataset"
id: "polyglot-tagger/finetranslations-filtered"
source: "huggingface"
url: "https://huggingface.co/datasets/polyglot-tagger/finetranslations-filtered"
downloads: 45
summary: "다국어 번역 데이터셋으로, 다양한 언어의 번역 학습에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
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
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# polyglot-tagger/finetranslations-filtered

> dataset · [Hugging Face](https://huggingface.co/datasets/polyglot-tagger/finetranslations-filtered)

다국어 번역 데이터셋으로, 다양한 언어의 번역 학습에 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[번역]] — ner · readme = `FineTranslations` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:translation = `Each file is in this format for languages in ISO 639 2-letter codes` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `Each file is in this format for languages in ISO 639 2-letter codes` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `94 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `78` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-3.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `train/en/en.parquet
train/es/es.parquet` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `sentence` 열 p90 313자 ≈ 78 토큰 (viewer statistics, default/train)
