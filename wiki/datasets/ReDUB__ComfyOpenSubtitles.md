---
type: "dataset"
id: "ReDUB/ComfyOpenSubtitles"
source: "huggingface"
url: "https://huggingface.co/datasets/ReDUB/ComfyOpenSubtitles"
downloads: 12
summary: "다국어 자막 병렬 번역 데이터셋으로 번역 연구에 활용됨."
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
  - "[[ar]]"
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[중국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# ReDUB/ComfyOpenSubtitles

> dataset · [Hugging Face](https://huggingface.co/datasets/ReDUB/ComfyOpenSubtitles)

다국어 자막 병렬 번역 데이터셋으로 번역 연구에 활용됨.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:translation = `- `input_text`: The input text in the source language.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `- `output_text`: The corresponding translation in the target language.` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `9 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `unknown` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The source data for this dataset consists of subtitles from various movies and TV shows.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset is typically divided into training splits with varying sizes.` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high
