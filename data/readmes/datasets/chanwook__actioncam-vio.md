---
license: cc-by-4.0
language:
- ko
tags:
- robotics
- slam
- visual-inertial-odometry
- action-camera
- umi
pretty_name: actioncam-vio dataset
---

# actioncam-vio 데이터셋

[actioncam-vio](https://github.com/redEddie/actioncam-vio) 파이프라인(UMI 스타일
액션캠 VIO)의 원본 영상 + SLAM 산출물입니다. 액션캠 하나로 촬영한 MP4에서
RGB + IMU(내장 텔레메트리)를 추출해 캘리브레이션·ORB-SLAM3 mono-inertial까지
재현할 수 있습니다.

## 카메라

| 카메라 | 영상 | IMU | FOV (H/V/D) |
|---|---|---|---|
| GoPro HERO7 Black | 2704×2028 @59.94, H.264 | GPMF 197.7 Hz | 120.5°/93.7°/146.6° |
| Insta360 Ace Pro 2 | 2688×2016 @59.94, HEVC | 트레일러 994 Hz | 130.1°/104.0°/152.3° |

- **인카메라 안정화 OFF 상태로 촬영** (VIO 기하 보존)
- IMU는 영상 파일 안에 포함되어 있음 (별도 파일 없음 — 파이프라인이 추출)
- ChArUco 보드: 10×8칸, 정사각형 0.023 m, `DICT_ARUCO_ORIGINAL` legacy 패턴

## 구성

```
hero7black/   GoPro 원본 5편 (보드 1, SLAM 4)         ~5.3 GB
acepro2/      Insta360 원본 6편 (보드 2, SLAM 4 — 주간/야간/지하주차장)  ~5.0 GB
              + 웹캠(UVC) 모드 보드 영상 2편 (1080p30 MJPEG — VLA 롤아웃 기하 캘리브레이션용)
outputs/      ORB-SLAM3 산출물 (궤적 csv/tum, 통계, 맵 점군 ply, rerun rrd)
              — 코드 저장소 커밋 02d695a 기준 산출물 (ORB-SLAM3 비결정성 때문에
                재실행 결과와 수 % 차이 가능; 문서의 수치는 이 산출물 기준)
videos.csv    영상별 메타데이터 (해상도/길이/용도/장면)
```

영상별 상세는 `videos.csv` 참조. 대표 결과:
- 근거리 ATE(ChArUco mm급 기준 대비): **Ace Pro 2 1.23 cm / HERO7 1.88 cm** (rigid)
- 저조도(지하주차장/야간 공원): **99.8% / 98.8% 추적** — VID_528(주간)과
  VID_521(야간)은 같은 장소의 주/야간 페어 벤치마크

## 사용법

```bash
# 코드 저장소와 같은 배치로 다운로드
hf download chanwook/actioncam-vio --repo-type dataset --local-dir data
# 이후 github.com/redEddie/actioncam-vio 의 README 명령이 그대로 동작
```

## 주의

- 공공장소에서 촬영된 영상으로 행인이 포함될 수 있습니다. 연구 목적으로만
  사용하고, 재배포 시 해당 지역 개인정보 규정을 준수하세요.
