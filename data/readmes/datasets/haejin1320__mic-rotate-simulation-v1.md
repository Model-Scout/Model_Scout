---
license: cc-by-4.0
task_categories:
- audio-to-audio
language:
- ko
tags:
- microphone
- rotation
- spatial-audio
- room-impulse-response
- stereo
pretty_name: MicRotate Simulation Dataset
size_categories:
- 1K<n<10K
---

# MicRotate Simulation Dataset

Android 스마트폰 마이크 회전(0° Portrait → 90° Landscape)에 따른
스테레오 오디오 변환 AI 모델 학습용 시뮬레이션 데이터셋.

## Dataset Description

- **Source**: pyroomacoustics 3D Room Impulse Response 시뮬레이션
- **Phone model**: 78.1mm × 163.6mm (Samsung Galaxy S-class 기준)
- **Mic positions**: MIC_TOP [-10mm, +71.8mm], MIC_BOT [-5mm, -71.8mm] (폰 중심 기준)
- **Rotation**: Portrait (0°) → Landscape CW (90°)
- **Sample rate**: 48 kHz
- **Bit depth**: 32-bit float
- **Channels**: Stereo (ch0=MIC_TOP, ch1=MIC_BOT)

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| `pair_id` | int | 페어 고유 ID |
| `source_type` | str | speech / sine_sweep / white_noise / pink_noise / environmental |
| `audio_0deg_ch0` | Audio | Portrait 0° MIC_TOP (48kHz) |
| `audio_0deg_ch1` | Audio | Portrait 0° MIC_BOT (48kHz) |
| `audio_90deg_ch0` | Audio | Landscape 90° MIC_TOP (48kHz) |
| `audio_90deg_ch1` | Audio | Landscape 90° MIC_BOT (48kHz) |
| `room_id` | str | 룸 ID (small_dead, medium_office 등) |
| `rt60` | float | 잔향 시간 (초) |
| `rotation_direction` | str | 회전 방향 (cw=시계방향) |

## Source Type Distribution

| Type | Count (train) | Notes |
|------|---------------|-------|
| speech | 1800 | VCTK 48kHz / LibriSpeech 16→48kHz |
| sine_sweep | 450 | Log sweep 20Hz–20kHz |
| white_noise | 450 | White Gaussian Noise |
| pink_noise | 450 | FFT 기반 1/f |
| environmental | 450 | FSD50K CC-BY / pink noise fallback |

## Room Environments

| Room | Dims (m) | RT60 (s) |
|------|-----------|----------|
| small_dead | 4×3.5×2.7 | 0.15 |
| small_live | 4×3.5×2.7 | 0.35 |
| medium_office | 7×5.5×3 | 0.50 |
| medium_living | 6×5×2.8 | 0.45 |
| large_hall | 15×10×4 | 1.20 |
| anechoic | 8×6×3 | 0.01 |

## Licenses

- Speech data (VCTK): CC BY 4.0
- Environmental (FSD50K): CC BY 4.0
- Simulation code: MIT
