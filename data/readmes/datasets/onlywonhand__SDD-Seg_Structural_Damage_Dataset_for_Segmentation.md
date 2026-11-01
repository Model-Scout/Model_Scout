---
license: cc-by-nc-4.0
task_categories:
- image-segmentation
- image-classification
- object-detection
language:
- ko
tags:
- civil-engineering
- structural-health-monitoring
- crack-detection
- construction
size_categories:
- 100K<n<1M
---

# Struct-Damage-Seg-V1 (Structural Damage Segmentation Dataset)

## 📌 소개 (Introduction)
이 데이터셋은 토목 구조물(교량, 터널, 옹벽 등)의 손상 탐지(Damage Detection)와 구조물 부재 분류(Structural Component Classification)를 동시에 수행하기 위해 구축된 멀티태스크 데이터셋입니다.

AI Hub의 '시설물 균열 탐지 데이터' 등을 기반으로 재가공되었으며, **ConvNeXt V2** 등의 최신 모델 학습에 최적화된 **14채널 세그멘테이션 마스크**를 포함하고 있습니다.

## 📂 데이터셋 구조 (Structure)
데이터셋은 원본 이미지, 전처리된 마스크, 그리고 메타데이터가 담긴 CSV 파일로 구성됩니다.

- **images/**: 원본 촬영 이미지 (JPG)
- **masks/**: 전처리된 마스크 이미지 (PNG, Indexed Color)
- **train_labels.csv**: 학습용 데이터 인덱스 및 메타데이터
- **val_labels.csv**: 검증용 데이터 인덱스 및 메타데이터

### CSV 컬럼 설명
| 컬럼명 | 설명 | 예시 |
| :--- | :--- | :--- |
| `image_path` | 이미지 파일의 상대/절대 경로 | `./images/image_01.jpg` |
| `mask_path` | 마스크 파일의 경로 | `./masks/image_01.png` |
| `structure_class_id` | 구조물 부재 ID (0~5) | `3` (Slab) |
| `damage_types` | 포함된 손상 종류 ID | `1\|3` (Crack + Efflorescence) |
| `patterns` | 손상 패턴 속성 | `수직\|망상형` |
| `raw_loc` | 원본 데이터의 촬영 위치 설명 | `철도교량-상부구조` |

---

## 🏷️ 클래스 정의 (Class Definitions)

이 데이터셋은 **총 14개 채널**의 출력을 가정하고 설계되었습니다. 모델 학습 시 아래 매핑 테이블을 참고하십시오.

### 1. 손상 클래스 (Damage Segmentation) - Channels 0~7
마스크 이미지(PNG)의 픽셀 값에 해당합니다.

| ID | Class Name | 한글 명칭 | 설명 |
| :--- | :--- | :--- | :--- |
| **0** | Background | 배경 | 손상이 없는 영역 |
| **1** | Crack | 균열 | 콘크리트 표면의 갈라짐 |
| **2** | Corrosion | 철근 부식 | 철근 노출 및 녹 발생 |
| **3** | Efflorescence | 백화 | 표면에 하얗게 일어난 석회 물질 |
| **4** | Mold | 곰팡이/이끼 | 습기로 인한 오염 |
| **5** | Spalling | 박락/박리 | 콘크리트가 떨어져 나간 상태 (들뜸 포함) |
| **6** | (Reserved) | - | (현재 사용 안 함, 필요 시 Strain 등으로 활용) |
| **7** | Waterleak | 누수 | 물이 새어나온 흔적 |

### 2. 구조물 클래스 (Structure Classification) - Channels 8~13
이미지 전체에 대한 분류(Weakly Supervised) 라벨입니다.

| ID | Class Name | 한글 명칭 | 매핑된 원본 키워드 예시 |
| :--- | :--- | :--- | :--- |
| **0** | Background | 미분류/기타 | - |
| **1** | Column | 기둥/교각 | 교각, 기둥 |
| **2** | Beam | 보/거더 | 거더, 빔 |
| **3** | Slab | 슬래브/상판 | 상부구조, 상판, 슬래브, 교량(미상세) |
| **4** | Opening | 개구부 | 창호, 개구부 |
| **5** | Wall | 벽체 | 옹벽, 터널, 지하차도, 방음벽 |

---

## 🛠️ 사용 방법 (Usage Example)

이 데이터셋을 `Dataset` 클래스로 로드하여 14채널 텐서로 변환하는 Python 예제입니다.

```python
import cv2
import torch
import pandas as pd
from torch.utils.data import Dataset
import numpy as np

class StructureDamageDataset(Dataset):
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        row = self.df.iloc[idx]
        
        # 이미지 로드
        image = cv2.imread(row['image_path'])
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # 마스크 로드 (PNG 파일은 0~7의 손상 값을 가짐)
        mask_png = cv2.imread(row['mask_path'], cv2.IMREAD_UNCHANGED)
        
        # 14채널 통합 마스크 생성 (H, W, 14)
        H, W = image.shape[:2]
        target = np.zeros((H, W, 14), dtype=np.float32)
        
        # [Ch 0~7] 손상 정보 One-hot Encoding
        for cls_id in range(1, 8):
            target[:, :, cls_id] = (mask_png == cls_id).astype(np.float32)
            
        # [Ch 8~13] 구조물 정보 (Weakly Supervised - 전체 채우기)
        struct_id = int(row['structure_class_id']) # 0~5
        target[:, :, 8 + struct_id] = 1.0 
        
        return image, target