---
license: apache-2.0
tags:
  - multilingual
  - code
  - programming
  - localization
task_categories:
  - translation
annotations_creators:
  - machine-generated
  - expert-generated
size_categories:
  - 10K<n<100K
pretty_name: Legesher Language Packs
language:
  - "am"
  - "ar"
  - "bn"
  - "bs"
  - "ca"
  - "cs"
  - "cy"
  - "da"
  - "de"
  - "el"
  - "en"
  - "es"
  - "fa"
  - "fi"
  - "fr"
  - "ga"
  - "gd"
  - "gl"
  - "gu"
  - "he"
  - "hi"
  - "hr"
  - "hu"
  - "id"
  - "it"
  - "ja"
  - "kn"
  - "ko"
  - "lv"
  - "mk"
  - "ml"
  - "mn"
  - "ms"
  - "my"
  - "ne"
  - "nl"
  - "no"
  - "pl"
  - "pt"
  - "ro"
  - "ru"
  - "si"
  - "sr"
  - "su"
  - "sv"
  - "sw"
  - "te"
  - "th"
  - "tl"
  - "tr"
  - "uk"
  - "ur"
  - "uz"
  - "vi"
  - "xh"
  - "zh"
configs:
  - config_name: vocabulary
    data_files:
      - split: train
        path: data/vocabulary.parquet
  - config_name: locales
    data_files:
      - split: train
        path: data/locales.parquet
  - config_name: pl_terminology
    data_files:
      - split: train
        path: data/pl_terminology.parquet
  - config_name: packs
    data_files:
      - split: train
        path: data/packs.parquet
---

# Legesher Language Packs

![Legesher language packs](assets/language-packs-card.png)

Legesher's language packs 📦 are the localization layer for code; the fixed
vocabulary of a programming language in other natural languages.

Every reserved word within a programming language's grammar (keywords,
builtins, exceptions, error messages) is compiled into a language pack that,
when utilized by Legesher, allows code to be in any language and it compiles
all the same.

| Release | Languages supported | Target | Versions | License | `legesher-i18n` | Commit |
| --- | --- | --- | --- | --- | --- | --- |
| `0.5.0` | 56 | `python` | `3.10`-`3.14` | Apache-2.0 | `0.23.0` | `0a17d02f32c7` |

## Languages

