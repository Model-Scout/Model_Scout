---
license: apache-2.0
language:
- ko
tags:
- pill-detection
- object-detection
- yolo
- healthcare
pretty_name: HealthEat Pill Detection (YOLO format)
size_categories:
- 10K<n<100K
task_categories:
- object-detection
---

# HealthEat Pill Detection — YOLO 정제본

3팀 HealthEat 프로젝트의 알약 검출 학습용 정제본 데이터셋.
AI Hub 약품 데이터 + 코드잇 Kaggle 알약 데이터를 팀 공통 클렌징 + YOLO 포맷 통합. 총 10,392장.

## 구성

| 분할 | 이미지 수 | 라벨 (annotations) |
|---|---|---|
| train | 8,302 | (clean_df 기반) |
| val | 2,090 | (clean_df 기반) |
| **총** | **10,392** | **39,864** |

총 클래스 수: **118종** (한국 식약처 등재 의약품)

## 정제 파이프라인

원본 데이터 (AI Hub TS_1/3/4/5/6/7/8 + TL_1/3/4/5/6/7/8, 코드잇 Kaggle train_images) → 팀 공통 클렌징 → YOLO 포맷 변환 → split

### 공통 제거 기준 (4가지)
1. 좌표/IoU 완전 중복 (같은 좌표 IoU=1.0)
2. bbox 경계 초과 (x/y<0 or x+w>이미지폭 or y+h>이미지높이)
3. 명백한 오류 (bbox w/h/area≤0 or NaN)
4. 라벨 누락/오류 (이름 vs 값 대조 sanity check)

### Split 전략
\sklearn.GroupShuffleSplit\ (groups=combo, val_ratio=0.2, seed=42)
- Combo Group 방식 (이미지 + 조합 모두 train/val에 분리됨)
- val 클래스 118/118 (전체 클래스 검증 가능)
- Image overlap = 0, Combo overlap = 0

원본: 40,844 ann / 10,697 img → 정제 후: 39,864 ann / 10,392 img (305장 제거)

## 폴더 구조

\\\
images/
  train/   *.jpg / *.png (8,302장)
  val/     *.jpg / *.png (2,090장)
labels/
  train/   *.txt (YOLO 형식)
  val/     *.txt (YOLO 형식)
pill.yaml   클래스명 매핑
\\\

각 라벨 파일은 \<class_idx> <x_center> <y_center> <width> <height>\ (정규화 좌표) 형식. 클래스 인덱스는 0~117 (118 클래스).

## 사용

\\\python
from huggingface_hub import snapshot_download

local_dir = snapshot_download(
    repo_id='wony98/healtheat-pill-yolo',
    repo_type='dataset',
    local_dir='./dataset_yolo'
)
# 받은 후 그대로 YOLO/RTMDet 학습에 사용 가능
\\\

## 출처

- AI Hub 약품 데이터 (TS_1/3/4/5/6/7/8 + TL_1/3/4/5/6/7/8 시리즈, 2번 시리즈는 가이드에 따라 제외)
- 코드잇 Kaggle 알약 검출 competition train 데이터
- 팀 자체 공통 전처리 (clean_df 39,864 ann)

## 관련 자산

- **GitHub**: https://github.com/ZerofZero/codeit10_pj1
- **모델**: 
  - [healtheat-pill-rtmdet-baseline](https://huggingface.co/wony98/healtheat-pill-rtmdet-baseline) (배포)
  - [healtheat-pill-rtmdet-v4](https://huggingface.co/wony98/healtheat-pill-rtmdet-v4) (분석 우위)
- **합성 데이터**:
  - [synthetic-baseline](https://huggingface.co/datasets/wony98/healtheat-pill-synthetic-baseline)
  - [synthetic-v2](https://huggingface.co/datasets/wony98/healtheat-pill-synthetic-v2)
  - [synthetic-v3](https://huggingface.co/datasets/wony98/healtheat-pill-synthetic-v3)
- **Kaggle (별도 zip 형태)**: https://www.kaggle.com/datasets/wony98/pill-detection-preprocessed

## 라이선스

Apache 2.0. 단 원본 데이터는 AI Hub / 코드잇 Kaggle 출처이므로 해당 약관 함께 따름.
출처 명시 + 상업적 이용 시 원본 라이선스 확인 필요.
