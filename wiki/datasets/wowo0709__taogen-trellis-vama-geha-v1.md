---
type: "dataset"
id: "wowo0709/taogen-trellis-vama-geha-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/wowo0709/taogen-trellis-vama-geha-v1"
downloads: 78
summary: "TRELLIS VAMA / GEHA 원천 데이터로 TAO 재구성 및 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
---
# wowo0709/taogen-trellis-vama-geha-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/wowo0709/taogen-trellis-vama-geha-v1)

TRELLIS VAMA / GEHA 원천 데이터로 TAO 재구성 및 평가용 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Public, frozen native TRELLIS SS data, TAO reframing, pretrained assets` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `Training: 26,033 objects, one view/object/epoch` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `canonical evaluation targets` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `Quick100: 60 validation +40 held-out, frozen case IDs and seeds.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Training: 26,033 objects, one view/object/epoch, 5 epochs / global batch24 /5,425 steps.` · 신뢰도 medium
