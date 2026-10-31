---
license: other
task_categories:
- robotics
tags:
- LeRobot
- imitation-learning
- vision-language-action
- pi0.5
- openpi
- gr00t
- rdt
- teleoperation
- apple-vision-pro
language:
- ko
---

# ETRI VR Robotics Data Research — 데이터 · 가중치 저장소

Apple Vision Pro 텔레오퍼레이션으로 ROBOTIS **AI Worker FFW-BG2** 실물 시연 데이터를 모으고,
VLA(Vision-Language-Action) 모델 3종(π0.5 · GR00T N1.7 · RDT-1B)을 학습해 **"언어가 로봇의
행동을 실제로 바꾸는가"** 를 실기로 검증하는 연구의 데이터·가중치 정본입니다.

- **GitHub (코드 · 문서 · 연구 서사)**: https://github.com/logan0741/ETRI_VR_Robotics_data_research
- 수행: 김건희 (전남대학교 / ETRI) · 로봇: ROBOTIS AI Worker FFW-BG2 · 물체: YCB 세트

## 브랜치 안내 — 무엇을 받아야 하는가

| 브랜치 | 내용 | 이런 목적이면 |
|---|---|---|
| **`main`** (여기) | 이 문서 + **원본 시연 데이터** `data/raw/P0~P3` (태스크당 100 에피소드) | 원본 데이터로 직접 가공·학습하려면 |
| **`pi05`** | π0.5(openpi) 가중치 v8·v9 각 15종 + 가공 LeRobot 데이터셋(`data/v8`) + 깊이 라벨(`data/v9`) + 학습 레시피·실기 결과 문서 | π0.5 를 실행·재학습·비교하려면 |
| **`groot`** | GR00T N1.7 가중치 v8 15종 + GR00T 형식 데이터셋(`data/v8/*_groot`) + 문서 | GR00T 를 실행·재학습하려면 |
| **`rdt`** | RDT-1B 가중치(v6) + 데이터셋 + 정규화 통계·언어 임베딩 등 부속 | RDT 를 실행·재학습하려면 |
| **`result`** | 실물 로봇 회차 기록 — 모델이 실제로 본 입력 프레임 + `bridge.log`/`bringup.log` (v6·v7·v8) | 실기 결과를 검증·재분석하려면 |
| **`all_data`** | 학습 서버(RTX 6000 Ada ×3)·H100 서버·로봇 실행 PC 의 **전체 작업 디렉토리 tar** + 서버·PC 사양 문서 + v8 이전 가중치(`models_pre_v8/`)·실기 기록(`result_pre_v8/`)·초기 데이터 | 환경을 통째로 복원하거나, 위 브랜치에 없는 중간 산출물이 필요하면 |

> `v4` 브랜치는 `LIBERO_training` 의 부분집합이라 삭제했습니다. `LIBERO_training` 은 정리 이전의 통합 브랜치로, 내용이 위 브랜치들에 전부 옮겨졌으며(v8 이전 가중치·실기 기록·서버 스냅샷은 `all_data`, 옛 원본 tar 는 `main` `data/raw/legacy/`) 곧 삭제 예정입니다.

각 브랜치는 **자기 README 만 읽으면 실행까지 가능**하도록 썼습니다 (가중치 경로 · config 이름 ·
데이터 구조 · 학습 조건 · 실기 결과). 코드는 GitHub 저장소에 있습니다 — 학습은 `Train` 브랜치, 데이터 수집은 `VisionPro`, 실물 평가는 `LAB`.

---

## 연구 방법 요약

### 연구 질문

목표를 사다리로 정의합니다.

| 단계 | 내용 | 역할 |
|---|---|---|
| **L1** | 단일 과제 · 깨끗한 장면 (P0~P3 각각, 물체 2개, 1 파지 사이클) | 학습 |
| **L2** | 여러 과제를 **병합 학습** + 다물체 장면에서 단일 지시문 평가 | 학습 + 평가 |
| **L3** | 복합 프롬프트("A 하고 B 도 해라")로 한 에피소드에 2 사이클 연쇄 | **평가 전용 — zero-shot** |

**L1·L2 데이터만 학습한 VLA 가, 본 적 없는 복합 프롬프트(L3)를 수행할 수 있는가.** 복합 시연은
수집하지도 학습하지도 않습니다 — 학습시키면 창발이 아니기 때문입니다.

### 과제 4종 (지시문 문자열은 수집·학습·평가에 이대로 쓰입니다)

```text
P0  Pick up the tomato soup can and place it on the red plate.
P1  Pick up the tomato soup can and place it in the red bowl.
P2  Pick up the Cheez-It box and place it on the red plate.
P3  Pick up the Spam can and place it in the red bowl.
```

물체는 전부 YCB (`005_tomato_soup_can`, `003_cracker_box`, `010_potted_meat_can`, `029_plate`,
`024_bowl`) — 물리 모델이 공개돼 있어 MuJoCo 등 시뮬에서 같은 실험을 재현할 수 있습니다.
P0/P1 은 물체가 같고 목적지만 달라 **언어만이 분기 단서**인 쌍이고, 단독 학습(지시문 1종)은
언어가 죽어 있는 대조군입니다.

### 수집 → 가공 → 학습 → 평가

