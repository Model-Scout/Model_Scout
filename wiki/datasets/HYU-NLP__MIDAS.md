---
type: "dataset"
id: "HYU-NLP/MIDAS"
source: "huggingface"
url: "https://huggingface.co/datasets/HYU-NLP/MIDAS"
downloads: 42
summary: "6개 언어의 관용구와 그 의미, 예문을 포함한 다국어 관용구 데이터셋 MIDAS입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# HYU-NLP/MIDAS

> dataset · [Hugging Face](https://huggingface.co/datasets/HYU-NLP/MIDAS)

6개 언어의 관용구와 그 의미, 예문을 포함한 다국어 관용구 데이터셋 MIDAS입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Memorization or Reasoning? Exploring the Idiom Understanding of LLMs` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Memorization or Reasoning? Exploring the Idiom Understanding of LLMs` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:question_answering = `The dataset includes four JSON files, each corresponding to a specific language.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering = `text` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MIDAS is a comprehensive dataset spanning six typologically and culturally diverse languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This repository includes four language subsets of MIDAS.` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
