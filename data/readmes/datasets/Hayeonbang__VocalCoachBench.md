---
license: other
task_categories:
- audio-classification
- question-answering
- text-generation
language:
- en
- ko
pretty_name: VocalCoachBench
size_categories:
- 10K<n<100K
tags:
- music
- singing
- vocal-coaching
- arxiv:2609.04241
configs:
- config_name: recordings
  data_files:
  - split: train
    path: annotations/recordings.jsonl
- config_name: feedback_blocks
  data_files:
  - split: train
    path: annotations/feedback_blocks.jsonl
- config_name: atomic_claims
  data_files:
  - split: train
    path: annotations/atomic_claims.jsonl
- config_name: top3_issue_annotations
  data_files:
  - split: train
    path: annotations/top3_issue_annotations.jsonl
- config_name: triplet_rankings
  data_files:
  - split: train
    path: annotations/triplet_rankings.jsonl
- config_name: triplet_ranking_eval_units
  data_files:
  - split: train
    path: annotations/triplet_ranking_eval_units.jsonl
- config_name: segment_annotations
  data_files:
  - split: train
    path: annotations/segment_annotations.jsonl
- config_name: segment_consensus_events
  data_files:
  - split: train
    path: annotations/segment_consensus_events.jsonl
- config_name: source_datasets
  data_files:
  - split: train
    path: annotations/source_datasets.jsonl
---

# VocalCoachBench

**Accepted to NeurIPS 2026, Evaluations & Datasets Track**  
Hayeon Bang, Hounsu Kim, Wonil Kim, and Juhan Nam

