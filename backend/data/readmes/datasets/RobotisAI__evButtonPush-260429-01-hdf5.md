---
license: apache-2.0
language:
- en
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

# evButtonPush — 30Hz Multi-Camera RGB Demo Set v01

## 개요 / Overview

엘리베이터 콜 버튼 누르기 task에 대한 ROBOTIS OMY 6-DoF 매니퓰레이터 시연 데이터셋. Isaac Sim 5.1 + Isaac Lab 환경에서 scripted teacher (DLS-IK + force-feedback)로 자동 수집.

Imitation learning demo dataset for elevator call button press task using ROBOTIS OMY 6-DoF arm. Collected automatically via scripted teacher (DLS-IK + force-feedback) in Isaac Sim 5.1 + Isaac Lab.

## 데이터셋 정보 / Dataset Info

| 항목 | 값 |
|---|---|
| Demos | **40** |
| 모두 success=True | ✅ (button_pressed + LED_lit + door_open + home_reached) |
| Frames per demo | ~568 (variable) |
| Total frames | ~22,720 |
| Action/observation rate | **30 Hz** (sim 60 Hz physics, decimation=2) |
| Image resolution | **1920 × 1200** |
| Cameras | **3 cams**: cam_wrist (link6 mounted), cam_top, cam_belly |
| Action space | 7-dim (6 arm joints + 1 binary gripper) |
| State obs | qpos, qvel (10), eef_pos (3), eef_quat (4), call_button_pos (3), rel_dist (3), call_button_lit (1), action history |
| Total file size | ~31 GB |
| Format | Single HDF5 (multi-episode) |

## HDF5 구조 / Structure

```
data/
  demo_0/
    actions (T, 7) float32
    obs/
      cam_wrist (T, 1200, 1920, 3) uint8
      cam_top (T, 1200, 1920, 3) uint8
      cam_belly (T, 1200, 1920, 3) uint8
      joint_pos (T, 10) float32
      joint_vel (T, 10) float32
      eef_pos (T, 3) float32
      eef_quat (T, 4) float32
      call_button_pos (T, 3) float32
      rel_ee_call_button_distance (T, 3) float32
      call_button_lit (T, 1) float32
      actions (T, 7) float32
    initial_state/  (joint_position, root_pose, etc.)
    states/         (per-step robot/scene physics state)
  demo_1/
  ...
  demo_39/
```

각 demo 그룹 attrs: `success: True`, `num_samples: T`.

## Task / 환경 정보

- **Task**: `RobotisLab-CallButton-Right-OMY-Aux-v0`
- **Sim**: Isaac Sim 5.1, Isaac Lab
- **Robot**: OMY (6-DoF, RH-P12-RN gripper, 4-finger mimic)
- **Scene**:
  - Pedestal (cube, 0.8m × 0.8m × 0.908m)
  - Robot mounted on pedestal
  - Elevator (random USD from 100 variants per episode, hall-side facing)
  - Call button (CallBtn_0) on right side
- **Light**: DomeLight 5600 intensity, randomized per episode
- **Robot init**: front-of-button, 55-65cm standoff, ±5cm lateral random, joint randomization (Gaussian, std 0.02 rad)

## 수집 명령어 / Collection Command

```bash
# 30 demos (seeds 0-29)
/isaac-sim/python.sh scripts/my_codes/diffik_teacher_jointpos_aux.py \
  --num-demos 30 --seed 0 --headless --enable_cameras \
  --approach-steps 50 --press-steps 200 --stall-steps 10 \
  --contact-force-threshold 5.0 --hold-steps 15 \
  --return-steps 150 --home-idle-steps 75 --press-depth 0.035 \
  --dataset-file demo.hdf5

# 10 more (seeds 30-39) — same params
```

## Teacher Phases (per demo)

| Phase | Steps (30Hz) | 설명 |
|---|---|---|
| settle | initial | Gripper close + physics settle |
| approach | 50 | Joint-space cubic smoothstep HOME → goal_pre_q (IKPy) |
| press | up to 200 | DLS micro-thrust 4mm/step toward button (PUSH_STEP_M=0.004) |
| hold | 15 | Dwell after contact |
| retract | 150 | Smoothstep back to goal_pre_q |
| home_idle | 75 | Hold at HOME |

Press validation: gripper finger contact force > 5N triggers FSM button press → LED + door.

## Notes / 비고

- Per-demo **30 Hz action rate** is more realistic for real-world deployment (vs 60 Hz). Total wall-time per demo ~19s.
- All 40 demos verified `success=True` (pressed + LED lit + door opened + home reached).
- Image dimensions match Isaac Sim camera annotator output (1920 × 1200 PinholeCameraCfg).

## License

Apache 2.0 (model + data).
