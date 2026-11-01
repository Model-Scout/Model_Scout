---
type: "dataset"
id: "haor/openniji_5_1-27"
source: "huggingface"
url: "https://huggingface.co/datasets/haor/openniji_5_1-27"
downloads: 78
summary: "OpenNiji-Dataset의 이미지-텍스트 쌍 데이터셋으로, 이미지 생성 및 관련 작업에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[이미지 생성]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[비상업 전용]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# haor/openniji_5_1-27

> dataset · [Hugging Face](https://huggingface.co/datasets/haor/openniji_5_1-27)

OpenNiji-Dataset의 이미지-텍스트 쌍 데이터셋으로, 이미지 생성 및 관련 작업에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `the associated texts are included as prompts` · 신뢰도 low
- **작업**: [[이미지 생성]] — metadata · readme, task_categories = `text-to-image` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:image_generation = `Image: WebP (95% compressed)` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:image_generation = `Text: txt (containing prompt content)` · 신뢰도 medium
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme, task:image_generation = `image-text pairs` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `the associated texts are included as prompts` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `3 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Initial release, containing data collected from May 1st to May 27th.` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
