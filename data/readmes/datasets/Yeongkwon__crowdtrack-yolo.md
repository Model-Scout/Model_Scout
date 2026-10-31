---
license: apache-2.0
task_categories:
- object-detection
language:
- ko
- en
tags:
- person-detection
- pedestrian
- crowd
- cctv
- construction-site
- yolo
pretty_name: CrowdTrack Person Detection (YOLO)
size_categories:
- 1K<n<10K
configs:
- config_name: default
  drop_labels: true  # 폴더명(train/val)을 클래스로 오인해 label 열을 만드는 것 방지
  data_files:
  - split: train
    path: images/train/*
  - split: validation
    path: images/val/*
---

# CrowdTrack Person Detection (YOLO)

[Fleyderer/CrowdTrack-MOT](https://huggingface.co/datasets/Fleyderer/CrowdTrack-MOT)(원저: Fu et al., 2025, Fudan University의 CrowdTrack)에서 **5프레임마다 1장**을 골라 사람 검출용 **YOLO TXT** 라벨을 붙인 데이터셋입니다. 이미지 파일은 원본과 바이트까지 같습니다.

> 시연용 시퀀스 `track0027`(교량 공사장 고정 CCTV)과 같은 카메라의 `track0026`은 시연 성능을 정직하게 보이려고 **넣지 않았습니다**.

## 구성

| Split | 시퀀스 | 이미지 | 바운딩 박스 |
|---|---:|---:|---:|
| train | 30 | 6,251 | 126,055 |
| val | 1 | 240 | 3,133 |
| **합계** | **31** | **6,491** | **129,188** |

- 크기: 약 6.1GB
- 해상도: 1920×1080 (`track0024`, `track0025`만 2560×1440)
- 형식: `track0001`–`track0004`는 PNG, 나머지는 JPG
- 모든 이미지에 사람이 한 명 이상 있습니다.

### 클래스

| YOLO class | 이름 | 설명 |
|---:|---|---|
| 0 | `person` | 사람 (원본 MOT 정답의 전신 박스) |

## 디렉터리 구조

```
├── README.md
├── LICENSE
├── data.yaml                  # train: images/train, val: images/val, names: {0: person}
├── images/
│   ├── train/                 # {시퀀스}_{프레임:06d}.jpg|png
│   └── val/
└── labels/
    ├── train/                 # {시퀀스}_{프레임:06d}.txt
    └── val/
```

라벨은 줄마다 `0 cx cy w h`(이미지 크기로 정규화한 중심·크기, 소수 6자리)입니다. `data.yaml`에는 `path`가 없어서 받은 폴더 기준으로 경로를 찾습니다.

## 분할 방법

같은 카메라의 다른 시간대 영상은 배경이 같으므로 **카메라 단위**로 나눴습니다.

| 용도 | 시퀀스 | 장면 |
|---|---|---|
| train | 나머지 30개 | 이동·보행 시점 26개, 고정 CCTV 4개(`track0024`, `track0025` 철로 작업, `track0029`, `track0030` 생활구역 출입 통로) |
| val | `track0028` | 기초 굴착장 고정 CCTV |
| 제외(시연용) | `track0027` (시연), `track0026` (같은 카메라) | 교량 공사장 고정 CCTV |

프레임 번호 끝자리가 1·6인 프레임(1, 6, 11, …)만 골랐습니다. 이웃한 프레임은 거의 같기 때문입니다.

## 사용 예

```python
from huggingface_hub import snapshot_download
from ultralytics import YOLO

root = snapshot_download("Yeongkwon/crowdtrack-yolo", repo_type="dataset")
YOLO("yolo26n.pt").train(data=f"{root}/data.yaml", epochs=30, imgsz=640)
```

## 출처

| 구분 | 출처 |
|---|---|
| 원저작자 | Teng Fu, Yuwen Chen, Zhuofan Chen, Mengyang Zhao, Bin Li, Xiangyang Xue — Fudan University |
| 논문 | [CrowdTrack: A Benchmark for Difficult Multiple Pedestrian Tracking in Real Scenarios](https://arxiv.org/abs/2507.02479) (arXiv:2507.02479, 2025) |
| 원 배포처 | [GitHub: loseevaya/CrowdTrack](https://github.com/loseevaya/CrowdTrack), [HF: Loseevaya/CrowdTrack](https://huggingface.co/datasets/Loseevaya/CrowdTrack) |
| 직접 출처 | [HF: Fleyderer/CrowdTrack-MOT](https://huggingface.co/datasets/Fleyderer/CrowdTrack-MOT) (MOT 형식 변환, 프레임 밖 박스 잘라냄) |

### 원본 대비 변경 사항

- 5프레임마다 1장만 수록
- 시연용 시퀀스 `track0027`과 같은 카메라의 `track0026` 제외
- MOT `gt.txt`에서 YOLO TXT 라벨 생성(클래스 `person` 하나, 추적 ID는 쓰지 않음). 너비·높이 0인 박스는 제외
- 이미지 픽셀, 해상도, 파일 형식은 변경하지 않음

## 라이선스

[Apache License 2.0](LICENSE). 원 배포처(GitHub, HF)의 라이선스를 따릅니다. 원본 이미지와 어노테이션의 저작권은 원저작자에게 있습니다.

## 인용

이 데이터셋을 사용하면 원 논문을 인용해 주세요.

```bibtex
@article{fu2025crowdtrack,
  title   = {CrowdTrack: A Benchmark for Difficult Multiple Pedestrian Tracking in Real Scenarios},
  author  = {Fu, Teng and Chen, Yuwen and Chen, Zhuofan and Zhao, Mengyang and Li, Bin and Xue, Xiangyang},
  journal = {arXiv preprint arXiv:2507.02479},
  year    = {2025}
}
```
