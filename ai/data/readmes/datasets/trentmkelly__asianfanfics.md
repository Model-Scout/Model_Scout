---
license: cc-by-sa-4.0
language:
  - en
  - zh
  - ko
  - ja
  - multilingual
pretty_name: Asianfanfics Archive
tags:
  - fanfiction
  - web-fiction
  - archive
  - parquet
size_categories:
  - 1M<n<10M
configs:
  - config_name: stories
    data_files:
      - split: train
        path: stories/*.parquet
  - config_name: chapters
    data_files:
      - split: train
        path: chapters/*.parquet
---

# Asianfanfics Archive

This dataset contains metadata and public chapter text from Asianfanfics, packaged as zstd-compressed Parquet files.

Repository: `trentmkelly/asianfanfics`

## Contents

The dataset is split into two Hugging Face configs:

| Table | Rows | Files | Description |
|---|---:|---:|---|
| `stories` | 1,727,491 | 4 | Story-level metadata and text-fetch status. |
| `chapters` | 4,114,576 | 42 | Chapter-level metadata, fetch status, and fetched public text when available. |

Total compressed Parquet size: about 4.2 GiB.

## Text Coverage

Chapter fetch status counts:

| Status | Rows | Meaning |
|---|---:|---|
| `fetched` | 2,045,265 | Public chapter text is present in `chapters.text`. |
| `skipped_gated` | 1,236,406 | Chapter/story appeared login-, member-, or subscription-gated. |
| `missing_body` | 820,399 | No static public chapter body was available. |
| `empty_body` | 11,776 | Chapter body was present but empty. |
| `not_found` | 730 | Chapter page was unavailable. |

Stored chapter text totals approximately 14,918,091,815 characters.

Story text status counts:

| Status | Stories |
|---|---:|
| `fetched` | 302,857 |
| `no_public_text` | 235,124 |
| `skipped_gated` | 211,049 |

Unavailable story IDs are included in `stories` for index completeness, but do not have story text.

## Columns

### `stories`

Includes story ID, URL, title, author, status/rating, publication/update metadata, engagement counters, tags/characters JSON, availability status, and text-fetch status fields.

### `chapters`

Includes story ID, chapter index, URL, title, word-count metadata, fetch status, fetch error, and `text` for chapters where public text was fetched.

## License

This dataset is released under the Creative Commons Attribution-ShareAlike 4.0 International license (`CC-BY-SA-4.0`).
