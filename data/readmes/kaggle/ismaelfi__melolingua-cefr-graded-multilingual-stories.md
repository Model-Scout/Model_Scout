# MeloLingua CEFR-Graded Multilingual Stories

118 CEFR A1–B2 stories in 6 languages with aligned English translations

# MeloLingua CEFR-Graded Multilingual Stories Dataset

The **MeloLingua CEFR-Graded Multilingual Stories Dataset** is a public educational corpus of **118 graded language-learning stories** in German, Spanish, French, Italian, Korean, and Russian. It pairs target-language text with sentence-aligned English translations and includes contextual vocabulary, comprehension questions, sentence-building exercises, teaching metadata, provenance, and canonical lesson links.

## Dataset snapshot

- **118** public stories across **6** target languages
- CEFR coverage: **A1–B2**
- **35 A1**, **36 A2**, **24 B1**, and **24 B2** records
- Sentence-aligned English translations
- JSON plus story, sentence, vocabulary, and question CSV views
- Licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

## Language coverage

| Language | Stories | CEFR coverage |
| --- | ---: | --- |
| German | 25 | A1–B2 |
| Spanish | 24 | A1–B2 |
| French | 24 | A1–B2 |
| Italian | 25 | A1–B2 |
| Korean | 10 | A1–A2 |
| Russian | 10 | A1–A2 |

## What each record contains

Each story includes a stable identifier; language, locale, script, and CEFR metadata; title, summary, themes, setting tags, grammar focus, and learning outcomes; ordered target-language sentences paired with English translations; vocabulary in context; comprehension questions; sentence-building exercises; a canonical lesson URL; source hashes; and export metadata.

## Files and intended uses

- `data/stories.json` — complete nested story records for educational applications, APIs, retrieval, and qualitative research.
- `data/stories.csv` — one row per story for spreadsheets, filtering, and catalogue analysis.
- `data/sentences.csv` — sentence-aligned parallel text for translation and retrieval experiments.
- `data/vocabulary.csv` — vocabulary-in-context analysis.
- `data/questions.csv` — educational question-answering and comprehension prototypes.
- `schema/story.schema.json` — validation and integration schema.

## Methodology and provenance

Version 1.0.0 is a structured snapshot of 118 public graded stories, published on **27 August 2026**. The export preserves story text and translations, normalizes educational structure, creates deterministic CSV views, and retains canonical URLs and source hashes. Automated validation checks record counts, language and level coverage, sentence alignment, URLs, hashes, and schema-compatible fields.

The CEFR labels are MeloLingua editorial teaching labels. They are not official test scores or proficiency certifications. For the CEFR framework, see the [Council of Europe level descriptions](https://www.coe.int/en/web/common-european-framework-reference-languages/level-descriptions).

## Suitable uses

This dataset supports classroom reading activities, non-commercial lesson adaptations, multilingual search and retrieval, parallel-text interfaces, vocabulary-in-context analysis, educational question-answering prototypes, and research on digital graded readers.

## License and citation

Dataset contents are available under [Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/). For attribution, cite:

> MeloLingua CEFR-Graded Multilingual Stories Dataset, version 1.0.0, MeloLingua, 2026.

Source code, complete documentation, and citation metadata: [github.com/MeloLingua/melolingua-language-stories-dataset](https://github.com/MeloLingua/melolingua-language-stories-dataset)

Original lessons and canonical story links: [melolingua.com](https://melolingua.com)

출처: Kaggle (ismaelfi/melolingua-cefr-graded-multilingual-stories)
태그: education, linguistics, text, translation, multilingual
라이선스: Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
수정일: 2026-08-28T09:55:01.367Z