| Pack | Language | Native name | Status | Package |
| --- | --- | --- | --- | --- |
| `am` | Amharic | አማርኛ | `experimental` | `0.0.3` |
| `ar` | Arabic | العربية | `experimental` | `0.0.5` |
| `bn` | Bengali | বাংলা | `experimental` | `0.0.3` |
| `bs` | Bosnian | Bosanski | `experimental` | `0.0.3` |
| `ca` | Catalan | Català | `experimental` | `0.0.3` |
| `cs` | Czech | Čeština | `experimental` | `0.0.3` |
| `cy` | Welsh | Cymraeg | `experimental` | `0.0.3` |
| `da` | Danish | Dansk | `experimental` | `0.0.4` |
| `de` | German | Deutsch | `experimental` | `0.0.4` |
| `el` | Greek | Ελληνικά | `experimental` | `0.0.5` |
| `en` | English | English | `experimental` | `0.0.4` |
| `es` | Spanish | Español | `experimental` | `0.0.5` |
| `fa` | Persian | فارسی | `experimental` | `0.0.3` |
| `fi` | Finnish | Suomi | `experimental` | `0.0.5` |
| `fr` | French | Français | `experimental` | `0.0.4` |
| `ga` | Irish | Gaeilge | `experimental` | `0.0.3` |
| `gd` | Scottish Gaelic | Gàidhlig | `experimental` | `0.0.3` |
| `gl` | Galician | Galego | `experimental` | `0.0.3` |
| `gu` | Gujarati | ગુજરાતી | `experimental` | `0.0.3` |
| `he` | Hebrew | עברית | `experimental` | `0.0.5` |
| `hi` | Hindi | हिन्दी | `experimental` | `0.0.5` |
| `hr` | Croatian | Hrvatski | `experimental` | `0.0.3` |
| `hu` | Hungarian | Magyar | `experimental` | `0.0.5` |
| `id` | Indonesian | Bahasa Indonesia | `experimental` | `0.0.4` |
| `it` | Italian | Italiano | `experimental` | `0.0.5` |
| `ja` | Japanese | 日本語 | `experimental` | `0.0.4` |
| `kn` | Kannada | ಕನ್ನಡ | `experimental` | `0.0.3` |
| `ko` | Korean | 한국어 | `experimental` | `0.0.5` |
| `lv` | Latvian | Latviešu | `experimental` | `0.0.3` |
| `mk` | Macedonian | Македонски | `experimental` | `0.0.3` |
| `ml` | Malayalam | മലയാളം | `experimental` | `0.0.3` |
| `mn` | Mongolian | Монгол | `experimental` | `0.0.3` |
| `ms` | Malay | Bahasa Melayu | `experimental` | `0.0.4` |
| `my` | Burmese | မြန်မာ | `experimental` | `0.0.3` |
| `ne` | Nepali | नेपाली | `experimental` | `0.0.1` |
| `nl` | Dutch | Nederlands | `experimental` | `0.0.4` |
| `no` | Norwegian | Norsk | `experimental` | `0.0.5` |
| `pl` | Polish | Polski | `experimental` | `0.0.5` |
| `pt` | Portuguese | Português | `experimental` | `0.0.5` |
| `ro` | Romanian | Română | `experimental` | `0.0.3` |
| `ru` | Russian | Русский | `experimental` | `0.0.5` |
| `si` | Sinhala | සිංහල | `experimental` | `0.0.3` |
| `sr` | Serbian | Српски | `experimental` | `0.0.3` |
| `su` | Sundanese | Basa Sunda | `experimental` | `0.0.4` |
| `sv` | Swedish | Svenska | `experimental` | `0.0.5` |
| `sw` | Swahili | Kiswahili | `experimental` | `0.0.1` |
| `te` | Telugu | తెలుగు | `experimental` | `0.0.3` |
| `th` | Thai | ไทย | `experimental` | `0.0.5` |
| `tl` | Filipino | Filipino | `experimental` | `0.0.1` |
| `tr` | Turkish | Türkçe | `experimental` | `0.0.5` |
| `uk` | Ukrainian | Українська | `experimental` | `0.0.1` |
| `ur` | Urdu | اردو | `experimental` | `0.0.4` |
| `uz` | Uzbek | O'zbek | `experimental` | `0.0.3` |
| `vi` | Vietnamese | Tiếng Việt | `experimental` | `0.0.5` |
| `xh` | Xhosa | isiXhosa | `experimental` | `0.0.1` |
| `zh` | Chinese | 中文 | `experimental` | `0.0.6` |

## What a pack is made of

### Target

Each language pack is created based on the requirements of a programming
language, its target, which sets the categories it carries, the reserved words
in each, and the forms a rendering is allowed to take. The specific versions of
a programming language a particular reserved word belongs to are noted as well,
so the language pack grows with the progression of a programming language.

### Categories

| Category | Subcategories | Terms | What it holds |
| --- | --- | --- | --- |
| `keywords` | `keyword` | 39 | The words the grammar reserves. A rendering cannot collide with anything else in the vocabulary. All are legal identifiers except `except*`, whose renderings carry the marker through. |
| `builtins` | `builtin_func`, `builtin_type`, `special_constant` | 73 | Functions, types and constants available without importing anything: `print`, `dict`, `Ellipsis`. |
| `exceptions` | `exception` | 70 | The error hierarchy, from `BaseException` down. |
| `implicit_params` | `implicit_param` | 2 | `self` and `cls`. Conventional parameter names that Legesher treats deterministically, not words the grammar reserves. |
| `symbols` | -- | 33 | What a symbol is called: `_` is *underscore* in English. Prose names, not identifiers. |
| `variable_conventions` | -- | 15 | The idiomatic short name for a variable role: the loop counter, the throwaway, the accumulator. |
| `messages` | 20 message families | 54 | Error-message templates with named `{placeholders}`, and the traceback scaffolding that frames them. |

## Maturity

| Stage | What it means |
| --- | --- |
| `experimental` | Machine-drafted, then curated by maintainers and passed through the mechanical gates: identifier validity, cross-section collision checks, Unicode normalization, and a regeneration check proving the packs match their source of truth. No native speaker has signed off. |
| `reviewed` | A native speaker of the language has reviewed the pack and signed off on it. |
| `official` | Certified review plus term screening. |

## The dataset

