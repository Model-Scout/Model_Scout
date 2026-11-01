---
configs:
- config_name: crossref
  default: true
  data_files:
  - split: train
    path: crossref/train.jsonl
  - split: validation
    path: crossref/validation.jsonl
  - split: test
    path: crossref/test.jsonl
- config_name: affrodb
  data_files:
  - split: train
    path: affrodb/train.jsonl
  - split: validation
    path: affrodb/validation.jsonl
  - split: test
    path: affrodb/test.jsonl
- config_name: datacite
  data_files:
  - split: train
    path: datacite/train.jsonl
  - split: validation
    path: datacite/validation.jsonl
  - split: test
    path: datacite/test.jsonl
- config_name: synth-openalex
  data_files:
  - split: train
    path: synth-openalex/train.jsonl
  - split: validation
    path: synth-openalex/validation.jsonl
  - split: test
    path: synth-openalex/test.jsonl
- config_name: synth-openalex-hardened
  data_files:
  - split: train
    path: synth-openalex-hardened/train.jsonl
  - split: validation
    path: synth-openalex-hardened/validation.jsonl
  - split: test
    path: synth-openalex-hardened/test.jsonl
- config_name: synth-openalex-non-latin
  data_files:
  - split: train
    path: synth-openalex-non-latin/train.jsonl
  - split: validation
    path: synth-openalex-non-latin/validation.jsonl
  - split: test
    path: synth-openalex-non-latin/test.jsonl
task_categories:
- text-classification
- token-classification
language:
- en
- am
- ar
- as
- be
- bg
- bn
- el
- fa
- gu
- he
- hi
- hy
- ja
- ka
- kk
- km
- kn
- ko
- ky
- lo
- mk
- ml
- mn
- my
- ne
- or
- pa
- ps
- ru
- si
- sr
- ta
- te
- tg
- th
- uk
- ur
- zh
license: cc0-1.0
tags:
- ror
- affiliation-matching
- organization-disambiguation
- entity-linking
- synthetic
pretty_name: ROR Affiliation Matching (DataCite + Crossref + AffRoDB + Synthetic OpenAlex)
size_categories:
- 10K<n<100K
---

# ROR Affiliation Matching (DataCite + Crossref + AffRoDB + Synthetic OpenAlex)

Raw author-affiliation strings paired with the ROR (Research Organization
Registry) identifiers they should resolve to, prepared for training and
evaluating affiliation matching and entity-linking systems.

The dataset ships **six subsets** (loadable as Hugging Face configs), each
split into train/validation/test:

| Subset | Records | Source | Empty-label rows |
| --- | --- | --- | --- |
| `crossref` *(default)* | 3,000 | Crossref-derived affiliation strings | yes (483) |
| `affrodb` | 1,374 | AffRoDB (expert-judged) | no |
| `datacite` | 4,723 | DataCite-derived unique affiliations, ROR reannotated | yes (2,269) |
| `synth-openalex` | 3,000 | Synthetic, OpenAlex-distributed | yes (60) |
| `synth-openalex-hardened` | 3,000 | Synthetic, hardened against lexical matching | no |
| `synth-openalex-non-latin` | 3,000 | Synthetic, native non-Latin scripts | no |

```python
from datasets import load_dataset

# default subset = crossref
ds = load_dataset("cometadata/ror-matching-train-validation-test")

# pick a subset explicitly
crossref = load_dataset("cometadata/ror-matching-train-validation-test", "crossref")
affrodb  = load_dataset("cometadata/ror-matching-train-validation-test", "affrodb")
datacite = load_dataset("cometadata/ror-matching-train-validation-test", "datacite")
synth    = load_dataset("cometadata/ror-matching-train-validation-test", "synth-openalex")
hardened = load_dataset("cometadata/ror-matching-train-validation-test", "synth-openalex-hardened")
nonlatin = load_dataset("cometadata/ror-matching-train-validation-test", "synth-openalex-non-latin")

crossref["train"], crossref["validation"], crossref["test"]
```

## Dataset structure

All subsets share the same schema. Each split is a JSON Lines file where every
record has two fields:

| Field | Type | Description |
| --- | --- | --- |
| `affiliation_string` | string | The raw, unnormalized affiliation string as it appears in the source. |
| `ror_ids` | list of string | Matching ROR IDs as full URLs (`https://ror.org/...`). May be empty in the `crossref`, `datacite`, and `synth-openalex` subsets (see below). |

Example:

```json
{"affiliation_string": "School of Sport and Exercise Sciences Swansea University Swansea UK", "ror_ids": ["https://ror.org/053fq8t95"]}
```

## `crossref` subset

Crossref-derived affiliation strings (from a 2024-02-19 snapshot) paired with the
ROR IDs they resolve to. Unlike `affrodb`, this subset **includes unmatched
records**: a record whose `ror_ids` is an empty list (`[]`) represents an
affiliation with no assigned ROR organization. These rows are retained so the
subset can also be used to evaluate no-match / abstention behavior.

