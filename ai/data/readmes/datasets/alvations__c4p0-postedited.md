---
pretty_name: c4p0 (post-edited)
license: other
license_name: research-use
task_categories:
  - translation
language:
  - en
  - de
  - es
  - fr
  - it
  - ja
  - ko
  - ru
  - zh
  - nl
  - la
tags:
  - parallel-corpus
  - post-edited
  - back-translation
  - c4
  - claude
size_categories:
  - 1K<n<100K
configs:
  - config_name: en-de
    data_files:
      - split: train
        path: "data/en-de/*.parquet"
  - config_name: en-en
    data_files:
      - split: train
        path: "data/en-en/*.parquet"
  - config_name: de-de
    data_files:
      - split: train
        path: "data/de-de/*.parquet"
  - config_name: es-en
    data_files:
      - split: train
        path: "data/es-en/*.parquet"
  - config_name: fr-en
    data_files:
      - split: train
        path: "data/fr-en/*.parquet"
  - config_name: ja-en
    data_files:
      - split: train
        path: "data/ja-en/*.parquet"
  - config_name: ko-en
    data_files:
      - split: train
        path: "data/ko-en/*.parquet"
  - config_name: la-en
    data_files:
      - split: train
        path: "data/la-en/*.parquet"
  - config_name: nl-en
    data_files:
      - split: train
        path: "data/nl-en/*.parquet"
  - config_name: ru-en
    data_files:
      - split: train
        path: "data/ru-en/*.parquet"
  - config_name: zh-en
    data_files:
      - split: train
        path: "data/zh-en/*.parquet"
  - config_name: xx-en
    data_files:
      - split: train
        path: "data/xx-en/*.parquet"
  - config_name: und-en
    data_files:
      - split: train
        path: "data/und-en/*.parquet"
---

# c4p0 (post-edited)

Companion to `alvations/c4p0`. Rows from the upstream consolidated
`alvations/c4p0` with a non-empty source AND non-empty translation are
run through Claude Haiku 4.5 to:

1. Fix encoding issues in the source (mojibake -> Unicode).
2. Detect the source language.
3. Clean the noisy LLM translation (strip "Translation:" prefixes,
   wrapper quotes, formatting noise) — kept even when the underlying
   translation is poor.
4. Generate a fresh, clean reference translation from the source.

## Schema

| column                 | type   | description |
| ---------------------- | ------ | ----------- |
| `source`               | string | encoding-fixed source sentence |
| `cleaned_translation`  | string | noisy LLM translation with prefixes / noise stripped |
| `postedited_reference` | string | fresh Claude-produced translation of the source |
| `url`                  | string | source-document URL (passthrough) |
| `src_lang`             | string | 2-char ISO 639-1, Claude-detected |
| `tgt_lang`             | string | 2-char ISO 639-1 |

## Layout

```
data/
  zh-en/
    recovered-00000-of-00001.parquet
  en-de/
    prototype-00000-of-00001.parquet
    recovered-00000-of-00001.parquet
  ...
```

Configs are named `<src_lang>-<tgt_lang>` using Claude-detected source
language and the target language declared at request time.

## Pair `src_lang` notes

The current configs reflect what Claude actually detected in the
source text, not the original c4p0 `pair` column. Some pairs:

- `xx-en` / `und-en` / `??-en` — Claude returned a placeholder code,
  usually for short or mixed-script source text
- `en-en` — Claude detected English in the source even though the
  upstream c4p0 pair was something like `en-de` (the upstream prompt
  used English as the back-translation pivot)

## Durability

The producing pipeline (`postedit_full.py`) writes every Claude
response to a local JSONL sink with `flush() + fsync()` before the
next call. The sink at
`/Users/alvas/jean-claude/stash/alvations-c4p0/_postedit_sinks/<pair>.jsonl`
is the durable source of truth; the parquet on this repo is a
refreshed view uploaded every 500 rows.

## License

Research use, under the upstream c4p0 / Common Crawl terms. Reusers
should cite both `alvations/c4p0` and Anthropic Claude.
