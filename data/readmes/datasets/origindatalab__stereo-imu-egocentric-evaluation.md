---
license: cc-by-nc-4.0
pretty_name: "Stereo + IMU Egocentric Capture — Technical Evaluation (Field Note #03)"
language:
- en
- ko
tags:
- robotics
- physical-ai
- egocentric
- stereo-vision
- imu
- multimodal
- sensor-fusion
- data-quality
- technical-evaluation
- real-world-data
task_categories:
- other
size_categories:
- n<1K
---

<div align="center">

# Stereo + IMU Egocentric Capture
### Technical Evaluation · Field Note #03

**ORIGIN DATA LAB** · Real-World Data Production for Physical AI

![Physical AI](https://img.shields.io/badge/Physical_AI-Real--World_Data-172554?style=for-the-badge)
![Stereo](https://img.shields.io/badge/Stereo-1600%C3%971200-2563eb?style=for-the-badge)
![IMU](https://img.shields.io/badge/6--Axis_IMU-%E2%89%88502_Hz-0f766e?style=for-the-badge)
![Evaluation](https://img.shields.io/badge/Status-Technical_Evaluation-f59e0b?style=for-the-badge)

**[English Field Note](https://origindatalab.io/technical-field-notes/stereo-imu-egocentric-sample.html)** · **[한국어 기술노트](https://origindatalab.io/ko/technical-field-notes/stereo-imu-egocentric-sample.html)** · **[GitHub evidence repository](https://github.com/origin-data-lab/stereo-imu-egocentric-evaluation)**

</div>

> **Short answer.** In a 120 s head-mounted stereo + IMU recording, all **3,600 / 3,600** stereo pairs shared the device frame tick, the device-recorded left/right exposure-centre offset had a median of **20.5 µs**, and the IMU delivered **≈501.7 Hz with no gaps** on the same clock as the video. Under auto-exposure, using the frame tick instead of the **exposure centre** biases frame time by about **5 ms**.

> **Publication scope:** technical evaluation, measurement figures and documentation only. The underlying raw stereo videos and IMU time series are not distributed here, and this is not a production calibration certificate or a robot-learning benchmark.

## At a glance

| Evaluated recording | Stereo streams | IMU | Frame coverage |
|:--|:--|:--|:--|
| **120 seconds** | **2 × 1600 × 1200 @ 30 fps** | **6-axis · ~501.7 Hz** | **3,600 frames per camera** |

A head-mounted stereo egocentric recording of an indoor two-handed workbench assembly task was evaluated for frame correspondence, timing, sensor continuity, image quality and calibration evidence. Measurements and limitations are presented separately to avoid conflating **recorded evidence**, **estimates** and **unverified claims**.

## Evaluation summary

| Metric / claim | Observation | Evidence status |
|:--|:--|:--|
| Stereo frame tick correspondence | 3,600 / 3,600 matched pairs | **Verified in evaluated record** |
| Frame counter continuity | No missing increments observed | **Verified in evaluated record** |
| Visual motion alignment | Peak at zero-frame lag; r = 0.997 | **Evaluated** |
| Left/right exposure-center difference | Median 20.5 µs; mean 21.1 ± 2.9 µs | **Device-reported; not independently verified** |
| IMU sample rate | Approximately 501.7 Hz | **Verified in evaluated record** |
| IMU continuity | No observed gaps, duplicates or saturation in tested range | **Verified in evaluated record** |
| Camera–IMU timing offsets | Left −1.1 ms; right −1.2 ms | **Estimate — consistent within a few ms only** |
| Stereo calibration for evaluated capture mode | Mode-matched Kalibr calibration: median angular epipolar error 0.41 px | **Verified (update, see [Field Note #04](https://origindatalab.io/technical-field-notes/stereo-calibration-check.html))** |
| Camera–IMU extrinsics | Kalibr values exist; not verifiable from this recording | **Calibrated, not independently verified** |
| Robot-learning performance | Not tested | **Not assessed** |

> **Update, 23 October 2026.** A Kalibr calibration produced in the same 1600 × 1200 mode was validated on this recording without adjustment ([Field Note #04](https://origindatalab.io/technical-field-notes/stereo-calibration-check.html) · [dataset card](https://huggingface.co/datasets/origindatalab/stereo-calibration-validation)). The same target-free video–gyro method, applied to a recording with a Kalibr camera–IMU reference, missed the reference time shift by several milliseconds — so the −1.1 / −1.2 ms figures indicate alignment within a few milliseconds, not a measured offset.

## Visual evidence gallery

### 01 · Stereo imagery and exposure timing

![Stereo frame pair](figures/stereo-pair-frame-1500.webp)

*Representative stereo image pair from the evaluated recording. Monitor screens are blurred for public release.*

![Stereo exposure timing](figures/stereo-exposure-timing.webp)

*Timing analysis based on recorded camera metadata. Exposure-center differences are device-reported rather than externally certified.*

### 02 · IMU signal quality and sampling

![IMU raw signals](figures/imu-raw-signals.webp)

![IMU interval and head rate](figures/imu-interval-head-rate.webp)

*Inertial signals and sampling interval diagnostics for the evaluated segment.*

### 03 · Visual–inertial temporal relationship

![Visual rotation vs gyroscope](figures/visual-rotation-vs-gyro.webp)

![Camera IMU offset windows](figures/camera-imu-offset-windows.webp)

*Visual motion and gyroscope comparison. Camera–IMU offsets are diagnostic estimates, not certified hardware synchronization.*

### 04 · Stereo rectification with the originally supplied (mode-mismatched) file

![Rectification residual map](figures/rectification-residual-map.webp)

![Rectification residual summary](figures/rectification-residual-summary.webp)

*These residuals come from a calibration file produced in a different (16:9) mode. A mode-matched calibration has since been validated at 0.41 px (Field Note #04).*

### 05 · Frame-level image quality

![Image quality per frame](figures/image-quality-per-frame.webp)

*Image-quality variation across the evaluated recording.*

## What is verified — and what is not

**Supported by the evaluated record:** video decoding, frame continuity, recorded stereo tick pairing, IMU continuity, diagnostic motion comparison and (since 23 Oct 2026) mode-matched stereo calibration fit.

**Requires additional validation:** independent optical stereo timing confirmation, metric depth accuracy, and independent camera–IMU extrinsic and time-offset verification. **No downstream VLA/robot policy training performance is claimed.**

See [VALIDATION_STATUS.md](VALIDATION_STATUS.md) for the full evidence matrix and [TECHNICAL_REPORT.md](TECHNICAL_REPORT.md) for methods, interpretation and limitations.

## Repository contents

| Path | Description |
|:--|:--|
| `README.md` | Dataset card, measurement summary and evidence gallery |
| `TECHNICAL_REPORT.md` | Technical evaluation methodology and findings |
| `VALIDATION_STATUS.md` | Claim-by-claim validation boundaries |
| `figures/*.webp` | Nine diagnostic figures from the published evaluation |

**Not included:** source MP4 recordings, raw IMU logs, full per-frame sensor metadata, calibration parameters, training-ready annotations or dataset splits. The Dataset Viewer may not show sample rows because this is a documentation-only technical evidence release.

## Cite

```bibtex
@misc{origindatalab2026fieldnote03,
  author       = {{Origin Data Lab}},
  title        = {Stereo + IMU Egocentric Capture: Measured Synchronization, Timing Model and Calibration Findings},
  howpublished = {Technical Field Note \#03},
  year         = {2026},
  url          = {https://origindatalab.io/technical-field-notes/stereo-imu-egocentric-sample.html}
}
```

## Custom data production and evaluation pilots

Origin Data Lab supports scoped real-world data collection for robotics and Physical AI, including egocentric/stereo video, inertial metadata, field operations, quality review and engineering-oriented deliverables. Production specifications and acceptance criteria are agreed per project.

**[Request a technical evaluation or paid pilot](https://origindatalab.io/contact.html)** · **contact@origindatalab.io**

---

<sub>Origin Data Lab · October 2026 · Text and figures: CC BY-NC 4.0 — attribution to Origin Data Lab.</sub>
