---
license: apache-2.0
language:
- ko
tags:
- pill-detection
- object-detection
- synthetic-data
- healthcare
pretty_name: HealthEat Pill Synthetic Dataset (v3)
size_categories:
- 1K<n<10K
task_categories:
- object-detection
---

# HealthEat Pill Synthetic Dataset — v3 (v3/v4 학습용)

3팀 HealthEat 프로젝트의 알약 검출 v3/v4 노트북 학습용 합성 데이터.
palm 마스크 처방 + 거대 알약 차단 적용. 총 7,309장.

## 구성

| 분할 | 이미지 수 |
|---|---|
| train | 6,509 |
| val | 800 |
| **총** | **7,309** |

## v3 주요 처방 (vs v2)

| 항목 | v2 | v3 |
|---|---|---|
| palm 배경 풀 | 6장 | 42장 (Nano Banana API 생성, 8장 폐기 후) |
| palm 비율 | 3.2% | 21.5% (7배 확대) |
| MAX_PILL_AREA_POST | 0.50 | 0.20 (거대 알약 차단) |
| palm 마스크 침식 | 없음 | 100px (손가락 끝 알약 배치 차단) |
| 마스크 모델 | — | rembg isnet-general-use + u2net_human_seg (palm 폴백) |

## 합성 파이프라인

1. 알약 누끼: rembg isnet-general-use 모델로 추출
2. 배경: 7 카테고리 배경 풀 (palm 42장 포함)
3. palm 마스크: 100px morphology erode (손가락 끝 영역 깎음)
4. 합성: 1280×1280 캔버스, 양질 분포 기반 알약 크기, 거대 알약 차단
5. 분할: 9:1 (train 6,509 + val 800)

## 사용처

- **v3 노트북**: \tmdet_tiny_synth_trainv3.ipynb\ 학습 (max_epochs=13, EMA hook)
- **v4 노트북**: \tmdet_tiny_synth_trainv4_a100.ipynb\ 학습 (v3 데이터 그대로 재사용)

v4 모델: Top-1 46.8% (baseline 대비 +17pp 개선)

## 포맷

YOLO 형식. zip 내부 구조:

\\\
synthetic_v3/
  images/
    train/   synth_*.jpg
    val/     synth_*.jpg
  labels/
    train/   synth_*.txt
    val/     synth_*.txt
\\\

각 라벨은 \<class_idx> <x_center> <y_center> <width> <height>\ (정규화). 클래스 0~117 (118 클래스).

## 사용

\\\python
from huggingface_hub import hf_hub_download

zip_path = hf_hub_download(
    repo_id='wony98/healtheat-pill-synthetic-v3',
    filename='synthetic_v3.zip',
    repo_type='dataset'
)
\\\

## 출처

- 알약 누끼: AI Hub 약품 데이터 + 코드잇 Kaggle 알약 데이터에서 추출
- palm 배경: Google Gemini 2.5-flash-image (Nano Banana API) 자동 생성 후 수작업 검수
- 기타 배경: 팀 자체 수작업 검수
- 합성 코드: 팀 자체 작성 (synthetic_images_v3.ipynb)

## 관련 자산

- **GitHub**: https://github.com/ZerofZero/codeit10_pj1
- **모델**: 
  - [healtheat-pill-rtmdet-v4](https://huggingface.co/wony98/healtheat-pill-rtmdet-v4) (이 데이터로 학습된 분석 우위 모델)
- **다른 합성 데이터**:
  - [synthetic-baseline](https://huggingface.co/datasets/wony98/healtheat-pill-synthetic-baseline)
  - [synthetic-v2](https://huggingface.co/datasets/wony98/healtheat-pill-synthetic-v2)

## 라이선스

Apache 2.0. 단 알약 누끼 추출 원본은 AI Hub / Kaggle 출처이므로 해당 약관 함께 따름.
