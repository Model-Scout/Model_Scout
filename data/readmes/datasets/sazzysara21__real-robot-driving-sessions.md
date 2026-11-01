---
license: cc-by-4.0
language:
  - ko
  - en
tags:
  - robotics
  - time-series
  - sensor-data
  - real-robot
  - obstacle-avoidance
  - edge
  - industrial
  - multimodal
  - condition-monitoring
pretty_name: Real-Robot Driving Sessions (20 Hz telemetry)
---

# Real-Robot Driving Sessions: the 18 minutes that trained our 101-parameter driver

Three real driving sessions of our tracked test robot, recorded at 20 Hz on the test floor.

**These are the exact sessions that trained
[NCDTech/real-robot-driving-mlp-numpy](https://huggingface.co/NCDTech/real-robot-driving-mlp-numpy)**, the weight file shown running in
[this video](https://youtu.be/6DJX0T6qrtM).

We can prove the lineage.

Our desktop studio logs every training run, and the entry for that weight file reads:

```
2026-04-24 16:14:25 | build_dataset 시작: 3 파일 —
  session_20260417_165126.bin, session_20260417_154754.bin, session_20260421_142743.bin
```

Those three files are this dataset.

## What one session looks like

![Session overview: ultrasonic distances, motor PWM, and control mode over 320 seconds](assets/01_session_overview.png)

## Files

| session | samples | duration | driving mode mix |
|---------|---------|----------|------------------|
| `session_20260417_154754` | 7,088 | 372.7 s | AUTO 16 % · MANUAL 53 % |
| `session_20260417_165126` | 6,080 | 320.5 s | AUTO 47 % · MANUAL 27 % |
| `session_20260421_142743` | 3,760 | 383.2 s | MANUAL 75 % |
| total | **16,928** | **~18 min** | |

Each session ships in two forms.

`.csv` is the accessible form: 71 columns, one row per 50 ms sample.

`.bin` is the untouched original written by the robot's recorder (parsed with zero dropped chunks and zero truncated bytes).

## Columns (CSV)

| group | columns |
|-------|---------|
| meta | `t_s` (seconds from session start), `sequence`, `ctrl_source` (`IDLE` / `AUTO` / `MANUAL`) |
| ultrasonic | `ultra_{front,left,right,back,grip}_mm` + per-channel `_valid` flags |
| pose | `heading_deg`, `pitch_deg`, `roll_deg`, `pos_x_mm`, `pos_y_mm` (dead-reckoning) |
| motors | `motor_{left,right,arm,grip}_pwm` (-255..255), `current_{left,right,arm,grip}_ma` |
| IMU | `imu0..imu5` × `ax, ay, az, gx, gy, gz` (36 raw int16 channels, 3 MCUs × 2 IMUs) |
| camera | `cam_fps`, `cam_wifi_rssi`, `cam_jpeg_kb` |
| audio | `audio_level_db`, `audio_peak_freq_hz` |
| environment | `env_lux_0..2`, `env_co2_ppm`, `env_temp_c`, `env_humidity_rh` |

The model used only six features from all of this: front/left/right distances plus their frame-to-frame deltas.

Everything else is here because the robot logged it anyway, and multimodal robot telemetry is rare at this size.

Motor currents, 36 IMU channels, and environment sensors at a fixed 20 Hz: this is the same recording discipline we now focus on the predictive maintenance (PdM) of aging mechanical equipment.

## Load it

```python
import pandas as pd

df = pd.read_csv("session_20260417_165126.csv")
auto = df[df.ctrl_source == "AUTO"]
print(len(df), "samples,", len(auto), "in AUTO mode")
```

## Honest notes

Total driving time is about 18 minutes.

That is genuinely small, and it shows in the model: STOP and BACK actions barely occur in these sessions, so the trained network scored 0 % on those classes.

We publish the data anyway, because this is what real early-stage robot data looks like, and because exactly this gap is why our current systems run a class-distribution check inside self QA/QC on every stage.

You can watch that self QA/QC system working, and chatting about its own reports through an on-premise LLM, in [our 22-minute demo video](https://youtu.be/ftsw_vbfw6E).

`pos_x_mm` / `pos_y_mm` are dead-reckoning estimates and drift over time.

IMU channels are raw int16 readings, unscaled.

`ultra_front_mm` comes from the hand-mounted sensor: on this robot the front ultrasonic rides on the hand (per our 2026-03-31 sensor mapping sheet), and `ultra_grip_mm` is a spare channel.

## 한국어

궤도 시험 로봇의 **실주행 세션 3개**(20 Hz, 총 16,928샘플, 약 18분)입니다.

[real-robot-driving-mlp-numpy](https://huggingface.co/NCDTech/real-robot-driving-mlp-numpy) 모델을 학습시킨 **바로 그 파일들**이며, 계보는 학습 당시 앱 로그(위 인용)로 증명됩니다.

각 세션은 원본 `.bin`(기록기 출력 그대로)과 변환 `.csv`(71컬럼: 초음파 5방+IMU 36채널+모터 PWM/전류+자세+카메라+오디오+환경) 두 형태로 제공됩니다.

모터 전류·IMU 36채널·환경 센서를 고정 20 Hz로 기록하는 이 계측 규율을, 지금은 노후 기계식 설비의 예지보전(PdM)에 집중해 쓰고 있습니다.

정직 고지: 총 18분짜리 작은 데이터라 정지/후진 동작이 거의 없고, 그래서 학습된 모델의 해당 클래스 정확도가 0%였습니다.

이런 구멍을 잡으려고 지금의 저희 시스템은 모든 단계에 클래스 분포 검사를 포함한 셀프 QA/QC를 심었습니다.

그 셀프 QA/QC가 실제로 돌아가며 온프레미스 LLM과 대화하는 모습은 [22분 데모 영상](https://youtu.be/ftsw_vbfw6E)에서 볼 수 있습니다.

Learn more: https://huggingface.co/NCDTech · https://ncdtech.org · 주행 영상: https://youtu.be/6DJX0T6qrtM · Self QA/QC demo: https://youtu.be/ftsw_vbfw6E · More robot footage: https://huggingface.co/spaces/NCDTech/robot-lab