| Split | Records | Empty `ror_ids` | Multi-ROR records | Total ROR refs | Avg ROR/matched |
| --- | --- | --- | --- | --- | --- |
| train | 2,400 | 384 | 180 | 2,241 | 1.11 |
| validation | 300 | 52 | 21 | 277 | 1.12 |
| test | 300 | 47 | 22 | 277 | 1.09 |
| total | 3,000 | 483 | 223 | 2,795 | 1.11 |

All 3,000 affiliation strings are unique, so no affiliation appears in more than
one split.

### Label construction

Labels are the ROR IDs supplied by the source Crossref-derived dataset, taken
as-is with order-preserving de-duplication. HTML character entities in the
affiliation strings (e.g. `&#x0026;`) were decoded to their literal characters.
No `exact`/`ancestor` distinction is made.

## `affrodb` subset

A reformatted, split version of AffRoDB (see source and citation below). Every
record has at least one ROR match, so there are no empty-label rows.

| Split | Records | Multi-ROR records | Total ROR refs | Avg ROR/record |
| --- | --- | --- | --- | --- |
| train | 1,099 | 64 | 1,175 | 1.07 |
| validation | 137 | 14 | 157 | 1.15 |
| test | 138 | 11 | 152 | 1.10 |
| total | 1,374 | 89 | 1,484 | 1.08 |

All 1,374 affiliation strings are unique, so no affiliation appears in more than
one split.

### Label construction

Labels come from the `final_judgment` field of the source data, which records
expert decisions about which organizations an affiliation refers to. The source
distinguishes two match types:

- `exact`: the affiliation directly names this organization.
- `ancestor`: the affiliation names a sub-unit, and this is a parent or ancestor
  organization in ROR.

Here the two types are collapsed into a single `ror_ids` list and treated as
equally required matches. The `exact` entries are listed first, then `ancestor`,
with order-preserving de-duplication. In the source, 360 records carried an
`exact` match, 1,040 carried an `ancestor` match, and 26 carried both. The
`exact` and `ancestor` sets never overlapped within a record.

## `datacite` subset

A sample of unique affiliation strings drawn from the July 2026 DataCite corpus.
Each record was independently re-annotated against the affiliation-linking
rubric and the ROR v2 registry: all explicitly mentioned organizations with ROR
records are included, unmentioned parents are not inferred, and historical or
withdrawn records are resolved to their current ROR entity. Empty `ror_ids`
represent affiliations for which no explicitly named organization could be
linked to ROR.

| Split | Records | Empty `ror_ids` | Multi-ROR records | Total ROR refs | Avg ROR/matched |
| --- | --- | --- | --- | --- | --- |
| train | 3,778 | 1,806 | 314 | 2,402 | 1.22 |
| validation | 472 | 242 | 30 | 277 | 1.20 |
| test | 473 | 221 | 27 | 292 | 1.16 |
| total | 4,723 | 2,269 | 371 | 2,971 | 1.21 |

All 4,723 affiliation strings are unique, so no affiliation appears in more than
one split. The source reannotation file has SHA-256
`9b6887696ad421c950eebda6181e7a29e026f2b542f4e55747df2744633533c8`.
The deterministic split assignment digest is
`8d9942764a941d53850e599aef49b300371059ac5080499536e0caf77f6fcc45`.

### Label construction

The source annotations were produced by a ROR matching agent and then reviewed
one affiliation per agent under a shared rubric. Final records preserve the raw
DataCite affiliation string and contain ordered, de-duplicated full ROR URLs.
The reannotation verified 4,026 source label lists and revised 697; the final
subset contains 2,269 no-match records. All unique output IDs were checked
against ROR v2, with withdrawn records excluded and successors followed where
available.

## `synth-openalex` subset

Fully synthetic affiliation strings generated by an LLM from ROR registry
records, with target organizations sampled so that their frequency follows the
distribution of works across ROR-affiliated organizations in OpenAlex (highly
published organizations appear proportionally more often). Labels were assigned
in a separate LLM re-annotation pass over the generated strings; records where
that pass assigned no ROR ID are retained as no-match rows (`ror_ids: []`).

| Split | Records | Empty `ror_ids` | Multi-ROR records | Total ROR refs | Avg ROR/matched |
| --- | --- | --- | --- | --- | --- |
| train | 2,400 | 51 | 822 | 3,320 | 1.41 |
| validation | 300 | 5 | 103 | 419 | 1.42 |
| test | 300 | 4 | 100 | 416 | 1.41 |
| total | 3,000 | 60 | 1,025 | 4,155 | 1.41 |

All 3,000 affiliation strings are unique, so no affiliation appears in more than
one split.

## `synth-openalex-hardened` subset

