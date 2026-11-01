---
type: "dataset"
id: "rokokot/question-type-and-complexity"
source: "huggingface"
url: "https://huggingface.co/datasets/rokokot/question-type-and-complexity"
downloads: 103
summary: "다국어 질문 유형과 언어 복잡성 분석을 위한 질문 유형 및 복잡성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
  - "[[질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[영어]]"
  - "[[fi]]"
  - "[[id]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
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
  - "[[중규모 데이터]]"
---
# rokokot/question-type-and-complexity

> dataset · [Hugging Face](https://huggingface.co/datasets/rokokot/question-type-and-complexity)

다국어 질문 유형과 언어 복잡성 분석을 위한 질문 유형 및 복잡성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 high
- **작업**: [[정보 추출]] — ner · readme = `automatically annotated with question types (polar/content) and a set of linguistic complexity features` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories, task_ids = `question-answering` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:information_extraction, task:question_answering = `It contains questions from two distinct sources (TyDi QA and Universal Dependencies v2.15)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `automatically annotated with question types (polar/content) and a set of linguistic complexity features` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[fi]] — metadata · languages = `fi` · 신뢰도 high
- **언어**: [[id]] — metadata · languages = `id` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `7 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `23` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `linguistics/NLP research focusing on question classification and linguistic complexity analysis across multiple languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Train(silver)/test(gold)/dev(mix) split using complementary data sources` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 91자 ≈ 23 토큰 (viewer statistics, base/validation)
