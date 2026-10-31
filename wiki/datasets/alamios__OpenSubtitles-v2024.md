---
type: "dataset"
id: "alamios/OpenSubtitles-v2024"
source: "huggingface"
url: "https://huggingface.co/datasets/alamios/OpenSubtitles-v2024"
downloads: 973
summary: "OpenSubtitles-v2024은 영화 및 TV 자막 번역 데이터로 기계 번역 등에 활용됩니다."
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
# alamios/OpenSubtitles-v2024

> dataset · [Hugging Face](https://huggingface.co/datasets/alamios/OpenSubtitles-v2024)

OpenSubtitles-v2024은 영화 및 TV 자막 번역 데이터로 기계 번역 등에 활용됩니다.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:translation = `aligned sentence pairs` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `aligned sentence pairs` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `85 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `unknown` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `translated movie and TV subtitles from opensubtitles.org` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Each config (e.g. `en-es`) contains a single `train` split with aligned sentence pairs` · 신뢰도 medium
