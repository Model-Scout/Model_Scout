---
license: cc-by-sa-4.0
language:
- en
- ja
- zh
- fr
- de
- it
- es
- ko
- ru
- pt
- pl
tags:
- video-games
- playstation
- game-metadata
- semantic-search
- multilingual
- retro-gaming
pretty_name: PS1 Discovery Corpus
size_categories:
- 1K<n<10K
task_categories:
- text-retrieval
- sentence-similarity
configs:
- config_name: default
  data_files:
  - split: train
    path: ps1_corpus.parquet
---

# PS1 Discovery Corpus

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20943284.svg)](https://doi.org/10.5281/zenodo.20943284) &nbsp; [Canonical repo & full docs on GitHub →](https://github.com/kenrinzero/ps1-discovery-corpus)

A multilingual metadata corpus of **7,995 PlayStation 1 games**, built to be searched
**by feel** — *"a cozy fishing game with an anime aesthetic"*, *"a 1996/97 Japanese game
where you could send letters"*, *"a bleak sci-fi adventure nobody remembers"* — rather than
by popularity or rigid filters. It is deliberately biased toward **obscure and
Japan-exclusive titles**: the long tail most databases skip.

The dataset's value is its **editorial layer**: every row carries an original,
evidence-grounded short description and a set of controlled-vocabulary tags spanning mood,
setting, mechanics, cultural lineage, and quality — the axes you actually search by when you
half-remember a game.

> **This is the Hugging Face mirror** (data + dataset viewer). The canonical source, the full
> `DATA_DICTIONARY`, `ATTRIBUTION`, and `TAG_VOCABULARY` live on
> [GitHub](https://github.com/kenrinzero/ps1-discovery-corpus).

## What's in it

- **7,995 games × 127 columns** — 7,861 with a full PlayStation DataCenter catalogue entry,
  plus 134 thin wiki-only stubs (flagged `is_stub=1`).
- **`curated_short_desc`** — original, evidence-grounded editorial prose on **100%** of rows.
  The highest-value field and the primary search surface.
- **`tags`** — a JSON object, 10 dimensions, a 330-tag controlled vocabulary, ~16.7 tags/game
  (genre, mood, setting, mechanic, cultural_lineage, discovery, quality, difficulty, length,
  recommendation). Every dimension is always present; an unsupported one is an explicit `[]`.
- **Facts** — `year`, `regions`, `developer`/`publisher`, ratings/scores, prices, playtimes —
  plus Wikipedia lead-summary extracts in **10 languages**, Wikidata IDs, and per-source
  `*_url` pointers.

## How to use it for "find by feel"

A hybrid: embed the prose for *feel*, filter and re-rank with the structured columns.

- **Embed `curated_short_desc` only.** Don't fold the flattened `tags` into the embedded text —
  boilerplate tags (`Single-Player` is on every row, `Save-Point` ~99%) homogenise the vectors
  and dilute the prose that carries the "feel".
- **Structured filtering / re-ranking** on `tags` + numeric columns. Discriminative discovery
  tags are deliberately rare (`Cult-Classic` 66 rows, `Mainstream-Hit` 24), so a "famous vs
  forgotten" axis is better served by re-ranking on `tags` + `popularity` than by the embedding.
  Year and region are filters too, not vibe.
- **Exclude `is_stub=1`** from the search index (134 thin rows).
- **De-dupe regional editions before display.** Rows are **one per regional release (serial)**,
  so a multi-region game appears multiple times. Don't collapse them by `wikidata_qid` alone —
  one Q-ID can span a whole series/sequel set; match Q-ID **and** base title.

## Coverage caveats

- **Japan bias is deliberate** (~4,400 Japan-only rows) — it's the point of the project.
- Facts and our own tags/descriptions cover every row, but third-party facets are filled only
  where a source had data (abstention is intentional, not a gap).
- **Tags are coarse by design** — discovery dimensions, not a fine-grained mechanic ontology;
  granular intent (e.g. "send letters") lives only in `curated_short_desc`.
- Third-party editorial **prose is not redistributed** (kept as `*_url` links); TVTropes text is
  excluded (CC BY-NC-SA). Our `curated_short_desc` replaces them as the searchable text.

## License & attribution

Released under **CC BY-SA 4.0**. The data is (1) **facts** (not copyrightable), (2) **our own
editorial** (`curated_short_desc`, `tags`), (3) **Wikipedia lead extracts** (CC BY-SA,
attributed), and (4) **Wikidata** IDs (CC0). Use it freely, including commercially; **credit the
project and the upstream sources** — see
[ATTRIBUTION.md](https://github.com/kenrinzero/ps1-discovery-corpus/blob/main/ATTRIBUTION.md) —
and share derivatives under the same license.

## Citation

Archived on Zenodo with a citable DOI: **[10.5281/zenodo.20943284](https://doi.org/10.5281/zenodo.20943284)**.

Compiled, cross-linked, and editorially processed with substantial assistance from **Claude
Opus 4.8** (Anthropic) — source reconciliation, the controlled-vocabulary tagging and
short-description passes (each adversarially verified against each game's own evidence), and
packaging. The dataset's design, direction, and final review are the maintainer's.

## Disclaimer

Community research dataset. Not affiliated with or endorsed by Sony Interactive Entertainment
or any listed source. Facts are corroborated across multiple databases but may contain errors;
corrections welcome.
