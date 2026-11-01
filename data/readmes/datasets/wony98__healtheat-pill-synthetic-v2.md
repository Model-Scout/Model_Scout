---
license: apache-2.0
language:
- ko
tags:
- pill-detection
- object-detection
- synthetic-data
- healthcare
pretty_name: HealthEat Pill Synthetic Dataset (v2)
size_categories:
- 1K<n<10K
task_categories:
- object-detection
---

# HealthEat Pill Synthetic Dataset — v2

3팀 HealthEat 프로젝트의 알약 검출 v2 노트북 학습용 합성 데이터.
양질 분포 매칭 + 알약 크기 lognormal 적용. 총 7,994장.

## 구성

| 분할 | 이미지 수 |
|---|---|
| train | 7,194 |
| val | 800 |
| **총** | **7,994** |

## v2 주요 처방 (vs baseline)

| 항목 | baseline | v2 |
|---|---|---|
| 알약 크기 분포 | 균일 | lognormal (양질 매칭) |
| 합성 코드 | v1 | v2 (방향 1+2+3 통합) |
| 배경 카테고리 | 6종 | 동일 (palm 비율 작음) |

## 합성 파이프라인

1. 알약 누끼: rembg isnet-general-use 모델로 추출
2. 배경: 6 카테고리 배경 풀 (수작업 검수)
3. 합성: 1280×1280 캔버스, 양질 분포 기반 알약 크기 결정
4. 분할: 9:1 (train 7,194 + val 800)

## 포맷

YOLO 형식. zip 내부 구조:

\\\
synthetic_v2/
  images/
    train/   synth_00000.jpg ~ synth_07193.jpg
    val/     synth_00000.jpg ~ synth_00799.jpg
  labels/
    train/   synth_00000.txt ...
    val/     synth_00000.txt ...
\\\

각 라벨은 \<class_idx> <x_center> <y_center> <width> <height>\ (정규화). 클래스 0~117 (118 클래스).

## 사용

\\\python
from huggingface_hub import hf_hub_download

zip_path = hf_hub_download(
    repo_id='wony98/healtheat-pill-synthetic-v2',
    filename='synthetic_v2.zip',
    repo_type='dataset'
)
\\\

## 출처

- 알약 누끼: AI Hub 약품 데이터 + 코드잇 Kaggle 알약 데이터에서 추출
- 배경: 팀 자체 수작업 검수
- 합성 코드: 팀 자체 작성 (synthetic_images_v2.ipynb)

## 관련 자산

- **GitHub**: https://github.com/ZerofZero/codeit10_pj1
- **다른 합성 데이터**:
  - [synthetic-baseline](https://huggingface.co/datasets/wony98/healtheat-pill-synthetic-baseline)
  - [synthetic-v3](https://huggingface.co/datasets/wony98/healtheat-pill-synthetic-v3) (v3/v4 학습용)

## 라이선스

Apache 2.0. 단 알약 누끼 추출 원본은 AI Hub / Kaggle 출처이므로 해당 약관 함께 따름.
