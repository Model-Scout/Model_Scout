---
type: "dataset"
id: "wecover/OPUS"
source: "huggingface"
url: "https://huggingface.co/datasets/wecover/OPUS"
downloads: 1320
summary: "OPUS의 여러 병렬 말뭉치를 언어쌍별로 25,000개씩 수집한 번역 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# wecover/OPUS

> dataset · [Hugging Face](https://huggingface.co/datasets/wecover/OPUS)

OPUS의 여러 병렬 말뭉치를 언어쌍별로 25,000개씩 수집한 번역 데이터셋입니다.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:translation = `25,000 samples (randomly sampled within the first 100,000 samples) per language pair of each corpus were collected` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `25,000 samples (randomly sampled within the first 100,000 samples) per language pair of each corpus were collected` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `91 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Corpus from https://opus.nlpl.eu has been collected.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `25,000 samples (randomly sampled within the first 100,000 samples) per language pair of each corpus were collected` · 신뢰도 low