| Config | One row per | Answers |
| --- | --- | --- |
| `locales` | natural language | who is this language? |
| `pl_terminology` | (target, category, source term) | what vocabulary does the target carry, and on which versions? |
| `vocabulary` | (locale, target, version, category, source term) | what is it called in this language? |
| `packs` | (locale, target) | how far along is this pairing? |

### `pl_terminology`

The programming language's own terminology. No natural language appears in
this config.

* `target`, `category`, `source_term`: the key
* `subcategory`: the finer kind, as in the table above
* `source_text`: the English surface, where `source_term` is not itself that
  surface. `symbols` carry the name, so `paren_open` is *opening parenthesis*.
  `variable_conventions` carry the identifier, so `accumulator` is `total`.
  `messages` carry the template. Null on `keywords`, `builtins`, `exceptions`
  and `implicit_params`, where `source_term` is the English. A message with no
  text carries `""`, which is a different fact from null: `AssertionError` on a
  bare `assert` genuinely has no message
* `glyph`: the character a symbol names, so `paren_open` is `(`. Null on every
  other category, and null on the symbols with no printable form: indentation,
  a line break, a space
* `pl_versions`: the target versions the entry is valid for

Availability lives here, once: `except*` carries `["3.11", ...]`, and a term
in two categories carries two rows with their own sets, so `type` is a builtin
on every version and a keyword only from 3.12.

This config is also the coverage checklist. A `pl_terminology` entry with no
matching `vocabulary` rows for a locale is a gap in that pack, stated by the
data rather than discovered downstream: the `symbols`, `variable_conventions`
and `messages` categories ship their source-side inventory ahead of any
locale's renderings for exactly that reason.

### `vocabulary`

The renderings, one row per (locale, target, version, category, source term).

* `locale`: join into `locales`; `target`, `category`, `source_term`: join
  into `pl_terminology`
* `pl_version`: rows are given resolved, so each states what you would get on
  that version of the target
* `translation`: the rendering Legesher ships
* `defined_at`: the version whose pack file defines this rendering. A row
  inherits when `defined_at` differs from `pl_version`. This is a fact about
  the rendering, not the term: Sinhala redefines terms at 3.13 to conjunct
  forms, so its `defined_at` differs from every other language's on the same
  term

`category` is part of the key on purpose: `type` is rendered once as a
keyword and once as a builtin, and those renderings may differ.

### `locales`

Natural-language identity: names (`language_name`, `native_name`), identity
tags (`iso639_2`, `bcp47`), script properties (`rtl`, `has_case_distinction`).

`locale` is a pack id, not a language tag. Where the two differ, `locale` is
the shorter form: `no` is BCP 47 `nb`, `zh` is `zh-Hans`, `sr` is `sr-Cyrl`.
Join to anything keyed by language tag on `bcp47`, or you drop exactly the rows
that differ.

### `packs`

The shipping unit, one row per (locale, target) pairing.

* `package_version`: the semver of this pairing's own distributable. A row
  reading `ar` / `python` / `0.0.5` means these are the words
  in `legesher-i18n-python-ar==0.0.5`. Each pairing versions on its own clock
* `tier`: the maturity of exactly this pairing
* `pl_versions`: the target versions this pack covers

### JSON

`json/<locale>/<target>.json` is the loadable form: the translations alone,
with the pack's `package_version` and a `pl_version_range` string naming the
versions it covers. Values are the latest version's resolved rendering over
the union of terms across the range; the parquet configs carry the full
per-version structure the JSON leaves out.

## Normalization

Python normalizes identifiers to NFKC when it parses them (PEP 3131), so a rendering whose own NFKC form differs from it is typed one way and resolved another.

> [!NOTE]
> 23 renderings in this release are NFKC-unstable, all in Thai (`th`), all through `U+0E33` THAI CHARACTER SARA AM. If you compare a `translation` value against a name taken from a running interpreter, normalize both to NFKC first.

## Packages

Legesher uses this dataset as the language packs for coding in other natural
languages. Each language ships as its own distribution,
`legesher-i18n-python-<locale>`, so Arabic is `legesher-i18n-python-ar`, and they are
loaded by `legesher-i18n`, which resolves a pack against the interpreter you are
running.

## Citation

```bibtex
@misc{legesher_language_packs,
  title        = {Legesher Language Packs: programming vocabulary rendered in natural languages},
  version      = {0.5.0},
  author       = {Legesher},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/legesher/language-packs}}
}
```
