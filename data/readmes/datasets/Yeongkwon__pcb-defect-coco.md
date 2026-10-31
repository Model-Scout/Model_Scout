---
license: mit
task_categories:
- object-detection
language:
- ko
- en
tags:
- pcb
- defect-detection
- manufacturing
- coco
- synthetic
pretty_name: PCB Defect Detection (COCO)
size_categories:
- n<1K
configs:
- config_name: default
  drop_labels: true  # 폴더명(train/val)을 클래스로 오인해 label 열을 만드는 것 방지
  data_files:
  - split: train
    path: train/*.jpg
  - split: validation
    path: val/*.jpg
---

# PCB Defect Detection (COCO)

[RobotHuman/PCB_defect](https://huggingface.co/datasets/RobotHuman/PCB_defect)(원저: Huang & Wei, 2019, Peking University)의 Pascal VOC 어노테이션을 **COCO JSON** 형식으로 변환하고 train/val로 분할한 데이터셋입니다. 이미지와 바운딩 박스 좌표는 원본과 동일합니다.

> ⚠️ 결함은 템플릿 보드 촬영 이미지에 Photoshop으로 합성한 것으로, 실제 공정에서 발생한 결함이 아닙니다.

## 구성

| Split | 이미지 | 바운딩 박스 |
|---|---:|---:|
| train | 555 | 2,371 |
| val | 138 | 582 |
| **합계** | **693** | **2,953** |

이미지 해상도는 2240–3056 × 1586–2530 px로 이미지마다 다릅니다.

### 클래스

| `category_id` | 이름 | 설명 | train 박스 | val 박스 |
|---:|---|---|---:|---:|
| 1 | `missing_hole` | 있어야 할 구멍이 없음 | 397 | 100 |
| 2 | `mouse_bite` | 배선·패드 가장자리가 갉아먹힌 듯 깎임 | 390 | 102 |
| 3 | `open_circuit` | 연결돼야 할 배선이 끊어짐 (단선) | 393 | 89 |
| 4 | `short` | 떨어져 있어야 할 배선이 붙음 (단락) | 394 | 97 |
| 5 | `spur` | 배선 옆으로 튀어나온 돌기 | 388 | 100 |
| 6 | `spurious_copper` | 회로와 무관한 위치의 구리 잔여물 | 409 | 94 |

## 디렉터리 구조

```
├── README.md
├── LICENSE
├── annotations/
│   ├── instances_train.json   # COCO detection
│   └── instances_val.json
├── train/                     # *.jpg
└── val/
```

`bbox`는 `[x, y, width, height]` 절대 픽셀 좌표이고, `iscrowd`는 모두 0입니다.

## 분할 방법

원본 클래스 폴더별로 파일명을 정렬한 뒤 `random.Random(42)`로 섞어, 각 클래스의 20%(23장)를 val로, 나머지를 train으로 나눴습니다.

## 사용 예

```python
from huggingface_hub import snapshot_download

root = snapshot_download("Yeongkwon/pcb-defect-coco", repo_type="dataset")

from pycocotools.coco import COCO
coco = COCO(f"{root}/annotations/instances_train.json")
```

## 출처

| 구분 | 출처 |
|---|---|
| 원저작자 | Weibo Huang, Peng Wei — Open Lab on Human Robot Interaction, Peking University |
| 논문 | [A PCB Dataset for Defects Detection and Classification](https://arxiv.org/abs/1901.08204) (arXiv:1901.08204, 2019) |
| 직접 출처 | [RobotHuman/PCB_defect](https://huggingface.co/datasets/RobotHuman/PCB_defect) (이미지 693장 + Pascal VOC XML) |
| 이전 배포처 | [GitHub: Ixiaohuihuihui/Tiny-Defect-Detection-for-PCB](https://github.com/Ixiaohuihuihui/Tiny-Defect-Detection-for-PCB), [Kaggle: akhatova/pcb-defects](https://www.kaggle.com/datasets/akhatova/pcb-defects) |

### 원본 대비 변경 사항

- Pascal VOC XML → COCO JSON(`annotations/`) 변환
- 클래스별 8:2 train/val 분할
- 이미지 픽셀, 클래스 라벨, 박스 좌표는 변경하지 않음

## 라이선스

[MIT](LICENSE). 직접 출처인 [RobotHuman/PCB_defect](https://huggingface.co/datasets/RobotHuman/PCB_defect)의 라이선스 표기를 따릅니다. 원본 이미지와 어노테이션의 저작권은 원저작자에게 있습니다.

원 배포처(GitHub, Kaggle)에는 라이선스가 명시되어 있지 않습니다(Kaggle 표기: Unknown). 상업적으로 이용하려면 원저작자의 이용 조건을 별도로 확인하세요.

## 인용

이 데이터셋을 사용하면 원 논문을 인용해 주세요.

```bibtex
@article{huang2019pcb,
  title   = {A PCB Dataset for Defects Detection and Classification},
  author  = {Huang, Weibo and Wei, Peng},
  journal = {arXiv preprint arXiv:1901.08204},
  year    = {2019}
}
```
