---
type: "dataset"
id: "wdcqc/starcraft-remastered-melee-maps"
source: "huggingface"
url: "https://huggingface.co/datasets/wdcqc/starcraft-remastered-melee-maps"
downloads: 4530
summary: "스타크래프트 리마스터의 1,815개 근접전 맵을 타일셋별로 분류한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[이미지 생성]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# wdcqc/starcraft-remastered-melee-maps

> dataset · [Hugging Face](https://huggingface.co/datasets/wdcqc/starcraft-remastered-melee-maps)

스타크래프트 리마스터의 1,815개 근접전 맵을 타일셋별로 분류한 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 medium
- **작업**: [[이미지 생성]] — metadata · task_categories = `image-to-image` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:image_generation = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:image_generation = `To use this dataset, extract the `staredit\\scenario.chk` files from the map files using StormLib` · 신뢰도 medium
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — task_rule · task:image_generation = `image` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `unknown` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This is a dataset containing 1,815 Starcraft:Remastered melee maps, categorized into tilesets.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset is used to train this model: https://huggingface.co/wdcqc/starcraft-platform-terrain-32x32` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
