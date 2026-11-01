---
annotations_creators: []
language:
  # Top 30 (>50 rows each)
  - tr
  - ru
  - it
  - en
  - eo
  - hu
  - de
  - fr
  - pt
  - mk
  - es
  - he
  - fi
  - nl
  - pl
  - sr
  - mr
  - el
  - da
  - cs
  - sv
  - bg
  - la
  - zh
  - ro
  - ia
  - ja
  - uk
  - tt
  - tl
  - id
  - nb
  - lt
  - az
  # Berber and constructed/niche
  - ber
  - tok
  - ile
  - tlh
  - jbo
  - lfn
  - vo
  - avk
  - nov
  - ido
  - ldn
  - afh
  # Additional living languages across the long tail
  - ar
  - bn
  - fa
  - br
  - ceb
  - hi
  - vi
  - pam
  - hy
  - be
  - ko
  - sk
  - oc
  - et
  - war
  - ms
  - hr
  - eu
  - yi
  - af
  - km
  - ca
  - kha
  - dtp
  - is
  - ga
  - sl
  - sq
  - cv
  - kw
  - ang
  - pms
  - prg
  - ug
  - lv
  - lzh
  - egl
  - ur
  - sah
  - nds
  - mi
  - tvl
  - ch
  - th
  - cy
  - non
  - yo
  - ln
  - grc
  - arq
  - orv
  - sw
  - rif
  - gl
  - crh
  - jv
  - dsb
  - am
  - csb
  - sgs
  - ext
  - nog
  - arz
  - hsb
  - nah
  - kk
  - su
  - mhr
  - cbk
  - ilo
  - zsm
  - nst
  - zza
  - hoc
  - max
  - kek
  - hif
  - mul
language_creators: []
license: cc-by-2.0
multilinguality:
  - multilingual
pretty_name: Multilingual Sentences (Adaption)
size_categories:
  - 1K<n<10K
source_datasets:
  - extended|https://huggingface.co/datasets/Reubencf/PolyglotText
tags:
  - adaption
  - instruction-tuning
  - multilingual
  - tatoeba
  - sentences
  - low-resource
  - constructed-languages
task_categories:
  - translation
  - text-generation
task_ids: []
---

