---
license: cc-by-nc-4.0
task_categories:
  - robotics
tags:
  - LeRobot
  - egocentric
  - hand-pose
  - depth
  - gopro
language:
  - en
  - ko
size_categories:
  - n<1K
configs:
  - config_name: default
    data_files: data/*/*.parquet
---

# pick-and-place-gopro-v1 (LeRobot v2.1)

Egocentric head-mounted camera dataset from the **Pick and place** domain.

> ⚠ **License — sample dataset is for non-commercial use only (CC-BY-NC-4.0).**
> For commercial licensing, please contact us → **business@zen-o.xyz**.

## About ZenO

ZenO Labs builds an egocentric data pipeline for training **Physical AI**
and robot learning policies.  Head-mounted GoPro / smartphone footage is
processed into LeRobot v2.1 datasets with multiple modalities aligned
frame-by-frame:

- 6-DoF head trajectory (visual-inertial SLAM)
- Hand pose — 21 keypoints × 2 hands, with temporal post-processing
- Depth — per-pixel depth maps as video
- Action segments (where annotated)

**This release is a free sample** — a small preview of what we collect.
For larger / customized datasets we offer:

- Longer recordings + more episodes per domain (cooking, assembly,
  laundry, dishwashing, bartending, …)
- Custom task scenarios on demand
- Higher framerate (60 fps), 4K source, synchronized multi-camera
- Stricter QA + curation tier

Contact us for pricing and data scoping:
**business@zen-o.xyz** · **support@zen-o.xyz** · Telegram **@zenoglasses**

## Dataset description

- Source: GoPro head-mounted camera (egocentric POV)
- Domain: `Pick and place`
- Coordinate frame: ROS REP 103 (X=forward, Y=left, Z=up)
- Format: LeRobot v2.1 — parquet (per-episode) + meta JSON + mp4 videos

## Quick use

```python
from lerobot.common.datasets.lerobot_dataset import LeRobotDataset
ds = LeRobotDataset("zeno-labs/pick-and-place-gopro-v1")
# Or after local download:
# ds = LeRobotDataset.from_root("./pick-and-place-gopro-v1")
```

## Modalities

- **head trajectory** (6-DoF, x,y,z + quaternion)
- **hand pose** (21 keypoints × 2 hands)
- **depth** (per-pixel depth map video)

## Hand pose — how to access

Each frame stores 21 MediaPipe keypoints **per hand** in two separate parquet
columns.  These are not embedded in the videos — they are numeric data.

| Column | Shape | Meaning |
|---|---|---|
| `observation.hand_pose.left`  | `[21, 3]` (float32) | 21 keypoints, [x_pixel, y_pixel, z_relative] |
| `observation.hand_pose.right` | `[21, 3]` (float32) | same, right hand |

- `x_pixel`, `y_pixel`: pixel coordinates in the **source video resolution**
  (e.g. 1920×1080 for GoPro Hero 9 wide).  Already aligned to
  `observation.images.head` frame.
- `z_relative`: MediaPipe's relative depth (~ −1..+1, **not metric**).  Smaller
  = closer to camera.  Use `observation.images.depth` if you need metric depth.
- **Missing detection** → all 63 values are `0.0` (not NaN).  Detect with
  `np.allclose(kp, 0)` per frame.

Keypoint order follows the standard
[MediaPipe Hands topology](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker)
(0=wrist, 4=thumb tip, 8=index tip, 12=middle tip, 16=ring tip, 20=pinky tip).

### Quick visualize (per-frame overlay)

```python
import cv2, numpy as np, pyarrow.parquet as pq

t = pq.read_table(
    "https://huggingface.co/datasets/zeno-labs/pick-and-place-gopro-v1/resolve/main/data/chunk-000/episode_000000.parquet"
)
df = t.to_pandas()

# pick a frame
i = 100
left  = np.asarray(df["observation.hand_pose.left"].iloc[i],  dtype=np.float32)  # (21, 3)
right = np.asarray(df["observation.hand_pose.right"].iloc[i], dtype=np.float32)

img = cv2.imread("frame_100.png")  # extract the same frame from the head video
for kp_set, color in [(left, (0, 255, 0)), (right, (0, 0, 255))]:
    if np.allclose(kp_set, 0): continue
    for x, y, _z in kp_set:
        cv2.circle(img, (int(x), int(y)), 4, color, -1)
cv2.imwrite("overlay.png", img)
```

### Quick load (LeRobot)

```python
ds = LeRobotDataset("zeno-labs/pick-and-place-gopro-v1")
sample = ds[0]
left  = sample["observation.hand_pose.left"]   # tensor [21, 3]
right = sample["observation.hand_pose.right"]
```

## Stats

| Metric | Value |
|---|---|
| Episodes | 1 |
| Frames | 7,915 |
| Total duration (~) | 4.4 min |
| Videos | 2 |

## Schema (`meta/info.json`)

```json
{
  "codebase_version": "v2.1",
  "robot_type": "egocentric_head_camera",
  "total_episodes": 1,
  "total_frames": 7915,
  "total_tasks": 1,
  "total_videos": 2,
  "total_chunks": 1,
  "chunks_size": 1000,
  "fps": 30,
  "splits": {
    "train": "0:1"
  },
  "data_path": "data/chunk-{episode_chunk:03d}/episode_{episode_index:06d}.parquet",
  "video_path": "videos/chunk-{episode_chunk:03d}/{video_key}/episode_{episode_index:06d}.mp4",
  "features": {
    "observation.state": {
      "dtype": "float32",
      "shape": [
        7
      ],
      "names": [
        "x",
        "y",
        "z",
        "qx",
        "qy",
        "qz",
        "qw"
      ]
    },
    "timestamp": {
      "dtype": "float32",
      "shape": [
        1
      ],
      "names": null
    },
    "frame_index": {
      "dtype": "int64",
      "shape": [
        1
      ],
      "names": null
    },
    "episode_index": {
      "dtype": "int64",
      "shape": [
        1
      ],
      "names": null
    },
    "index": {
      "dtype": "int64",
      "shape": [
        1
      ],
      "names": null
    },
    "task_index": {
      "dtype": "int64",
      "shape": [
        1
      ],
      "names": null
    },
    "observation.images.head": {
      "dtype": "video",
      "shape": [
        720,
        1280,
        3
      ],
      "names": [
        "height",
        "width",
        "channel"
      ],
      "info": {
        "video.fps": 30.0,
        "video.height": 720,
        "video.width": 1280,
        "video.channels": 3,
        "video.codec": "h264",
        "video.pix_fmt": "yuv420p",
        "video.is_depth_map": false,
        "has_audio": false
      }
    },
    "observation.hand_pose.left": {
      "dtype": "float32",
      "shape": [
        21,
        3
      ],
      "names": [
        "keypoint",
        "xyz"
      ]
    },
    "observation.hand_pose.right": {
      "dtype": "float32",
      "shape": [
        21,
        3
      ],
      "names": [
        "keypoint",
        "xyz"
      ]
    },
    "observation.images.depth": {
      "dtype": "video",
      "shape": [
        540,
        1920,
        3
      ],
      "names": [
        "height",
        "width",
        "channel"
      ],
      "info": {
        "video.fps": 30.0,
        "video.height": 540,
        "video.width": 1920,
        "video.channels": 3,
        "video.codec": "h264",
        "video.pix_fmt": "yuv420p",
        "video.is_depth_map": true,
        "has_audio": false
      }
    }
  }
}
```

## Interactive trajectory viewer

Each episode has an interactive 3D path viewer (head pose + original video + QA metrics).  Click a link below — opens directly in your browser.

| Episode | Task | View |
|---------|------|------|
| 000000 | aucro donut | [view trajectory](https://zeno-studio-stg.up.railway.app/trajectory/331d0b8b-31bf-4944-937f-66ef67dec698?code=W7WHH3K4) |

> ⚠ Access codes are embedded in these links and may be rotated **without prior notice**.  If a link returns an error, the code has been refreshed — please contact ZenO Labs for new codes.

## Limitations

- Hand pose detection rate varies per video (sideways / occluded hands have lower recall).
- Body keypoints are not included — hands only.
- Coordinate frame is ROS REP 103 (X=forward, Y=left, Z=up); remap if your stack uses a different convention.
- Episodes may be re-published; pin to a specific commit SHA for strict reproducibility.

## Reproducibility

This dataset may be updated with new commits.  To pin a specific snapshot,
reference an explicit HF revision (commit SHA):

```python
ds = LeRobotDataset("zeno-labs/pick-and-place-gopro-v1", revision="<commit-sha>")
```

## Contact

- General support: **support@zen-o.xyz**
- Business / commercial license: **business@zen-o.xyz**
- Telegram: **@zenoglasses**

## Citation

If you use this dataset in academic work, please cite:

```bibtex
@misc{zeno-pick-and-place-gopro-v1,
  title={ZenO Egocentric Dataset — Pick and place (gopro, v1, LeRobot v2.1)},
  author={ZenO Labs},
  year={2026},
  publisher={Hugging Face Datasets},
  howpublished={\url{https://huggingface.co/datasets/zeno-labs/pick-and-place-gopro-v1}}
}
```

---

Generated by ZenO Studio.
