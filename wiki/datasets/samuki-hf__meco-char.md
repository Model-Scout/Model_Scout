---
type: "dataset"
id: "samuki-hf/meco-char"
source: "huggingface"
url: "https://huggingface.co/datasets/samuki-hf/meco-char"
downloads: 193
summary: "MECO 다국어 문자 단위 시선추적 데이터로 읽기 시간 분석에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# samuki-hf/meco-char

> dataset · [Hugging Face](https://huggingface.co/datasets/samuki-hf/meco-char)

MECO 다국어 문자 단위 시선추적 데이터로 읽기 시간 분석에 활용됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Preprocessed fixation data derived from the MECO (Multilingual Eye-tracking Corpus) reading-time dataset, character-indexed.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding = `character-indexed` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Flat per-language analysis files: <lang>.csv (one row per fixation across all readers/trials) and stimulus_<lang>.csv (per-character stimulus table)` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `13 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MECO (Multilingual Eye-tracking Corpus) reading-time dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Preprocessed fixation data derived from the MECO (Multilingual Eye-tracking Corpus) reading-time dataset` · 신뢰도 low
