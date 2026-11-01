---
license: cc-by-4.0
task_categories:
  - text-to-speech
  - automatic-speech-recognition
language:
  - en
  - zh
  - ja
  - de
  - fr
  - es
  - it
  - cs
  - et
  - pl
  - sl
  - fi
  - sv
  - el
  - pt
  - ro
  - nl
  - hu
  - lt
  - da
  - hr
  - lv
  - mt
  - sk
  - ko
  - bg
  - ca
  - fa
  - ar
  - mn
  - id
  - cy
pretty_name: Mumospee
tags:
  - Speech
  - Video
---

# Mumospee: A MUltiMOdal SPEEch Corpus

The Mumospee dataset supports the [Meetween](https://meetween.eu/) project's mission of enabling inclusive, language-neutral collaboration across virtual environments. The release provides metadata and download URLs for a curated collection of speech audio sourced from publicly available datasets, optimized for processing on high-performance computing clusters.

## Mumospee Overview

Mumospee is a comprehensive multilingual speech-metadata corpus featuring:

- **140,084 hours** of speech metadata across **53,983,241 samples**
- Coverage of 25 EU languages plus a long tail of additional languages
- Collections drawn from existing datasets in different speaking styles and content genres:

```python
_TAGS = ["CoVoST", "GigaSpeech", "PeopleSpeech", "Librispeech", "LibriTTS", "Emilia", "MOSEL"]
```

A smaller version with fewer than 1000 rows is also available as [mumospee_small](https://huggingface.co/datasets/meetween/mumospee_small) for testing purposes.

## Dataset Statistics

### Overview (All Splits Combined)

| Metric | Value |
|--------|-------|
| Total samples | 53,983,241 |
| Total audio duration | 140,084h 10m 12.4s (140,084.2 hours) |
| Average duration per sample | 9.34s |
| Avg transcript length | 16.5 words |
| Total parquet shards | 29 |

### Per-Split Overview

| Split | # Samples | Duration | Avg Duration | Avg Words | Shards |
|-------|----------:|---------:|-------------:|----------:|-------:|
| `train` | 53,319,102 | 139,005h 44m 08.1s (139,005.7h) | 9.39s | 16.5 | 27 |
| `test` | 341,118 | 547h 25m 08.3s (547.4h) | 5.78s | 10.3 | 1 |
| `validation` | 323,021 | 531h 00m 56.0s (531.0h) | 5.92s | 10.4 | 1 |

### Language Distribution

| Value | train samples | train % | test samples | test % | validation samples | validation % | Total samples | Total % | Total Duration | Total Dur % |
|-------|----------:|---------:|----------:|---------:|----------:|---------:|----------:|---------:|---------------:|------------:|
| `en` | 28,643,120 | 53.72% | 266,720 | 78.19% | 248,203 | 76.84% | 29,158,043 | 54.01% | 67,241h 32m 58.9s | 48.00% |
| `zh` | 19,969,319 | 37.45% | 0 | 0.00% | 0 | 0.00% | 19,969,319 | 36.99% | 49,922h 40m 38.9s | 35.64% |
| `ja` | 869,665 | 1.63% | 0 | 0.00% | 0 | 0.00% | 869,665 | 1.61% | 1,715h 27m 58.6s | 1.22% |
| `de` | 841,219 | 1.58% | 13,511 | 3.96% | 13,511 | 4.18% | 868,241 | 1.61% | 2,682h 25m 04.8s | 1.91% |
| `fr` | 777,904 | 1.46% | 14,760 | 4.33% | 14,760 | 4.57% | 807,424 | 1.50% | 2,428h 51m 30.3s | 1.73% |
| `es` | 165,080 | 0.31% | 13,221 | 3.88% | 13,221 | 4.09% | 191,522 | 0.35% | 939h 03m 30.5s | 0.67% |
| `it` | 123,812 | 0.23% | 8,183 | 2.40% | 8,940 | 2.77% | 140,935 | 0.26% | 886h 02m 54.3s | 0.63% |
| `cs` | 106,037 | 0.20% | 0 | 0.00% | 0 | 0.00% | 106,037 | 0.20% | 842h 13m 51.9s | 0.60% |
| `et` | 100,734 | 0.19% | 1,571 | 0.46% | 1,576 | 0.49% | 103,881 | 0.19% | 783h 51m 52.6s | 0.56% |
| `pl` | 102,193 | 0.19% | 0 | 0.00% | 0 | 0.00% | 102,193 | 0.19% | 811h 23m 20.4s | 0.58% |
| `sl` | 100,710 | 0.19% | 360 | 0.11% | 509 | 0.16% | 101,579 | 0.19% | 779h 12m 25.6s | 0.56% |
| `fi` | 100,236 | 0.19% | 0 | 0.00% | 0 | 0.00% | 100,236 | 0.19% | 788h 31m 35.8s | 0.56% |
| `sv` | 99,891 | 0.19% | 0 | 0.00% | 0 | 0.00% | 99,891 | 0.19% | 787h 41m 55.6s | 0.56% |
| `el` | 99,761 | 0.19% | 0 | 0.00% | 0 | 0.00% | 99,761 | 0.18% | 787h 42m 47.6s | 0.56% |
| `pt` | 99,487 | 0.19% | 0 | 0.00% | 0 | 0.00% | 99,487 | 0.18% | 781h 43m 50.3s | 0.56% |
| `ro` | 99,411 | 0.19% | 0 | 0.00% | 0 | 0.00% | 99,411 | 0.18% | 788h 28m 42.2s | 0.56% |
| `nl` | 99,400 | 0.19% | 0 | 0.00% | 0 | 0.00% | 99,400 | 0.18% | 787h 51m 08.8s | 0.56% |
| `hu` | 99,143 | 0.19% | 0 | 0.00% | 0 | 0.00% | 99,143 | 0.18% | 776h 56m 01.5s | 0.55% |
| `lt` | 99,078 | 0.19% | 0 | 0.00% | 0 | 0.00% | 99,078 | 0.18% | 771h 23m 15.8s | 0.55% |
| `da` | 98,868 | 0.19% | 0 | 0.00% | 0 | 0.00% | 98,868 | 0.18% | 768h 47m 46.0s | 0.55% |
| `hr` | 97,028 | 0.18% | 0 | 0.00% | 0 | 0.00% | 97,028 | 0.18% | 767h 17m 38.4s | 0.55% |
| `lv` | 92,504 | 0.17% | 1,629 | 0.48% | 1,125 | 0.35% | 95,258 | 0.18% | 707h 04m 04.2s | 0.50% |
| `mt` | 94,360 | 0.18% | 0 | 0.00% | 0 | 0.00% | 94,360 | 0.17% | 735h 44m 26.9s | 0.53% |
| `sk` | 92,345 | 0.17% | 0 | 0.00% | 0 | 0.00% | 92,345 | 0.17% | 731h 14m 15.9s | 0.52% |
| `ko` | 92,184 | 0.17% | 0 | 0.00% | 0 | 0.00% | 92,184 | 0.17% | 217h 10m 58.0s | 0.16% |
| `bg` | 89,209 | 0.17% | 0 | 0.00% | 0 | 0.00% | 89,209 | 0.17% | 684h 51m 35.5s | 0.49% |
| `ca` | 54,255 | 0.10% | 12,730 | 3.73% | 12,730 | 3.94% | 79,715 | 0.15% | 120h 28m 33.5s | 0.09% |
| `fa` | 4,348 | 0.01% | 3,445 | 1.01% | 3,445 | 1.07% | 11,238 | 0.02% | 14h 20m 48.6s | 0.01% |
| `ar` | 2,776 | 0.01% | 1,695 | 0.50% | 1,758 | 0.54% | 6,229 | 0.01% | 11h 28m 01.2s | 0.01% |
| `mn` | 2,018 | 0.00% | 1,759 | 0.52% | 1,761 | 0.55% | 5,538 | 0.01% | 8h 21m 37.1s | 0.01% |
| `id` | 1,243 | 0.00% | 844 | 0.25% | 792 | 0.25% | 2,879 | 0.01% | 2h 58m 58.9s | 0.00% |
| `cy` | 763 | 0.00% | 690 | 0.20% | 690 | 0.21% | 2,143 | 0.00% | 3h 20m 59.3s | 0.00% |
| `nn` | 426 | 0.00% | 0 | 0.00% | 0 | 0.00% | 426 | 0.00% | 3h 24m 46.5s | 0.00% |
| `la` | 289 | 0.00% | 0 | 0.00% | 0 | 0.00% | 289 | 0.00% | 2h 21m 50.7s | 0.00% |
| `ru` | 113 | 0.00% | 0 | 0.00% | 0 | 0.00% | 113 | 0.00% | 0h 53m 07.0s | 0.00% |
| `he` | 66 | 0.00% | 0 | 0.00% | 0 | 0.00% | 66 | 0.00% | 0h 28m 39.7s | 0.00% |
| `sq` | 40 | 0.00% | 0 | 0.00% | 0 | 0.00% | 40 | 0.00% | 0h 14m 25.8s | 0.00% |
| `tr` | 35 | 0.00% | 0 | 0.00% | 0 | 0.00% | 35 | 0.00% | 0h 17m 23.8s | 0.00% |
| `gl` | 15 | 0.00% | 0 | 0.00% | 0 | 0.00% | 15 | 0.00% | 0h 07m 15.9s | 0.00% |
| `uk` | 10 | 0.00% | 0 | 0.00% | 0 | 0.00% | 10 | 0.00% | 0h 04m 41.9s | 0.00% |
| `af` | 2 | 0.00% | 0 | 0.00% | 0 | 0.00% | 2 | 0.00% | 0h 00m 36.8s | 0.00% |
| `jw` | 1 | 0.00% | 0 | 0.00% | 0 | 0.00% | 1 | 0.00% | 0h 00m 30.0s | 0.00% |
| `ur` | 1 | 0.00% | 0 | 0.00% | 0 | 0.00% | 1 | 0.00% | 0h 00m 30.0s | 0.00% |
| `sr` | 1 | 0.00% | 0 | 0.00% | 0 | 0.00% | 1 | 0.00% | 0h 00m 30.0s | 0.00% |
| `hy` | 1 | 0.00% | 0 | 0.00% | 0 | 0.00% | 1 | 0.00% | 0h 00m 16.7s | 0.00% |
| `no` | 1 | 0.00% | 0 | 0.00% | 0 | 0.00% | 1 | 0.00% | 0h 00m 30.0s | 0.00% |

### Tag / Source Distribution

| Value | train samples | train % | test samples | test % | validation samples | validation % | Total samples | Total % | Total Duration | Total Dur % |
|-------|----------:|---------:|----------:|---------:|----------:|---------:|----------:|---------:|---------------:|------------:|
| `Emilia` | 40,237,834 | 75.47% | 0 | 0.00% | 0 | 0.00% | 40,237,834 | 74.54% | 101,585h 04m 02.8s | 72.52% |
| `GigaSpeech` | 5,053,116 | 9.48% | 0 | 0.00% | 0 | 0.00% | 5,053,116 | 9.36% | 6,297h 24m 07.6s | 4.50% |
| `CoVoST` | 3,591,777 | 6.74% | 290,706 | 85.22% | 288,492 | 89.31% | 4,170,975 | 7.73% | 6,519h 01m 42.7s | 4.65% |
| `MOSEL` | 2,300,046 | 4.31% | 0 | 0.00% | 0 | 0.00% | 2,300,046 | 4.26% | 18,127h 01m 37.8s | 12.94% |
| `PeopleSpeech` | 1,501,271 | 2.82% | 34,898 | 10.23% | 18,622 | 5.76% | 1,554,791 | 2.88% | 5,987h 42m 22.5s | 4.27% |
| `LibriTTS` | 353,817 | 0.66% | 9,955 | 2.92% | 10,340 | 3.20% | 374,112 | 0.69% | 585h 37m 48.6s | 0.42% |
| `Librispeech` | 281,241 | 0.53% | 5,559 | 1.63% | 5,567 | 1.72% | 292,367 | 0.54% | 982h 18m 30.3s | 0.70% |

### License Distribution

| Value | train samples | train % | test samples | test % | validation samples | validation % | Total samples | Total % |
|-------|----------:|---------:|----------:|---------:|----------:|---------:|----------:|---------:|
| `CC-BY-NC-4.0` | 40,237,834 | 75.47% | 0 | 0.00% | 0 | 0.00% | 40,237,834 | 74.54% |
| `unknown` | 5,053,116 | 9.48% | 0 | 0.00% | 0 | 0.00% | 5,053,116 | 9.36% |
| `CC0` | 3,591,777 | 6.74% | 290,706 | 85.22% | 288,492 | 89.31% | 4,170,975 | 7.73% |
| `CC-BY-4.0` | 2,935,104 | 5.50% | 15,514 | 4.55% | 15,907 | 4.92% | 2,966,525 | 5.50% |
| `CC-BY;CC-BY-SA` | 1,501,271 | 2.82% | 34,898 | 10.23% | 18,622 | 5.76% | 1,554,791 | 2.88% |

`unknown` rows correspond to the **GigaSpeech** subset. GigaSpeech's code and manifest are licensed under Apache 2.0, but the audio is governed by the [GigaSpeech Data User Agreement](https://github.com/SpeechColab/GigaSpeech#dataset-download) and the platform terms (YouTube, podcasts, audiobooks) of the underlying clips. Use is limited to non-commercial academic research; raw-audio redistribution is prohibited upstream.

## Data quality notes

### MOSEL durations

Per-segment durations for all 2,300,046 MOSEL rows are sourced from VoxPopuli's authoritative segment manifest ([`unlabelled_v2.tsv`](https://dl.fbaipublicfiles.com/voxpopuli/annotations/unlabelled_v2.tsv.gz)), keyed by `(event_id, segment_no)` parsed from the row's `path`. Coverage is 100% — no MOSEL row has a missing or zero duration. Median segment is 30.0 s; minimum is 14.95 s.

### MOSEL audio and language-label caveats

MOSEL audio is hosted in a separate repository, [`meetween/mumospee_mosel`](https://huggingface.co/datasets/meetween/mumospee_mosel). Two known caveats apply to MOSEL-tagged rows and are documented on that repository's data card:

- **Audio coverage is incomplete for some languages** (`voxpopuli.download_audios` did not finish for the full language set). Per-segment transcripts and durations in this dataset remain valid for the affected rows; the missing audio can be fetched from FBK-MT/mosel or VoxPopuli upstream.
- **Per-segment language labels are inherited from VoxPopuli's session-level metadata and are not human-verified at the utterance level.** A fastText `lid.176` sanity check disagrees with the declared language on ~1.5% of MOSEL rows, mostly on close-language pairs and short transcripts; the original declared labels are kept as-is here.

Subsets other than MOSEL (CoVoST, GigaSpeech, Emilia, PeoplesSpeech, LibriSpeech, LibriTTS) carry the language labels supplied by their original curators and are not independently verified.

### Notes

- `train`: 0 rows with unparseable duration
- `test`: 0 rows with unparseable duration
- `validation`: 0 rows with unparseable duration

## Mumospee dataset structure

Each row in the metadata represents one audio sample with the following fields:

- `path`: the relative path of the audio file
- `url`: the link to download the parquet shard containing the audio
- `type`: the sample type (`audio` or `video`)
- `duration`: duration in seconds
- `language`: language of the audio
- `transcript`: transcript text
- `tag`: origin dataset (one of `_TAGS` above)
- `split`: `train`, `test`, or `validation`
- `license`: license governing this sample

Example row:

```json
{
  "path": "3660-172183-0000.flac",
  "url": "https://huggingface.co/datasets/meetween/mumospee_librispeech/resolve/main/librispeech-parquet/dev-other.parquet",
  "type": "audio",
  "duration": 5.405,
  "language": "en",
  "transcript": "GERAINT AS HE HAD BEEN USED TO DO WHEN HE WAS AT ARTHUR'S COURT FREQUENTED TOURNAMENTS",
  "tag": "Librispeech",
  "split": "validation",
  "license": "CC-BY-4.0"
}
```

## Intended Uses

This dataset is designed to enable SpeechLLM and other large language models to support language-neutral virtual meeting applications.

## Data Sources

The release includes metadata and download URLs for the following publicly available datasets:

- [CoVoST](https://github.com/facebookresearch/covost) (specifically CoVoST 2)
- [GigaSpeech](https://github.com/SpeechColab/GigaSpeech)
- [PeopleSpeech](https://mlcommons.org/datasets/peoples-speech/)
- [LibriSpeech](https://www.openslr.org/12)
- [LibriTTS](https://openslr.org/60/)
- [Emilia](https://emilia-dataset.github.io/Emilia-Demo-Page/#dataset)
- [MOSEL](https://huggingface.co/datasets/FBK-MT/mosel)

## Example usage

```python
# pip install datasets

from datasets import load_dataset

# ── Load all splits at once ───────────────────────────────────────────────────

dataset = load_dataset("meetween/mumospee")
print(dataset)
# DatasetDict({
#     train:      Dataset({features: [...], num_rows: ...})
#     test:       Dataset({features: [...], num_rows: ...})
#     validation: Dataset({features: [...], num_rows: ...})
# })

# ── Load a specific split ─────────────────────────────────────────────────────

train_data      = load_dataset("meetween/mumospee", split="train")
test_data       = load_dataset("meetween/mumospee", split="test")
validation_data = load_dataset("meetween/mumospee", split="validation")
```

## License

The metadata is published under `CC-BY-4.0`. Each individual sample is governed by its own license, recorded per-row in the `license` column. Users must comply with the licensing terms of each underlying dataset.

## Changelog

### Latest update (2026-06-08)

- **Repackaged from a single 43 GB `dataset.csv` into 29 sharded Parquet files** (27 `train`, 1 `test`, 1 `validation`). Streaming, columnar reads, and `load_dataset(...)` are substantially faster, and CSV parsing edge cases are eliminated.
- **Recomputed all headline statistics directly from the released data.** Earlier versions of this card cited duration totals from upstream documentation; the figures above are now computed from the actual rows in the parquet shards.
- **Backfilled MOSEL `duration` for all 2,300,046 rows** from VoxPopuli's segment manifest. Previously these rows carried no real per-segment duration (the ingest hard-coded `"n/a"`, which a downstream cleanup step had converted to `0.0`, silently zeroing out ~18,000 hours of MOSEL).
- **Row repair pass on the metadata:**
  - rows whose `transcript` contained unescaped commas (and so were split into >9 fields) were re-joined into the correct 9-column shape;
  - rows whose `duration` carried a unit suffix (e.g. `"3.5 s"`) were stripped to a numeric value;
  - rows whose `language` was empty or longer than 5 characters were dropped;
  - exact duplicate rows were removed.
- **Corrected `license` attribution.** The `license` value for `tag == Emilia` rows is now reported as `CC-BY-NC-4.0` to match the upstream Emilia license; an earlier version of this card had bucketed those rows under `CC-BY-4.0` in the distribution table even though the per-row values were already correct.
- **Corrected MOSEL `language` for 55,387 rows** by overwriting with the VoxPopuli interpretation-channel code embedded in `path` (e.g. `..._bg_3` → `bg`).
- **`duration` set to NaN for 252 CoVoST rows** whose source MP3 bytes are unreadable upstream (mutagen and ffprobe both fail to parse them). These rows still carry valid `path`, `transcript`, and `language`; users requiring duration should filter with `df["duration"].notna()`.
- **Schema verification:** 0 rows with empty `language`, 0 rows with `len(language) > 5`, 0 rows with `duration == 0` (252 CoVoST rows are null/NaN — see above — and excluded from duration statistics).

The row schema (`path, url, type, duration, language, transcript, tag, split, license`), the `_TAGS` set, and the `load_dataset(...)` filters are unchanged.
