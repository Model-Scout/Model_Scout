---
license: other
license_name: 3d-front-terms-of-use
license_link: LICENSE
pretty_name: 3D-FRONT Indoor Renders
task_categories:
  - image-segmentation
  - depth-estimation
  - object-detection
language:
  - en
  - ko
size_categories:
  - 10K<n<100K
extra_gated_prompt: >-
  This dataset is derived from 3D-FRONT / 3D-FUTURE (Alibaba / Tao Bao) and may
  be used for scientific research purposes only. By requesting access you agree
  to the original 3D-FRONT Data Sets Use License Agreement (included as
  3D-FRONT-ToU.pdf) and accept that you will pass the same terms on to anyone
  you share this data with.
extra_gated_fields:
  Name: text
  Affiliation: text
  Intended research use: text
  I agree to the original 3D-FRONT terms and will not use this for commercial purposes: checkbox
---

# Indoor Scene Renders from 3D-FRONT / 3D-FUTURE

20,240 photo-realistic indoor scene renders with instance segmentation, 6DoF
object poses, camera intrinsics and depth — rendered from the 3D-FRONT scene
layouts and 3D-FUTURE furniture models.

**This is not a copy of the original 3D-FUTURE render set.** It is a separate
render set built from the same assets. See *Differences from the original* below.

## Why this exists

The 3D-FUTURE technical report describes 20,240 rendered indoor images, but
**those images were never part of any public release** — the mirrors that carry
3D-FRONT and 3D-FUTURE contain scenes, furniture and textures only. The official
Tianchi distribution pages now return 404 and the listed contact address does not
answer, so the images cannot be obtained from the source either.

This repository provides a render set of the same size, produced with a
documented and reproducible pipeline.

## What is in here

| Folder | Contents |
| --- | --- |
| `renders/` | 20,240 rooms in 102 WebDataset tar shards (~148 MB each, 15.1 GB total), plus `shard_index.json` and `SHA256SUMS`. |
| `defects/` | `3d-front-defects.json` — defects we found in the original data, as identifiers and measurements. |
| `code/` | The full pipeline: selection, rendering, verification, repair, packing. |
| `docs/` | The original terms of use, our Korean translation, and the working plan. |

### Reading the shards

Each room contributes four members sharing one key, so any WebDataset-style
loader groups them automatically:

```
<scene_id>_<room_id>.rgb.png
<scene_id>_<room_id>.depth.png
<scene_id>_<room_id>.instance.png
<scene_id>_<room_id>.json
```

```python
import webdataset as wds

dataset = wds.WebDataset("renders/renders-{000..101}.tar").decode()
for sample in dataset:
    rgb = sample["rgb.png"]
    depth = sample["depth.png"]        # 16-bit, millimetres
    instance = sample["instance.png"]  # pixel value = placement_index + 1
    meta = sample["json"]
```

Plain `tarfile` works too. `shard_index.json` maps every room name to the shard
holding it, under the key `room_to_shard`, so a single room can be pulled
without downloading everything. `SHA256SUMS` covers all 102 shards — verify
with `sha256sum -c SHA256SUMS`. Shards are built deterministically: member
order is sorted and timestamps are fixed, so repacking the same renders
reproduces the same bytes.

### Per-room files

| Member | Meaning |
| --- | --- |
| `<key>.rgb.png` | 1024 × 768 colour image |
| `<key>.depth.png` | 16-bit depth. Millimetres. `0` means background or beyond 20 m. |
| `<key>.instance.png` | Instance segmentation. Pixel value = `placement_index + 1`; `0` is background. |
| `<key>.json` | Resolution, camera intrinsics, field of view, camera pose (4×4), and per-object 6DoF pose, scale and bounding box. |

**Coordinate systems differ by field, and the file says so in its own
`coordinate_note`.** Object positions and rotations are in the original y-up
frame, with quaternions in scalar-last `[x, y, z, w]` order. Bounding boxes and
`camera_to_world` are in Blender's z-up frame.

## What this is not

**We do not redistribute 3D-FRONT or 3D-FUTURE.** To reproduce the renders you
need to obtain those datasets yourself and accept their terms. This repository
carries only what we made: the images, our annotations, our defect measurements
and our code.

## Differences from the original render set

The 3D-FUTURE paper's images and ours are not interchangeable.

