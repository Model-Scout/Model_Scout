---
# Both the MIT- and Apache-2.0-derived subsets are permissive and allow
# inclusion in a differently-licensed compilation, provided their notices are
# retained -- that retention is the NOTICE file shipped beside this card. CC BY
# 4.0 governs the COMPILATION; it does not relicense the contributed parts.
license: cc-by-4.0
language:
  - am
  - ar
  - bn
  - bs
  - ca
  - cs
  - cy
  - da
  - de
  - el
  - en
  - es
  - fa
  - fi
  - fil
  - fr
  - ga
  - gd
  - gl
  - gu
  - he
  - hi
  - hr
  - hu
  - id
  - it
  - ja
  - kn
  - ko
  - lv
  - mk
  - ml
  - mn
  - ms
  - my
  - nb
  - ne
  - nl
  - pl
  - pt
  - ro
  - ru
  - si
  - sr
  - su
  - sv
  - sw
  - te
  - th
  - tr
  - uk
  - ur
  - uz
  - vi
  - xh
  - zh
configs:
  - config_name: concepts
    data_files:
      - split: train
        path: data/concepts.parquet
  - config_name: terms
    data_files:
      - split: train
        path: data/terms.parquet
  - config_name: options
    data_files:
      - split: train
        path: data/options.parquet
  - config_name: endorsements
    data_files:
      - split: train
        path: data/endorsements.parquet
  - config_name: contributors
    data_files:
      - split: train
        path: data/contributors.parquet
---

# Legesher language corpus

![Legesher language corpus](assets/language-corpus-card.png)

## What this corpus is

A concept-centric corpus of reserved-word translations for programming
languages: every candidate rendering ("option") of a programming-language
concept in a human locale that anyone -- Legesher, another open-source project,
a community reviewer, or a model -- ever offered, together with every
endorsement a person attached to it.

This is a **growing dataset**, and append-only by design. New locales, new
concepts, new renderings, and new endorsements arrive with each release, and
nothing already published is rewritten in place: a rendering that is superseded
stays, with its replacement recorded alongside it. Treat a revision as a
snapshot of the evidence to date, not as a finished vocabulary.

Options are keyed by content-addressed, stable uids (`opt_` + 24 hex), so the
corpus survives database rebuilds and re-exports byte-identically -- an
`option_uid` you pin today means the same rendering in every later revision.

Locales ride on `options.locale` as canonical-case BCP 47 tags; there is no
separate locales config.

## Languages

All 56 locales carried by `options.locale` in this export, as BCP 47 tag
followed by language name. The primary-subtag rollup in the frontmatter above
is what the Hub indexes for search; this is the full list, script subtags and
all.

`am` Amharic · `ar` Arabic · `bn` Bengali · `bs` Bosnian · `ca` Catalan ·
`cs` Czech · `cy` Welsh · `da` Danish · `de` German · `el` Greek ·
`en` English · `es` Spanish · `fa` Persian · `fi` Finnish · `fil` Tagalog ·
`fr` French · `ga` Irish · `gd` Scottish Gaelic · `gl` Galician ·
`gu` Gujarati · `he` Hebrew · `hi` Hindi · `hr` Croatian · `hu` Hungarian ·
`id` Indonesian · `it` Italian · `ja` Japanese · `kn` Kannada · `ko` Korean ·
`lv` Latvian · `mk` Macedonian · `ml` Malayalam · `mn-Cyrl` Mongolian ·
`ms` Malay · `my` Burmese · `nb` Norwegian · `ne` Nepali · `nl` Dutch ·
`pl` Polish · `pt` Portuguese · `ro` Romanian · `ru` Russian · `si` Sinhala ·
`sr-Cyrl` Serbian · `su` Sundanese · `sv` Swedish · `sw` Swahili ·
`te` Telugu · `th` Thai · `tr` Turkish · `uk` Ukrainian · `ur` Urdu ·
`uz-Latn` Uzbek · `vi` Vietnamese · `xh` Xhosa · `zh-Hans` Chinese

## Configs

Five configs. Load one with
`load_dataset("legesher/language-corpus", "options")`.

