---
license: other
license_name: source-specific-licenses
license_link: https://github.com/ken-jo/qev/blob/main/docs/DATA.md
language:
- en
- ko
task_categories:
- text-classification
- image-classification
tags:
- multimodal
- typed-decisions
- synthetic
dataset_info:
- config_name: vision-2026-10-v3-coverage-manifest
  features:
  - name: id
    dtype: string
  - name: source
    dtype: string
  - name: subtask
    dtype: string
  - name: vision_only
    dtype: bool
  - name: n_images
    dtype: int64
  - name: image_sha256
    sequence: string
  - name: image_dhash64
    sequence: string
  - name: n_options
    dtype: int64
  - name: gold
    dtype: string
  - name: option_sha256
    sequence: string
  - name: holdout
    dtype: bool
  - name: added_v3
    dtype: bool
  - name: construction
    dtype: string
  - name: option_generators
    sequence: string
  - name: other_image_gold_ref
    sequence: string
  - name: seed
    dtype: string
  - name: rerender_palette
    dtype: string
  - name: rerender_labels
    sequence: string
  - name: rerender_negative_modes
    sequence: string
  - name: rerender_gold_slot
    dtype: int64
  - name: upstream_key
    dtype: string
  - name: upstream_label
    dtype: int64
configs:
- config_name: vision-2026-10-v3-coverage-manifest
  data_files:
  - split: train
    path: vision-mix-2026-10-v3/manifests/*.jsonl
- config_name: vision-2026-10-coverage-manifest
  data_files:
  - split: train
    path: vision-mix-2026-10/manifests/*.jsonl
- config_name: vision-2026-10-synthetic
  data_files:
  - split: train
    path: vision-mix-2026-10/synthetic/items.jsonl
- config_name: vision-2026-10-nlvr2
  data_files:
  - split: train
    path: vision-mix-2026-10/nlvr2/train.jsonl
  - split: dev
    path: vision-mix-2026-10/nlvr2/dev.jsonl
- config_name: vision-2026-10-nlvr2-test
  data_files:
  - split: test
    path: vision-mix-2026-10/nlvr2/test.jsonl
- config_name: starter-v2
  data_files:
  - split: train
    path: viewer/starter-v2/train.jsonl
  - split: dev
    path: viewer/starter-v2/dev.jsonl
  - split: calibration
    path: viewer/starter-v2/calibration.jsonl
  - split: test
    path: viewer/starter-v2/test.jsonl
- config_name: policy-v3
  data_files:
  - split: train
    path: viewer/policy-v3/train.jsonl
  - split: dev
    path: viewer/policy-v3/dev.jsonl
  - split: calibration
    path: viewer/policy-v3/calibration.jsonl
  - split: test
    path: viewer/policy-v3/test.jsonl
- config_name: policy-v6
  data_files:
  - split: train
    path: viewer/policy-v6/train.jsonl
  - split: dev
    path: viewer/policy-v6/dev.jsonl
  - split: calibration
    path: viewer/policy-v6/calibration.jsonl
  - split: test
    path: viewer/policy-v6/test.jsonl
- config_name: policy-v8
  data_files:
  - split: train
    path: viewer/policy-v8/train.jsonl
  - split: dev
    path: viewer/policy-v8/dev.jsonl
  - split: calibration
    path: viewer/policy-v8/calibration.jsonl
  - split: test
    path: viewer/policy-v8/test.jsonl
- config_name: foundation-v11
  data_files:
  - split: train
    path: viewer/foundation-v11/train.jsonl
  - split: dev
    path: viewer/foundation-v11/dev.jsonl
  - split: calibration
    path: viewer/foundation-v11/calibration.jsonl
  - split: test
    path: viewer/foundation-v11/test.jsonl
- config_name: workflow-v12
  data_files:
  - split: train
    path: viewer/workflow-v12/train.jsonl
  - split: dev
    path: viewer/workflow-v12/dev.jsonl
  - split: calibration
    path: viewer/workflow-v12/calibration.jsonl
  - split: test
    path: viewer/workflow-v12/test.jsonl
- config_name: workflow-v12-cohort
  data_files:
  - split: train
    path: viewer/workflow-v12-cohort/train.jsonl
  - split: dev
    path: viewer/workflow-v12-cohort/dev.jsonl
  - split: calibration
    path: viewer/workflow-v12-cohort/calibration.jsonl
  - split: test
    path: viewer/workflow-v12-cohort/test.jsonl
- config_name: workflow-v12b
  data_files:
  - split: train
    path: viewer/workflow-v12b/train.jsonl
  - split: dev
    path: viewer/workflow-v12b/dev.jsonl
  - split: calibration
    path: viewer/workflow-v12b/calibration.jsonl
  - split: test
    path: viewer/workflow-v12b/test.jsonl
- config_name: workflow-v12c
  data_files:
  - split: train
    path: viewer/workflow-v12c/train.jsonl
  - split: dev
    path: viewer/workflow-v12c/dev.jsonl
  - split: calibration
    path: viewer/workflow-v12c/calibration.jsonl
  - split: test
    path: viewer/workflow-v12c/test.jsonl
- config_name: workflow-v12d
  data_files:
  - split: train
    path: viewer/workflow-v12d/train.jsonl
  - split: dev
    path: viewer/workflow-v12d/dev.jsonl
  - split: calibration
    path: viewer/workflow-v12d/calibration.jsonl
  - split: test
    path: viewer/workflow-v12d/test.jsonl
- config_name: workflow-v12e
  data_files:
  - split: train
    path: viewer/workflow-v12e/train.jsonl
  - split: dev
    path: viewer/workflow-v12e/dev.jsonl
  - split: calibration
    path: viewer/workflow-v12e/calibration.jsonl
  - split: test
    path: viewer/workflow-v12e/test.jsonl
- config_name: workflow-v12f
  data_files:
  - split: train
    path: viewer/workflow-v12f/train.jsonl
  - split: dev
    path: viewer/workflow-v12f/dev.jsonl
  - split: calibration
    path: viewer/workflow-v12f/calibration.jsonl
  - split: test
    path: viewer/workflow-v12f/test.jsonl
- config_name: workflow-v13g
  data_files:
  - split: train
    path: viewer/workflow-v13g/train.jsonl
  - split: dev
    path: viewer/workflow-v13g/dev.jsonl
  - split: calibration
    path: viewer/workflow-v13g/calibration.jsonl
  - split: test
    path: viewer/workflow-v13g/test.jsonl
- config_name: workflow-v13h
  data_files:
  - split: train
    path: viewer/workflow-v13h/train.jsonl
  - split: dev
    path: viewer/workflow-v13h/dev.jsonl
  - split: calibration
    path: viewer/workflow-v13h/calibration.jsonl
  - split: test
    path: viewer/workflow-v13h/test.jsonl
- config_name: workflow-v13-final
  data_files:
  - split: train
    path: viewer/workflow-v13-final/train.jsonl
  - split: dev
    path: viewer/workflow-v13-final/dev.jsonl
  - split: calibration
    path: viewer/workflow-v13-final/calibration.jsonl
  - split: test
    path: viewer/workflow-v13-final/test.jsonl
---

# QEV data

Training data for QEV decision models: the October 2026 vision mixes for [QEV-2B](https://huggingface.co/ken-jo/QEV-2B) and [QEV-0.8B](https://huggingface.co/ken-jo/QEV-0.8B) (the first release and v3), and historical snapshots for [QEV 0.2.1](https://huggingface.co/ken-jo/qev).

## October 2026 vision mix v3: QEV-2B and QEV-0.8B v3

The v3 releases of [QEV-0.8B](https://huggingface.co/ken-jo/QEV-0.8B/tree/bb7107f413e855949462b900b26a622f4817160e) (revision `bb7107f`) and [QEV-2B](https://huggingface.co/ken-jo/QEV-2B/tree/7534f3b77eddaff5de4e6e75801677b976b5d2f5) (revision `7534f3b`) were trained on a revised mix, documented in [`vision-mix-2026-10-v3/`](vision-mix-2026-10-v3/README.md):

- **Diversified distractors:** the options of 16,195 items in seven sources were regenerated with 3 to 6 options each, mixing answers from other images, perturbed values and same-image annotations. The earlier "other questions about the same image" scheme appears in 30% of these items. 60% of Mind2Web items were re-rendered with new marks and negatives.
- **Targeted fixes:** 707 CORD field-presence items gained receipt-text decoys, and 157 new upstream TRAIN rows (127 Hateful Memes, 30 A-OKVQA) replaced rows removed by the near-duplicate filter.
- **Exclusions:** 2,063 items whose images are near-duplicates (dHash distance 4 or less) of evaluation-board or internal DEV images were removed.
- **Coverage mix:** 51,091 items from 18 sources (49,275 trained on, 1,816 held out for selection). The manifests (config `vision-2026-10-v3-coverage-manifest`) list ids, gold letters, hashes and how each item was built. They contain no third-party text or images.
- **Unchanged:** NLVR2 ids and teacher probabilities, and the synthetic items (v3 uses 5,414 of them), are those in `vision-mix-2026-10/`. The 4,658 replay items are again not released.

The sources and licenses are those of the first October 2026 release below.

## October 2026 vision release: QEV-2B and QEV-0.8B

[QEV-2B](https://huggingface.co/ken-jo/QEV-2B) and [QEV-0.8B](https://huggingface.co/ken-jo/QEV-0.8B) were trained on a new vision mix. It is documented in [`vision-mix-2026-10/`](vision-mix-2026-10/README.md):

- **Coverage mix:** 52,997 items from 18 sources (51,138 trained on, 1,859 held out for selection). For the 17 third-party sources, the manifests list each item's id, gold letter and the hashes of its options and images. They contain no third-party text or images. Build scripts are included to rebuild the items from the original train splits.
- **Synthetic set:** 6,000 items with images, released in full under Apache-2.0.
- **NLVR2:** 2,048 TRAIN, 256 DEV and 512 TEST ids, with QEV 0.2.1 teacher probabilities for TRAIN and DEV.
- **Not released:** 4,658 internal replay items and their targets.

The licenses differ by source; see the table in [`vision-mix-2026-10/README.md`](vision-mix-2026-10/README.md#sources-and-terms). FUNSD (non-commercial) and Hateful Memes (research-only) are listed by id and hash only.

The historical text and image corpora below are unchanged.

## Historical corpora

**Configurations overlap. Do not concatenate them or assume independent test sets.**

ZIPs in `corpora/` use `qev-<stage>.zip` and contain eligible
original records, images and license notices. Extracted stage folders and original
record/source IDs preserve the recorded training provenance.
Viewer rows expose request/target schemas as JSON strings; parse with `json.loads`.
IDs, group IDs, language and original split assignments are preserved.

| Configuration | Rows | Train | Dev | Calibration | Test |
| --- | ---: | ---: | ---: | ---: | ---: |
| starter-v2 | 8972 | 7008 | 771 | 714 | 479 |
| policy-v3 | 4192 | 2400 | 448 | 448 | 896 |
| policy-v6 | 6592 | 4800 | 448 | 448 | 896 |
| policy-v8 | 16734 | 9582 | 1790 | 1786 | 3576 |
| foundation-v11 | 19279 | 10841 | 2440 | 2132 | 3866 |
| workflow-v12 | 19100 | 11212 | 2712 | 2344 | 2832 |
| workflow-v12-cohort | 23788 | 11212 | 2712 | 7032 | 2832 |
| workflow-v12b | 19100 | 11212 | 2712 | 2344 | 2832 |
| workflow-v12c | 19100 | 11212 | 2712 | 2344 | 2832 |
| workflow-v12d | 19100 | 11212 | 2712 | 2344 | 2832 |
| workflow-v12e | 19100 | 11212 | 2712 | 2344 | 2832 |
| workflow-v12f | 19100 | 11212 | 2712 | 2344 | 2832 |
| workflow-v13g | 19100 | 11212 | 2712 | 2344 | 2832 |
| workflow-v13h | 19100 | 11212 | 2712 | 2344 | 2832 |
| workflow-v13-final | 19100 | 11212 | 2712 | 2344 | 2832 |

Counts include repeated observations across stages; the sum is not a unique count.

## Licenses and exclusions

This collection is not uniformly Apache-2.0. Read [LICENSES.md](LICENSES.md),
per-record source/license fields, and the original notices in `licenses/`.
Authored data and typed-decisions use Apache-2.0; Beans/TrashNet use MIT;
BANKING77 uses CC-BY-4.0; SNLI derivatives retain CC-BY-SA-4.0.
Original observations were selected and converted into typed decision views.
Synthetic labels are not observed outcomes; typed-decisions uses teacher agreement.

CIFAR-10 evaluation requests/images are excluded because redistribution rights are
unresolved. `excluded/` records references and hashes for direct upstream reconstruction.
No selected training rows were removed by that exclusion.

## Use and limitations

Extract one corpus ZIP under `data/` in the source repository. Image paths are relative
to that corpus. Manifests record original and exported record/image hashes.
Group and image-byte split checks apply within each corpus, not across historical stages.
They do not prove distinct physical objects or absence from Qwen pretraining.
Korean generated examples are retained; personal project notes are not included.
Old test groups have been inspected. Future models need untouched final populations.
Full retraining from all historical intermediate checkpoints is not turnkey.

[Training details](https://github.com/ken-jo/qev/blob/main/docs/TRAINING.md).

[GitHub: ken-jo/qev](https://github.com/ken-jo/qev)
