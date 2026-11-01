---
task_categories:
- translation
language:
- en
- ko
tags:
- game
- text
- translation
pretty_name: KUEST
size_categories:
- 1K<n<10K
---

# **KUEST**: **K**orean game **U**sage **E**valuation **S**uite for llm **T**ranslation

📄 **Paper:** [KUEST: Korean Game Usage Evaluation Suite for LLM Translation](https://www2.statmt.org/wmt26/pdf/2026.wmt-1.86.pdf) (WMT 2026)

A WMT26 MT test suite focusing on translation blind spots that surface when translating English into Korean in the game domain.

Translation direction: English → Korean (`en` → `ko_KR`)

## Participant information

- **Test suite name:** **KUEST** (**K**orean game **U**sage **E**valuation **S**uite for llm **T**ranslation)
- **Institution:** Pseudo Lab
- **Contact:** Minjoo Choi — mjchoi0831@gmail.com

## Team Members
- **Minjoo Choi**
- Yeonseo Cho
- Gunwoo Han
- Jaejun Jung
- Hyemi Kim
- Junhyeop Kim
- Yiji Yoon
- Jinwoo Jang

## Overview

- **Language direction:** English → Korean (`src_lang` = `en`, `tgt_lang` = `ko_KR`)
- **Domain:** Video games (Cataclysm: Dark Days Ahead 2025 `ko_25.po`, Battle for Wesnoth PO modules)
- **Submission file:** `KUEST.jsonl` (JSON Lines, UTF-8)
- **Segments:** 1,796
- **Source tokens:** ~19,996 (whitespace), well under the 1M per-participant limit
- **License:** Mixed collection — each record is licensed individually via its `license` field (`CC-BY-SA-3.0` for Cataclysm-DDA, `GPL-2.0` for Battle for Wesnoth). Submitted source sentences may be made public for research purposes. See [Sources & licensing](#sources--licensing).

## What it probes

KUEST targets phenomena where fluent MT output can still be wrong for Korean in the game domain. It groups items into four categories:

| Category | Items | Focus |
|---|---:|---|
| **TA** — Terminology & Accuracy | 331 | Glossary canonical compliance; polysemy disambiguation by context |
| **PP** — Persona & Pragmatics | 388 | Speech-register/honorific consistency by speaker persona; **dual-prompt** (baseline vs. persona-enriched regime R) |
| **TR** — Translation Robustness | 507 | Placeholder reordering, tag preservation, length constraints |
| **CT** — Cultural Transcreation | 570 | Honorifics, onomatopoeia, idioms, naming, hate speech, etc. |
| **Total** | **1,796** | |

Items are ordered TA → PP → TR → CT.

### Subcategory breakdown

| Category | Subcategory | Items |
|---|---|---:|
| TA | `glossary_compliance` | 264 |
| TA | `polysemy` | 67 |
| PP | `persona_pragmatics` (baseline) | 194 |
| PP | `persona_pragmatics-regime_r` (regime R) | 194 |
| TR | `placeholder_reordering_consistency` | 172 |
| TR | `placeholder_reordering_diverse` | 190 |
| TR | `tag_preservation` | 95 |
| TR | `length_constraint_refine` | 50 |
| CT | `cultural_reference` | 33 |
| CT | `gender_stereotyping` | 20 |
| CT | `hate_speech` | 56 |
| CT | `idiom_proverb` | 16 |
| CT | `interjection` | 39 |
| CT | `naming_transcreation` | 45 |
| CT | `speech_style_adaptation` | 273 |
| CT | `wordplay` | 88 |

### PP dual-prompt (regime R)

PP ships the same 194 speaker utterances (97 speaker pairs × `-a`/`-b`) under **two prompt regimes** so the effect of persona context on the translation can be measured:

- **baseline** — the fixed prompt `Translate from en to ko_KR.` (subcategory `PP-persona_pragmatics`; 194 rows).
- **regime R** — an English prompt enriched with speaker persona/relationship facts (speaker name, role tier, in-game unit type where available, speech act, and social-standing relationship), without prescribing specific Korean endings (subcategory `PP-persona_pragmatics-regime_r-001-a … -097-b`; 194 rows).

`src_text` and `ref_text` are identical across the two regimes; only `prompt` differs.

## Record format

Every line contains the seven WMT fields plus two provenance fields (`source`, `license`):

```json
{"dataset_id": "KUEST", "doc_id": "en-ko_KR_#_KUEST_#_CT-idiom_proverb-001", "src_lang": "en", "tgt_lang": "ko_KR", "prompt": "Translate from en to ko_KR.", "src_text": "Your skill in speaking to other people. Covers ability in boasting, flattery, threats, persuasion, lies, and other facets of interpersonal communication. Works best in conjunction with a high level of intelligence.", "ref_text": "사람들과 대화하는 기술입니다. 자랑, 아첨, 위협, 설득, 거짓말 등 사람들과의 소통 전반에 영향을 미칩니다. 지능이 높은 캐릭터와 결합하면 금상첨화일 것입니다.", "source": "CDDA", "license": "CC-BY-SA-3.0"}
```

- `doc_id` pattern: `en-ko_KR_#_KUEST_#_<category>-<subcategory>-<NNN>`; numbering restarts at `001` per subcategory (3-digit zero-pad). The PP category splits each speaker pair into two rows with `-a` / `-b` suffixes; the regime R rows reuse the source subcategory stem with a `-regime_r-` infix (`PP-persona_pragmatics-regime_r-…`), keeping the original pair numbering (`001`–`097`).
- `prompt` is fixed (`Translate from en to ko_KR.`) for every row **except** the 194 regime R rows (`PP-persona_pragmatics-regime_r-*`), which carry persona-enriched prompts (see PP dual-prompt above).
- `ref_text` holds the Korean reference (never null in this suite); it is identical across both PP regimes.
- `source` is the upstream project the record's text is derived from (`CDDA` or `Wesnoth`).
- `license` is the SPDX identifier governing that record's `src_text` and `ref_text` (`CC-BY-SA-3.0` or `GPL-2.0`).

## Sources & licensing

`KUEST.jsonl` is not under a single license: it is a collection in which each record is licensed independently according to its `license` field.

| Source (`source`) | License (`license`) | TA | PP | TR | CT | Total |
|---|---|---:|---:|---:|---:|---:|
| Cataclysm: Dark Days Ahead (`CDDA`) | `CC-BY-SA-3.0` | 243 | 0 | 412 | 200 | 855 |
| Battle for Wesnoth (`Wesnoth`) | `GPL-2.0` | 88 | 388 | 95 | 370 | 941 |
| **Total** | | **331** | **388** | **507** | **570** | **1,796** |

Filter on `license` to obtain a single-license subset. Attribution, compilation terms and redistribution requirements are described in [`DATASET-LICENSE.md`](DATASET-LICENSE.md); the full license texts are in [`licenses/`](licenses/).

## Text normalization

- Paragraph/line breaks are encoded as `\n\n` (per the WMT format note).
- Tabs and other control characters are replaced with a single space.
- Placeholders and tags (`%s`, `{n}`, `<span ...>`, `$player_…`) are preserved; source↔reference placeholder parity was verified for all TR items.

## Citation

If you use KUEST, please cite:

```bibtex
@inproceedings{choi-etal-2026-kuest,
  title     = {{KUEST}: Korean Game Usage Evaluation Suite for {LLM} Translation},
  author    = {Choi, Minjoo and Jung, Jaejun and Han, Gunwoo and Kim, Junhyeop and
               Yoon, Yiji and Kim, Hyemi and Cho, Yeonseo and Jang, Jinwoo},
  booktitle = {Proceedings of the Eleventh Conference on Machine Translation (WMT)},
  pages     = {1491--1512},
  year      = {2026},
  publisher = {Association for Computational Linguistics},
  url       = {https://www2.statmt.org/wmt26/pdf/2026.wmt-1.86.pdf}
}
```