| Config | One row is | Columns |
| --- | --- | --- |
| `concepts` | A programming-language concept, independent of any human language | `slug` (the public, frozen key), `definition_en`, `definition_source`, `category`, `pattern_class`, `notes`, `created_at`, `updated_at` |
| `terms` | That concept's surface form in one programming language | `concept_slug`, `programming_language`, `name`, `category`, `subcategory`, `version_added`, `version_removed`, `usage_note`, `doc_url`, `export_role`, `created_at`, `updated_at` |
| `options` | One candidate rendering of one concept in one locale — the heart of the corpus | `option_uid`, `concept_slug`, `locale`, `programming_language`, `pl_scope`, `surface_form`, `first_seen_at`, `withdrawn_at`, `sources`; plus the cached validation verdict `identifier_valid`, `nfkc_stable`, `script_consistent`, `collides_en_keyword`, `min_interpreter_ok`, `validator_version`, `checked_at` (all null when a rendering has not been validated) |
| `endorsements` | One endorsement event: a person standing behind a rendering | `uid`, `option_uid`, `contributor_id`, `method`, `rung_at_endorsement`, `created_at`, `retracted_at` |
| `contributors` | A reviewer, as an opaque token | `id` (`c_` + 16 hex), `current_rung`, `joined_at` |

An option's endorsement count is `COUNT(*)` over its `endorsements` rows with
`retracted_at IS NULL`; no config ships a precomputed count column.

## Where each rendering came from

The single most important column here is `options.sources`, a list saying what
kinds of source attested that rendering. The vocabulary is cut on one question
-- *what do we owe for this?* -- so four values, four obligations:

