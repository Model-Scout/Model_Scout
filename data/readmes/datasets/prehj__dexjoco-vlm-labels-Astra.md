---
language:
- en
- ko
tags:
- robotics
- dexjoco
- vlm-labels
configs:
- config_name: anchors
  default: true
  data_files:
  - split: train
    path: labels/anchors.parquet
- config_name: frame_index
  data_files:
  - split: train
    path: labels/frame_index.parquet
- config_name: episodes
  data_files:
  - split: train
    path: labels/episodes.parquet
---

# DexJoCo VLM labels — Astra v3

Six single-arm DexJoCo tasks, 600 episodes, **13,352 labeled stride-16 anchors**
over **218,993 original frames**. Model: `gemini/gemini-3.8-flash` via an
OpenAI-compatible LiteLLM endpoint. These are annotation sidecars, not robot
images, action trajectories, contact ground truth, or compression-speed labels.

## Files

| File | Purpose |
|---|---|
| `labels/anchors.parquet` | Actual VLM labels, grades A–D, conf, instruction, measured facts, camera names and prompt/image hashes |
| `labels/frame_index.parquet` | Every source frame, exact matching keys, label status, nullable grades/conf and `is_labeled` mask |
| `labels/episodes.parquet` | All episode lengths, task-local dataset offsets and source packed parquet chunk/file indices |
| `labels/excluded_anchors.parquet` | 42 stride anchors excluded because their 16-action window contains an all-zero absolute target |
| `validation.json` | Coverage audit, task-wise grade/conf distributions, within-episode variation |
| `run_summary.json` | Actual API run counts, time and billed response cost |
| `prompts/`, `prompt_spec.py` | Executed prompt text and its message builder |
| `manifest.json` | Release settings and file SHA256 checksums |

The six tasks are `click_mouse`, `fold_glasses`, `hammer_nail`, `pick_bucket`,
`pinch_tongs`, `water_plant`, with 100 episodes each. Separate bimanual DexJoCo
datasets are outside this release.

## Matching to the original packed LeRobot dataset

**Join by `(task, episode_index, frame_index)`.** Episode and frame indices repeat
across tasks. `episode_index` is the dataset's episode id (`ep_local` in raw
labeling logs); `frame_index` is local to the episode. `dataset_row_index` equals
the episode's `dataset_from_index + frame_index`, within that task's dataset.
It is not the physical row offset of every packed parquet file. Use the episode
metadata for packed file location and its row offset; do not concatenate task
datasets and assume these indices become globally unique.

```python
from datasets import load_dataset
labels = load_dataset('prehj/dexjoco-vlm-labels-Astra', 'anchors', split='train')
all_frames = load_dataset('prehj/dexjoco-vlm-labels-Astra', 'frame_index', split='train')
```

```python
import pandas as pd
labels = pd.read_parquet('labels/frame_index.parquet')
# source is your source data frame with task, episode_index, frame_index columns.
keys = ['task', 'episode_index', 'frame_index']
assert not labels.duplicated(keys).any()
merged = source.merge(labels, on=keys, how='left', validate='one_to_one', indicator=True)
assert merged['_merge'].eq('both').all(), 'Wrong dataset or mismatched keys'
loss_mask = merged['is_labeled'].to_numpy()
# Compute supervised loss only where loss_mask=True. Null conf is NOT zero conf.
```

`frame_index.parquet` deliberately has null labels on unsampled frames. Status:

- `labeled_anchor`: an actual Gemini response at a valid multiple of 16.
- `unsampled`: a complete, valid 16-action window that is between stride anchors.
- `zero_target_window`: a complete window containing an all-zero absolute target;
  this cannot be interpreted as a real target jump.
- `incomplete_horizon`: fewer than 16 remaining recorded actions.

There are 13,394 complete stride-16 candidate windows, of which 42 are excluded.
All remaining **13,352** have a valid response. The frame index covers every
original frame including tails. No interpolation, forward filling, contact
override, or speed decision is silently applied. If dense targets are needed,
define that postprocessing separately, within each episode, with an explicit mask
and provenance; do not present interpolated values as direct VLM annotations.

## Questions and confidence

The single USER message contains two views of the same moment (scene then wrist),
GUIDANCE, instruction, action-derived motion facts, and four 1–5 checks:

- A (negative): operating movable parts of a held object.
- B (negative): directing a held tool into a localized impact.
- C (positive): pressing a surface-supported target.
- D (positive): moving/tilting an already grasped object as a whole through clear space.

The prompt uses the common value scale of RoboCasa v22 / Libero v3d / HumanData
v3. It contains no YES/NO SYSTEM instruction and no 2x/3x/4x demand sentences.
Dataset-relative arm/wrist/finger speed, reversal and slowing facts are retained.
The facts use recorded future action targets, so this is an offline annotation
procedure, not a causal online gate that has access only to current observation.

`grade_A`–`grade_D` are integer grades, **not probability-weighted expected grades**:
this API returned no grade logprobs. Let `g=(grade-1)/4` for each question. Then

`conf = (1 + g_C/3 + 2*g_D/3 - 2*g_A/3 - g_B/3) / 2`.

`vlm_label` in the anchors table aliases `conf`. These are provisional comparison
weights, not calibrated success probabilities or validated compression thresholds.
Conf is in [0,1], with a discrete set of possible values. All-four grade 1 gives
conf=0.5, not 0. Grades are retained so weights can be changed without relabeling.
The labels do not select a speed. No contact-boundary labels have been merged.

## Verification and provenance

The release audit reads original episode metadata, action arrays and frame-index
columns. It reconstructs all expected stride anchors and zero-target exclusions,
checks no missing/duplicate keys, confirms offsets, validates all grade responses
and confidence formulas, and verifies all 13,352 assembled prompt texts/hashes.
Stored tile hashes agree with the execution manifest; this audit does not rerun
image decoding or establish physical ground truth for the VLM grades.

Prompt source and verification: [quantization_label_gr00t, dexjoco-v3-prompt](https://github.com/rakybond007/quantization_label_gr00t/tree/dexjoco-v3-prompt),
commit `82d060b`. Source actions use absolute arm and finger targets; the action
compression operator is block-last, not summation of absolute poses.

Run: 2026-09-18, concurrency 8, temperature 0, low reasoning, max tokens 1024;
approximately 2h09m and USD 36.99, excluding small preliminary tests. Coverage and
format checks do not prove that the grades predict compression safety; policy
evaluation is a separate experiment. Original dataset permissions continue to
govern use of the underlying demonstrations.
