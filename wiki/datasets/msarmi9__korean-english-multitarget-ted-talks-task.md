---
type: "dataset"
id: "msarmi9/korean-english-multitarget-ted-talks-task"
source: "huggingface"
url: "https://huggingface.co/datasets/msarmi9/korean-english-multitarget-ted-talks-task"
downloads: 119
summary: "TED 강연의 영어-한국어 병렬 문장 쌍으로 기계 번역 연구에 활용되는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# msarmi9/korean-english-multitarget-ted-talks-task

> dataset · [Hugging Face](https://huggingface.co/datasets/msarmi9/korean-english-multitarget-ted-talks-task)

TED 강연의 영어-한국어 병렬 문장 쌍으로 기계 번역 연구에 활용되는 데이터셋입니다.

## 분류

- **작업**: [[번역]] — ner · readme = `Machine Translation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `Parallel English-Korean Text Corpus` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `Parallel English-Korean Text Corpus` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `118` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-nd-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Parallel English-Korean Text Corpus` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Approximately 166k train, 2k validation, and 2k test sentence pairs.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `english` 열 p90 176자 ≈ 118 토큰 (viewer statistics, default/validation)