| `sources` value | What it means | What we owe |
| --- | --- | --- |
| `legesher` | Produced by the Legesher project: our own packs, curated corrections, values we composed from existing pack material | nothing beyond this licence |
| `upstream` | Lifted from another open-source project | that project's notice and credit -- see [Upstream projects](#upstream-projects) |
| `community` | Offered or attested by an individual through our native-review process | credit on request, withdrawal on request -- see [Community contributions](#community-contributions) |
| `model` | Generated by a language model | disclosure of which model -- see [Machine-generated renderings](#machine-generated-renderings) |

An option can carry more than one value: the same rendering is often proposed
by a model and then independently attested by a reviewer. `sources` says who
offered a rendering, never how good it is -- standing comes only from the
`endorsements` rows recorded against it.

Row-level detail beyond these four values is deliberately not published: the
finer-grained provenance field carries reviewer labels that identify people,
and no part of this dataset is a route from an opaque contributor id back to a
person. That is also why the upstream project names live in this card rather
than in a column -- the obligation is machine-visible (`upstream`), the
identity of the upstream project is human-readable here.

## Upstream projects

This section and the three that follow walk the `sources` vocabulary in the
order the work actually happened. Other people rendered these concepts before
we did, and `upstream` is where their work enters the corpus — under their own
licence, with their notice retained.

| Project | Licence | What we pulled | Details |
| --- | --- | --- | --- |
| [legesher-translations](https://github.com/legesher/legesher-translations) | [MIT](https://github.com/legesher/legesher-translations/blob/main/LICENSE.md) | Reserved-word renderings — the original community translation set | A Legesher repository (`Copyright (c) 2019 Legesher`). Its 149 contributors are credited in [`.all-contributorsrc`](https://github.com/legesher/legesher-translations/blob/main/.all-contributorsrc), which stays the canonical roster |
| [UniversalPython](https://github.com/UniversalPython/UniversalPython) | [Apache-2.0](https://github.com/UniversalPython/UniversalPython/blob/main/LICENSE) | Urdu (`ur`) renderings | **Adapted, not reproduced verbatim** — normalised to our identifier conventions and re-keyed onto our concept slugs |
| [Latino](https://github.com/lenguaje-latino/latino) | [MIT](https://github.com/lenguaje-latino/latino/blob/master/LICENSE.txt) | Spanish (`es`) renderings | GitHub's licence API reports `NOASSERTION`; it could not classify the file's formatting, but the text itself is standard MIT |

Is there a dataset we should add? Open a discussion on
[this dataset](https://huggingface.co/datasets/legesher/language-corpus/discussions) -- if a
project has rendered these concepts in a language, we would rather credit it
than duplicate it.

## Legesher-produced renderings

Renderings marked `legesher` are the project's own work product, and they are
the bulk of the corpus. They arrive by three routes:

* **Language packs.** Terms authored for Legesher's per-locale language packs,
  written against the concept inventory (the `concepts` config) and its
  English definitions, then run through the pack pipeline's mechanical gates.
  Those per-row verdicts are not summarised away: they ship in this corpus as
  the validation columns on the `options` config, listed in
  [Configs](#configs), so a consumer can apply exactly the filters we do.
* **Curated corrections.** Fixes a maintainer made to an existing rendering
  -- a wrong form, a corrupted import, a style-guide violation. The corpus is
  append-only evidence, so the superseded rendering stays, and the correction
  enters as a new option alongside it.
* **Composed values.** Renderings a human assembled from existing pack
  material, for example compounding two already-attested words to cover a new
  concept. No model was asked; calling these `model` would overstate the
  machine's involvement, so they are `legesher`.

`legesher` describes who produced a rendering, not how good it is. That is the
division the whole corpus runs on: Legesher, the upstream projects, and the
models all **propose** — only the people in the next section **attest**. So a
Legesher-produced rendering carries exactly the native-speaker standing its
`endorsements` rows give it, and no more. Much of our own work sits here
waiting for that review rather than shipping as settled, and the corpus is
built to show you which is which.

## Community contributions

This is the other half of the section above. Renderings marked `community`
come from native speakers who reviewed our vocabulary — most often vocabulary
Legesher or an upstream project proposed — and their endorsements are what
turn a proposal into an attested rendering. A speaker can also offer a
rendering of their own, which is what makes `community` a source kind and not
only a review signal; either way the same rows carry it.

Each review is a recorded session in which a reviewer endorses, passes on, or
flags a rendering. Only endorsements appear here (the `endorsements` config),
and a reviewer's standing at the time rides on `rung_at_endorsement`.

Reviewers appear as opaque tokens, and a contributor may ask to be credited by
name or to be removed. Either request is honoured without losing the
endorsement itself, so the record of *what* was agreed survives a person's
decision about *whether to be named* — see [Privacy](#privacy).

The practical consequence for a consumer: join `options` to `endorsements` on
`option_uid` and you can separate what was proposed from what a native speaker
stood behind. That join, not the `sources` column, is the quality signal.

## Machine-generated renderings

Renderings marked `model` were produced by a language model:

| Model | Licence |
| --- | --- |
| [Aya 101](https://huggingface.co/CohereLabs/aya-101) (Cohere For AI) | Apache-2.0 |
| Claude (Anthropic) | outputs owned by the API customer |

Where the generating run recorded a specific model version it is retained in
the source database; the earliest machine-generated rows predate version
recording, so this card discloses the model family rather than promising a
per-row version.

They are a starting point, not an endorsement. A machine-generated rendering
carries no native-speaker attestation until one is recorded against it -- which
is what the `endorsements` config is for, and why packs built from this corpus
ship labelled experimental. Values a human composed from existing pack
material are `legesher`, not `model` -- see "Legesher-produced renderings"
above.

## Licence and attribution

This dataset is released under **CC BY 4.0**. You may share and adapt it,
including commercially, with attribution.

Part of it comes from other open-source projects that carry their own terms.
CC BY 4.0 governs the **compilation** and does not relicense the contributed
parts; each project's own licence is linked under
[Upstream projects](#upstream-projects), and the notices they ask us to retain
travel with the data in [`NOTICE`](NOTICE). Which obligation attaches to which
row is [`options.sources`](#where-each-rendering-came-from).

## Privacy

Contributors appear here only as opaque salted tokens -- never a name, email,
or handle -- and the mapping back to a person has never been part of any
published revision. Reviewer labels, the free text attached to an endorsement,
and moderation reports are all held back.

The full posture, including how withdrawal works, is [`PRIVACY.md`](PRIVACY.md)
beside this card.

