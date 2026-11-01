---
language:
- ja
- en
- zh
- es
- fr
- pt
- ko
tags:
- text-to-speech
- data-audit
- provenance
pretty_name: Piper-plus multilingual 7-language v8 — aggregate audit
configs:
- config_name: summary
  data_files:
  - split: audit
    path: data/summary.parquet
- config_name: language-summary
  data_files:
  - split: audit
    path: data/language-summary.parquet
- config_name: archive-parts
  data_files:
  - split: audit
    path: data/archive-parts.parquet
- config_name: source-provenance
  data_files:
  - split: audit
    path: data/source-provenance.parquet
---

# Piper-plus multilingual 7-language v8 — aggregate audit

This metadata-only audit describes
`ayousanz/piper-plus-multilingual-7lang-v8-dataset` at revision
`d6774fdd1ea77f21fdd7105f63ce8973c01642ad`. It contains no audio, transcripts,
speaker identifiers, cache tensors, embeddings, or per-utterance paths.

The fixed revision has 342,855 training rows across 3,682 speakers plus a speaker-safe
1,200-row holdout with ten additional speakers. The seven observed language IDs are
0–5 and 7; ID 6 is unused although the config declares eight language slots. All nine
split archive hashes match Hub LFS, and the essential archive contains exactly one
192-dimensional float32 embedding per training row.

The referenced source-rights manifest was due for review on 2026-08-18, omits three
current source families, and has no entry whose stated selected counts exactly match v8.
The provenance table records these gaps. No umbrella license is declared; each source's
license and restrictions must be applied independently.
