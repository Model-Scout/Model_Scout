---
type: "dataset"
id: "KETI-NLP/KoEVD"
source: "huggingface"
url: "https://huggingface.co/datasets/KETI-NLP/KoEVD"
downloads: 156
summary: "KoEVD는 한국어 발화에 대한 위험 판단과 응답 안전성 평가를 위한 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[리랭킹]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# KETI-NLP/KoEVD

> dataset · [Hugging Face](https://huggingface.co/datasets/KETI-NLP/KoEVD)

KoEVD는 한국어 발화에 대한 위험 판단과 응답 안전성 평가를 위한 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[리랭킹]] — ner · readme = `candidate-response safety choice` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:reranking = `linking five evaluation or analysis targets through source utterances` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `candidate-response safety choice, direct-generation response harmfulness, descriptive response strategies` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean slang, idioms, relationships, and sociocultural references motivate depth within one language` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `The `test` name only exposes evaluation records through the library API.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `KoEVD is human-curated and AI-assisted, with guideline design, candidate drafting, rewriting, relabeling, adjudication and filtering.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
