---
type: "dataset"
id: "xhluca/publichealth-qa"
source: "huggingface"
url: "https://huggingface.co/datasets/xhluca/publichealth-qa"
downloads: 2152
summary: "CDC와 WHO의 COVID-19 관련 Q&A 쌍 데이터셋으로 질의응답 모델에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[vi]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# xhluca/publichealth-qa

> dataset · [Hugging Face](https://huggingface.co/datasets/xhluca/publichealth-qa)

CDC와 WHO의 COVID-19 관련 Q&A 쌍 데이터셋으로 질의응답 모델에 활용됨.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `This dataset contains question and answer pairs sourced from Q&A pages and FAQs from CDC and WHO pertaining to COVID-19.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `This dataset contains question and answer pairs sourced from Q&A pages and FAQs from CDC and WHO pertaining to COVID-19.` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `8 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `187` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-3.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — ner · readme = `This dataset contains question and answer pairs sourced from Q&A pages and FAQs from CDC and WHO pertaining to COVID-19.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `They were produced and collected between 2019-12 and 2020-04.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `answer` 열 p90 750자 ≈ 187 토큰 (viewer statistics, korean/test)
