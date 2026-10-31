---
type: "dataset"
id: "jizerro/vlm2-orderless-balanced-5000"
source: "huggingface"
url: "https://huggingface.co/datasets/jizerro/vlm2-orderless-balanced-5000"
downloads: 169
summary: "교통사고 조작 쌍에 대한 VLM-2 미세조정을 위한 5,000개 균형 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[교통·모빌리티]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# jizerro/vlm2-orderless-balanced-5000

> dataset · [Hugging Face](https://huggingface.co/datasets/jizerro/vlm2-orderless-balanced-5000)

교통사고 조작 쌍에 대한 VLM-2 미세조정을 위한 5,000개 균형 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Balanced 5,000-example subset for VLM-2 traffic accident maneuver-pair fine-tuning.` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:visual_qa = `This dataset contains label and prompt records only.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:visual_qa = `This dataset contains label and prompt records only.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[교통·모빌리티]] — ner · readme = `Balanced 5,000-example subset for VLM-2 traffic accident maneuver-pair fine-tuning.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Balanced 5,000-example subset for VLM-2 traffic accident maneuver-pair fine-tuning.` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
