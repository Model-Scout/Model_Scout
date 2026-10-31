---
type: "dataset"
id: "sil-ai/bloom-vist"
source: "huggingface"
url: "https://huggingface.co/datasets/sil-ai/bloom-vist"
downloads: 61
summary: "Bloom Library의 363개 언어 시각 스토리텔링 데이터셋으로, 비주류 언어 커뮤니티 문학 창작 지원용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
  - "[[조건부 이용]]"
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# sil-ai/bloom-vist

> dataset · [Hugging Face](https://huggingface.co/datasets/sil-ai/bloom-vist)

Bloom Library의 363개 언어 시각 스토리텔링 데이터셋으로, 비주류 언어 커뮤니티 문학 창작 지원용입니다.

## 분류

- **작업**: [[이미지 이해]] — ner · readme = `This version of the Bloom Library data is developed specifically for the Visual Story Telling (VIST) task.` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:visual_qa = `image IDs, image URLs` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:visual_qa = `corresponding text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:visual_qa = `corresponding text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `406 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `cc-by-nd-4.0` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Bloom Library data is developed specifically for the visual story telling (or VIST) task.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Currently all languages include a train split only.` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
