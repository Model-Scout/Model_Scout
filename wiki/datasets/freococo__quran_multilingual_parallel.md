---
type: "dataset"
id: "freococo/quran_multilingual_parallel"
source: "huggingface"
url: "https://huggingface.co/datasets/freococo/quran_multilingual_parallel"
downloads: 66
summary: "quran_multilingual_parallel은 54개 언어로 된 꾸란 구절별 병렬 번역 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[번역]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# freococo/quran_multilingual_parallel

> dataset · [Hugging Face](https://huggingface.co/datasets/freococo/quran_multilingual_parallel)

quran_multilingual_parallel은 54개 언어로 된 꾸란 구절별 병렬 번역 데이터셋입니다.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `It contains over 6,200 verse-level alignments in 54 human languages, formatted in a machine-friendly .csv structure with language-specific translation fields.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `It contains over 6,200 verse-level alignments in 54 human languages, formatted in a machine-friendly .csv structure with language-specific translation fields.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `54 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `151` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `It is intended for linguistic, computational, and cross-lingual AI applications — not only for religious interpretation.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset presents a clean, structurally-aligned multilingual parallel corpus of the Qur’anic text.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `burmese` 열 p90 605자 ≈ 151 토큰 (viewer statistics, default/train)