| | Original | Ours |
| --- | --- | --- |
| Images | 20,240 | 20,240 |
| How the count is filled | 20,240 designs built on 5,000 designer rooms, one image each | 20,240 different rooms, one image each |
| Camera | Chosen by professional designers | Chosen automatically, with clearance and framing constraints |
| Renderer | V-Ray 6 | Blender Cycles (BlenderProc 2.8.0) |
| Resolution | Not published | 1024 × 768 (our choice) |
| Field of view | Provided per image, value not published | 60° horizontal (our choice) |
| Instances per image | 5.1 | 5.4 |

Because the renderer and the camera policy differ, **these images are not a
substitute for the originals in any pixel-level comparison**, and results
measured on them should not be placed side by side with numbers from the
original set without saying so.

## Defects we found in the original data

Published as `defects/3d-front-defects.json` so anyone can apply the same quality
filtering to data they obtain themselves.

| Defect | What goes wrong |
| --- | --- |
| Furniture meshes authored in centimetres | The model enters the scene at 100–153× its declared size. One children's bed measured 220 m × 122 m × 186 m. Scale values look normal, so filtering on scale does not catch it. |
| Truncated or missing textures | Three files are truncated — 76–99% of the file is empty, so the object renders almost black, and the file still opens without error. One is missing outright. |
| `NaN` placement coordinates | Standard JSON has no `NaN`, so annotations carrying it fail to parse in some languages. |

The manifest also lists placements whose rotation is not a pure yaw, and rooms
that ATISS-style preprocessing discards because of out-of-range scale values.

## Reproducing

Each step feeds the next, so the order matters.

```bash
python verify_recovery.py 3D-FRONT-raw            # archive integrity
python prepare_dataset.py 3D-FRONT-raw 3D-FRONT-data
python select_rooms.py 3D-FRONT-data --target 20240  --out render_rooms.json
python select_rooms.py 3D-FRONT-data --target 999999 --out all_candidates.json
python census_broken_textures.py                  # must run before rendering
bash run_render_batches.sh 100
python fill_missing_rooms.py --apply              # then re-run the render step
python repair_renders.py --delete                 # then re-run the render step
python pack_shards.py --out renders --rooms-per-shard 200
```

`build_defect_manifest.py` regenerates `defects/3d-front-defects.json` from the
same data. On one RTX 5080 the render step took **10.3 hours** (1.84 s per room)
and produced 15.06 GB.

The renderer is restarted every 100 rooms on purpose: in a single long-lived
process the time per room climbs steadily (1.9 s → 4.7 s over 330 rooms). We did
not find the cause; restarting caps it, and costs about 5 s per batch.

## Licence

Derived from 3D-FRONT / 3D-FUTURE. The original **3D-FRONT Data Sets Use License
Agreement** (`docs/3D-FRONT-ToU.pdf`) applies to this work:

- **Scientific research purposes only.** No commercial use of the data, of works
  derived from it, or of results obtained with it.
- **Pass the terms on.** If you share this data or anything derived from it, the
  recipient must be bound by the same agreement.
- **Cite the source.** 3D-FRONT and 3D-FUTURE, plus this repository.

We claim no licence over the underlying 3D-FRONT / 3D-FUTURE content and grant
none. 3D-FUTURE carries its own separate agreement (dated 2020-03-28) which we
were unable to obtain; if you need certainty about the furniture models,
consult it.

## Citation

```bibtex
@article{fu2021_3dfront,
  title   = {3D-FRONT: 3D Furnished Rooms with layOuts and semaNTics},
  author  = {Fu, Huan and Cai, Bowen and Gao, Lin and Zhang, Ling-Xiao and Wang, Jiaming and Li, Cao and Zeng, Qixun and Sun, Chengyue and Jia, Rongfei and Zhao, Binqiang and Zhang, Hao},
  journal = {arXiv preprint arXiv:2011.09127},
  year    = {2021}
}

@article{fu2021_3dfuture,
  title   = {3D-FUTURE: 3D Furniture Shape with TextURE},
  author  = {Fu, Huan and Jia, Rongfei and Gao, Lin and Gong, Mingming and Zhao, Binqiang and Maybank, Steve and Tao, Dacheng},
  journal = {International Journal of Computer Vision},
  year    = {2021}
}
```
