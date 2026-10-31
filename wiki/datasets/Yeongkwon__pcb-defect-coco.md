---
type: "dataset"
id: "Yeongkwon/pcb-defect-coco"
source: "huggingface"
url: "https://huggingface.co/datasets/Yeongkwon/pcb-defect-coco"
downloads: 673
summary: "PCB 결함 탐지를 위한 COCO 형식의 어노테이션 데이터셋으로, train/val로 분할되어 있음."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[정보 추출]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Yeongkwon/pcb-defect-coco

> dataset · [Hugging Face](https://huggingface.co/datasets/Yeongkwon/pcb-defect-coco)

PCB 결함 탐지를 위한 COCO 형식의 어노테이션 데이터셋으로, train/val로 분할되어 있음.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `Pascal VOC 어노테이션을 COCO JSON 형식으로 변환하고 train/val로 분할한 데이터셋입니다.` · 신뢰도 low
- **작업**: [[이미지 인식]] — metadata · task_categories = `object-detection` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:vision = `이미지와 바운딩 박스 좌표는 원본과 동일합니다.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:information_extraction = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `RobotHuman/PCB_defect(원저: Huang & Wei, 2019, Peking University)의 Pascal VOC 어노테이션을 COCO JSON 형식으로 변환하고 train/val로 분할한 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Pascal VOC 어노테이션을 COCO JSON 형식으로 변환하고 train/val로 분할한 데이터셋입니다.` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
