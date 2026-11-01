---
type: "dataset"
id: "neulab/PangeaBench-xm100"
source: "huggingface"
url: "https://huggingface.co/datasets/neulab/PangeaBench-xm100"
downloads: 55
summary: "XM100은 다국어 다중모달 평가를 위한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
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
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# neulab/PangeaBench-xm100

> dataset · [Hugging Face](https://huggingface.co/datasets/neulab/PangeaBench-xm100)

XM100은 다국어 다중모달 평가를 위한 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Crossmodal-3600: A Massively Multilingual Multimodal Evaluation Dataset` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:visual_qa = `Crossmodal-3600: A Massively Multilingual Multimodal Evaluation Dataset` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:visual_qa = `Crossmodal-3600: A Massively Multilingual Multimodal Evaluation Dataset` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `36 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `This is a copy from https://google.github.io/crossmodal-3600/` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
