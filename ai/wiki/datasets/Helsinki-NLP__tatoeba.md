---
type: "dataset"
id: "Helsinki-NLP/tatoeba"
source: "huggingface"
url: "https://huggingface.co/datasets/Helsinki-NLP/tatoeba"
downloads: 768
summary: "Tatoeba의 359개 언어 번역 문장 모음으로 다국어 번역에 활용됨."
readme_status: "template"
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
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Helsinki-NLP/tatoeba

> dataset · [Hugging Face](https://huggingface.co/datasets/Helsinki-NLP/tatoeba)

Tatoeba의 359개 언어 번역 문장 모음으로 다국어 번역에 활용됨.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:translation = `translated sentences` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `translated sentences` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `358 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This is a collection of translated sentences from Tatoeba` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[Helsinki-NLP__opus-mt_tiny_kor-eng|Helsinki-NLP/opus-mt_tiny_kor-eng]]
- [[alirezamsh__small100|alirezamsh/small100]]
- [[entai2965__small100-ctranslate2|entai2965/small100-ctranslate2]]
