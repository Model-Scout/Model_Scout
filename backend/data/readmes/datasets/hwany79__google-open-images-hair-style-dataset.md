---
language:
- en
- ko
license: mit
task_categories:
- image-classification
- object-detection
- image-segmentation
pretty_name: Google Open Images Hair Style Dataset
size_categories:
- 1K<n<10K
tags:
- computer-vision
- open-images
- hair-style
- human
- image-classification
- object-detection
- segmentation
- custom-dataset
dataset_info:
  features:
  - name: image
    dtype: image
  - name: label
    dtype: string
  splits:
  - name: train
  - name: validation
---

# Google Open Images — Hair Style Dataset

> 🇺🇸 English | [🇰🇷 한국어](#korean)

---

## Overview

This dataset is a curated custom subset of the [Google Open Images V7](https://storage.googleapis.com/openimages/web/index.html) dataset, specifically filtered to include images of **humans with various hair styles**.  
It is intended for use in computer vision research and applications such as **hair style classification**, **person detection**, and **instance segmentation**.

| Split | Purpose |
|-------|---------|
| `train` | Model training |
| `validation` | Model evaluation / hyperparameter tuning |

---

## Dataset Description

### Source
- **Original Dataset**: [Google Open Images V7](https://storage.googleapis.com/openimages/web/index.html)
- **Filter Criteria**: Images containing human subjects with annotated hair-style-related labels
- **Download Tool**: [FiftyOne](https://voxel51.com/fiftyone/) open-source dataset management library

### Annotation Types
This dataset provides three types of annotations:

| Type | File | Description |
|------|------|-------------|
| Classification | `classifications.csv` | Image-level labels (e.g., whether a certain label is present) |
| Detection | `detections.csv` | Bounding box coordinates for detected objects |
| Segmentation | `segmentations.csv` + `masks/` | Pixel-level instance segmentation masks |

### Label Files Detail

| File | Columns | Description |
|------|---------|-------------|
| `classifications.csv` | `ImageID`, `Source`, `LabelName`, `Confidence` | Image-level positive/negative labels |
| `detections.csv` | `ImageID`, `LabelName`, `Confidence`, `XMin`, `XMax`, `YMin`, `YMax`, `IsOccluded`, `IsTruncated`, `IsGroupOf`, `IsDepiction`, `IsInside` | Bounding box annotations (normalized 0~1) |
| `segmentations.csv` | `MaskPath`, `ImageID`, `LabelName`, `BoxID`, `BoxXMin`, `BoxXMax`, `BoxYMin`, `BoxYMax`, `PredictedIoU`, `Clicks` | Segmentation polygon/mask references |
| `masks/` | PNG images | Binary mask images (0=background, 255=object) |

### Metadata Files

| File | Description |
|------|-------------|
| `classes.csv` | Mapping of label codes (e.g., `/m/xxxxx`) to human-readable class names |
| `hierarchy.json` | Class hierarchy tree (parent-child relationships between labels) |
| `image_ids.csv` | Mapping of `ImageID` to original image URL, Flickr URL, license info, etc. |
| `segmentation_classes.csv` | List of classes that have segmentation annotations available |

---

## Dataset Structure

```text
google-open-images-hair-style-dataset/
│
├── train/
│   ├── data/                        ← Raw image files (.jpg)
│   ├── labels/
│   │   ├── masks/
│   │   │   ├── 0/                   ← Segmentation mask images (part 0)
│   │   │   └── 1/                   ← Segmentation mask images (part 1)
│   │   ├── classifications.csv
│   │   ├── detections.csv
│   │   └── segmentations.csv
│   └── metadata/
│       ├── classes.csv
│       ├── hierarchy.json
│       ├── image_ids.csv
│       └── segmentation_classes.csv
│
└── validation/
    ├── data/                        ← Raw image files (.jpg)
    ├── labels/
    │   ├── masks/
    │   │   ├── 0/                   ← Segmentation mask images (part 0)
    │   │   └── 1/                   ← Segmentation mask images (part 1)
    │   ├── classifications.csv
    │   ├── detections.csv
    │   └── segmentations.csv
    └── metadata/
        ├── classes.csv
        ├── hierarchy.json
        ├── image_ids.csv
        └── segmentation_classes.csv
```

---

## Usage Example

```python
from datasets import load_dataset

ds = load_dataset("hwany79/google-open-images-hair-style-dataset")
print(ds)
```

### Loading with pandas (CSV labels)

```python
import pandas as pd

# Load detection annotations
detections = pd.read_csv("train/labels/detections.csv")
print(detections.head())

# Filter by label (e.g., Person)
person_df = detections[detections["LabelName"] == "/m/01g317"]
print(f"Person detections: {len(person_df)}")
```

---

## License

This dataset is derived from [Google Open Images V7](https://storage.googleapis.com/openimages/web/index.html).  
Images are licensed under [Creative Commons Attribution 2.0](https://creativecommons.org/licenses/by/2.0/).  
Annotations are licensed under [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).  

This repository is released under the **MIT License**.

---

## Citation

If you use this dataset in your research, please cite the original Open Images dataset:

```bibtex
@article{OpenImages,
  author = {Alina Kuznetsova and Hassan Rom and Neil Alldrin and Jasper Uijlings and Ivan Krasin and Jordi Pont-Tuset and Shahab Shahab and Stefan Popov and Matteo Malloci and Alexander Kolesnikov and Tom Duerig and Vittorio Ferrari},
  title = {The Open Images Dataset V4},
  year = {2020},
  journal = {International Journal of Computer Vision (IJCV)}
}
```

---

<a name="korean"></a>

# Google Open Images — 헤어 스타일 데이터셋

> [🇺🇸 English](#top) | 🇰🇷 한국어

---

## 개요

이 데이터셋은 [Google Open Images V7](https://storage.googleapis.com/openimages/web/index.html) 데이터셋에서  
**다양한 헤어 스타일을 가진 사람 이미지**만을 필터링하여 구성한 커스텀 서브셋입니다.  
**헤어 스타일 분류**, **사람 탐지**, **인스턴스 세그멘테이션** 등 컴퓨터 비전 연구 및 응용에 활용할 수 있습니다.

| 분할 | 용도 |
|------|------|
| `train` | 모델 학습용 |
| `validation` | 모델 평가 / 하이퍼파라미터 튜닝용 |

---

## 데이터셋 설명

### 출처
- **원본 데이터셋**: [Google Open Images V7](https://storage.googleapis.com/openimages/web/index.html)
- **필터 기준**: 헤어 스타일 관련 레이블이 어노테이션된 사람 이미지
- **다운로드 도구**: [FiftyOne](https://voxel51.com/fiftyone/) 오픈소스 데이터셋 관리 라이브러리

### 어노테이션 유형

| 유형 | 파일 | 설명 |
|------|------|------|
| 분류 (Classification) | `classifications.csv` | 이미지 수준의 레이블 (특정 레이블의 존재 여부) |
| 탐지 (Detection) | `detections.csv` | 객체의 바운딩 박스 좌표 |
| 세그멘테이션 (Segmentation) | `segmentations.csv` + `masks/` | 픽셀 단위 인스턴스 세그멘테이션 마스크 |

### 레이블 파일 상세

| 파일 | 컬럼 | 설명 |
|------|------|------|
| `classifications.csv` | `ImageID`, `Source`, `LabelName`, `Confidence` | 이미지 수준 긍정/부정 레이블 |
| `detections.csv` | `ImageID`, `LabelName`, `Confidence`, `XMin`, `XMax`, `YMin`, `YMax`, `IsOccluded`, `IsTruncated`, `IsGroupOf`, `IsDepiction`, `IsInside` | 바운딩 박스 어노테이션 (0~1 정규화 좌표) |
| `segmentations.csv` | `MaskPath`, `ImageID`, `LabelName`, `BoxID`, `BoxXMin`, `BoxXMax`, `BoxYMin`, `BoxYMax`, `PredictedIoU`, `Clicks` | 세그멘테이션 마스크 참조 정보 |
| `masks/` | PNG 이미지 | 이진 마스크 이미지 (0=배경, 255=객체) |

### 메타데이터 파일

| 파일 | 설명 |
|------|------|
| `classes.csv` | 레이블 코드(예: `/m/xxxxx`)와 사람이 읽을 수 있는 클래스 이름 매핑 |
| `hierarchy.json` | 클래스 계층 트리 (레이블 간 부모-자식 관계) |
| `image_ids.csv` | `ImageID`와 원본 이미지 URL, Flickr URL, 라이선스 정보 등의 매핑 |
| `segmentation_classes.csv` | 세그멘테이션 어노테이션이 존재하는 클래스 목록 |

---

## 데이터셋 구조

```text
google-open-images-hair-style-dataset/
│
├── train/
│   ├── data/                        ← 원본 이미지 파일 (.jpg)
│   ├── labels/
│   │   ├── masks/
│   │   │   ├── 0/                   ← 세그멘테이션 마스크 이미지 (파트 0)
│   │   │   └── 1/                   ← 세그멘테이션 마스크 이미지 (파트 1)
│   │   ├── classifications.csv
│   │   ├── detections.csv
│   │   └── segmentations.csv
│   └── metadata/
│       ├── classes.csv
│       ├── hierarchy.json
│       ├── image_ids.csv
│       └── segmentation_classes.csv
│
└── validation/
    ├── data/                        ← 원본 이미지 파일 (.jpg)
    ├── labels/
    │   ├── masks/
    │   │   ├── 0/                   ← 세그멘테이션 마스크 이미지 (파트 0)
    │   │   └── 1/                   ← 세그멘테이션 마스크 이미지 (파트 1)
    │   ├── classifications.csv
    │   ├── detections.csv
    │   └── segmentations.csv
    └── metadata/
        ├── classes.csv
        ├── hierarchy.json
        ├── image_ids.csv
        └── segmentation_classes.csv
```

---

## 사용 예시

```python
from datasets import load_dataset

ds = load_dataset("hwany79/google-open-images-hair-style-dataset")
print(ds)
```

### pandas로 CSV 레이블 로드하기

```python
import pandas as pd

# 탐지 어노테이션 로드
detections = pd.read_csv("train/labels/detections.csv")
print(detections.head())

# 특정 레이블로 필터링 (예: 사람)
person_df = detections[detections["LabelName"] == "/m/01g317"]
print(f"사람 탐지 수: {len(person_df)}")
```

---

## 라이선스

이 데이터셋은 [Google Open Images V7](https://storage.googleapis.com/openimages/web/index.html)에서 파생되었습니다.  
이미지는 [Creative Commons Attribution 2.0](https://creativecommons.org/licenses/by/2.0/) 라이선스가 적용됩니다.  
어노테이션은 [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) 라이선스가 적용됩니다.  

이 리포지토리는 **MIT 라이선스**로 공개됩니다.

---

## 인용

이 데이터셋을 연구에 활용하시는 경우, 원본 Open Images 데이터셋을 다음과 같이 인용해 주세요:

```bibtex
@article{OpenImages,
  author = {Alina Kuznetsova and Hassan Rom and Neil Alldrin and Jasper Uijlings and Ivan Krasin and Jordi Pont-Tuset and Shahab Shahab and Stefan Popov and Matteo Malloci and Alexander Kolesnikov and Tom Duerig and Vittorio Ferrari},
  title = {The Open Images Dataset V4},
  year = {2020},
  journal = {International Journal of Computer Vision (IJCV)}
}
```
