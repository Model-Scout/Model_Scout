---
language:
- en
- ko
tags:
- robotics
- imitation-learning
- action-chunking-transformer
- robotwin
- simulation
- point-cloud
size_categories:
- n<1K
configs:
- config_name: default
  data_files:
  - split: train
    path: train.parquet
  - split: validation
    path: val.parquet
  - split: test
    path: test.parquet
---

## Browser video previews

The Dataset Viewer default configuration lists565 stored-Expert sensor preview videos
(Train295 / Validation145 / Test125). The video column is playable in the browser once
the Hub viewer finishes processing. Each MP4 shows head depth (fixed0–1.5m color scale),
left wrist RGB and right wrist RGB, synchronized from original stored frames at10Hz.
These are demonstrations used for training/evaluation splits, NOT ACT closed-loop inference videos.
They are a viewing derivative; original numeric observations/actions remain in HDF5.
Click the video row's hdf5_path to identify the corresponding source file under Files.
Raw565 HDF5 upload completion is tracked by uploaded_checksums.json; video availability
does not imply the raw HDF5 upload is finished.

Example [stored train episode grid00 video](https://huggingface.co/datasets/Chunsam0916/sweepick-robotwin/resolve/main/previews/train/episode_grid00_a0000.mp4).

# SWEEPICK RoboTwin paired appearance dataset

565 successful simulated Expert episode views from 113 distinct motion trajectories.
Each family contains one original raytraced view and four additional appearance variants.
These are 113 motion trajectories, not 565 independent motions.

| Split | Trajectory families | Episode views |
|---|---:|---:|
| Train | 59 | 295 |
| Validation | 29 | 145 |
| Test | 25 | 125 |

All appearance variants of a trajectory stay in the same split. Fit normalization on Train only.
Val/Test must not be used for gradient updates; reserve Test for independent final evaluation.
143 spatial points were attempted: 80 Train, 32 Val, 31 Test. Only successful Expert trajectories
were retained here: 59/29/25. Failed locations are not episode files in this dataset.
The immutable spatial split definitions are in `spatial_splits.json` when present.

## Task and capture
SWEEPICK dual SO101 P-gripper on TurtleBot; 40x40x40mm cube, fixed yaw.
Home → Pregrasp → Grasp → Lift (at least30mm) → measured Stow → Hold2simulation seconds.
No mobile carrying drive. Physics250Hz, policy observations10Hz. Simulation uses raytraced wrist RGB.
Head is depth/IR only: depth and derived PointCloud, no head RGB policy input.
XYZ is in TurtleBot `base_footprint`, meters, X forward / Y left / Z up.

New paired variants use native RoboTwin table/wall textures and lighting with stratified HSV cube colors.
Train uses the seen texture pool; Val/Test use unseen textures. Geometry, object yaw/size/physics,
head calibration and motion trajectories remain fixed. Variants rerender at the same physics tick;
head depth/PointCloud geometry is reused. These are simulated observations, not real robot recordings.

## HDF5 schema
- `timestamp`: observation simulation time seconds.
- `state/{left_arm_joint_states,left_ee_joint_states,right_arm_joint_states,right_ee_joint_states}`:
  observed joint positions, radians, 5+1+5+1 dimensions.
- `action/` with matching names: absolute commanded joint positions, radians; not deltas.
- `vision/head_depth_m`, `vision/head_depth_valid`: metric depth and validity mask.
- `vision/pointcloud/{frame:06}`: variable-length XYZ points in base frame.
- `vision/cam_left_wrist/colors`, `vision/cam_right_wrist/colors`: JPEG byte arrays, RGB decoded240x320.
- `gripper/requested_robotwin_normalized`: RoboTwin normalized gripper request, separate from motor radians.
- `phase`, `control/phase`: Expert annotations, for analysis/labels; not policy observations.
- `control/{timestamp,q,action,gripper_requested}`: full physics-rate control trace.
- `block_world_xyz`: ground-truth object pose annotation for diagnostics/success, NOT policy input.
- `paired/`: additional pairing diagnostics on appearance variants when present.
- root attributes include metadata, success/metrics, split, fixed seeds and provenance fingerprints.

Joint order: left shoulder_pan, shoulder_lift, elbow_flex, wrist_flex, wrist_roll, gripper motor;
then the same six for the right arm. Gripper motor radians require a separate actual-driver conversion;
RoboTwin close request0.0 is not a real servo tick command.

## Public export
Source total is approximately86.2GiB. HDF5 numerical and image datasets are retained.
Embedded private `headcal` calibration metadata and absolute local filesystem paths are removed/replaced
in public copies. Calibration hashes remain for provenance. Source files are not modified.
Use `dataset_manifest.json` for filenames/splits and `uploaded_checksums.json` after full upload for
original source SHA256 and exported file SHA256. Export hashes differ because metadata was sanitized.
The upload is incomplete until every565episode file and `uploaded_checksums.json` are present.
No calibration source archive, local private head_profile.json, credentials, checkpoints or URDF assets are included.

## Usage
```python
from huggingface_hub import hf_hub_download
import h5py
path = hf_hub_download('Chunsam0916/sweepick-robotwin',
    'data/train/episode_grid00_a0000.hdf5', repo_type='dataset')
with h5py.File(path, 'r') as f:
    print(f['timestamp'].shape, list(f['vision']))
```
Files are custom episodic HDF5; load with h5py. No Parquet conversion is implied.
Repository browser availability does not imply the automatic tabular Dataset Viewer can render these HDF5 payloads.

Simulation success does not establish hardware safety or real-world success. Collision proxies and sim-to-real
sensor/actuator differences remain unvalidated. Ground-truth annotations must not leak into policy inputs.

Upstream simulation project: https://github.com/jtjin0916/RoboTwin
No additional reuse license is declared in this initial card; maintainers must specify dataset and asset reuse terms.
