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
  - ru
  - ta
  - tr
pretty_name: Mumospee
tags:
  - Speech
  - Video
---

# Mumospee: A MUltiMOdal SPEEch Corpus

The Mumospee dataset supports the [Meetween](https://meetween.eu/) project's mission of enabling inclusive, language-neutral collaboration across virtual environments. The release provides metadata and download URLs for a curated collection of speech audio sourced from publicly available datasets, optimized for processing on high-performance computing clusters.

## Mumospee Overview

Mumospee is a comprehensive multilingual speech-metadata corpus featuring:

- **224,117 hours** of speech metadata across **65,757,486 samples**
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
| Total samples | 65,757,486 |
| Total audio duration | 224,117h 20m 23.0s (224,117.3h) |
| Average duration per sample | 12.27s |
| Avg transcript length | 21.0 words |
| Total parquet shards | 35 |


### Per-Split Overview

| Split | # Samples | Duration | Avg Duration | Avg Words | Shards |
|-------|----------:|---------:|-------------:|----------:|-------:|
| `train` | 64,995,066 | 222,881h 24m 09.6s (222,881.4h) | 12.35s | 21.1 | 33 |
| `test` | 398,191 | 639h 06m 04.1s (639.1h) | 5.78s | 10.5 | 1 |
| `validation` | 364,229 | 596h 50m 09.3s (596.8h) | 5.90s | 10.4 | 1 |


### Language Distribution

| Value | train samples | train % | test samples | test % | validation samples | validation % | Total samples | Total % | Total Duration | Total Dur % |
|-------|----------:|---------:|----------:|---------:|----------:|---------:|----------:|---------:|---------------:|------------:|
| `en` | 30,354,591 | 46.70% | 302,179 | 75.89% | 269,449 | 73.98% | 30,926,219 | 47.03% | 72,634h 44m 09.5s | 32.41% |
| `zh` | 19,969,304 | 30.72% | 0 | 0.00% | 0 | 0.00% | 19,969,304 | 30.37% | 49,922h 33m 08.9s | 22.28% |
| `de` | 1,288,162 | 1.98% | 13,511 | 3.39% | 13,511 | 3.71% | 1,315,184 | 2.00% | 6,264h 10m 16.0s | 2.80% |
| `fr` | 1,241,292 | 1.91% | 14,760 | 3.71% | 14,760 | 4.05% | 1,270,812 | 1.93% | 6,129h 37m 57.4s | 2.74% |
| `ja` | 870,783 | 1.34% | 684 | 0.17% | 635 | 0.17% | 872,102 | 1.33% | 1,718h 30m 51.3s | 0.77% |
| `es` | 629,900 | 0.97% | 13,221 | 3.32% | 13,221 | 3.63% | 656,342 | 1.00% | 4,639h 34m 39.7s | 2.07% |
| `it` | 588,543 | 0.91% | 8,183 | 2.06% | 8,940 | 2.45% | 605,666 | 0.92% | 4,614h 59m 36.9s | 2.06% |
| `pt` | 571,574 | 0.88% | 4,023 | 1.01% | 3,318 | 0.91% | 578,915 | 0.88% | 4,452h 55m 29.7s | 1.99% |
| `nl` | 571,403 | 0.88% | 1,699 | 0.43% | 1,699 | 0.47% | 574,801 | 0.87% | 4,501h 00m 46.2s | 2.01% |
| `sv` | 567,993 | 0.87% | 0 | 0.00% | 0 | 0.00% | 567,993 | 0.86% | 4,511h 52m 00.0s | 2.01% |
| `pl` | 567,309 | 0.87% | 0 | 0.00% | 0 | 0.00% | 567,309 | 0.86% | 4,517h 07m 24.8s | 2.02% |
| `lv` | 563,787 | 0.87% | 1,629 | 0.41% | 1,125 | 0.31% | 566,541 | 0.86% | 4,440h 37m 21.7s | 1.98% |
| `cs` | 565,495 | 0.87% | 0 | 0.00% | 0 | 0.00% | 565,495 | 0.86% | 4,517h 07m 22.8s | 2.02% |
| `ro` | 563,319 | 0.87% | 0 | 0.00% | 0 | 0.00% | 563,319 | 0.86% | 4,481h 04m 42.5s | 2.00% |
| `fi` | 563,305 | 0.87% | 0 | 0.00% | 0 | 0.00% | 563,305 | 0.86% | 4,472h 22m 31.4s | 2.00% |
| `sl` | 560,950 | 0.86% | 360 | 0.09% | 509 | 0.14% | 561,819 | 0.85% | 4,389h 53m 19.1s | 1.96% |
| `et` | 558,644 | 0.86% | 1,571 | 0.39% | 1,576 | 0.43% | 561,791 | 0.85% | 4,362h 52m 02.6s | 1.95% |
| `hu` | 559,069 | 0.86% | 0 | 0.00% | 0 | 0.00% | 559,069 | 0.85% | 4,390h 00m 33.0s | 1.96% |
| `mt` | 556,919 | 0.86% | 0 | 0.00% | 0 | 0.00% | 556,919 | 0.85% | 4,361h 28m 18.0s | 1.95% |
| `el` | 556,641 | 0.86% | 0 | 0.00% | 0 | 0.00% | 556,641 | 0.85% | 4,398h 06m 42.3s | 1.96% |
| `da` | 553,516 | 0.85% | 0 | 0.00% | 0 | 0.00% | 553,516 | 0.84% | 4,322h 44m 48.0s | 1.93% |
| `bg` | 553,022 | 0.85% | 0 | 0.00% | 0 | 0.00% | 553,022 | 0.84% | 4,325h 19m 31.7s | 1.93% |
| `lt` | 551,298 | 0.85% | 0 | 0.00% | 0 | 0.00% | 551,298 | 0.84% | 4,297h 54m 19.8s | 1.92% |
| `sk` | 545,302 | 0.84% | 0 | 0.00% | 0 | 0.00% | 545,302 | 0.83% | 4,315h 11m 03.5s | 1.93% |
| `hr` | 339,551 | 0.52% | 0 | 0.00% | 0 | 0.00% | 339,551 | 0.52% | 2,683h 37m 11.3s | 1.20% |
| `ko` | 92,182 | 0.14% | 0 | 0.00% | 0 | 0.00% | 92,182 | 0.14% | 217h 09m 58.0s | 0.10% |
| `ca` | 54,173 | 0.08% | 12,730 | 3.20% | 12,730 | 3.50% | 79,633 | 0.12% | 119h 48m 09.3s | 0.05% |
| `ru` | 12,112 | 0.02% | 6,300 | 1.58% | 6,110 | 1.68% | 24,522 | 0.04% | 38h 40m 15.3s | 0.02% |
| `zh-CN` | 7,085 | 0.01% | 4,898 | 1.23% | 4,843 | 1.33% | 16,826 | 0.03% | 26h 37m 10.2s | 0.01% |
| `fa` | 4,347 | 0.01% | 3,445 | 0.87% | 3,445 | 0.95% | 11,237 | 0.02% | 14h 20m 32.8s | 0.01% |
| `tr` | 3,966 | 0.01% | 1,629 | 0.41% | 1,624 | 0.45% | 7,219 | 0.01% | 7h 52m 17.3s | 0.00% |
| `mn` | 2,018 | 0.00% | 1,759 | 0.44% | 1,761 | 0.48% | 5,538 | 0.01% | 8h 21m 37.1s | 0.00% |
| `ar` | 2,029 | 0.00% | 1,695 | 0.43% | 1,758 | 0.48% | 5,482 | 0.01% | 5h 35m 01.6s | 0.00% |
| `sv-SE` | 2,160 | 0.00% | 1,595 | 0.40% | 1,349 | 0.37% | 5,104 | 0.01% | 4h 24m 34.4s | 0.00% |
| `id` | 1,243 | 0.00% | 844 | 0.21% | 792 | 0.22% | 2,879 | 0.00% | 2h 58m 58.9s | 0.00% |
| `ta` | 1,358 | 0.00% | 786 | 0.20% | 384 | 0.11% | 2,528 | 0.00% | 3h 04m 21.3s | 0.00% |
| `cy` | 721 | 0.00% | 690 | 0.17% | 690 | 0.19% | 2,101 | 0.00% | 3h 01m 18.5s | 0.00% |


### Tag / Source Distribution

| Value | train samples | train % | test samples | test % | validation samples | validation % | Total samples | Total % | Total Duration | Total Dur % |
|-------|----------:|---------:|----------:|---------:|----------:|---------:|----------:|---------:|---------------:|------------:|
| `Emilia` | 40,237,834 | 61.91% | 0 | 0.00% | 0 | 0.00% | 40,237,834 | 61.19% | 101,585h 04m 02.8s | 45.33% |
| `MOSEL` | 12,679,032 | 19.51% | 0 | 0.00% | 0 | 0.00% | 12,679,032 | 19.28% | 100,316h 58m 51.7s | 44.76% |
| `GigaSpeech` | 6,016,616 | 9.26% | 19,931 | 5.01% | 5,715 | 1.57% | 6,042,262 | 9.19% | 7,544h 42m 14.1s | 3.37% |
| `CoVoST` | 3,925,255 | 6.04% | 327,848 | 82.33% | 323,985 | 88.95% | 4,577,088 | 6.96% | 7,114h 56m 33.1s | 3.17% |
| `PeopleSpeech` | 1,501,271 | 2.31% | 34,898 | 8.76% | 18,622 | 5.11% | 1,554,791 | 2.36% | 5,987h 42m 22.4s | 2.67% |
| `LibriTTS` | 353,817 | 0.54% | 9,955 | 2.50% | 10,340 | 2.84% | 374,112 | 0.57% | 585h 37m 48.6s | 0.26% |
| `Librispeech` | 281,241 | 0.43% | 5,559 | 1.40% | 5,567 | 1.53% | 292,367 | 0.44% | 982h 18m 30.3s | 0.44% |


### License Distribution

| Value | train samples | train % | test samples | test % | validation samples | validation % | Total samples | Total % |
|-------|----------:|---------:|----------:|---------:|----------:|---------:|----------:|---------:|
| `CC-BY-NC-4.0` | 40,237,834 | 61.91% | 0 | 0.00% | 0 | 0.00% | 40,237,834 | 61.19% |
| `CC-BY-4.0` | 13,314,090 | 20.48% | 15,514 | 3.90% | 15,907 | 4.37% | 13,345,511 | 20.30% |
| `apache-2.0` | 6,016,616 | 9.26% | 19,931 | 5.01% | 5,715 | 1.57% | 6,042,262 | 9.19% |
| `CC0` | 3,925,255 | 6.04% | 327,848 | 82.33% | 323,985 | 88.95% | 4,577,088 | 6.96% |
| `CC-BY;CC-BY-SA` | 1,501,271 | 2.31% | 34,898 | 8.76% | 18,622 | 5.11% | 1,554,791 | 2.36% |

`apache-2.0` rows are the **GigaSpeech** subset: its transcripts/manifest are Apache-2.0, but the audio is governed by the [GigaSpeech Data User Agreement](https://github.com/SpeechColab/GigaSpeech#dataset-download) — non-commercial research only, no raw-audio redistribution.

## Data quality notes

- **MOSEL audio** is hosted separately at [`meetween/mumospee_mosel`](https://huggingface.co/datasets/meetween/mumospee_mosel) (VoxPopuli PLENARY sessions, 23 EU languages); each row's `url` points to the whole-session shard there.
- **Language labels** are those declared by each source and are not independently verified; for MOSEL they come from VoxPopuli session-level metadata (~1.5% disagree with a fastText check).
- **252 CoVoST rows** have `duration = NaN` (unreadable source audio) — filter with `df["duration"].notna()`; all other rows have a valid numeric duration.

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

- [CoVoST](https://github.com/facebookresearch/covost) (specifically CoVoST 2 — full 36 language pairs since 2026-06-22)
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

### 2026-07-02

- Repackaged the corpus into sharded Parquet for faster, streaming-friendly loading.
- Extended CoVoST to the full CoVoST 2 catalogue.
- Refreshed the GigaSpeech, LibriTTS, and MOSEL subsets from their source datasets — correcting transcripts, licenses, and audio download links, and expanding coverage.
- Recomputed all dataset statistics from the released data.