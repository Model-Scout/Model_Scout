---
type: "dataset"
id: "Unbabel/TowerBlocks-v0.2"
source: "huggingface"
url: "https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2"
downloads: 350
summary: "기계 번역, 자동 후처리, 개체명 인식 등 번역 관련 작업용 대화형 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
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
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Unbabel/TowerBlocks-v0.2

> dataset · [Hugging Face](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2)

기계 번역, 자동 후처리, 개체명 인식 등 번역 관련 작업용 대화형 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `paraphrase generation` · 신뢰도 medium
- **작업**: [[정보 추출]] — ner · readme = `named-entity recognition` · 신뢰도 medium
- **작업**: [[번역]] — ner · readme = `a language model specialized for translation tasks such as machine translation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:information_extraction, task:translation = `conversational dataset for translation related tasks` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `a language model specialized for translation tasks such as machine translation` · 신뢰도 medium
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
- **도메인**: [[일반]] — ner · readme = `a language model specialized for translation tasks such as machine translation` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `TowerBlocks is the dataset used to train TowerInstruct-v0.1` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
