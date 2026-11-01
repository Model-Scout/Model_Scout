---
license: cc-by-4.0
task_categories:
- audio-classification
language:
- en
- de
- zh
- fr
- ko
- ja
pretty_name: Emolia VoiceNet Gemini Annotations
tags:
- speech
- voice
- emotion
- prosody
- annotation
- gemini
size_categories:
- 100K<n<1M
configs:
- config_name: default
  data_files:
  - split: train
    path: data/annotations.parquet
---

# Emolia VoiceNet Gemini Annotations

**468,180 dimension-level annotations** over **236,613 Emolia speech clips**,
each scored **0-6** (0-2 for the content-safety dimension) on one of **57 perceptual
voice / speech dimensions** - arousal, valence, brightness, resonance placement, speaking
styles, genuineness, recording quality, and more - by **Gemini 3.5 Flash (non-thinking,
temperature 0)**. This repository ships the **annotations, audio provenance, per-dimension
statistics, and the full scoring taxonomy**. The annotated audio is **also included here** as WebDataset shards under `webdataset/` (see [Audio (WebDataset)](#audio-webdataset) below); the manifest additionally lets you fetch any clip on demand from the two source audio repos.

## Audio (WebDataset)

The annotated audio is now **included in this repo** as
[WebDataset](https://github.com/webdataset/webdataset) tar shards under
[`webdataset/`](webdataset), alongside the annotation parquets. **236,556 clips**
are packed across **84 shards** (~80.8 GB of FLAC, repacked verbatim - no
re-encoding). Each sample is a `{key}.flac` + `{key}.json` pair sharing one key (the
clip's `emolia_id`); the JSON carries `emolia_id`, `language`, `duration`, and the
per-dimension `annotations` / `rounds` for that clip. See
[`webdataset/README.md`](webdataset/README.md) for the full schema, and
[`webdataset/index.parquet`](webdataset/index.parquet) for a `(shard, key, emolia_id)`
listing.

```python
import webdataset as wds
from huggingface_hub import HfApi

REPO = "laion/emolia-voicenet-gemini-annotations"
api = HfApi()
# list every shard in the repo (per-worker shard counts differ, so enumerate rather
# than brace-expand a rectangular range)
shards = sorted(
    f for f in api.list_repo_files(REPO, repo_type="dataset")
    if f.startswith("webdataset/") and f.endswith(".tar")
)
urls = [f"https://huggingface.co/datasets/{REPO}/resolve/main/{s}" for s in shards]

ds = (
    wds.WebDataset(urls, shardshuffle=False)
       .decode(wds.torch_audio)          # decodes the .flac
       .to_tuple("flac", "json")
)
for audio, meta in ds:
    wav, sr = audio                       # (tensor, sample_rate)
    print(meta["emolia_id"], meta["language"], meta["annotations"])
    break
```

The shards also follow the brace-expandable pattern
`emolia-voicenet-w{00..07}-{00000..00010}.tar`, but per-worker shard
counts differ, so enumerating the actual files (as above) avoids 404s.

The audio can still be fetched per-clip on demand via `data/manifest.parquet` (see
[How to get the audio for an annotation](#how-to-get-the-audio-for-an-annotation)) - the
WebDataset shards are simply a self-contained, streamable copy of the same clips.

## What this is

The [VoiceNet-Ext taxonomy](https://arxiv.org/abs/2505.20033) (Schumann et al., 2025)
defines 57 fine-grained, ordinal voice-performance dimensions. We took speech clips from
the **Emolia** corpus, selected candidates spread across score levels for each dimension
using **VoiceCLAP** zero-shot bucketing, and had **Gemini 3.5 Flash** listen to each clip
and emit a single integer for the one dimension it was selected for, following that
dimension's full 0-6 level rubric. Each row is one `(clip, dimension) -> score` judgement.

- Clips are multilingual: predominantly English and German, plus smaller amounts of
  Chinese, French, Korean and Japanese.
- Labels are **model-generated** (Gemini), not human annotations.
- No chain-of-thought was used: `thinkingBudget = 0`, temperature 0, so scores are direct
  single-token judgements.

## How it was made

1. **Candidate selection.** For every dimension, clips were drawn from Emolia and bucketed
   0-6 via **VoiceCLAP** zero-shot similarity against the level descriptions, to spread
   candidates across the ordinal range rather than sampling the corpus prior.
2. **Round 1.** Each candidate was re-scored by Gemini 3.5 Flash on its dimension using the
   verbatim rubric (196,500 annotations).
3. **Round 2.** The 196 most under-represented `(dimension x bucket)` cells (bottom-half,
   below-average Gemini count) were topped up with ~1,000 fresh CLAP-agreement candidates
   each, adding 195,995 annotations. This raised mean balance from 0.533 to 0.551.
4. **Round 3.** A final targeted top-up of the **worst-performing / most data-starved**
   dimensions: for the **24** hardest dimensions we refilled their **starved score levels**
   (**76** `(dimension x level)` cells) using only **dual-CLAP-agreement** candidates (clips
   both CLAP models agree belong in the target level), adding 75,685 annotations. Two
   dimensions were intentionally excluded: **`R_MIXD`** (CLAP-blind - the embedders cannot
   resolve it, so no reliable candidates exist) and **`ROUG`** (its candidate pool was already
   exhausted). This lifted mean balance to **0.552**.
5. **Cost.** Round 1 $109.83 + Round 2 $112.17 + Round 3 $42.77 = **~$264.77**
   total (gemini-3.5-flash batch API, 50% batch discount).
6. **Parse reliability.** Only **234 / 468,180** responses
   (0.050%) failed to parse to an integer; those rows keep a null
   `gemini_score` (the raw text is preserved in `annotations_raw.parquet`).

## Files & schema

### `data/annotations.parquet` - the labels (468,180 rows)

| column | dtype | description |
|---|---|---|
| `__emolia_id__` | string | Emolia clip id (e.g. `EN_B00020_S08991_W000042`) |
| `dim` | string | dimension code (one of 57, e.g. `AROU`) |
| `dim_name` | string | human-readable dimension name |
| `gemini_score` | Int64 (nullable) | Gemini score, 0-6 (0-2 for `EXPL`); null on parse failure |
| `round` | int64 | annotation round (1, 2 or 3) |

### `data/annotations_raw.parquet` - raw model text (468,180 rows)

| column | dtype | description |
|---|---|---|
| `__emolia_id__` | string | Emolia clip id |
| `dim` | string | dimension code |
| `raw` | string | verbatim Gemini output before integer parsing |

### `data/manifest.parquet` - audio provenance (468,058 rows, one per `(clip, dim)`)

| column | dtype | description |
|---|---|---|
| `__emolia_id__` | string | Emolia clip id |
| `dim` | string | dimension code |
| `round` | int64 | round that produced this clip (1, 2 or 3) |
| `audio_repo` | string | HF dataset repo holding the audio tar |
| `source_tar` | string | tar member inside that repo |
| `key` | string | tar entry base name |

Audio repos: round 1 -> [`laion/emolia-thinking-balanced-buckets`](https://huggingface.co/datasets/laion/emolia-thinking-balanced-buckets),
rounds 2 & 3 -> [`VoiceNet/emolia-thinking`](https://huggingface.co/datasets/VoiceNet/emolia-thinking).
**Member naming differs**: in round 1 the flac member is `{key}.flac`
(key = `DIM__bN__<emolia_id>`); in rounds 2 & 3 the flac member is `{key}.flac`
(key = a numeric string like `001999`). See the snippet below.

### `stats/per_dimension_stats.parquet` / `.csv`

Per dimension: `name`, `levels` (k), `count`, `count_0..count_6`, `mean_gemini_score`,
and `balance` = **normalized Shannon entropy** of the score histogram (0 = everything in
one level, 1 = perfectly even across the k levels).

### `taxonomy/voicenet_dimensions.md`

The full English rubric: all 57 dimensions with their 0-6 level descriptions.

## Statistics

- **Total annotations:** 468,180  ·  **unique clips:** 236,613  ·  **dimensions:** 57
- **Rounds:** 196,500 (round 1) + 195,995 (round 2) + 75,685 (round 3)
- **Mean per-dimension balance:** 0.552 (round 1: 0.533 -> +round 2: 0.551 -> +round 3: 0.552)
- Coarse perceptual axes (arousal, valence, formality, tempo, gender...) spread nicely
  across all 7 levels; fine resonance / timbre axes collapse - Gemini assigns almost
  everything to one level, so those behave as 1-2-level axes with these labels.

### Best-balanced dimensions

| dim | name | count | levels | mean | balance |
|---|---|--:|--:|--:|--:|
| `S_MONO` | Monologue Style | 6,500 | 7 | 2.66 | 0.891 |
| `AROU` | Arousal | 5,500 | 7 | 3.03 | 0.877 |
| `VALN` | Valence | 5,500 | 7 | 3.25 | 0.856 |
| `VOLT` | Volatility | 5,500 | 7 | 2.69 | 0.830 |
| `DFLU` | Disfluency | 5,500 | 7 | 1.99 | 0.796 |
| `S_CASU` | Casual Style | 6,500 | 7 | 3.61 | 0.791 |
| `STNC` | Stance | 5,500 | 7 | 3.06 | 0.789 |
| `S_FORM` | Formal Style | 5,500 | 7 | 2.81 | 0.780 |

### Worst-balanced (hardest) dimensions

| dim | name | count | levels | mean | balance |
|---|---|--:|--:|--:|--:|
| `R_ORAL` | Oral Resonance | 8,500 | 7 | 3.04 | 0.276 |
| `DARC` | Dynamic Arc | 10,500 | 7 | 2.09 | 0.259 |
| `EXPL` | Content Appropriateness (3-point Scale) | 3,500 | 3 | 0.07 | 0.229 |
| `METL` | Metallic Character | 13,500 | 7 | 2.09 | 0.214 |
| `R_THRT` | Throat Resonance | 13,500 | 7 | 3.07 | 0.170 |
| `R_NASL` | Nasal Resonance | 13,500 | 7 | 3.04 | 0.152 |
| `R_MASK` | Mask Resonance | 14,500 | 7 | 2.93 | 0.144 |
| `R_MIXD` | Mixed Resonance | 9,499 | 7 | 2.98 | 0.030 |

### Full per-dimension table (sorted by balance)

| dim | name | count | levels | mean | balance |
|---|---|--:|--:|--:|--:|
| `S_MONO` | Monologue Style | 6,500 | 7 | 2.66 | 0.891 |
| `AROU` | Arousal | 5,500 | 7 | 3.03 | 0.877 |
| `VALN` | Valence | 5,500 | 7 | 3.25 | 0.856 |
| `VOLT` | Volatility | 5,500 | 7 | 2.69 | 0.830 |
| `DFLU` | Disfluency | 5,500 | 7 | 1.99 | 0.796 |
| `S_CASU` | Casual Style | 6,500 | 7 | 3.61 | 0.791 |
| `STNC` | Stance | 5,500 | 7 | 3.06 | 0.789 |
| `S_FORM` | Formal Style | 5,500 | 7 | 2.81 | 0.780 |
| `COGL` | Cognitive Load | 7,500 | 7 | 2.10 | 0.775 |
| `S_DRAM` | Dramatic Style | 6,500 | 7 | 3.09 | 0.764 |
| `S_AUTH` | Authoritative Style | 6,500 | 7 | 2.57 | 0.759 |
| `S_CONV` | Conversational Style | 7,500 | 7 | 3.00 | 0.753 |
| `S_STRY` | Storytelling Style | 7,500 | 7 | 2.96 | 0.742 |
| `AGEV` | Voice Age | 8,500 | 7 | 3.12 | 0.723 |
| `ARSH` | Arousal Shift | 9,500 | 7 | 3.03 | 0.723 |
| `S_TECH` | Teacher/Didactic Style | 9,500 | 7 | 1.52 | 0.722 |
| `RANG` | Pitch Range | 6,500 | 7 | 3.31 | 0.721 |
| `BKGN` | Background Noise | 4,500 | 5 | 3.01 | 0.714 |
| `S_NARR` | Narrator Style | 6,500 | 7 | 2.79 | 0.706 |
| `VULN` | Vulnerability | 7,500 | 7 | 2.85 | 0.706 |
| `S_PLAY` | Playful Style | 6,500 | 7 | 2.55 | 0.677 |
| `FOCS` | Focus | 9,500 | 7 | 3.02 | 0.657 |
| `TEMP` | Tempo | 6,500 | 7 | 2.76 | 0.648 |
| `ATCK` | Attack | 5,500 | 7 | 2.94 | 0.624 |
| `BRGT` | Brightness | 9,500 | 7 | 2.90 | 0.622 |
| `EMPH` | Emphasis | 6,500 | 7 | 3.29 | 0.620 |
| `S_ASMR` | ASMR Style | 9,500 | 7 | 2.14 | 0.588 |
| `TENS` | Tension | 6,500 | 7 | 2.27 | 0.572 |
| `RESP` | Respiration | 7,500 | 7 | 2.49 | 0.549 |
| `VALS` | Valence Shift | 8,500 | 7 | 2.94 | 0.546 |
| `S_NEWS` | Newsreader Style | 6,500 | 7 | 0.82 | 0.539 |
| `RCQL` | Recording Quality | 7,500 | 7 | 3.20 | 0.532 |
| `CHNK` | Chunking | 6,500 | 7 | 2.69 | 0.531 |
| `CLRT` | Articulation Clarity | 11,360 | 7 | 3.03 | 0.526 |
| `ESTH` | Esthetics | 8,500 | 7 | 3.31 | 0.515 |
| `GEND` | Perceived Gender | 8,500 | 7 | 3.08 | 0.505 |
| `S_CART` | Cartoonish Style | 10,500 | 7 | 1.08 | 0.474 |
| `R_CHST` | Chest Resonance | 6,500 | 7 | 2.93 | 0.454 |
| `SMTH` | Smoothness | 7,498 | 7 | 2.76 | 0.444 |
| `S_RANT` | Ranting/Angry Style | 11,500 | 7 | 1.12 | 0.441 |
| `VFLX` | Velocity Flux | 10,500 | 7 | 3.13 | 0.439 |
| `HARM` | Harmonicity | 11,500 | 7 | 2.84 | 0.436 |
| `S_WHIS` | Whisper-Talk Style | 11,500 | 7 | 1.19 | 0.436 |
| `STRU` | Structure | 7,500 | 7 | 2.84 | 0.423 |
| `REGS` | Register | 7,500 | 7 | 1.60 | 0.415 |
| `ROUG` | Roughness | 7,498 | 7 | 2.33 | 0.376 |
| `WARM` | Warmth | 8,500 | 7 | 2.90 | 0.369 |
| `FULL` | Fullness | 10,325 | 7 | 2.94 | 0.343 |
| `R_HEAD` | Head Resonance | 11,500 | 7 | 2.91 | 0.282 |
| `R_ORAL` | Oral Resonance | 8,500 | 7 | 3.04 | 0.276 |
| `DARC` | Dynamic Arc | 10,500 | 7 | 2.09 | 0.259 |
| `EXPL` | Content Appropriateness (3-point Scale) | 3,500 | 3 | 0.07 | 0.229 |
| `METL` | Metallic Character | 13,500 | 7 | 2.09 | 0.214 |
| `R_THRT` | Throat Resonance | 13,500 | 7 | 3.07 | 0.170 |
| `R_NASL` | Nasal Resonance | 13,500 | 7 | 3.04 | 0.152 |
| `R_MASK` | Mask Resonance | 14,500 | 7 | 2.93 | 0.144 |
| `R_MIXD` | Mixed Resonance | 9,499 | 7 | 2.98 | 0.030 |

## How to get the audio for an annotation

```python
import io, tarfile, soundfile as sf, pandas as pd
from huggingface_hub import hf_hub_download

man = pd.read_parquet("data/manifest.parquet")
r = man[(man.dim == "AROU")].iloc[0]           # pick any (clip, dim) row

tar_path = hf_hub_download(
    repo_id=r.audio_repo, repo_type="dataset", filename=r.source_tar
)
member = f"{r.key}.flac"                      # round1: DIM__bN__<id>.flac ; rounds 2/3: <numeric>.flac
with tarfile.open(tar_path) as tf:
    audio_bytes = tf.extractfile(member).read()
wav, sr = sf.read(io.BytesIO(audio_bytes))
print(r["__emolia_id__"], r.dim, wav.shape, sr)
```

Note the member-naming difference between rounds (the `key` column already encodes the
correct base name for each row, so `f"{r.key}.flac"` works for all rounds).

## Dimension glossary

Full level-by-level definitions are in
[`taxonomy/voicenet_dimensions.md`](taxonomy/voicenet_dimensions.md).

**Rhythm & Timing** (8): `TEMP` Tempo · `CHNK` Chunking · `SMTH` Smoothness · `CLRT` Articulation Clarity · `RANG` Pitch Range · `EMPH` Emphasis · `DFLU` Disfluency · `STRU` Structure

**Social & Interpersonal** (3): `STNC` Stance · `FOCS` Focus · `VULN` Vulnerability

**Speaker Identity** (3): `GEND` Perceived Gender · `AGEV` Voice Age · `REGS` Register

**Emotion & Affect** (3): `VALN` Valence · `AROU` Arousal · `VOLT` Volatility

**Physical Production** (4): `RESP` Respiration · `TENS` Tension · `COGL` Cognitive Load · `ATCK` Attack

**Spectral & Timbral** (7): `BRGT` Brightness · `ROUG` Roughness · `HARM` Harmonicity · `FULL` Fullness · `WARM` Warmth · `METL` Metallic Character · `ESTH` Esthetics

**Temporal Dynamics** (4): `VFLX` Velocity Flux · `DARC` Dynamic Arc · `ARSH` Arousal Shift · `VALS` Valence Shift

**Language & Recording** (3): `RCQL` Recording Quality · `BKGN` Background Noise · `EXPL` Content Appropriateness (3-point Scale)

**Resonance Placement** (7): `R_CHST` Chest · `R_THRT` Throat · `R_ORAL` Oral · `R_MASK` Mask · `R_NASL` Nasal · `R_HEAD` Head · `R_MIXD` Mixed

**Speaking Style** (15): `S_CASU` Casual · `S_CONV` Conversational · `S_FORM` Formal · `S_DRAM` Dramatic · `S_NARR` Narrator · `S_NEWS` Newsreader · `S_TECH` Teacher/Didactic · `S_AUTH` Authoritative · `S_PLAY` Playful · `S_CART` Cartoonish · `S_ASMR` ASMR · `S_WHIS` Whisper-Talk · `S_MONO` Monologue · `S_STRY` Storytelling · `S_RANT` Ranting/Angry

## Limitations & notes

- **Model-generated labels.** Scores come from Gemini 3.5 Flash, not humans. They reflect
  the model's perceptual judgement under the rubric, and inherit its biases.
- **Candidate selection is uneven across dimensions.** VoiceCLAP zero-shot bucketing is
  reliable for macro dimensions but **collapses on fine resonance** (`R_MIXD`, `R_MASK`,
  `R_NASL`, `R_THRT`, ...): Gemini rates ~90-99% of those clips in a single level, so those
  buckets are noisy and not usable as a balanced 7-level axis with these labels.
- **Duplicates.** 122 `(clip, dimension)` pairs
  (0.026%) appear in more than one round; the manifest is
  **deduplicated** to one row per pair (earliest round kept), while `annotations.parquet` retains
  every round's row.
- **Audio.** The annotated clips are packed as WebDataset shards under `webdataset/`; any
  clip can also be fetched on demand via the manifest from the two source audio repos.

## Project & Taxonomy

This dataset is the **label set of the VoiceNet project** — a family of models that predict **how**
speech is delivered across the 57 perceptual voice/prosody dimensions defined here.

- **GitHub project & docs:** <https://github.com/LAION-AI/voicenet> — self‑contained documentation,
  inference and training guides, and the EmoNet emotion taxonomy.
- **Live demo:** <https://projects.laion.ai/voicenet/> — VoiceNet predictions on 100 diverse
  multilingual Emolia clips.
- **Taxonomy:** the full 57‑dimension 0–6 rubric ships here as
  [`taxonomy/voicenet_dimensions.md`](taxonomy/voicenet_dimensions.md) and is mirrored on GitHub as
  [`taxonomy/voicenet_taxonomy.md`](https://github.com/LAION-AI/voicenet/blob/main/taxonomy/voicenet_taxonomy.md).
- **Trained predictors:** [`laion/voicenet-dimension-predictors-commercial`](https://huggingface.co/laion/voicenet-dimension-predictors-commercial)
  are trained on these annotations.

The VoiceNet taxonomy and project come from the **forthcoming VoiceNet paper** (not yet published).

## License & citation

Released under **CC-BY-4.0**. Annotations and pipeline by **LAION**; source speech from the
**Emolia** corpus; taxonomy from **VoiceNet-Ext** (Schumann et al., 2025,
<https://arxiv.org/abs/2505.20033>).

```bibtex
@misc{emolia_voicenet_gemini,
  title  = {Emolia VoiceNet Gemini Annotations},
  author = {LAION},
  year   = {2026},
  note   = {Gemini 3.5 Flash annotations of Emolia speech over the VoiceNet-Ext 57-dimension taxonomy},
  url    = {https://huggingface.co/datasets/laion/emolia-voicenet-gemini-annotations}
}
```
