---
type: "dataset"
id: "Genius1237/TyDiP"
source: "huggingface"
url: "https://huggingface.co/datasets/Genius1237/TyDiP"
downloads: 615
summary: "TyDiP는 9개 언어로 된 위키백과 편집자 대화의 공손성 분류 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[af]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[hi]]"
  - "[[hu]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[ta]]"
  - "[[vi]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Genius1237/TyDiP

> dataset · [Hugging Face](https://huggingface.co/datasets/Genius1237/TyDiP)

TyDiP는 9개 언어로 된 위키백과 편집자 대화의 공손성 분류 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `The TyDiP dataset is a dataset of requests in conversations between wikipedia editors` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The TyDiP dataset is a dataset of requests in conversations between wikipedia editors that have been annotated for politeness.` · 신뢰도 low
- **언어**: [[af]] — metadata · languages = `af` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[hi]] — metadata · languages = `hi` · 신뢰도 high
- **언어**: [[hu]] — metadata · languages = `hu` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `10 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[ta]] — metadata · languages = `ta` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `35` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — tag_match · readme, tags = `wikipedia` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 139자 ≈ 35 토큰 (viewer statistics, ko/test)

## 이 데이터로 학습한 모델

- [[Genius1237__xlm-roberta-large-tydip|Genius1237/xlm-roberta-large-tydip]]
