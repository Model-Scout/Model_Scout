---
type: "dataset"
id: "Highsky7/Topview_Lane"
source: "huggingface"
url: "https://huggingface.co/datasets/Highsky7/Topview_Lane"
downloads: 36
summary: "BevLane은 자율주행 및 로봇 내비게이션을 위한 BEV 시점 차선 분할 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교통·모빌리티]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Highsky7/Topview_Lane

> dataset · [Hugging Face](https://huggingface.co/datasets/Highsky7/Topview_Lane)

BevLane은 자율주행 및 로봇 내비게이션을 위한 BEV 시점 차선 분할 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `This dataset is intended for training and evaluating models for semantic segmentation, specifically for lane detection in a BEV space.` · 신뢰도 low
- **작업**: [[이미지 인식]] — metadata · task_categories = `image-segmentation` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:vision = `The dataset is composed of image files and their corresponding segmentation masks.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme = `The dataset is composed of image files and their corresponding segmentation masks.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[교통·모빌리티]] — ner · readme = `which are crucial components for autonomous driving systems and robotics navigation.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is intended for training and evaluating models for semantic segmentation` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