![banner](https://proteus-prod-public.s3.us-east-1.amazonaws.com/temp/b2080f8e-b45c-4860-ba77-972a1b81ec15.png)

This dataset is a remastered version of
[`Reubencf/PolyglotText`](https://huggingface.co/datasets/Reubencf/PolyglotText)
prepared using [Adaption's](https://adaptionlabs.ai/app/auth) Adaptive Data platform.

# Multilingual Sentences (Adaption)

**9,999 sentences across 123 languages.** A broad multilingual subset of
PolyglotText — originally derived from the
[Tatoeba](https://tatoeba.org) project — with Adaption-sharpened
`enhanced_prompt` / `enhanced_completion` / `reasoning_trace` columns.
Each row carries a source-language sentence, translations, and the
Adaption-processed fields.

### Dataset size

9,999 rows. Instruction-tuning format.

### Domain
- Language (38%)
- Other (18%)
- Religion (8%)

### Tone
- Informal (22%)
- Informative (22%)
- Dramatic (14%)

## Languages — full breakdown

This is a **massively multilingual** dataset with **123 distinct source
languages**, not 3. The Adaption auto-stats only surface the top three —
the real distribution spans high-resource, mid-resource, low-resource,
and several constructed languages.

### Top 30 source languages

| Language | Code | Rows |
|---|---|---:|
| Turkish | `tur` | 1,319 |
| Russian | `rus` | 1,265 |
| Italian | `ita` | 1,185 |
| English | `eng` | 998 |
| **Esperanto** (constructed) | `epo` | 874 |
| Hungarian | `hun` | 610 |
| German | `deu` | 504 |
| French | `fra` | 388 |
| Portuguese | `por` | 351 |
| Macedonian | `mkd` | 297 |
| Spanish | `spa` | 267 |
| Hebrew | `heb` | 203 |
| Finnish | `fin` | 196 |
| **Berber** | `ber` | 134 |
| Dutch | `nld` | 93 |
| Polish | `pol` | 88 |
| Serbian | `srp` | 79 |
| **Marathi** | `mar` | 72 |
| Greek | `ell` | 70 |
| Danish | `dan` | 67 |
| Czech | `ces` | 54 |
| Swedish | `swe` | 53 |
| Bulgarian | `bul` | 52 |
| Latin | `lat` | 49 |
| Mandarin | `cmn` | 43 |
| Romanian | `ron` | 42 |
| **Interlingua** (constructed) | `ina` | 40 |
| Japanese | `jpn` | 32 |
| **Toki Pona** (constructed) | `tok` | 29 |
| **Lingua Franca Nova** (constructed) | `lfn` | 28 |

### Mid tail (10–30 rows each)

Ukrainian (`ukr`), Tatar (`tat`), Tagalog (`tgl`), Indonesian (`ind`),
Norwegian Bokmål (`nob`), Lithuanian (`lit`), Azerbaijani (`aze`),
**Interlingue** (`ile`), **Klingon** (`tlh`), **Lojban** (`jbo`), Meadow Mari
(`mhr`), Chavacano (`cbk`), Bengali (`ben`), Persian (`pes`), Breton
(`bre`), Ilocano (`ilo`), Arabic (`ara`), Cebuano (`ceb`), Hindi (`hin`).

### Long tail (1–10 rows each)

An additional ~80 languages appear in small counts, including:

- **South / Southeast Asia**: Khmer (`khm`), Thai (`tha`), Vietnamese
  (`vie`), Urdu (`urd`), Javanese (`jav`), Sundanese (`sun`), Burmese
  implied via related scripts, Malay/Maori (`mri`), Kapampangan (`pam`),
  War (`war`), Ilokano.
- **African**: Amharic (`amh`), Yoruba (`yor`), Lingala (`lin`), Swahili
  (`swh`), Riffian Berber (`rif`), Shilha-like variants.
- **European micro-languages**: Low German (`nds`), West Frisian-adjacent,
  Old English (`ang`), Piedmontese (`pms`), Old East Slavic (`orv`),
  Upper Sorbian (`hsb`), Lower Sorbian (`dsb`), Samogitian (`sgs`),
  Extremaduran (`ext`), Kashubian (`csb`), Cornish (`cor`),
  Manx / Irish (`gle`), Welsh (`cym`).
- **Middle East / Central Asia / Caucasus**: Old Prussian (`prg`), Uyghur
  (`uig`), Sakha (`sah`), Chuvash (`chv`), Armenian (`hye`), Georgian
  (where present).
- **Constructed / historical / niche**: Volapük (`vol`), Kotava (`avk`),
  Novial (`nov`), Ido (`ido`), Láadan (`ldn`), Afrihili (`afh`),
  Ancient Egyptian (`egl`), Classical Chinese (`lzh`), Sumerian (`sux`),
  Ancient Greek (`grc`), Pre-Classical Latin variants, Old Norse (`non`).

Some rare codes (single-digit counts): `tvl` (Tuvaluan), `cha`
(Chamorro), `nah` (Nahuatl), `kaz` (Kazakh), `kek` (Q'eqchi'),
`arq` (Algerian Arabic), `crh` (Crimean Tatar), `hif` (Fiji Hindi),
`orv` (Old East Slavic), `swh` (Swahili), and others.

The full distribution is available by reading the dataset's `lang`
column and running a value-count.

## Schema

| Column | Type | Meaning |
|---|---|---|
| `sentence_id` | string | Tatoeba sentence identifier |
| `lang` | string | ISO-639-3 source-language code |
| `text` | string | The sentence itself |
| `translations` | list[dict] | Per-language translations (where available) |
| `enhanced_prompt` | string | Adaption-sharpened prompt |
| `enhanced_completion` | string | Adaption-sharpened completion |
| `reasoning_trace` | string | Adaption-generated reasoning trace |

## Intended Use

- Multilingual instruction tuning across a long tail of languages.
- Benchmarking low-resource and constructed-language capability in
  multilingual LLMs.
- Seed data for translation and cross-lingual transfer research.

## Limitations

- Distribution is heavily skewed toward Turkish, Russian, Italian,
  English, and Esperanto — the long tail languages appear only a handful
  of times each.
- Sentences are short isolated utterances (Tatoeba-style), not
  full-document text.
- Adaption's sharpening was performed by a model; values like
  `enhanced_completion` inherit model bias and may introduce subtle
  meaning drift on very low-resource languages.

## License

Source sentences from Tatoeba are **CC BY 2.0**. Adaption-generated
columns (`enhanced_prompt`, `enhanced_completion`, `reasoning_trace`)
are released under the same license.

## Related

- Original corpus (10M+ rows of Tatoeba-derived multilingual text):
  [`Reubencf/PolyglotText`](https://huggingface.co/datasets/Reubencf/PolyglotText)
- Adaption collection:
  [`Reubencf/proper-adaption`](https://huggingface.co/collections/Reubencf/proper-adaption)

## Evaluation Results

- **Quality Gains:**
<img src="https://proteus-prod-public.s3.us-east-1.amazonaws.com/temp/24055e95-0bf3-4cee-aceb-ee407c29af54.png" alt="QualityGains" style="max-width: 50%; display: block; margin-left: auto; margin-right: auto;" />

- **Grade Improvement:**
<img src="https://proteus-prod-public.s3.us-east-1.amazonaws.com/temp/2fac8719-543d-432f-8e4a-5cdddb57fd24.png" alt="Grade" style="max-width: 50%; display: block; margin-left: auto; margin-right: auto;" />

- **Percentile Chart:**
<img src="https://proteus-prod-public.s3.us-east-1.amazonaws.com/temp/b592e434-ebb4-4054-8491-e09bfbf9ec0f.png" alt="Percentile Chart" style="max-width: 50%; display: block; margin-left: auto; margin-right: auto;" />

## Citation

If you use this dataset in your research or downstream work, please cite:

```bibtex
@misc{adaption_multilingual_sentences_2026,
  author       = {Fernandes, Reuben Chagas},
  title        = {Adaption Multilingual Sentences: 123-Language Text Subset},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/Reubencf/Adaption-multilingual-sentences}}
}
```

APA-style:

> Reuben Chagas Fernandes (2026). *Adaption Multilingual Sentences: 123-Language Text Subset* [Dataset]. Hugging Face. https://huggingface.co/datasets/Reubencf/Adaption-multilingual-sentences

