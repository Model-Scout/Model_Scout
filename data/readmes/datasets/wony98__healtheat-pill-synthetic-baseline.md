---
license: apache-2.0
language:
- ko
tags:
- pill-detection
- object-detection
- synthetic-data
- healthcare
pretty_name: HealthEat Pill Synthetic Dataset (baseline)
size_categories:
- 1K<n<10K
task_categories:
- object-detection
---

# HealthEat Pill Synthetic Dataset — baseline 학습용

3팀 HealthEat 프로젝트의 알약 검출 baseline 모델 학습용 합성 데이터.
6 카테고리 배경에 알약 누끼 합성, 총 8,000장.

## 구성

| 분할 | 이미지 수 |
|---|---|
| train | 7,200 |
| val | 800 |
| **총** | **8,000** |

## 카테고리 (6종 배경)

- dark_surface (어두운 표면)
- palm_hand (손바닥)
- white_paper (흰 종이)
- fabric (직물)
- marble_tile (대리석/타일)
- gray_surface (회색 표면)

## 합성 파이프라인

1. 알약 누끼: 약 7,503개 (rembg isnet-general-use 모델로 추출)
2. 배경: 카테고리별 수작업 검수 매크로 텍스처 이미지
3. 합성: 1280×1280 캔버스, 알약 2~4개 무작위 배치, YOLO 라벨 자동 생성

## 포맷

YOLO 형식 (이미지 + .txt 라벨 페어). zip 내부 구조:

\\\
images/
  train/   synth_00000.jpg ~ synth_07199.jpg
  val/     synth_00000.jpg ~ synth_00799.jpg
labels/
  train/   synth_00000.txt ...
  val/     synth_00000.txt ...
\\\

각 라벨 파일은 \<class_idx> <x_center> <y_center> <width> <height>\ (정규화 좌표) 형식. 클래스 인덱스는 0~117 (118 클래스). 클래스명 매핑은 [healtheat-pill-rtmdet-baseline](https://huggingface.co/wony98/healtheat-pill-rtmdet-baseline) 레포의 \pill.yaml\ 참조.

## 사용

\\\python
from huggingface_hub import hf_hub_download

zip_path = hf_hub_download(
    repo_id='wony98/healtheat-pill-synthetic-baseline',
    filename='synthetic_combined.zip',
    repo_type='dataset'
)
\\\

## 출처

- 알약 누끼: AI Hub 약품 데이터 + 코드잇 Kaggle 알약 데이터에서 추출
- 배경: 팀 자체 수작업 검수
- 합성 코드: 팀 자체 작성

## 관련 자산

- **GitHub**: https://github.com/ZerofZero/codeit10_pj1
- **모델**: https://huggingface.co/wony98/healtheat-pill-rtmdet-baseline (이 데이터로 학습됨)
- **다른 합성 데이터**:
  - [synthetic-v2](https://huggingface.co/datasets/wony98/healtheat-pill-synthetic-v2) (v2 노트북 학습용)
  - [synthetic-v3](https://huggingface.co/datasets/wony98/healtheat-pill-synthetic-v3) (v3/v4 노트북 학습용)

## 라이선스

Apache 2.0. 단 알약 누끼 추출 원본은 AI Hub / Kaggle 출처이므로 해당 약관 함께 따름.
