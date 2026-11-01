---
pretty_name: mGENRE title trie + Wikidata QID lookup + QID attributes + QID labels (impresso NEL assets)
license: cc-by-nc-4.0
language:
  - multilingual
  - af
  - am
  - ar
  - as
  - az
  - be
  - bg
  - bm
  - bn
  - br
  - bs
  - ca
  - cs
  - cy
  - da
  - de
  - el
  - en
  - eo
  - es
  - et
  - eu
  - fa
  - ff
  - fi
  - fr
  - fy
  - ga
  - gd
  - gl
  - gn
  - gu
  - ha
  - he
  - hi
  - hr
  - ht
  - hu
  - hy
  - id
  - ig
  - is
  - it
  - ja
  - jv
  - ka
  - kg
  - kk
  - km
  - kn
  - ko
  - ku
  - ky
  - la
  - lg
  - ln
  - lo
  - lt
  - lv
  - mg
  - mk
  - ml
  - mn
  - mr
  - ms
  - my
  - ne
  - nl
  - no
  - om
  - or
  - pa
  - pl
  - ps
  - pt
  - qu
  - ro
  - ru
  - sa
  - sd
  - si
  - sk
  - sl
  - so
  - sq
  - sr
  - ss
  - su
  - sv
  - sw
  - ta
  - te
  - th
  - ti
  - tl
  - tn
  - tr
  - uk
  - ur
  - uz
  - vi
  - wo
  - xh
  - yo
  - zh
task_categories:
  - text-retrieval
tags:
  - entity-linking
  - named-entity-linking
  - entity-disambiguation
  - text2text-generation
  - mgenre
  - marisa-trie
  - wikidata
  - constrained-decoding
  - impresso
size_categories:
  - 10M<n<100M
viewer: false
---

# mGENRE title trie + Wikidata QID lookup — impresso NEL assets

