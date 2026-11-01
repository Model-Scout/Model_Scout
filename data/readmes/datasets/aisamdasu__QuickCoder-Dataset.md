---
license: other
language:
  - ko
  - en
tags:
  - code
  - fill-in-the-middle
  - jsonl
  - tokenizer
  - moe
  - dense
pretty_name: QuickCoder-Dataset
size_categories:
  - 10M<n<100M
---

# QuickCoder-Dataset

This dataset repository stores upload-ready JSONL training checkpoints for code
completion and fill-in-the-middle training. Checkpoints are appended in
approximately 20 GiB units so they can also be copied to Google Drive and loaded
from Colab/H100 training jobs. New checkpoints use one JSONL file per 20 GiB
checkpoint. The long-term target is 400 GiB total mirrored to Hugging Face and
Google Drive.

## Current Upload Status

Only validation-passing checkpoints should be uploaded or used for training.

| Checkpoint | Size | JSONL | In-bundle duplicates | Status |
| --- | ---: | --- | ---: | --- |
| `checkpoint_20260611_104104_bundle01_20g` | 19.04 GiB | valid, single JSONL | 0 | uploaded to Hugging Face; Google Drive cloud verified by rclone SHA256/size check |
| `checkpoint_20260611_112534_bundle01_20g` | 19.11 GiB | valid, single JSONL | 0 | uploaded to Hugging Face; Google Drive cloud verified by rclone SHA256/size check |
| `checkpoint_20260611_143422_bundle01_20g` | 19.19 GiB | valid, single JSONL | 0 | uploaded to Hugging Face; Google Drive upload pending user confirmation |

Current Hugging Face dataset repo:

```text
aisamdasu/QuickCoder-Dataset
```

## Repository Layout

```text
README.md
dataset_guide/
tokenizer/
dense/
moe/
dataset/
  checkpoint_YYYYMMDD_HHMMSS_bundleNN_20g/
    dataset/
      checkpoint_YYYYMMDD_HHMMSS_bundleNN_20g.jsonl
dataset_guide/
  checkpoint_reports/
    checkpoint_YYYYMMDD_HHMMSS_bundleNN_20g/
      MANIFEST.json
      BALANCE_REPORT.md
      CHECKSUMS.txt
```

## Record Format

Each line is one UTF-8 JSON object. The main training payload is `text`.
Metadata can appear in top-level fields and in `meta`.

Common fields:

- `text`: canonical training string.
- `domain`: task family such as `code_fim` or `code_gen`.
- `difficulty`: coarse difficulty bucket.
- `meta.lang`: programming language.
- `meta.repo`, `meta.path`, `meta.license`, `meta.source`: source metadata when available.
- `meta.mode`: FIM ordering such as `psm` or `spm`.

FIM examples use explicit special tokens:

```text
<|fim_prefix|>{prefix}<|fim_suffix|>{suffix}<|fim_middle|>{middle}
```

Some FIM shards may use suffix-prefix-middle ordering for robustness.

## Source And License Notes

This is a mixed code dataset. Bundle 1 contains generated/unknown continuation
records and `the-stack-v2` FIM records with per-record source metadata such as
repository, path, and license where available. Consumers should filter by
`meta.license`, `meta.source`, and project policy before redistribution or
training.

The dataset card intentionally uses `license: other` because this repository
contains mixed-source records rather than one uniform license.

## Validation Contract

A checkpoint is upload-ready only when:

- JSONL parsing succeeds.
- Empty `text` count is zero.
- In-bundle duplicate count is zero.
- The checkpoint folder contains only one file:
  `dataset/<checkpoint>.jsonl`. Legacy checkpoints may contain several JSONL
  parts only until they are repackaged.
- `MANIFEST.json`, `BALANCE_REPORT.md`, and `CHECKSUMS.txt` are present under
  `dataset_guide/checkpoint_reports/<checkpoint>/`.
- Shared `tokenizer/`, `dense/`, and `moe/` documentation lives at repository
  root, outside checkpoint folders.

Do not train on a checkpoint marked `Not Upload Ready`.
