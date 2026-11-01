---
license: cc-by-3.0
language:
- ko
task_categories:
- automatic-speech-recognition
pretty_name: Korean ASR pseudo-labels from YODAS2
size_categories:
- 1M<n<10M
source_datasets:
- espnet/yodas2
tags:
- korean
- speech-recognition
- pseudo-labels
- knowledge-distillation
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*.parquet
  - split: heldout
    path: data/heldout-*.parquet
  - split: dev
    path: data/dev-*.parquet
---

# korean-asr — Korean ASR pseudo-labels for YODAS2

**This repository contains transcripts and segment metadata only. It does not contain audio.**
Every row points into [`espnet/yodas2`](https://huggingface.co/datasets/espnet/yodas2) by
`(shard, video_id, start, end)`, so you fetch the audio from the upstream dataset and cut it
yourself. See [Reconstructing the audio](#reconstructing-the-audio).

| split | utterances | hours |
|---|---:|---:|
| `train` | 1,034,181 | 6,974.3 |
| `heldout` | 46,542 | 314.6 |
| `dev` (subset of `heldout`) | 3,000 | 20.4 |

Total labelled: **1,080,723 utterances / 7,288.9 hours** of Korean speech.

## What this is

Korean subset of YODAS2, re-segmented and re-transcribed with
[`Qwen/Qwen3-Omni-30B-A3B-Instruct`](https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct)
(Apache-2.0) to produce pseudo-labels for distilling a small streaming ASR model.

The original YODAS captions are YouTube auto-captions: unpunctuated in places, misaligned,
and often wrong on numbers and named entities. The `text` field here is the Omni transcript;
the original caption is kept alongside as `yodas_text` so you can compare or pick either.

## Fields

| field | type | meaning |
|---|---|---|
| `id` | string | segment id, `<video_id>_<index>` |
| `video_id` | string | YouTube video id, as used by YODAS2 |
| `shard` | string | YODAS2 shard the video lives in, e.g. `ko000` |
| `start`, `end` | float32 | segment boundaries in seconds, relative to the full-length YODAS2 audio |
| `duration` | float32 | `end - start` |
| `text` | string | **pseudo-label** from Qwen3-Omni — the intended training target |
| `yodas_text` | string | original YODAS2 caption for the same span |
| `tier` | string | `A` or `B`, agreement quality (below) |
| `zip_agree` | float32 | token Jaccard between `text` and an independent Zipformer transcript |
| `code_switch` | bool | segment mixes Hangul and Latin script |

## Tiers

Each segment was independently transcribed a second time with a Zipformer ASR model, and
`zip_agree` is the token-level Jaccard overlap between that transcript and the Omni label.
Two models agreeing is weak evidence the label is right; two models disagreeing is strong
evidence something is wrong.

| tier | rule | shipped |
|---|---|---|
| A | `zip_agree >= 0.25` | yes |
| B | `0.10 <= zip_agree < 0.25` | yes |
| C | `zip_agree < 0.10` | **no** |
| D | Zipformer produced nothing | **no** |

Only A and B are in this release. C and D are withheld because a manual audit found the
failure mode below concentrated there.

## Known limitations — read before training on this

- **Labels are machine-generated and not human-verified.** Treat the whole thing as
  pseudo-labels, not ground truth.
- **Qwen3-Omni sometimes translates instead of transcribing.** Asked to transcribe Korean,
  it occasionally emits an English or Chinese rendering of the content. Measured on a manual
  audit: tier A was **99.9% clean**, but tier C ran **13.6% contaminated**. This is the main
  reason C and D are withheld. Tier B sits between the two and was not separately audited —
  if you need maximum precision, filter to `tier == "A"`.
- **Short segments are unreliable for language ID.** Language identification collapses below
  a few seconds, so a short non-Korean segment can survive filtering. A language-ID pass over
  the corpus was still running when this snapshot was cut; a later revision may remove roughly
  0.1% more rows.
- **Splits are separated by video, not by utterance.** Chunks from one video share a speaker,
  recording chain and topic, and their captions come from one auto-caption pass, so splitting
  per-utterance leaks. `train` and `heldout` share **zero** videos (verified). `dev` is a
  3,000-utterance sample *drawn from* `heldout` — so if you tune on `dev`, final numbers on
  the full `heldout` are mildly optimistic; report on `heldout` minus `dev` if you need it clean.
- **Numbers are spelled out as spoken.** `제2014다32호` appears as `제 이천십사 다시 삼십이 호`.
  This suits ASR training; it will look wrong if you expected written form.

## Reconstructing the audio

```python
from datasets import load_dataset

meta = load_dataset("nhatminh/korean-asr", split="train")
row = meta[0]
# row["shard"], row["video_id"], row["start"], row["end"], row["text"]
```

Fetch the matching long-form audio from `espnet/yodas2` and slice `[start, end]`. Audio in
this pipeline was resampled to 16 kHz mono.

## Licence and attribution

This dataset is released under **CC-BY-3.0**, inherited from its source.

- Audio and original captions: [`espnet/yodas2`](https://huggingface.co/datasets/espnet/yodas2),
  CC-BY-3.0, built from YouTube videos published under the Creative Commons Attribution licence.
- Pseudo-labels: generated with `Qwen/Qwen3-Omni-30B-A3B-Instruct` (Apache-2.0).

If you use this, cite YODAS as well:

```bibtex
@inproceedings{li2023yodas,
  title={{YODAS}: Youtube-Oriented Dataset for Audio and Speech},
  author={Li, Xinjian and Takamichi, Shinnosuke and Saeki, Takaaki and Chen, William
          and Shiota, Sayaka and Watanabe, Shinji},
  booktitle={2023 IEEE Automatic Speech Recognition and Understanding Workshop (ASRU)},
  year={2023},
  organization={IEEE}
}
```

## Privacy

The speech comes from public YouTube videos released under CC-BY, and this repository
redistributes no audio. If you are a speaker in this corpus and want a video removed,
open a discussion on this repository and the affected rows will be dropped.
