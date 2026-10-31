---
pretty_name: c4p0 (consolidated)
license: other
license_name: research-use
task_categories:
  - translation
  - text-generation
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
tags:
  - back-translation
  - parallel-corpus
  - synthetic
  - c4
size_categories:
  - 100K<n<1M
configs:
  - config_name: all
    data_files: "data/*/*.parquet"
  - config_name: de-en
    data_files: "data/de-en/*.parquet"
  - config_name: en-de
    data_files: "data/en-de/*.parquet"
  - config_name: en-engb
    data_files: "data/en-engb/*.parquet"
  - config_name: en-es
    data_files: "data/en-es/*.parquet"
  - config_name: en-fr
    data_files: "data/en-fr/*.parquet"
  - config_name: en-it
    data_files: "data/en-it/*.parquet"
  - config_name: en-ja
    data_files: "data/en-ja/*.parquet"
  - config_name: en-ko
    data_files: "data/en-ko/*.parquet"
  - config_name: en-ru
    data_files: "data/en-ru/*.parquet"
  - config_name: en-zh
    data_files: "data/en-zh/*.parquet"
  - config_name: es-en
    data_files: "data/es-en/*.parquet"
  - config_name: fr-en
    data_files: "data/fr-en/*.parquet"
  - config_name: it-en
    data_files: "data/it-en/*.parquet"
  - config_name: ja-en
    data_files: "data/ja-en/*.parquet"
  - config_name: ko-en
    data_files: "data/ko-en/*.parquet"
  - config_name: zh-en
    data_files: "data/zh-en/*.parquet"
---

# c4p0 (consolidated)

Back-translation / round-trip translation traces over C4 source text,
produced by LLM-based MT prompts. Each row records the forward translation
(`source -> target`) plus the back-translation
(`target -> target_backto_source`) so the data can be used for noisy
parallel-corpus mining, distillation, or evaluation of translation
robustness.

This is the **consolidated** release. Earlier work was published as 46
separate repos (`alvations/c4p0`, `alvations/c4p0-<pair>`,
`alvations/c4p0-v1-<pair>`, `alvations/c4p0-v2-<pair>`,
`alvations/c4p0-x1-<pair>`). All of those have been merged here under a
single layout.

## Schema

| column                          | type                                       | notes |
| ------------------------------- | ------------------------------------------ | ----- |
| `source`                        | string                                     | input sentence |
| `target`                        | string                                     | extracted forward translation (may be empty when extraction failed) |
| `target_backto_source`          | string                                     | extracted back-translation |
| `raw_target`                    | list<struct<generated_text: string>>       | raw LLM forward-direction generation |
| `raw_target_backto_source`      | list<struct<generated_text: string>>       | raw LLM back-direction generation |
| `prompt`                        | string                                     | forward-translation instruction (e.g. "Translate from English to German") |
| `reverse_prompt`                | string                                     | back-translation instruction |
| `source_langid`                 | string                                     | langid output on `source` |
| `target_langid`                 | string                                     | langid output on `target` |
| `target_backto_source_langid`   | string                                     | langid output on `target_backto_source` |
| `doc_id`                        | int64                                      | per-document index |
| `sent_id`                       | int64                                      | per-sentence index inside a document |
| `timestamp`                     | string                                     | source-document timestamp |
| `url`                           | string                                     | source-document URL |
| `doc_hash`                      | string                                     | source-document hash |
| `dataset`                       | string                                     | upstream dataset id (e.g. `allenai/c4`); null for v0 / x1 |
| `source_lang`                   | string                                     | 2-char ISO source language; null for v0 / x1 |
| `target_lang`                   | string                                     | 2-char ISO target language; null for v0 / x1 |
| `version`                       | string                                     | `v0` / `v1` / `v2` / `x1` (see below) |
| `source_repo`                   | string                                     | originating sub-repo id (full path) |
| `pair`                          | string                                     | `<src>-<tgt>` (also encoded in the directory name) |

## Layout

```
data/
  de-en/
    v0-00000-of-00001.parquet
    v1-00000-of-00001.parquet
    v2-00000-of-00001.parquet
    x1-00000-of-00001.parquet
  en-de/
    ...
  ...
```

One config per language pair, plus a top-level `all` config that loads
every shard.

## Versions

| tag  | provenance |
| ---- | ---------- |
| `v0` | original release: `alvations/c4p0` (mixed pairs, split here by prompt) + `alvations/c4p0-<pair>` |
| `v1` | `alvations/c4p0-v1-<pair>` — first consolidated re-pass |
| `v2` | `alvations/c4p0-v2-<pair>` — larger / second consolidated re-pass |
| `x1` | `alvations/c4p0-x1-<pair>` — experimental third-pass dump |

Different versions may share `doc_hash` / `url` because they were generated
on overlapping source documents. Use `(doc_hash, sent_id, version)` if you
need a unique row key.

## Pairs

Pairs present in this release:
`de-en`, `en-de`, `en-engb`, `en-es`, `en-fr`, `en-it`, `en-ja`, `en-ko`,
`en-ru`, `en-zh`, `es-en`, `fr-en`, `it-en`, `ja-en`, `ko-en`, `zh-en`.

`en-engb` keeps the original-release naming and refers to a UK-English
target style.

## Stats

- 50 parquet shards
- 694,717 rows total
- 16 pairs × 4 versions (not every cell is populated; some
  pair × version combinations did not exist in the source repos)
- ~339 MB compressed (snappy parquet)

## Loading

```python
from datasets import load_dataset

# All data:
ds = load_dataset("alvations/c4p0", split="train")

# A specific pair:
ds_en_de = load_dataset("alvations/c4p0", "en-de", split="train")

# Filter to one version:
ds_v2 = ds.filter(lambda x: x["version"] == "v2")
```

## Notes

- `target` is sometimes empty when the LLM forward translation failed to
  parse; the unparsed generation is preserved in `raw_target`.
- `source_langid` / `target_langid` are best-effort detector output and
  can disagree with the prompt's stated direction (especially on short
  strings).
- The `source_repo` column is preserved so you can map any row back to
  the exact upstream sub-repo it came from.
