---
license: other
language:
- ko
tags:
- robotics
- lerobot
- open-manipulator-x
- imitation-learning
- manipulation
task_categories:
- robotics
---

# OMX 왼팔 모방학습 데이터 (Left-arm OMX imitation learning)

OpenMANIPULATOR-X(OMX) 왼팔(leader/follower) 텔레옵으로 수집한 LeRobot v3 데이터셋입니다.
과제: 블록을 집어 트레이에 놓기 (pick and place).

- 로봇: OMX follower(6 DOF + gripper) / OMX leader
- 기록: 30 fps, 카메라 2대 (top, wrist) 640x480
- 손목(`wrist_roll`)은 **degree 단위**의 연속 각도로 기록됩니다. 다른 단위로 만든 OMX 데이터와 바로 합치지 마세요.
- 그리퍼는 리더 개폐값을 오프셋 없이 직접 전달했습니다.

## 데이터 목록

| 폴더 | 수집일 | 에피소드 | 프레임 |
|---|---|---|---|
| `2026-10-29_v8` | 2026-10-29 | 10 | 11453 |
| `2026-10-30_v9` | 2026-10-30 | 10 | 8204 |
| `2026-10-30_v10` | 2026-10-30 | 10 | 7800 |
| `2026-10-30_v11` | 2026-10-30 | 10 | 10277 |
| `2026-10-31_v13` | 2026-10-31 | 10 | 8673 |
| `2026-10-31_v12_1ep` | 2026-10-31 | 1 | 626 |

각 폴더는 독립된 LeRobotDataset입니다 (`meta/`, `data/`, `videos/`).
`에피소드별 영상/`에는 에피소드 단위로 잘라낸 MP4(탑뷰/손목)와 `영상 목록.json`이 들어 있습니다.
`videos/`와 내용이 중복되므로 학습에는 쓰지 않고 확인용으로만 사용하세요.

## 구조

```
<session>/
  meta/info.json          # fps, features, 카메라 키, codebase_version
  meta/episodes/          # 에피소드 메타데이터
  data/                   # parquet (observation.state, action, ...)
  videos/                 # observation.images.top, observation.images.wrist (AV1)
  에피소드별 영상/탑뷰|손목/  # 확인용 MP4 (H.264)
  영상 목록.json
```

- 관절 키: `observation.state` / `action` = 6 관절 + `gripper.pos` (LeRobot 표준 순서)
- 카메라 키: `observation.images.top`, `observation.images.wrist`
- 태스크 문장: `Pick up the block and put it in the tray`

## 사용 방법

```bash
pip install "lerobot>=0.3"
hf download Purple-SY/omx-left-arm --repo-type dataset --local-dir omx-left-arm

python - <<'PY'
from lerobot.datasets.lerobot_dataset import LeRobotDataset
ds = LeRobotDataset("Purple-SY/omx-left-arm", root="omx-left-arm/2026-10-31_v13")
print(ds.meta.total_episodes, ds.meta.fps)
print(next(iter(ds)).keys())
PY
```

학습은 ACT / Diffusion Policy 같은 행동복제(imitation learning) 파이프라인을 권장합니다.
에피소드 수가 적으므로(세션당 10개) 정책 학습에는 여러 세션을 합쳐 50개 이상을 권장합니다.

## 라이선스 / 문의

랩 내부 공유용 데이터입니다. 외부 재배포 전 소유자에게 문의하세요.
