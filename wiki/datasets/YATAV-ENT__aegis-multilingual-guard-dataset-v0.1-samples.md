---
type: "dataset"
id: "YATAV-ENT/aegis-multilingual-guard-dataset-v0.1-samples"
source: "huggingface"
url: "https://huggingface.co/datasets/YATAV-ENT/aegis-multilingual-guard-dataset-v0.1-samples"
downloads: 64
summary: "AEGIS 다국어 가드/레드팀 데이터셋 공개 미리보기로, 12개 도메인별 100건씩 공격·비공격 프롬프트 포함 안전성 연구용 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# YATAV-ENT/aegis-multilingual-guard-dataset-v0.1-samples

> dataset · [Hugging Face](https://huggingface.co/datasets/YATAV-ENT/aegis-multilingual-guard-dataset-v0.1-samples)

AEGIS 다국어 가드/레드팀 데이터셋 공개 미리보기로, 12개 도메인별 100건씩 공격·비공격 프롬프트 포함 안전성 연구용 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `Records contain adversarial attack prompts (jailbreaks, prompt injections…` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `the label of every attack is "the assistant should refuse." This is a guardrail/classification corpus, not a corpus of harmful answers.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `25 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a multilingual red-team / guardrail corpus.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