Five [`marisa-trie`](https://github.com/s-yata/marisa-trie) native binaries that
support **multilingual entity linking with mGENRE**. They are the runtime assets
for the [`impresso-project/nel-mgenre-multilingual`](https://huggingface.co/impresso-project/nel-mgenre-multilingual)
model as run by the [`impresso-inference`](https://github.com/impresso/impresso-inference)
harness:

- a **title prefix tree** that constrains beam search to valid Wikipedia titles,
- a **`(language, title) → Wikidata QID` lookup** for offline QID resolution — GENRE's
  original, and a copy with every QID merged on Wikidata since replaced by its current
  target (the one used at inference),
- a **`QID → (facets, birthdate)` attribute table** for offline post-linking filters
  (disambiguation / name-page drop, birthdate anachronism, type mismatch, entity-type
  repair), and
- a **`QID → labels` table** (French / English / German Wikidata labels) to enrich
  linked entities with human-readable names.

All are mmap-loaded at startup, so cold start is **seconds regardless of file
size** (the legacy pickle path took ~57 min).

## Files

| File | Size | Format | Role |
|---|---|---|---|
| `titles_lang_all105_marisa_trie_with_redirect.marisa` | ~600 MB | `marisa_trie.Trie` (native `.save`/`.mmap`) | Prefix tree of valid `Title >> lang` token-id sequences (105 languages, redirects included). Drives constrained beam search via a `prefix_allowed_tokens_fn` callback. |
| `lang_title2wikidataID-normalized_with_redirect.marisa` | ~850 MB | `marisa_trie.BytesTrie` | Raw conversion of GENRE's lookup: `f"{lang}\x1f{title}"` → the lex-smallest Wikidata QID (ASCII), as of the ~2020 GENRE snapshot. Input of the resolved lookup below; not read at inference. |
| `lang_title2wikidataID.qid-resolved.marisa` | ~850 MB | `marisa_trie.BytesTrie` | Same keys; every QID merged on Wikidata since the GENRE snapshot replaced by its current target. Resolves generated titles to QIDs offline. |
| `qid2attrs.v2.marisa` | ~80 MB | `marisa_trie.RecordTrie` (fmt `"<HI"`) | Maps each Wikidata `QID` → `(facet_flags, birth_days)`. Per-QID attributes for offline post-linking filters. Supersedes `qid2attrs.marisa` (v1, `"<BI"` single class code), kept for older releases. |
| `qid2labels.marisa` | a few hundred MB | `marisa_trie.BytesTrie` | Maps each Wikidata `QID` → its packed `fr` / `en` / `de` labels (+ one fallback label). Per-QID names for output enrichment. |

The three GENRE-derived files hold **~89 million keys** each (`all105` = the 105
languages of the underlying mBART-50 / mGENRE vocabulary); `qid2attrs.v2.marisa` holds
**~20.2 million keys** — one per distinct QID reachable through the lookup — and
`qid2labels.marisa` one per such QID that still has a label on Wikidata.

## Provenance & construction

These files are converted, byte-faithfully, from Facebook Research's **GENRE**
public downloads at `https://dl.fbaipublicfiles.com/GENRE/`:

- `titles_lang_all105_marisa_trie_with_redirect.pkl` (~582 MB) — a pickled
  GENRE `MarisaTrie` wrapper. Conversion extracts the inner `marisa_trie.Trie`
  and re-saves it as a bare native binary so it can be `mmap`-ed directly.
- `lang_title2wikidataID-normalized_with_redirect.pkl` (~3.9 GB) — a
  `dict[(lang, title), str | set[QID]]`. Conversion streams it into a
  `marisa_trie.BytesTrie`, collapsing multi-QID values to the **lex-smallest
  QID** at build time (so the runtime does a single trie lookup instead of an
  ~8-minute normalisation pass per launch).

The conversion is performed by the `impresso-nel-stage-assets` tool in
[`impresso-inference`](https://github.com/impresso/impresso-inference)
(`src/impresso_inference/tasks/nel/cli/stage_assets.py`). Nothing about the entity
inventory is added or removed — this is a **format/packaging re-host** of the
GENRE data for fast startup.

### Resolved lookup (`lang_title2wikidataID.qid-resolved.marisa`)

About 2.8 % of the GENRE lookup's distinct QIDs (1.2 % of its keys) have since been **merged** into another
Wikidata item; the old id survives only as an `owl:sameAs` redirect, with no class,
birthdate or label. The `impresso-nel-stage-lookup` tool
(`src/impresso_inference/tasks/nel/cli/stage_lookup.py`) asks the
[QLever](https://qlever.dev/api/wikidata) Wikidata endpoint for those redirects (batched
`?item owl:sameAs ?target`), follows chains (up to 5 hops; a cycle leaves the QID as is),
and rewrites each merged value to its current target. Keys are unchanged; QIDs deleted
outright are kept as they are. The build is rejected if the key count changes, if a
sampled value is still a redirect, or if more than 10 % of keys would be rewritten.
The attribute and label tables below are built from this file, so they are keyed by
current QIDs only.

### QID attributes (`qid2attrs.v2.marisa`)

Unlike the two files above, `qid2attrs.v2.marisa` is **not** derived from GENRE — it is
built from **Wikidata** so that post-linking filters run fully offline (no live
Wikidata/Wikipedia HTTP calls). It is keyed by Wikidata QID and each value is a
fixed 6-byte record (`marisa_trie.RecordTrie`, struct format `"<HI"`), plus one
non-QID row `__format__` → `(2, 0)` identifying the layout:

| Field | Type | Meaning |
|---|---|---|
| `facet_flags` | `uint16` (`H`) | Bitmask of every facet the QID reaches (a QID can have several): bit 0 `pers`, 1 `org`, 2 `loc`, 3 `disambig`, 4 `name` (given/family name), 5 `periodical`, 6 `doctr` (religious text / law / treaty), 7 `time_cal` (year, century, decade, millennium, calendar day, weekday, holiday), 8 `period_event` (time interval / occurrence), 9 `vehicle`, 10 `taxon`. Bits 11–15 unused. |
| `birth_days` | `uint32` (`I`) | Earliest date of birth as **days since `0001-01-01`** (proleptic Gregorian); always `>= 0`. Sentinel `2147483648` (`2**31`) means *no/unusable birthdate* (absent, BCE, or imprecise). |

**Construction** — by the `impresso-nel-stage-qid-attrs` tool
(`src/impresso_inference/tasks/nel/cli/stage_qid_attrs.py`):

1. Enumerate the **linkable universe** = the distinct QID *values* of
   `lang_title2wikidataID.qid-resolved.marisa` (the only QIDs mGENRE can emit).
2. Pull attributes from the [QLever](https://qlever.dev/api/wikidata) Wikidata endpoint,
   in batches of 10,000 QIDs (`VALUES ?item`; each query stays under the public
   instance's 30 s limit, and a truncated result aborts the build):
   - **facets** via `wdt:P31/wdt:P279*` (or direct `wdt:P31`) against fixed roots —
     person `wd:Q5`; organization `wd:Q43229`; location `wd:Q27096213` + `wd:Q42124`;
     disambiguation pages via direct `wdt:P31` on the six page types (incl. human-name
     `wd:Q22808320` and surname `wd:Q66480449`); name `wd:Q202444` + `wd:Q101352`;
     periodical `wd:Q1002697`; doctrine `wd:Q179461` + `wd:Q7748` + `wd:Q131569`;
     calendar `wd:Q577` + `wd:Q578` + `wd:Q39911` + `wd:Q36507` + `wd:Q14795564` (+ direct
     `wd:Q41825`); period/event `wd:Q186081` + `wd:Q1190554`; vehicle `wd:Q42889`;
     taxon direct `wd:Q16521`;
   - **birthdate** via the earliest `wdt:P569` (conservative: only the earliest claim).
3. Pack one record per linkable QID.

**Role.** In `impresso-inference` the NEL writer looks up each linked QID here to drop
links that cannot be right — **disambiguation pages**, a person linked to a **name**
item, a person **born after** the article's publication date, and links whose QID is
**incompatible** with the mention's entity type (a date linked to a place, a newspaper
title linked to its city) — and to **repair** pers/org/loc entity types (e.g. an
`org`-tagged mention whose QID is a location).

### QID labels (`qid2labels.marisa`)

Also built from **Wikidata** (via QLever), keyed by the same linkable QIDs. Each value is
the UTF-8 string of **5 fields separated by `\x1f`** (an empty field = absent):

| # | Field | Meaning |
|---|---|---|
| 1 | `label_fr` | French label, else the item's `mul` label, else empty |
| 2 | `label_en` | English label, else `mul`, else empty |
| 3 | `label_de` | German label, else `mul`, else empty |
| 4 | `label_other` | Set **only when fields 1–3 are all empty**: the label in the item's own language |
| 5 | `label_other_lg` | Language code of `label_other` (e.g. `ja`, `lb`, `ru`) |

**Fallback rules.** `mul` is Wikidata's "default for all languages" label (introduced in
2024; many items now carry a name only there). A language field **never** takes another
language's label — only its own or `mul`. `label_other` is the label in a language whose
Wikipedia title maps to the QID in the lookup above (smallest code if several), else the
smallest language code with a label. QIDs with **no label at all** — in practice items
deleted on Wikidata since the GENRE snapshot (merged ones are already resolved) — are
**not stored**; a lookup miss means "no label".

**Coverage** (estimate from a 20,000-QID sample of the linkable set, batched build of
2026-10-02; refreshed on the full build): `label_fr` 74 %, `label_en` 91 %, `label_de` 70 %
(each incl. ~1.5–3 % filled from `mul`); `label_other` on ~8 %; ~1.5 % with no label.

**Construction** — by the `impresso-nel-stage-qid-labels` tool
(`src/impresso_inference/tasks/nel/cli/stage_qid_labels.py`): `rdfs:label` queries in
batches of 10,000 linkable QIDs (`VALUES ?item`, languages `fr`, `en`, `de`, `mul`); then
batched queries for all labels of the QIDs still empty, to pick `label_other`. Each query
stays under QLever's 30 s limit, a truncated result aborts the build, and the build is
rejected if fr/en/de coverage falls below 40 / 70 / 35 %.

> **Note (2026-10-02).** The first `qid2labels.marisa` published here (2026-10-01) was
> **truncated** (en ~15 % coverage) by QLever's 30 s limit, and is replaced by the
> batched rebuild.

**Wikidata snapshot.** The resolved lookup, `qid2attrs.v2.marisa` and `qid2labels.marisa` reflect the QLever
Wikidata index at the time they were built — see each file's commit date in this repo.

## Rebuild

Each file has exactly one build step, one console script, and one `make` target in
[`impresso-inference`](https://github.com/impresso/impresso-inference):

| Step | Console script | `make` target (CPU-only RCP pod) | Builds | Needs |
|---|---|---|---|---|
| 1 | `impresso-nel-stage-assets` | `runai-stage-nel-assets` | trie + GENRE lookup | GENRE downloads |
| 1b | `impresso-nel-stage-lookup` | `runai-stage-nel-lookup` | resolved lookup | step-1 lookup + QLever |
| 2a | `impresso-nel-stage-qid-attrs` | `runai-stage-nel-qid-attrs` | `qid2attrs.v2.marisa` | step-1b lookup + QLever |
| 2b | `impresso-nel-stage-qid-labels` | `runai-stage-nel-qid-labels` | `qid2labels.marisa` | step-1b lookup + QLever |
| all | — | `runai-stage-nel-all` | everything, 1 → 1b → 2b → 2a | — |

Steps 2a and 2b are independent of each other; rebuild them whenever 1b is rebuilt. Every tool skips an existing output
(`--force` to rebuild), supports a quick `--limit N` dry run, and uploads with `--push`.

## Intended use

Pair with `impresso-project/nel-mgenre-multilingual` (mGENRE, an mBART-50
sequence-to-sequence entity linker). mGENRE emits strings of the form
`"Wikipedia_Title >> xx"`:

- The **trie** restricts generation to valid titles at every decoder step
  (prevents hallucinated pages).
- The **lookup** turns the generated `(title, lang)` into a Wikidata QID without
  any live Wikipedia/Wikidata HTTP calls — suitable for offline / batch inference.
- The **attributes** drive offline post-linking filters; the **labels** give each linked
  entity its French / English / German name (`label_fr` / `label_en` / `label_de`).

In `impresso-inference`, the NEL task auto-downloads whichever runtime file is missing
from this dataset on first launch (`qid2labels.marisa` is staged ahead of its runtime
use in the NEL writer). See that repo's
`src/impresso_inference/tasks/nel/` for the full pipeline.

## How to load

```python
import marisa_trie

# Title trie — constrained decoding
trie = marisa_trie.Trie()
trie.mmap("titles_lang_all105_marisa_trie_with_redirect.marisa")

# (lang, title) -> QID lookup
lookup = marisa_trie.BytesTrie()
lookup.mmap("lang_title2wikidataID.qid-resolved.marisa")
qid = lookup[f"en\x1fGermany"][0].decode("ascii")   # -> "Q183"

# QID -> (facets, birthdate) attributes
from datetime import date, timedelta
FACETS = ["pers", "org", "loc", "disambig", "name", "periodical", "doctr",
          "time_cal", "period_event", "vehicle", "taxon"]   # bit i = FACETS[i]
BIRTH_NONE, EPOCH = 2**31, date(1, 1, 1)
attrs = marisa_trie.RecordTrie("<HI")
attrs.mmap("qid2attrs.v2.marisa")
flags, birth_days = attrs["Q42"][0]                 # Douglas Adams
facets = [f for i, f in enumerate(FACETS) if flags >> i & 1]   # -> ["pers"]
birth = None if birth_days == BIRTH_NONE else EPOCH + timedelta(days=birth_days)  # -> 1952-03-11

# QID -> labels (5 fields, "" = absent)
labels = marisa_trie.BytesTrie()
labels.mmap("qid2labels.marisa")
hit = labels.get("Q183")                             # None if the QID has no label
fr, en, de, other, other_lg = hit[0].decode("utf-8").split("\x1f")
# -> "Allemagne", "Germany", "Deutschland", "", ""
```

**Token-id encoding (trie only).** marisa-trie stores keys as UTF-8 strings, so
mGENRE token ids are encoded per character as `chr(t)` for `t < 55000` and
`chr(t + 10000)` otherwise — a 10 000-codepoint shift that skips the UTF-16
surrogate range. This matches the upstream GENRE byte layout; any consumer of the
trie must apply the same shift when decoding allowed-token sets. Keys are
`Title >> lang` token sequences.

## Licensing

Released under **CC BY-NC 4.0 (non-commercial)**, inherited from the upstream
[facebookresearch/GENRE](https://github.com/facebookresearch/GENRE) data the trie and
lookup are derived from. The underlying knowledge base is public: Wikidata
identifiers are **CC0**, and Wikipedia titles are **CC BY-SA**. Use for
non-commercial research consistent with the GENRE license.

`qid2attrs.v2.marisa` and `qid2labels.marisa` contain only **Wikidata data** (`P31`/`P279`/
`P569`, `rdfs:label`), which is **CC0**; their QID selection follows the GENRE-derived
lookup above, so they are distributed here under the same non-commercial terms for
consistency.

## Citation

The trie and lookup originate from mGENRE:

```bibtex
@article{de-cao-etal-2022-multilingual,
  title   = "Multilingual Autoregressive Entity Linking",
  author  = "De Cao, Nicola and Wu, Ledell and Popat, Kashyap and Artetxe, Mikel
             and Goyal, Naman and Plekhanov, Mikhail and Zettlemoyer, Luke and
             Cancedda, Nicola and Riedel, Sebastian and Petroni, Fabio",
  journal = "Transactions of the Association for Computational Linguistics",
  volume  = "10",
  year    = "2022",
  address = "Cambridge, MA",
  publisher = "MIT Press",
  url     = "https://aclanthology.org/2022.tacl-1.16",
  doi     = "10.1162/tacl_a_00460",
  pages   = "274--290"
}
```

## Acknowledgements

Repackaged for historical-newspaper entity linking by the
[Impresso project](https://impresso-project.ch) — an interdisciplinary effort on
historical media analysis across languages, time, and modalities. Funded by the
Swiss National Science Foundation ([CRSII5_173719](http://p3.snf.ch/project-173719),
[CRSII5_213585](https://data.snf.ch/grants/grant/213585)) and the Luxembourg
National Research Fund (grant No. 17498891).

- Model: [`impresso-project/nel-mgenre-multilingual`](https://huggingface.co/impresso-project/nel-mgenre-multilingual)
- Code: [`impresso/impresso-inference`](https://github.com/impresso/impresso-inference)
- Upstream data: [facebookresearch/GENRE](https://github.com/facebookresearch/GENRE)
