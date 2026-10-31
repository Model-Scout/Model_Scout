---
type: "dataset"
id: "ismaelfi/melolingua-cefr-graded-multilingual-stories"
source: "huggingface"
url: "https://huggingface.co/datasets/ismaelfi/melolingua-cefr-graded-multilingual-stories"
downloads: 103
summary: "MeloLingua CEFR 등급별 다국어 학습용 이야기 데이터셋으로 언어 학습에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
  - "[[번역]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[it]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ismaelfi/melolingua-cefr-graded-multilingual-stories

> dataset · [Hugging Face](https://huggingface.co/datasets/ismaelfi/melolingua-cefr-graded-multilingual-stories)

MeloLingua CEFR 등급별 다국어 학습용 이야기 데이터셋으로 언어 학습에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `The CEFR labels are editorial teaching labels` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **작업**: [[문서 검색]] — ner · readme = `multilingual search and retrieval` · 신뢰도 medium
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:question_answering, task:retrieval, task:translation = `Records include target-language text, sentence-aligned English translations` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:translation = `comprehension questions, sentence-building exercises` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `6 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `39` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[교육]] — tag_match · readme, tags = `education` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset supports classroom reading activities, non-commercial lesson adaptations` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `choices_json` 열 p90 158자 ≈ 39 토큰 (viewer statistics, questions/train)

## 같은 데이터의 사본·중복 등록

- `kaggle/ismaelfi/melolingua-cefr-graded-multilingual-stories`
