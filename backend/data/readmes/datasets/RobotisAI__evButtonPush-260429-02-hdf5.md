---
license: apache-2.0
language:
- ko
tags:
- robotics
- imitation-learning
- isaac-sim
- elevator-button
- omy-arm
- action-chunking-transformer
size_categories:
- 10K<n<100K
---

# evButtonPush — 30Hz 멀티카메라 RGB 데모셋 (50 종 distinct 엘베)

## 개요

엘리베이터 콜 버튼 누르기 task 의 ROBOTIS OMY 6-DoF 매니퓰레이터 시연 데이터셋. Isaac Sim 5.1 + Isaac Lab 환경에서 scripted teacher (DLS-IK + force-feedback) 로 자동 수집됨.

**핵심 차별점:** 각 데모마다 100종 elevator USD 풀에서 **서로 다른 변형 1개씩** 강제 사용 (`--usd-index`). 50 demos = **50 unique elevators (중복 0개)**. 형제 데이터셋 `260429-01` 은 episode 마다 random sample 이라 어떤 변형은 여러 번 나오고 다른 건 한 번도 안 나오는 분포라는 점에서 다름.

## 데이터셋 정보

| 항목 | 값 |
|---|---|
| 총 데모 수 | **50** (49 업로드 — bad-write 1개 제외) |
| Unique elevator USD | **50종 (모두 다름)** |
| 모두 success=True | ✅ (button_pressed + LED_lit + door_open + home_reached) |
| Frames per demo | ~650 ~ 740 (raw, 가변) |
| 제어/관측 주기 | **30 Hz** (sim 60 Hz physics, decimation=2) |
| 이미지 해상도 | **1920 × 1200** |
| 카메라 | **3대**: cam_wrist (link6), cam_top, cam_belly |
| Action 차원 | 7 (6 arm joint + 1 binary gripper) |
| State 관측 | qpos (10), qvel (10), eef_pos (3), eef_quat (4), call_button_pos (3), rel_dist (3), call_button_lit (1), button_pixel_uv_{wrist,top,belly} (각 3: u, v, valid) |
| 총 용량 | ~50 GB |
| Format | Per-demo HDF5 — `demo_NN.hdf5`, 약 1 GB/개 |

## HDF5 구조

```
demo_NN.hdf5
└── data/
    └── demo_<seed>/
        ├── actions (T, 7) float32
        ├── processed_actions (T, 10)
        ├── obs/
        │   ├── cam_wrist (T, 1200, 1920, 3) uint8
        │   ├── cam_top   (T, 1200, 1920, 3) uint8
        │   ├── cam_belly (T, 1200, 1920, 3) uint8
        │   ├── joint_pos (T, 10) float32
        │   ├── joint_vel (T, 10) float32
        │   ├── eef_pos (T, 3)
        │   ├── eef_quat (T, 4)
        │   ├── call_button_pos (T, 3)
        │   ├── call_button_lit (T, 1)              # 실제 press 시점 0 → 1 전환
        │   ├── rel_ee_call_button_distance (T, 3)
        │   ├── button_pixel_uv_wrist (T, 3)        # u, v, valid (1920×1200 픽셀 좌표)
        │   ├── button_pixel_uv_top   (T, 3)
        │   └── button_pixel_uv_belly (T, 3)
        ├── initial_state/
        └── states/
```

각 demo root attrs: `elevator_usd_index`, `elevator_usd_path`.

## Task / 환경 정보

- **Task ID**: `RobotisLab-CallButton-Right-OMY-Aux-v0`
- **Sim**: Isaac Sim 5.1, Isaac Lab
- **Robot**: ROBOTIS OMY (6-DoF, RH-P12-RN gripper, 4-finger mimic)
- **Scene**:
  - Pedestal (큐브, 0.8m × 0.8m × 0.908m), 로봇이 위에 mount
  - Elevator (100 variants 중 demo 마다 distinct USD, hall-side 정면)
  - Call button `CallBtn_0` (오른쪽), 런타임에 box collider 주입
- **조명**: DomeLight, demo 마다 randomized
- **Robot 초기 자세**: 버튼 정면 standoff 0.55–0.65 m, lateral ±5 cm random, joint Gaussian noise std 0.02 rad

## 수집 방식

각 데모는 별도 teacher launch 로 수집 (`--num-demos 1 --usd-index $ID`).
elevator ID 는 `random.sample(range(1, 101), 30)` 으로 두 머신에서 각각 30개씩 추출 → 합쳐서 중복 제거 → 50종 unique.

```bash
docker exec isaac-sim bash -lc \
  "cd /workspace/robotis_lab/scripts/my_codes && \
   /isaac-sim/python.sh diffik_teacher_jointpos_aux.py \
     --num-demos 1 --usd-index $ID --seed $((100 + idx)) \
     --enable_cameras --press-depth 0.005 --press-up 0.010 --headless \
     --dataset-file /mnt/Dataset/aux_demos/v02/demo_${idx}_usd_${ID}.hdf5"
```

## Teacher Phases (per demo)

| Phase | Steps (30 Hz) | 설명 |
|---|---|---|
| settle | initial | gripper 닫기 + physics settle |
| approach | 300 | joint-space cubic smoothstep HOME → goal_pre_q (IKPy) |
| press | up to 1500 | DLS micro-thrust 4 mm/step (PUSH_STEP_M=0.004) 으로 버튼 향해 |
| hold | 60 | 접촉 후 dwell |
| retract | 200 | DLS 로 goal_pre_q 거쳐 home_tip_w 까지 |
| home_idle | 150 | HOME 자세 유지 |

Press 판정: 그리퍼 contact force > 10 N **AND** 버튼 거리 < 4 cm → FSM `press_call_button` → LED + door FSM 동작. **버튼에 런타임 `UsdPhysics.CollisionAPI` (Cube prim 위 box collider) 주입되어 있어서 force 가 진짜 접촉으로 잡힘 (이전 spawn-impulse 가짜가 아님).**

## 주의 / 비고

- `call_button_lit` 채널이 t=0 부터 1 인 게 아니라 **진짜 press 시점에 0 → 1 로 전환** — IL supervisory signal 로 의미가 있음.
- 50 demos 모두 `success=True` 검증 (press + LED + door + home_reached).
- demo 당 wall-time 약 22 초.
- 이미지 크기는 Isaac Sim PinholeCameraCfg 의 1920 × 1200.
- 50 sweep 중 1 demo 가 HDF5 bad-write 로 변환 단계에서 drop 됨 → 실제 학습 가능 데모는 **49개**.

## 라이선스

Apache 2.0 (데이터 + 부속 코드).
