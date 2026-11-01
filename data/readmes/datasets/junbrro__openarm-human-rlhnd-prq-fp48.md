---
language:
- en
- ko
tags:
- robotics
- hand-pose
- rlhnd
- openarm
---

# OpenArm Human RLHND PRQ / FP48 — Huiwon WAM-v1 subset

**The default release is now exactly the 1,187 episodes in
`/data/huiwon/data/openarm_wam_v1/human_as_openarm28/`.**
It contains 321,095 reference frames. The source selection, episode IDs, task
indices, and prompt strings match that dataset's metadata. Do not infer the
selection from the older `openarm_dataset_192x256` YAML sampling ratios.

| Dataset route | Reference subset | Episodes | Frames | FPS |
|---|---|---:|---:|---:|
| `rlwrld_human_lerobot` | `rlwrld_human_lerobot` | 472 | 68,065 | 20 |
| `open_air_fryer` | `openarm_validation_v2_junhyeong/open_air_fryer` | 52 | 10,751 | 20 |
| `close_air_fryer` | `openarm_validation_v2_junhyeong/close_air_fryer` | 52 | 12,518 | 20 |
| `left_hand_box_white_container` | `openarm_validation_v2_junhyeong/left_hand_box_white_container` | 101 | 25,362 | 20 |
| `anyh2r_prq30` | `anyh2r` | 510 | 204,399 | 30 |
| **Total** | | **1,187** | **321,095** | mixed |

The seven skill categories are PnP, PnP x 2, Open, Close, Pour, Move, and Flip.
There are 18 distinct instruction strings; skill categories are not instruction
IDs. The AnyH2R `stir` subset is excluded. Human PnP IDs
31, 67, 93, 256, 313, 409, and 458 are excluded, exactly as in the reference.
Episode IDs are deliberately not compacted. The box directory's historical
`left_hand` name does not change its right-hand instruction.

## Prompts and frame correspondence

`meta/tasks.jsonl`, `meta/episodes.jsonl`, and every parquet `task_index` agree
with the reference, including capitalization, punctuation, and wording. The
older `Left hand: None. Right hand:` prefix is absent where absent in WAM-v1.
Neither synonym substitution nor an additional language template is applied.

AnyH2R is retargeted from existing full-rate RLHND observations at native 30 Hz.
It is **not** an interpolation of the earlier 20 Hz cache. Four other subsets
retain their 20 Hz reference row timelines and already validated geometric
labels. Each `frame_maps/*.jsonl` identifies exact reference RGB frames; the
original high-resolution frame map is a separate field and must not be applied
again to the already sampled reference video. FP48 always uses the right-camera
coordinate system. AnyH2R's video bindings retain both left and right views;
the other subsets retain the right view.

## What is included

Offline PRQ labels, FP48 targets, validity masks, freshly recomputed per-subset
state/action statistics, frame maps, prompt tables, reference metadata hashes,
and numerical validation. No RGB videos, RLHND weights, MANO meshes, contact
outputs, or raw human data are uploaded. No new RLHND inference was performed
for this subset release.

PRQ/FP48 geometry retains the `rlhnd-rightcam-inspire-palm-v1` convention and
existing robot-derived FP48 normalization. The four right-hand subsets use
15D absolute-camera PRQ with next-frame actions; AnyH2R uses bimanual 30D PRQ
with a shared first-valid-right-wrist reference and same-frame actions.
Read `meta/label_contract.json` rather than assuming these actions have the
same coordinate or temporal convention. Invalid coordinates remain masked.

**This is a geometry-label companion for the paper's data selection, not the
original paper's 28D action tensor.** The reference FRED dataset has dummy
zero-filled 28D human state/actions and masks human action loss. Using these
PRQ labels for action or alignment supervision changes that training recipe.
The old pretrained HaWoR-target models are not claimed to be label-compatible.
Numerical checks do not certify visual accuracy, depth, or rollout success.

## Download and bind existing reference videos

```bash
hf download junbrro/openarm-human-rlhnd-prq-fp48 \
  --repo-type dataset --local-dir /your/cache/openarm-human-rlhnd

python /your/cache/openarm-human-rlhnd/prepare_labels.py \
  --output /your/new/dataset/rlhnd-wam-v1 \
  --video-root /data/huiwon/data/openarm_wam_v1/human_as_openarm28
```

Use a new output directory. For numerical labels without local videos, pass
`--labels-only` instead of `--video-root`. The helper verifies the selected
archive and every member hash before binding paths. `label_routes.json` gives
the dataset/cache routes. This root contains no extra box/ball/towel view.

`latest.json` is the authoritative default-release pointer. Old immutable
archives may remain in `releases/` for reproducibility; they are **not part of
this selection**. In particular, release `af6b5b6aefcc22db` was the previous
1,614-episode expanded MT corpus and must not be mixed into this paper subset.
Pin the HF commit or release ID when sharing an experiment.
