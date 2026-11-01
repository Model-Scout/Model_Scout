---
language:
- en
- ko
tags:
- lerobot
- robotics
- wmx-r2
---
# WMX R2 CR3A — axis_1000hz — LeRobot v3.0

**Public dataset. Downloading does not require authentication.** Created with LeRobot 0.4.4 using its create/save_episode/finalize APIs. Read with the unmodified official LeRobotDataset loader (PyAV video backend on Windows).

59 episodes; 1,018,389 frames; 1000 fps. Robot: Dobot CR3A, six axes; wrist RealSense D455; AG-160-95 gripper. Exact drive/IPC and R2/WMX build identifiers remain pending.

All 1,018,389 original axis rows are retained in order on a nominal 1000 Hz engine-cycle grid. Actual host-clock jitter is preserved in source.axis_host_time_ns. No axis resampling or video is present.

## Load from Hugging Face

The validated environment uses Python 3.12, LeRobot 0.4.4, PyAV 15.1.0, PyTorch 2.10.0 (CPU), and torchvision 0.25.0. See [environment.json](environment.json) and [requirements-lock.txt](requirements-lock.txt) for the complete tested environment. In a separate Python environment, install the loader and video backend:

```bash
python -m pip install "lerobot==0.4.4" "av==15.1.0"
```

The example below downloads only the files needed by LeRobot, avoiding the larger raw archive. It reads data and does not send robot commands. Leave `HF_HUB_OFFLINE` and `HF_DATASETS_OFFLINE` unset for the first download.

```python
from huggingface_hub import snapshot_download
from lerobot.datasets.lerobot_dataset import LeRobotDataset

repo_id = "movensys/wmx-r2-command-grounded-cr3a-axis-v0"
root = snapshot_download(
    repo_id=repo_id,
    repo_type="dataset",
    revision="main",  # Pin a commit ID for reproducible experiments.
    token=False,      # Public download; no login needed.
    local_dir="./datasets/axis",  # Ordinary files; no Windows symlink permission needed.
    allow_patterns=["meta/**", "data/**", "videos/**"],
)
ds = LeRobotDataset(repo_id=repo_id, root=root, video_backend="pyav")
sample = ds[0]
print(ds.num_episodes, len(ds), ds.fps)
print(sample["action"].shape)             # torch.Size([12])
print(sample["observation.state"].shape)  # torch.Size([12])
```

After the files are downloaded, reuse the returned `root` for local loading. For strictly offline loading, omit `snapshot_download` and set `HF_HUB_OFFLINE=1` and `HF_DATASETS_OFFLINE=1` before importing the libraries.

## Repository layout and paired dataset

- `meta/`: LeRobot v3 info, statistics, task and episode metadata.
- `data/`: numeric Parquet shards.
- `annotations/episode_mapping.json` and `annotations/episodes.jsonl`: original run IDs, labels and outcome evidence.
- [conversion_policy.json](conversion_policy.json), [loading_validation.json](loading_validation.json), [environment.json](environment.json), and [requirements-lock.txt](requirements-lock.txt): conversion and validation records.

Both derivatives represent the same fixed 59 recorded runs. The [1000 Hz axis dataset](https://huggingface.co/datasets/movensys/wmx-r2-command-grounded-cr3a-axis-v0) preserves every axis row for motion analysis; the [30 fps camera dataset](https://huggingface.co/datasets/movensys/wmx-r2-command-grounded-cr3a-camera-v0) provides wrist RGB and nearest-time axis state for vision-based learning. They are not separate train/test sets.

The original CSV/AVI data, label package, loading and plotting examples are stored once in [the axis repository's raw/source_package](https://huggingface.co/datasets/movensys/wmx-r2-command-grounded-cr3a-axis-v0/tree/main/raw/source_package). This repository includes that raw archive. Raw-package paths in copied labels resolve relative to that package; context-only archive paths remain provenance identifiers and may not correspond to uploaded files. Locate converted data/video shards through `meta/info.json` and episode metadata. Do not move shards independently of their metadata.

## Validation
All numeric rows were compared against selected source rows. First/middle/last samples of every episode were read through LeRobotDataset; a PyTorch DataLoader batch was also checked. Camera MP4s were fully decoded and counts checked; sampled decoded images were compared with selected original AVI frames. See [loading_validation.json](loading_validation.json) for scope and measured results. The conversion fast path skips embed_images only for image-free numeric Arrow features; loader/library files were not modified.

## Semantics and limits

| Feature | Meaning | Loaded shape / units |
|---|---|---|
| `action` | Engine command positions for joints j0–j5, followed by command velocities j0–j5 | `(12,)`; configured rad, rad/s |
| `observation.state` | Controller-reported feedback positions j0–j5, followed by feedback velocities j0–j5; not estimated from images | `(12,)`; configured rad, rad/s |
| `observation.tracking_error` | Command position minus feedback position for j0–j5 | `(6,)`; configured rad |

`action` = 6 engine command positions [configured rad], then 6 engine command velocities [configured rad/s]. `observation.state` = 6 feedback positions then 6 feedback velocities. `observation.tracking_error` = command minus feedback position, computed before float32 conversion. These action features describe engine setpoints; they are not a complete robot policy command interface. No live robot commands are provided.

`source.*` features are integer provenance and quality metadata, not recommended policy inputs. Axis host ns is original SYSTEM_TIME × 100. Neither this field nor the LeRobot regular-grid `timestamp` is verified EtherCAT DC. Sensor exposure, ROS camera header, reception and axis clocks have not been calibrated; nearest-time offsets are not physical synchronization accuracy.

Invalid/unverified FBTRQ is excluded. Acceleration, measured cycle-level I/O, gripper position/force, depth and engine overruns are absent. Gripper service commands remain in annotations/events, not inferred physical feedback. Numeric model features are float32; original float64 data remains in the source package. Absolute source clocks and row/cycle indices remain int64.

One dataset episode corresponds to one recorded run, not necessarily a full successful task. Frame index and timestamp restart per episode. Original IDs, phase, task group and outcome evidence are in annotations/episode_mapping.json and annotations/episodes.jsonl. T007 is partial (orientation not satisfied); T008's later correction is contextual and not silently incorporated into fixed59. Controller success, user confirmation, image estimates and unreviewed outcomes remain distinct. Preflight footage and gaps between separate runs must not be described as continuous task recording.

No held-out train/test split is supplied; LeRobot's default train=0:59 is a storage view of all episodes, not an independent evaluation split. Use the original session split_group to prevent leakage. This is a small correlated demonstration dataset. Do not infer evaluation generalization or reliable force/pose ground truth.

## Public availability and license

This repository is publicly accessible. Public availability does not itself grant an open-source or open-data license. No explicit reuse license has been assigned; licensing remains pending the dataset owner's decision. Contact Movensys for reuse terms.

Historical preparation records (including `LICENSE_PENDING.txt`, `conversion_policy.json`, and files in the original raw package) may still describe the earlier pre-publication or restricted-review stage. They are preserved as provenance; this README describes the current public availability. Original data and labels have not been changed by this documentation update.