[Paper](https://arxiv.org/abs/2609.04241) ·
[Demo and leaderboard](https://hayeonbang.github.io/VocalCoachBench/) ·
[Evaluation files](evaluation/README.md)

![VocalCoachBench overview](VCB.png)

VocalCoachBench is a singing-audio benchmark for evaluating vocal coaching
judgments. This release contains expert annotations for 515 singing recordings:
free-form coaching feedback, atomic diagnosis/correction claims, Top-3 issue
labels, same-song triplet rankings, and segment-conditioned issue labels.

> **Release version: `canonical515_physical_audio_1064refs`.**
> Canonical Top-3 denominator: **515 recordings (A=207, B=308)**.
> `top3_issue_annotations.jsonl` contains 1,064 annotations covering all 515
> recording IDs. An earlier filename-only join covered 511 IDs because four
> pairs of distinct physical audio files shared a submission filename. That
> pre-repair 511-ID count must not be used as the benchmark denominator. See
> `metadata/CANONICAL_EVALUATION.md` and `metadata/top3_join_policy.json`.

This release contains 1,064 recording-level expert reviews from 18 vocal
trainers: 504 recordings have two experts, nine have six, and two have one.
Its 4,506 feedback blocks yield 12,216 atomic claims: 6,162 diagnoses,
4,593 corrections, and 1,461 strengths. Earlier arXiv and dataset snapshots
contain counts from before the physical-audio join repairs; the versioned
counts and [release notes](metadata/PUBLIC_RELEASE.md) govern this release.

Subsets:

- `same_song` / Dataset A: 207 *Amazing Grace* performances from DAMP-S-AG.
  Audio is not redistributed; use `audio_filename` to match the official release.
- `diverse_song` / Dataset B: 308 recordings from multiple public singing
  datasets. Redistributable audio is included when source terms allow it.

## What Is Included

| File | Rows | Description |
|---|---:|---|
| `annotations/recordings.jsonl` | 515 | One row per benchmark recording, with subset/source metadata and audio access fields. |
| `annotations/feedback_blocks.jsonl` | 4,506 | Expert coaching feedback blocks, grouped by recording and anonymized annotator; covers all 515 recordings. |
| `annotations/atomic_claims.jsonl` | 12,216 | Atomic issue, correction, and strength claims extracted from feedback blocks; covers all 515 recordings. |
| `annotations/top3_issue_annotations.jsonl` | 1,064 | Expert Top-3 issue annotations joined by physical-audio identity; covers all 515 recordings. |
| `annotations/triplet_rankings.jsonl` | 450 | Raw same-song triplet ranking annotations, with benchmark inclusion fields. |
| `annotations/triplet_ranking_eval_units.jsonl` | 219 | One row per unique triplet, including the 2-of-3 pairwise agreement filter. |
| `annotations/segment_annotations.jsonl` | 2,526 | Processed local segment feedback annotations over 304 diverse-song recordings; see the version limitation below. |
| `annotations/segment_consensus_events.jsonl` | 262 | Segment-conditioned consensus events with IoU >= 0.3 and at least one shared issue tag. |
| `annotations/source_datasets.jsonl` | 10 | Source dataset counts, links, licenses, and redistribution status. |
| `metadata/category_ontology.json` | - | Seven issue labels and their parent categories. |
| `metadata/triplet_ranking_policy.json` | - | Machine-readable triplet ranking inclusion policy and counts. |
| `metadata/top3_join_policy.json` | - | Machine-readable canonical Top-3 join policy, counts, source hashes, and fallback audit. |
| `metadata/claims_join_policy.json` | - | Physical-audio join policy, counts, and source hashes for feedback blocks and atomic claims. |
| `metadata/canonical_top3_recording_inventory.jsonl` | 515 | One-row-per-recording Top-3 coverage audit with annotation counts and human-pair eligibility. |
| `metadata/CANONICAL_EVALUATION.md` | - | Frozen canonical Top-3 denominator and evaluation rules. |
| `metadata/PUBLIC_RELEASE.md` | - | Release version, final leaderboard definitions, and segment limitations. |
| `metadata/excluded_submission_files.json` | - | Historical/non-Top-3 exclusion metadata; superseded for canonical Top-3 by the hash-aware join policy. |
| `metadata/release_stats.json` | - | Release-level counts. |
| `metadata/croissant_rai_vocalcoachbench.json` | - | Machine-readable schema, source provenance, and Responsible AI metadata. |
| `evaluation/leaderboard.json` | - | Versioned final leaderboard with metric definitions, coverage, and provenance. |
| `evaluation/README.md` | - | Result definitions, evaluation policies, prompt snapshots, and reproducibility scope. |

Audio, when redistributed, is stored in `audio/diverse_song/` and
`audio/segment_clips_iou03/`. Rows without redistributed audio have `audio_path`
or `clip_path` set to `null`.

## Dataset Browser

A lightweight static browser is included at [`demo/index.html`](demo/index.html)
for inspecting recordings, redistributed audio, expert feedback blocks, atomic
claims, Top-3 issue annotations, consensus segment events, and triplet ranking
metadata.

## Source Datasets

VocalCoachBench uses existing public singing datasets as audio sources. The
benchmark contribution is the vocal-coaching annotation layer, task definitions,
evaluation metadata, and code for using these public sources. We do not claim the
original public audio datasets as part of our submission.

| Source dataset | Records | Audio in this package | License / terms note | Official source |
|---|---:|---|---|---|
| DAMP-S-AG | 207 | Not included; use official source | Smule Research Data License Agreement | [link](https://zenodo.org/records/3596940) |
| PopBuTFy | 85 | Not included; permission pending | CC BY-NC-SA 4.0; author registration terms request that download links not be redistributed | [link](https://github.com/MoonInTheRiver/NeuralSVB) |
| N20EMv2 | 65 | Included | CC BY-SA 4.0 | [link](https://zenodo.org/records/10814703) |
| LM-SSD | 7 | Included | CC BY 4.0 | [link](https://audiolabs-erlangen.de/resources/MIR/LM-SVR) |
| NUS-48E | 41 | Included | CC BY 4.0 | [link](https://zenodo.org/records/19595152) |
| MedleyDB | 32 | Not included; permission pending | CC BY-NC-SA 4.0 with author request not to republish without consent | [link](https://medleydb.weebly.com/downloads.html) |
| MedleyVox | 12 | Included | CC BY-NC-SA 4.0 | [link](https://zenodo.org/records/7984549) |
| MRSSing | 43 | Included | CC BY 4.0 | [link](https://huggingface.co/datasets/verstar/MRSAudio) |
| URSing | 14 | Included | CC BY 4.0 | [link](https://zenodo.org/records/6404999) |
| GTSinger | 9 | Included | CC BY-NC-SA 4.0 | [link](https://huggingface.co/datasets/GTSinger/GTSinger) |

## Schema Notes

The public join key is `recording_id`. For construction of the canonical
Dataset-B Top-3, feedback-block, and atomic-claim tables, raw submissions are first resolved to physical recordings
by audio SHA-256 and only then assigned `recording_id`; joining raw annotations
by `audio_filename` alone is prohibited because filenames are not unique. Most
rows also include `dataset` and `subset`; annotator IDs are stable anonymized
IDs. Feedback blocks and atomic claims can also be joined by `block_uid`.

The final evaluation prompts use these seven issue labels:

- `PITCH`
- `RHYTHM`
- `DICTION`
- `BREATH`
- `PHONATION`
- `TECHNIQUE`
- `EXPRESSION`

Parent categories are `Musical Accuracy`, `Technical Production`, and `Delivery`.
The released annotation files and `metadata/category_ontology.json` retain the
legacy label `VOCALIZATION`. It is an alias of `PHONATION`, not an eighth class;
normalize the two labels to the same class when scoring. See
`metadata/category_ontology.json` for the parent mapping.

Triplet ranking evaluation uses only triplets with at least 2-of-3 pairwise
agreement between two expert rankings. Use
`triplet_ranking_eval_units.jsonl` or filter `triplet_rankings.jsonl` with
`benchmark_included == true`. This yields 378
reference annotations over 189 unique evaluation
triplets.

## Evaluation and Version Notes

The [final leaderboard](evaluation/leaderboard.json), updated 2026-10-26, uses
schema `vcb_final_leaderboard_v1` and dataset version
`canonical515_physical_audio_1064refs`. Its policy is `strict_all_attempts`:
stored first responses are evaluated, and malformed or missing outputs count as
errors. Expert references have equal total weight per recording.

| Evaluation | Main denominator and interpretation |
|---|---|
| Top-3 | Seven-class macro-F1 over 515 recordings / 1,064 expert references; each recording has unit total weight. |
| Segment | Seven-class macro-F1 over the frozen 262 consensus events. |
| Direct and score-derived ranking | 189 triplets / 567 pair decisions, scored against both expert orders: 1,134 reference attempts. These are separate tasks. |
| Diagnosis strict hit / hit | 6,162 expert issue claims; strict hit counts `STRICT_HIT`, and hit also includes `COARSE_HIT`. |
| Prescription validity / diagnosis-to-prescription E2E | 2,575 fixed slots (515 × 5); missing prescriptions count as failures. |
| Human expert-vs-expert Top-3 | 513 recordings with at least two experts; the two single-expert recordings are excluded. |

The final leaderboard's Claims extension reports format failures: invalid JSON
produces zero emitted claims and remains in the fixed denominators. Main and
Simple prompt protocols and concatenated-audio Direct variants are labeled
separately. Unavailable results are `null`, not zero. See
[evaluation/README.md](evaluation/README.md) for the full metric definitions.

**Segment limitation:** the released 2,526 segment annotations cover 304
Dataset-B recordings, and the leaderboard retains its frozen 262-event set.
A separately staged physical-audio join repair produces 2,583 annotations over
308 recordings and 271 consensus events. That staged revision is not installed
in this release; it needs new audio clips and model predictions before a new
benchmark version can replace the 262-event results. See
[metadata/PUBLIC_RELEASE.md](metadata/PUBLIC_RELEASE.md).

## Audio Redistribution

- DAMP-S-AG same-song audio is excluded. Download it from the official Zenodo
  release and match by `audio_filename`.
- PopBuTFy and MedleyDB audio are excluded pending redistribution permission.
- Other diverse-song audio is included when allowed by source terms.

Redistributed full-recording audio files are copied from their public source
datasets without additional audio processing. The segment clips are derived time
crops for the segment-conditioned task. We do not claim copyright or ownership
over the original source audio; users should follow and cite the original source
datasets and their licenses or terms.

If any original dataset author or maintainer requests removal of redistributed
audio, or prefers source-link-only access, we will remove the affected audio files
from this package and switch those rows to official-source-link based distribution.

## Privacy

Annotator names, raw local paths, and source submission filenames containing
annotator names are not included in public annotation rows.

## Loading Example

```python
from datasets import load_dataset

repo_id = "Hayeonbang/VocalCoachBench"
recordings = load_dataset(repo_id, "recordings", split="train")
claims = load_dataset(repo_id, "atomic_claims", split="train")
triplet_units = load_dataset(repo_id, "triplet_ranking_eval_units", split="train")

same_song = recordings.filter(lambda row: row["subset"] == "same_song")
eval_triplets = triplet_units.filter(lambda row: row["benchmark_included"])
```

The `train` split name is a storage convention for the annotation tables, not a
benchmark training partition. Record the dataset revision when reporting
results, and pass `revision="<commit-sha>"` to reproduce that snapshot.

## Citation

If you use VocalCoachBench, please cite the paper and the original audio
datasets relevant to your work:

```bibtex
@misc{bang2026vocalcoachbench,
  title = {VocalCoachBench: Benchmarking Audio-Language Models on Expert Feedback for Singing},
  author = {Hayeon Bang and Hounsu Kim and Wonil Kim and Juhan Nam},
  year = {2026},
  eprint = {2609.04241},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2609.04241},
  note = {Accepted to the NeurIPS 2026 Evaluations \& Datasets Track}
}
```