1. **수집** — Vision Pro (WebXR 손 트래킹) → FastAPI `:8012` (pose · 카메라 4채널 아틀라스 · 20Hz 레코더)
   → 팔 브릿지 `:8013` (게이트 · 캘리브 · pinocchio IK) → 로봇 컨테이너 joint 릴레이 → ros2_control 100Hz.
   왼팔 단독, 오른팔·리프트 고정. 카메라 헤드 좌/우(ZED Mini) + 손목 좌/우(RealSense D405), 640×480.
   판정은 수집자 육안 (성공 + 회복 시연 유지, 최종 실패 드롭).
2. **가공** — 원본 20Hz pkl → **LeRobot 10fps, state 8 / action 8** (왼팔 7 + 왼그리퍼 1).
   물체 좌표·상수축을 넣지 않는 "자기 관절값만" 표준형이라 가중치가 이식 가능합니다.
   action 은 다음 프레임 목표 관절값(절대값) — π0.5·GR00T 모두 팔은 내부적으로 델타로 배우고 출력은 절대 목표 관절값(실행기에서 state 를 더하지 않는다).
3. **학습** — 태스크당 **정확히 100 에피소드**, 전 런 **epoch 2.4 정렬**, 스텝은 변환본 실측 프레임에서
   자동 산출. 조합 15종(단독 4 + 2조합 6 + 3조합 4 + 4조합 1) × π0.5 · GR00T, 그리고 π0.5 는 깊이
   보조 손실(v9)까지 같은 행렬로 한 번 더.
4. **평가** — 실물 회차(10회 단위, 사람 육안 판정) · 결과는 `result` 브랜치. 판정은 세 갈래:
   지시문대로 / **엉뚱한 쪽으로 감**(언어 무시의 직접 증거) / 과제 실패.

### 지금까지의 주요 결과

- **병합 학습이 언어 분기를 만든다** — 학습에 없던 다물체 장면에서 지시문만 바꿔 목적지를 골랐고
  목표 혼동이 단독 3/10 → 병합 1/20 (2026-08-19, 66회차).
- **병목은 지각** — 방해물 하나로 단독 모델 성공률 80% → 30%. 파지 실패 대부분이 "그리퍼를 물체 위에서
  닫으며 누름"(손목캠 거리 오차) → v9(깊이 보조) 설계 근거.
- **4과제 병합(p0123) 단독 평가에서 실패 68% 가 물체 선택 실패**(같은 목적지로 가는 다른 물체를 잡음).
  학습 장면에 대상 물체가 하나뿐이라 이름으로 고르는 법을 배운 적이 없음 — 방해물 포함 재수집이 다음 단계.

---

## 이 브랜치의 데이터 — `data/raw/`

| 폴더 | 지시문 | 장면 | 에피소드 | 수집일 |
|---|---|---|---|---|
| `P0/` | Pick up the tomato soup can and place it on the red plate. | soup + plate | 100 | 2026-08-03 (87) + 08-04 검증분 편입 (13) |
| `P1/` | Pick up the tomato soup can and place it in the red bowl. | soup + bowl | 100 | 2026-08-11 ~ 12 |
| `P2/` | Pick up the Cheez-It box and place it on the red plate. | box + plate | 100 | 2026-08-12 ~ 18 |
| `P3/` | Pick up the Spam can and place it in the red bowl. | Spam + bowl | 100 | 2026-08-18 ~ 21 |

에피소드당 tar 1개 (`F_ffw_sg2_follower_L_fastapi_leader_real_<YYYYMMDD_HHMMSS>_<NNN>.tar`):

```
F_..._<NNN>/
  data_<timestamp>.pkl × N     20Hz 스텝 (관절 위치 · 명령 · 그리퍼 · 메타)
  cam_head_l.mp4  cam_head_r.mp4  cam_wrist_l.mp4  cam_wrist_r.mp4   (640×480)
```

각 폴더의 `episodes.txt` 가 포함 목록, `rejected.txt` 가 제외 에피소드와 사유입니다.
상세 규약: `data/raw/README.md`. LeRobot 변환·병합 스크립트는 GitHub 저장소와 `all_data` 의
서버 tar(`vla_tools/`, `vla_runs/scripts/`)에 있습니다.

## 받는 법

```bash
# git-lfs 필수. 브랜치 하나만, 필요한 폴더만 받는 것을 권장
GIT_LFS_SKIP_SMUDGE=1 git clone -b pi05 --single-branch \
  https://huggingface.co/datasets/ETRI7203/ETRI_VR_Robotics_data_research hf_pi05
cd hf_pi05 && git lfs pull --include="models/v8/pi05_v8_p0123/17899/**"
```

## Citation

```bibtex
@misc{kim2026etrivrvla,
  title        = {ETRI VR Robotics Data Research: Vision Pro Teleoperation Data Collection and
                  Language-Conditioned VLA Training on the ROBOTIS AI Worker FFW-BG2},
  author       = {Kim, Geonhui},
  year         = {2026},
  howpublished = {\url{https://github.com/logan0741/ETRI_VR_Robotics_data_research}},
  note         = {Weights and data: \url{https://huggingface.co/datasets/ETRI7203/ETRI_VR_Robotics_data_research}}
}
```
