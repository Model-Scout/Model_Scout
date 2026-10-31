---
type: "dataset"
id: "juletxara/tydiqa_xtreme"
source: "huggingface"
url: "https://huggingface.co/datasets/juletxara/tydiqa_xtreme"
downloads: 163
summary: "11개 언어의 질문-답변 쌍 20만 개로 구성된 다국어 질의응답 데이터셋입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# juletxara/tydiqa_xtreme

> dataset · [Hugging Face](https://huggingface.co/datasets/juletxara/tydiqa_xtreme)

11개 언어의 질문-답변 쌍 20만 개로 구성된 다국어 질의응답 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories, task_ids = `question-answering` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:question_answering = `questions are written by people who want to know the answer` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `question-answer pairs` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `11 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `TyDi QA is a question answering dataset covering 11 typologically diverse languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `We also include "translate-train" and "translate-test" splits for each non-English languages from XTREME` · 신뢰도 medium
