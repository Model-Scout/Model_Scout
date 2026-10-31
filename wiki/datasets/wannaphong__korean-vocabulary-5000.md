---
type: "dataset"
id: "wannaphong/korean-vocabulary-5000"
source: "huggingface"
url: "https://huggingface.co/datasets/wannaphong/korean-vocabulary-5000"
downloads: 141
summary: "Koko Korean 5K는 5,000개의 한국어 단어와 9개 언어 번역을 포함한 다국어 어휘 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
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
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# wannaphong/korean-vocabulary-5000

> dataset · [Hugging Face](https://huggingface.co/datasets/wannaphong/korean-vocabulary-5000)

Koko Korean 5K는 5,000개의 한국어 단어와 9개 언어 번역을 포함한 다국어 어휘 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 high
- **작업**: [[텍스트 생성]] — ner · readme = `Train Korean language models (vocabulary acquisition, masked LM, translation)` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:generation, task:translation = `5,000 carefully curated Korean vocabulary entries with English translations, romanization, contextual usage notes, and example sentences.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `5,000 carefully curated Korean vocabulary entries with English translations, romanization, contextual usage notes, and example sentences.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `11 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `87` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `Train Korean language models (vocabulary acquisition, masked LM, translation)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Train Korean language models (vocabulary acquisition, masked LM, translation)` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `context_description` 열 p90 346자 ≈ 87 토큰 (viewer statistics, de/train)
