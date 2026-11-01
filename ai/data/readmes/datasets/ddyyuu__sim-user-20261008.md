---
tags:
- lerobot
- robotics
- simulation
- imitation-learning
language:
- ko
configs:
- config_name: default
  data_files:
  - split: train
    path: "data/chunk-*/file-*.parquet"
---
# PAC2026 시뮬레이션 시연 데이터

팀 공동 학습을 위한 MuJoCo 조이스틱 시연 데이터의 2026-10-08 스냅샷입니다.
실물 Piper 데이터와는 별도입니다. 공유 범위와 재사용 라이선스는 프로젝트 팀이 정합니다.

- 시연: 259개 / 프레임: 331,753개 / 저장 속도: 30fps
- 형식: LeRobot v3.0 (수집 환경 LeRobot 0.4.4)
- observation.images.wrist: RGB 320×240, PNG 바이트가 Parquet에 포함됩니다.
- observation.state: XYZ(m) + 회전 6D, 총 9차원
- action: dx/dy/dz(m), 월드 기준 회전벡터 증분 drx/dry/drz(rad), 신호 0/1, 총 7차원
- action[t]는 직전 관측에서 현재 관측까지의 EE Delta입니다.
  현재 관측으로 학습할 미래 액션의 첫 타깃은 action[t+1]입니다.
- timestamp는 시뮬레이션의 명목 시간입니다. 실물 카메라 촬영 시간과 혼동하지 마세요.

## 팀원이 다운로드하고 학습하기

먼저 PAC2026 프로젝트와 의존성을 설치해야 합니다. 데이터만으로 프로그램이 설치되지는 않습니다.
아래 `ddyyuu/sim-user-20261008`을 실제 업로드된 저장소 ID로 바꾸세요.
비공개 저장소는 해당 조직 권한과 Hugging Face 로그인이 필요합니다.

```bash
source ~/pac2026/activate.sh
# 비공개 저장소라면 먼저 로그인
hf auth login
hf download ddyyuu/sim-user-20261008 --repo-type dataset \
  --local-dir "$HOME/pac2026/datasets/local/sim-user-20261008"
./pac.sh check sim --repo-id local/sim-user-20261008
./pac.sh bc sim --repo-id local/sim-user-20261008 \
  --out-dir outputs/bc_sim_shared_20261008 --epochs 20 --batch-size 8
```

다운로드 위치에는 같은 이름의 수집 중인 데이터셋을 사용하지 마세요.
기존 학습 출력 폴더가 있으면 새로운 out-dir 이름을 지정하세요.
현재 기본 ACT 학습은 wrist 이미지 한 대와 EE state, seam 특징을 사용하며
시뮬레이션 학습 타깃의 yaw 증분은 마스킹합니다. 원본 데이터의 yaw는 보존됩니다.
검사에서 발견된 짧은 시연은 episode_index=68, 50프레임이며 권장 길이 64보다 짧습니다.
형식·타임스탬프 검사는 실제 시연의 작업 성공 여부를 보증하지 않습니다.
