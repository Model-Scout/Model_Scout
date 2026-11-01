---
type: "dataset"
id: "RobotHuman/PCB_defect"
source: "huggingface"
url: "https://huggingface.co/datasets/RobotHuman/PCB_defect"
downloads: 3315
summary: "부품 실장 전 naked PCB 이미지로 6종 결함 위치 검출 및 유형 분류용 데이터셋"
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
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
dataset_size:
  - "[[소규모 데이터]]"
---
# RobotHuman/PCB_defect

> dataset · [Hugging Face](https://huggingface.co/datasets/RobotHuman/PCB_defect)

부품 실장 전 naked PCB 이미지로 6종 결함 위치 검출 및 유형 분류용 데이터셋

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `결함 유형 분류` · 신뢰도 medium
- **작업**: [[정보 추출]] — ner · readme = `결함 위치 검출` · 신뢰도 low
- **작업**: [[이미지 인식]] — metadata · task_categories = `image-classification` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:vision = `PCB 이미지` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:information_extraction = `text` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `본 데이터셋은 naked PCB(부품 실장 전 PCB) 이미지로 구성되어 있으며` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
