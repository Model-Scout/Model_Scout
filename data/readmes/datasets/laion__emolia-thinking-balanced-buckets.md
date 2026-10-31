---
license: cc-by-4.0
task_categories:
- audio-classification
- text-to-speech
language:
- en
- de
- zh
- fr
- ko
- ja
tags:
- audio
- speech
- voice
- emotion
- voicenet
- webdataset
size_categories:
- 100K<n<1M
---

# Emolia-Thinking — Balanced Per-Dimension Bucket Subset

A **balanced, per-dimension bucket subset** of
[`VoiceNet/emolia-thinking`](https://huggingface.co/datasets/VoiceNet/emolia-thinking),
derived from that dataset's zero-shot **VoiceNet-dimension** labels.

For every VoiceNet voice/prosody/timbre/style dimension, this subset draws a
roughly **equal number of clips from each ordinal bucket (0–6)**, so that
downstream training / probing sees a balanced distribution along each axis
instead of the strongly skewed natural distribution.

## How labels were produced

Each source clip in `VoiceNet/emolia-thinking` carries, for each of the **58
dimensions**, two independent **zero-shot CLAP** bucket predictions:

- `clap_comm__<DIM>` — CLAP "community" model bucket (0–6)
- `clap_large__<DIM>` — CLAP "large" model bucket (0–6)

## Selection rule (dual-CLAP agreement, union fallback)

For each of the **58 dimensions × 7 buckets**, we target **2000 clips**:

1. **Agreement pool** — clips where *both* CLAP models assign the same bucket
   `b` (`clap_comm__DIM == b AND clap_large__DIM == b`). If this pool has
   **≥ 2500** clips, we sample **2000** from it (`source = agreement`).
2. **Union fallback** — otherwise we use the union
   (`clap_comm__DIM == b OR clap_large__DIM == b`). If the union has ≥ 2000
   clips we sample **2000** (`source = union`); if it is smaller we take **all**
   of them (`source = short`).
3. **Spread across tars** — within a pool, candidates are ordered by
   `hash(shard || key || 'seed')` and the target count is taken from the top.
   This deterministically spreads the selection across source shards (no single
   tar dominates any bucket; observed max single-tar share per bucket ≈ 3%).

A clip may be selected for **multiple dimensions**, so the same audio can appear
under several `data/<DIM>/b<bucket>/` paths (deduplicated within each bucket).

Two dimensions are **structurally short** because they have fewer than 7 ordinal
levels, so their higher buckets are empty:

- `EXPL` (Content Appropriateness) — 3 levels (buckets 0–2 only)
- `BKGN` (Background Noise) — 5 levels (buckets 0–4 only)

This yields **800k** (clip × dimension) samples spanning **≈ 249k unique
clips**, built from **1034 / 1052** completed sweep shards (≈ 98% coverage).

## Layout

WebDataset-style tar shards:

```
data/<DIM>/b<bucket>/shard-<id>.tar
```

Each tar contains, per sample:

```
<emolia_id>.flac    # the audio
<emolia_id>.json    # the full original emolia-thinking annotation record
```

`<emolia_id>` is the globally-unique `__emolia_id__` from the source dataset
(the per-tar `key` filename repeats across tars, so it is **not** used as the
sample name here).

`<DIM>` is one of the 58 VoiceNet dimension codes (see `metadata/` and the
source dataset for the code → human-name mapping), and `<bucket>` ∈ {0..6}.

## Metadata

- `metadata/selection.parquet` — one row per (clip, dim, bucket):
  `__emolia_id__, shard, key, dim, bucket, source`.
- `metadata/agreement_plan.parquet` — per (dim, bucket) pool sizes and the
  chosen source (agreement / union / short) and selected count.
- `metadata/agreement_plan_dims.parquet` — per-dimension summary.

## Notes

- Labels are **zero-shot model predictions**, not human ground truth; treat them
  as weak/approximate supervision.
- Because a clip can satisfy several dimensions' bucket criteria, samples recur
  across dimensions; deduplicate by `__emolia_id__` if you need a flat clip set.
- Audio and annotation content are inherited unchanged from
  `VoiceNet/emolia-thinking`; please also cite / respect that dataset's terms.