Synthetic affiliation strings from the same OpenAlex-distributed generation
pipeline, each iteratively edited ("hardened") until the ROR affiliation
matching service no longer retrieves the target organization, while an
independent blind-model check confirms the target remains unambiguously
recoverable from a non-acronym surface form (a name or alias span carried in
the string). The subset therefore stresses matchers beyond exact lexical
retrieval. Every record has at least one target, so there are no empty-label
rows.

| Split | Records | Multi-ROR records | Total ROR refs | Avg ROR/record |
| --- | --- | --- | --- | --- |
| train | 2,400 | 572 | 2,992 | 1.25 |
| validation | 300 | 69 | 370 | 1.23 |
| test | 300 | 64 | 368 | 1.23 |
| total | 3,000 | 705 | 3,730 | 1.24 |

All 3,000 affiliation strings are unique, so no affiliation appears in more than
one split.

## `synth-openalex-non-latin` subset

Synthetic affiliation strings from the same OpenAlex-distributed generation
pipeline, written in the native non-Latin script and language of the target
organization's country and styled after per-language profiles derived from real
affiliation strings (e.g. omitting the country name where native strings
typically do). The sample covers 38 languages across 24 scripts, dominated by
Chinese, Japanese, Russian, Arabic, Korean, and Hindi. Every record has at
least one target, so there are no empty-label rows.

| Split | Records | Multi-ROR records | Total ROR refs | Avg ROR/record |
| --- | --- | --- | --- | --- |
| train | 2,400 | 269 | 2,675 | 1.11 |
| validation | 300 | 42 | 344 | 1.15 |
| test | 300 | 31 | 332 | 1.11 |
| total | 3,000 | 342 | 3,351 | 1.12 |

All 3,000 affiliation strings are unique, so no affiliation appears in more than
one split.

### Provenance of the synthetic subsets

The three `synth-openalex*` subsets are distributed here with only the two
schema fields. The source files additionally record full generation provenance
per record (generation and review models, reviewer verdicts, hardness-check
outcomes, and recoverability judgments), which was stripped for this
distribution.

## Construction details

The `crossref`, `affrodb`, and `datacite` subsets were shuffled with a fixed
seed (`random.Random(42)`) and divided 80/10/10 into train, validation, and
test. For `datacite`, the source field `affiliation` was renamed to
`affiliation_string`; affiliation text and ordered `ror_ids` values were
otherwise preserved.

The `make_splits.py` script in this repo reproduces the splits exactly using only
the Python standard library. It reads either the raw AffRoDB source (downloaded
from Zenodo or supplied locally) or an already-converted
`{affiliation_string, ror_ids}` JSONL file, and writes the three splits:

```bash
# affrodb: download the AffRoDB source from Zenodo, then write the splits.
python make_splits.py --download --output-dir affrodb

# crossref (or any pre-converted file): split a local {affiliation_string, ror_ids} JSONL.
python make_splits.py crossref.jsonl --output-dir crossref

# datacite: the splitter accepts its {affiliation, ror_ids} source shape directly.
python make_splits.py datacite.jsonl --output-dir datacite
```

Run `python make_splits.py --help` for the ratio and seed options.

The three `synth-openalex*` subsets were each drawn from a larger synthetic
source file (6,327 / 5,902 / 4,138 records respectively): the source was
shuffled with `random.Random(42)`, the first 3,000 records were taken as the
sample, and the sample was sliced 80/10/10 into train/validation/test. Bare ROR
IDs in the sources were normalized to full `https://ror.org/` URLs and
provenance fields were dropped. The `make_synth_splits.py` script in this repo
reproduces this exactly:

```bash
python make_synth_splits.py source.jsonl --output-dir synth-openalex --sample-size 3000
```

## Source and citation

The `affrodb` subset is derived from AffRoDB, redistributed under CC0 1.0. If you
use it, please cite the original work:

Kallipoliti, M., Chatzopoulos, S., & Vergoulis, T. (2025). AffRoDB: Curated
Mappings of affiliation strings to ROR identifiers (Version 1.0) [Dataset].
Zenodo. https://doi.org/10.5281/zenodo.15322097

```bibtex
@misc{kallipoliti_2025_affrodb,
  author    = {Kallipoliti, Myrto and Chatzopoulos, Serafeim and Vergoulis, Thanasis},
  title     = {AffRoDB: Curated Mappings of affiliation strings to ROR identifiers},
  year      = {2025},
  version   = {1.0},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.15322097},
  url       = {https://doi.org/10.5281/zenodo.15322097}
}
```

The `crossref` subset is built from Crossref affiliation metadata (CC0) labeled
with ROR identifiers (CC0).

The `datacite` subset is derived from unique affiliation strings in the July
2026 DataCite corpus. DataCite metadata is distributed under CC0; the ROR
identifiers and registry metadata used during reannotation are also CC0.
