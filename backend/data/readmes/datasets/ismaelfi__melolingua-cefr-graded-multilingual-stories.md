---
annotations_creators:
  - expert-generated
language_creators:
  - expert-generated
language:
  - de
  - es
  - fr
  - it
  - ko
  - ru
license: cc-by-nc-4.0
multilinguality:
  - translation
pretty_name: MeloLingua CEFR-Graded Multilingual Stories
size_categories:
  - n<1K
source_datasets:
  - original
task_categories:
  - translation
  - question-answering
  - text-generation
tags:
  - cefr
  - graded-readers
  - language-learning
  - parallel-text
  - reading-comprehension
  - education
configs:
  - config_name: stories
    data_files:
      - split: train
        path: stories.csv
  - config_name: sentences
    data_files:
      - split: train
        path: sentences.csv
  - config_name: vocabulary
    data_files:
      - split: train
        path: vocabulary.csv
  - config_name: questions
    data_files:
      - split: train
        path: questions.csv
---

# MeloLingua CEFR-Graded Multilingual Stories Dataset

The MeloLingua CEFR-Graded Multilingual Stories Dataset is a citable educational corpus of 118 public A1–B2 language-learning stories in German, Spanish, French, Italian, Korean, and Russian. Records include target-language text, sentence-aligned English translations, contextual vocabulary, comprehension questions, sentence-building exercises, teaching metadata, provenance, and canonical links to original lessons on [MeloLingua](https://melolingua.com).

## Composition

| Language | Stories | Levels |
| --- | ---: | --- |
| German | 25 | A1–B2 |
| Spanish | 24 | A1–B2 |
| French | 24 | A1–B2 |
| Italian | 25 | A1–B2 |
| Korean | 10 | A1–A2 |
| Russian | 10 | A1–A2 |

## Data files

- `data/stories.json`: complete nested records
- `data/stories.csv`: one story per row
- `data/sentences.csv`: one aligned target-language/English sentence pair per row
- `data/vocabulary.csv`: one vocabulary item per row
- `data/questions.csv`: one comprehension question per row

## Source and methodology

Version 1.0.0 is a structured snapshot of public MeloLingua graded stories published on 27 August 2026. Each record includes a canonical source URL and integrity hashes. The transformation normalizes educational fields and generates deterministic CSV views without rewriting story text or translations.

The CEFR labels are editorial teaching labels, not official test scores or proficiency certifications. For CEFR framework information, see the [Council of Europe level descriptions](https://www.coe.int/en/web/common-european-framework-reference-languages/level-descriptions).

## Suitable uses

The dataset supports classroom reading activities, non-commercial lesson adaptations, multilingual search and retrieval, parallel-text interfaces, vocabulary-in-context analysis, educational question-answering prototypes, and research on digital graded readers.

## License and citation

Dataset contents are available under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Cite as:

> MeloLingua CEFR-Graded Multilingual Stories Dataset, version 1.0.0, MeloLingua, 2026.

See the [GitHub repository](https://github.com/MeloLingua/melolingua-language-stories-dataset) for methodology, schema, validation, attribution, and citation metadata.