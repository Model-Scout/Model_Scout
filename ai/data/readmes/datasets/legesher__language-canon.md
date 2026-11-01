---
license: apache-2.0
tags:
  - multilingual
  - code
  - programming
  - localization
  - terminology
pretty_name: Legesher Language Canon
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
  - nl
  - pl
  - pt
  - ro
  - ru
  - si
  - sr
  - su
  - sv
  - te
  - th
  - tr
  - ur
  - uz
  - vi
  - zh
configs:
  - config_name: canon
    data_files:
      - split: train
        path: data/canon.parquet
  - config_name: locales
    data_files:
      - split: train
        path: data/locales.parquet
---

# Legesher language canon

![Legesher Language Canon](assets/language-canon-card.png)

## What this Canon is

A **centralized standard, created and curated by language communities**, for what
programming concepts are called in each natural language.

It holds language-specific renderings of programming keywords, builtins and
exceptions, and documents where each language stands in that process.

The language-canon builds on
[`legesher/language-corpus`](https://huggingface.co/datasets/legesher/language-corpus),
which gathers every rendering anyone has proposed. The corpus is the full
record of what has been suggested; the canon is the vocabulary that downstream
applications actually use.

Computer science as a global discipline is primarily based in English. A
developer who does not read English memorizes shapes rather than reading words
and connecting the terminology to related context. The hard part is not the
obvious vocabulary. It is the gray areas, where words are borrowed, created, or
derived from English (`elif` and `lambda` have no obvious answer in any
language), and settling them takes people who know a language's culture and the
stories woven into it, not only its grammar.

_Note: This is a **growing dataset**. A rendering here is the current answer,
not a final one, and each carries a rung recording how much review stands
behind it._

Renderings are keyed by content-addressed uids (`opt_` + 24 hex) shared with
the corpus, so an `option_uid` resolves there to every alternative proposed for
that concept and every endorsement attached to them.

## Languages

All 51 languages in this export, with where each one stands
on the maturity ladder. The primary-subtag rollup in the frontmatter is what
the Hub indexes for search; this is the full list, script subtags and all.

| Tag | Language | Native name | Status |
| --- | --- | --- | --- |
| `am` | Amharic | አማርኛ | `machine` |
| `ar` | Arabic | العربية | `experimental` |
| `bn` | Bengali | বাংলা | `experimental` |
| `bs` | Bosnian | Bosanski | `machine` |
| `ca` | Catalan | Català | `machine` |
| `cs` | Czech | Čeština | `machine` |
| `cy` | Welsh | Cymraeg | `machine` |
| `da` | Danish | Dansk | `machine` |
| `de` | German | Deutsch | `experimental` |
| `el` | Greek | Ελληνικά | `machine` |
| `en` | English | English | `machine` |
| `es` | Spanish | Español | `experimental` |
| `fa` | Persian | فارسی | `machine` |
| `fi` | Finnish | Suomi | `experimental` |
| `fr` | French | Français | `machine` |
| `ga` | Irish | Gaeilge | `machine` |
| `gd` | Scottish Gaelic | Gàidhlig | `machine` |
| `gl` | Galician | Galego | `machine` |
| `gu` | Gujarati | ગુજરાતી | `experimental` |
| `he` | Hebrew | עברית | `experimental` |
| `hi` | Hindi | हिन्दी | `experimental` |
| `hr` | Croatian | Hrvatski | `machine` |
| `hu` | Hungarian | Magyar | `machine` |
| `id` | Indonesian | Bahasa Indonesia | `experimental` |
| `it` | Italian | Italiano | `experimental` |
| `ja` | Japanese | 日本語 | `machine` |
| `kn` | Kannada | ಕನ್ನಡ | `machine` |
| `ko` | Korean | 한국어 | `machine` |
| `lv` | Latvian | Latviešu | `machine` |
| `mk` | Macedonian | Македонски | `machine` |
| `ml` | Malayalam | മലയാളം | `experimental` |
| `mn-Cyrl` | Mongolian | Монгол | `machine` |
| `ms` | Malay | Bahasa Melayu | `machine` |
| `my` | Burmese | မြန်မာ | `machine` |
| `nb` | Norwegian | Norsk | `machine` |
| `nl` | Dutch | Nederlands | `machine` |
| `pl` | Polish | Polski | `machine` |
| `pt` | Portuguese | Português | `experimental` |
| `ro` | Romanian | Română | `machine` |
| `ru` | Russian | Русский | `machine` |
| `si` | Sinhala | සිංහල | `machine` |
| `sr-Cyrl` | Serbian | Српски | `machine` |
| `su` | Sundanese | Basa Sunda | `machine` |
| `sv` | Swedish | Svenska | `machine` |
| `te` | Telugu | తెలుగు | `experimental` |
| `th` | Thai | ไทย | `machine` |
| `tr` | Turkish | Türkçe | `machine` |
| `ur` | Urdu | اردو | `experimental` |
| `uz-Latn` | Uzbek | O'zbek | `machine` |
| `vi` | Vietnamese | Tiếng Việt | `machine` |
| `zh-Hans` | Chinese | 中文 | `experimental` |

Today: **36** at `machine`, **15** at `experimental`.

The `locales` config carries the same list with the counts behind each status,
so you can sort and filter it rather than read it.

## The maturity ladder

Without other global examples to build from, each language's canon starts
drafted from machines and prior art. From there native speakers move it up:
`experimental`, then `reviewed`, then `official`. Once a language reaches
`official`, its canon becomes a resource for the community it exists to serve.

**The rung belongs to the language.** Each rendering carries its own so the
label stays auditable, but what you should read is the language's status: a
language is `experimental` while it is in progress, and `reviewed` or
`official` only once every one of its words has got there.

### `machine`

Drafted, not decided. The vocabulary came from a machine draft or from prior
art, and nobody has weighed in on any of it yet.

It is not arbitrary. Every rendering clears mechanical checks before it can be
selected: it has to be a valid identifier in its language, stable under the
Unicode normalization the interpreter applies, and free of collisions with
other terms in its vocabulary. What nobody has asked is whether it is the right
word — whether a programmer who speaks the language would recognise it.

Treat the whole vocabulary as a proposal.

### `experimental`

Review has begun. At least one word has been chosen or endorsed by a person —
a maintainer curating a batch, a native speaker correcting a term, or a
contributor putting their name behind a rendering someone else proposed.

Most of the endorsements here predate this dataset: they are the review history
of the community that built Legesher's original translations, where
contributors voted on renderings word by word. An endorsement attaches to the
specific option that was later selected, so it is evidence about *this word*,
not about the concept in general.

A language stays here for as long as the work is under way, however far along
it is. The `locales` config carries the counts if you want to know how far.

### `reviewed`

Every word has been signed off by several native speakers, so the vocabulary
reflects agreement rather than one person's preference.

The risk with a single reviewer is not that they are wrong. It is that they are
unrepresentative — a regional form, a register that reads formal or childish
elsewhere, a loanword one community has absorbed and another rejects. More than
one voice is what makes a vocabulary a shared answer.

How many voices, and how varied, is still being defined. We would rather say so
than publish a threshold we have not set.

### `official`

Ratified in a convened session, and screened.

Screening is separate from accuracy. A rendering can be a correct translation
and still be the wrong word to ship: offensive in another register, unfortunate
beside a neighbouring term, or colliding with something it should not. A status
of `official` means both questions were asked of the whole vocabulary and
answered by people with standing to answer them.

A language community makes this decision, not a threshold.

### Where things stand today

**36** at `machine`, **15** at `experimental`.

Review has begun in 15 languages, covering 505 of
9,375 renderings. No language has reached `reviewed`: that needs
every word signed off by more than one native speaker, and the threshold for
how many voices is still being defined.

We publish at this stage deliberately. A terminology set developed privately
and released once it is "ready" has already made every decision without the
people it is for. Publishing early makes the current state visible, citable
and arguable, while it is still genuinely open.

A language's status here describes its canon. It is not the same as the tier
of the language pack that ships from it.

## Configs

Two, joined on `locale`.

**`canon`** — one row per decision.

| Column | Meaning |
| --- | --- |
| `concept` | Language-neutral concept slug — what the construct *does* |
| `category` | Concept category: control flow, declaration, error handling, … |
| `locale` | BCP 47 language tag |
| `option_uid` | Content-addressed id of the chosen rendering; joins to the corpus |
| `surface_form` | The word itself |
| `status` | Rung on the maturity ladder |
| `identity_ok` | The rendering matches the English term **on purpose** |
| `decided_by` | Role that made the selection |
| `decided_at` | When the selection was made |

`identity_ok` marks a deliberate cognate or loanword — `stopiteration` in
Danish, `Lambda` in German. It does not mean "not translated yet"; without it
a reader could not tell a considered borrowing from an oversight.

**`locales`** — one row per language: `locale`, `language_name`,
`native_name`, `rtl`, `decisions`, a count at each rung, and
`native_reviewed`. Language attributes live only here, so a language is
described in exactly one place.

## Who decides, and how to take part

`decided_by` records the **role** that made a selection, never the person:
`automated` for migrations and batch jobs, `maintainer` for curation,
`native-reviewer` for a speaker of the language. Contributor identities are
not published in this dataset. Endorsements, attribution and withdrawal are
handled through
[`legesher/language-corpus`](https://huggingface.co/datasets/legesher/language-corpus),
which is the artifact that carries them.

The role answers a different question from the rung, and the two are
deliberately independent: `status` says **how much** review stands behind a
rendering, `decided_by` says **who** made the most recent call. A single
native reviewer is visible here without moving the rung, because their
judgement is real and is not yet a consensus.

This requires collaboration from people who do not just speak a language other
than English, but know its culture. If that is you, corrections, endorsements
and objections all move a rendering up the ladder, and disagreement is a
contribution rather than an obstacle.

## Licence and citation

Released under **Apache-2.0**. Legesher holds the compilation right in this
dataset and licenses it on those terms; the individual renderings arrive from
the corpus, whose own licence and attribution notices govern the contributed
parts.

```bibtex
@misc{legesher_language_canon,
  title  = {Legesher Language Canon},
  author = {Legesher},
  year   = {2026},
  howpublished = {\url{https://huggingface.co/datasets/legesher/language-canon}}
}
```
