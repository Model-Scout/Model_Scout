---
type: "dataset"
id: "Unbabel/TowerEval-Data-v0.1"
source: "huggingface"
url: "https://huggingface.co/datasets/Unbabel/TowerEval-Data-v0.1"
downloads: 35
summary: "기계 번역, 자동 후처리, 개체명 인식, 문법 오류 수정, 패러프레이즈 생성 평가용 데이터셋 모음입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[it]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[nl]]"
  - "[[pt]]"
  - "[[ru]]"
  - "[[중국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Unbabel/TowerEval-Data-v0.1

> dataset · [Hugging Face](https://huggingface.co/datasets/Unbabel/TowerEval-Data-v0.1)

기계 번역, 자동 후처리, 개체명 인식, 문법 오류 수정, 패러프레이즈 생성 평가용 데이터셋 모음입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `gramatical error correction` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — ner · readme = `named-entity recognition` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation, task:question_answering, task:translation = `language models specialized for translation tasks such as machine translation` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:translation = `language models specialized for translation tasks such as machine translation` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `10 languages` · 신뢰도 high
- **언어**: [[nl]] — metadata · languages = `nl` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `language models specialized for translation tasks such as machine translation` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `TowerEval-Data is the suite of datasets used to evaluate Tower` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
