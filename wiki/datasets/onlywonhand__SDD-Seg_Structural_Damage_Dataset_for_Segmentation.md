---
type: "dataset"
id: "onlywonhand/SDD-Seg_Structural_Damage_Dataset_for_Segmentation"
source: "huggingface"
url: "https://huggingface.co/datasets/onlywonhand/SDD-Seg_Structural_Damage_Dataset_for_Segmentation"
downloads: 179
summary: "토목 구조물 손상 탐지와 부재 분류를 위한 14채널 세그멘테이션 마스크 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[정보 추출]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[교통·모빌리티]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# onlywonhand/SDD-Seg_Structural_Damage_Dataset_for_Segmentation

> dataset · [Hugging Face](https://huggingface.co/datasets/onlywonhand/SDD-Seg_Structural_Damage_Dataset_for_Segmentation)

토목 구조물 손상 탐지와 부재 분류를 위한 14채널 세그멘테이션 마스크 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `손상 탐지(Damage Detection)와 구조물 부재 분류(Structural Component Classification)를 동시에 수행하기 위해 구축된 멀티태스크 데이터셋입니다.` · 신뢰도 low
- **작업**: [[이미지 인식]] — metadata · task_categories = `image-classification` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:vision = `원본 촬영 이미지 (JPG)` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:information_extraction = `text` · 신뢰도 medium
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme = `14채널 세그멘테이션 마스크` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[교통·모빌리티]] — ner · readme = `토목 구조물(교량, 터널, 옹벽 등)의 손상 탐지` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
