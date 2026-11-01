---
type: "dataset"
id: "cis-lmu/m_lama"
source: "huggingface"
url: "https://huggingface.co/datasets/cis-lmu/m_lama"
downloads: 229
summary: "53개 언어로 번역된 LAMA 벤치마크 데이터로, 다국어 지식 평가용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[언어 모델링]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# cis-lmu/m_lama

> dataset · [Hugging Face](https://huggingface.co/datasets/cis-lmu/m_lama)

53개 언어로 번역된 LAMA 벤치마크 데이터로, 다국어 지식 평가용입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories, task_ids = `text-classification` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `This data can be used for creating fill-in-the-blank queries like "Paris is the capital of [MASK]" across 53 languages.` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories, task_ids = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:language_modeling, task:question_answering = `This data can be used for creating fill-in-the-blank queries like "Paris is the capital of [MASK]" across 53 languages.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling, task:question_answering = `This data can be used for creating fill-in-the-blank queries like "Paris is the capital of [MASK]" across 53 languages.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `53 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a multilingual version of the LAMA benchmark (T-REx and GoogleRE) covering 53 languages.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `There is only one partition that is labelled as 'test data'.` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
