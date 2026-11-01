---
license: cc-by-sa-4.0
pretty_name: Multilingual Knowledge Training Pool
language:
- acm
- af
- am
- apc
- ar
- ars
- ary
- arz
- as
- az
- be
- bg
- bm
- bn
- bo
- ca
- ceb
- ckb
- cs
- da
- de
- el
- en
- es
- et
- eu
- fa
- ff
- fi
- fr
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
- ilo
- is
- it
- ja
- jv
- ka
- kac
- kea
- kk
- km
- kn
- ko
- ky
- lg
- ln
- lo
- lt
- luo
- lv
- mg
- mi
- mk
- ml
- mn
- mr
- ms
- mt
- my
- nb
- ne
- nl
- nso
- ny
- om
- or
- pa
- pl
- ps
- pt
- ro
- ru
- rw
- sd
- shn
- si
- sk
- sl
- sn
- so
- sq
- sr
- ss
- st
- su
- sv
- sw
- ta
- te
- tg
- th
- ti
- tl
- tn
- tr
- ts
- uk
- ur
- uz
- vi
- war
- wo
- xh
- yo
- zh
- zu
task_categories:
- question-answering
- multiple-choice
size_categories:
- 100K<n<1M
---

# Multilingual knowledge training pool

Public multiple-choice questions in many languages from seven datasets, read at the pinned
revisions named below and laid out twice. Train on either layer or on both.

## `pool.jsonl`

Every source rewritten into one shape, 328665 rows in 116 languages, one JSON object per line,
with these fields.

| Field | What it holds |
|---|---|
| `id` | a row identifier unique within this file |
| `question` | the question text, as its source publishes it |
| `context` | the passage the question is about, empty when there is none |
| `options` | the answer options, as a list of strings |
| `answer` | the letter of the correct option, A for the first option listed |
| `language` | the language of the row, as a short code |
| `language_label` | the language as its own source names it |
| `subject` | the subject label the source gives the row, or a constant naming the source's own task where it publishes none: reading comprehension for Belebele, commonsense for the X-CSQA rows |
| `source` | the name of the source directory the row came from |
| `source_repo`, `source_revision` | the dataset and the revision it was read at |
| `source_subset`, `source_split`, `source_id` | where the row sits in that set |
| `provenance_class` | how the row came to exist |
| `licence` | the licence of the source it came from |

The options of every row were permuted once when this file was built, under the recorded seed
20260913, and the answer letter is written in the permuted order, so that a source which publishes
its correct option in a fixed position cannot teach that position. Rows are deduplicated across
sources on the question together with its context and its option set, keeping the first source
that carries the question in the order of the sections below.

## `sources/`

The same data untouched, 351366 rows, one directory per source, holding the files at the paths, in
the format and with the columns its own repository publishes. Nothing here was renamed, reshaped,
reordered or deduplicated. Use this layer if you want a field the rewritten one drops, such as the
written explanations in the medical set or the country and regional labels in the local
examination set, or if you would rather order the options yourself.

## The sources

### `sources/include`

Regional examination and licensing questions collected in the country they are used in, written in
the language of that country rather than translated into it, across academic, professional and
licensing levels. From `CohereLabs/include-base-44` at revision
`d2e1f6015f67a43c02a9a68db98e2298e2d6a660`, 88 files, languages: 44, one directory per language,
named in English. 23409 rows here, of which 22862 also appear in `pool.jsonl`. Provenance class
`human`, licence `apache-2.0`. Its own fields are language, country, domain, subject,
regional_feature, level, question, option_a to option_d, and answer as the zero-based index of the
correct option.

Worth knowing. The answer column is an index, not a letter, and it is zero-based. The regional
questions are the point of the set: many of them cannot be answered without local knowledge, which
is what makes them different from questions written in English and translated.

### `sources/belebele`

Reading-comprehension questions over a short passage, written once in English by trained
annotators and rendered into every variant by professional translators, four options per question.
From `facebook/belebele` at revision `7899cdfa4e1e0d733fd77c848e2c273cb1d32be2`, 122 files,
languages: 122 language variants, one file per variant, named with a script code. 109035 rows
here, of which 108887 also appear in `pool.jsonl`. Provenance class `human`, licence `cc-by-
sa-4.0`. Its own fields are link, question_number, flores_passage, question, mc_answer1 to
mc_answer4, correct_answer_num as a one-based index, dialect, ds.

Worth knowing. Every question needs its passage, which travels in the context field of the curated
layer and in flores_passage in the raw one. A row without the passage is not answerable. The set
is published as an evaluation set and has one split.

### `sources/exams`

High-school examination questions collected from the official state examinations of several
ministries of education, over 24 subjects. From `mhardalov/exams` at revision
`4ff10804abb3341f8815cacd778181177bba7edd`, 2 files, languages: eleven, in the info.language field
of each row. 10633 rows here, of which 8259 also appear in `pool.jsonl`. Provenance class `human`,
licence `cc-by-sa-4.0`. Its own fields are id, question with a stem and choices holding parallel
text, label and para lists, answerKey, and info with the grade, the subject and the language.

Worth knowing. The multilingual configuration only, its train and validation splits, and its own
test split is left out. The subjects run past the sciences into history, philosophy and business,
and the subject field is how to select. No row is in English.

### `sources/aya_xcsqa`

Commonsense questions with five options each, translated by people from the English originals and
then written out as an instruction with lettered options by a fixed template. From
`CohereLabs/aya_collection` at revision `09069079fad96ad9c7f8781be8c1d70471dfa768`, 1 files,
languages: 16, in the language field of each row, named with a three-letter code. 16950 rows here,
of which 15689 also appear in `pool.jsonl`. Provenance class `collected`, licence `apache-2.0`.
Its own fields are id, inputs holding the question and the lettered options as one string, targets
holding the sentence that names the right letter, dataset_name, sub_dataset_name, task_type,
template_id, language, split, script.

Worth knowing. The only source that arrives already written as a question followed by lettered
options, which is why it is in. The options are lettered A to E rather than A to D, and the
instruction line inside inputs is in English whatever the language of the question.

### `sources/medmcqa`

Indian medical entrance examination questions, AIIMS and NEET PG, 1991 to the present, with the
examining body's own answer key. From `openlifescienceai/medmcqa` at revision
`91c6572c454088bf71b679ad90aa8dffcd0d5868`, 2 files, languages: English. 185499 rows here, of
which 167134 also appear in `pool.jsonl`. Provenance class `human`, licence `apache-2.0`. Its own
fields are id, question, opa to opd for the four options, cop for the zero-based index of the
correct one, choice_type, exp for a written explanation, subject_name, topic_name.

Worth knowing. English only, and the apache-2.0 tag covers the packaging rather than the examining
boards' copyright in the underlying questions, which the dataset card does not address. It is here
because it is the largest human-keyed examination set available in any language.

### `sources/ai2_arc`

Grade-school science examination questions written for human tests, in an easy and a challenge
partition. From `allenai/ai2_arc` at revision `210d026faf9955653af8916fad021475a3f00453`, 4 files,
languages: English. 4212 rows here, of which 4211 also appear in `pool.jsonl`. Provenance class
`human`, licence `cc-by-sa-4.0`. Its own fields are id, question, choices with parallel text and
label lists, answerKey.

Worth knowing. English only, and these items are widely present in web pretraining corpora, so a
model pretrained on web text may have met them already. The train and validation splits only,
since the test split is widely used as an evaluation set.

### `sources/mmlu_dev_val`

The development and validation splits of a well known English examination corpus covering 57
school and university subjects, written by graduate students from freely available course
material. From `cais/mmlu` at revision `c30699e8356da336a370243923dbaf21066bb9fe`, 2 files,
languages: English. 1628 rows here, of which 1623 also appear in `pool.jsonl`. Provenance class
`human`, licence `mit`. Its own fields are question, subject, choices as a list of four strings,
answer as a zero-based index.

Worth knowing. Only the development and validation splits of that repository are read. Its test
split is not part of this pool, in either layer.

## Languages

The rewritten layer holds 116 languages. The twenty largest by row count are `en` 174854, `vi`
3609, `zh` 3359, `ar` 3354, `pl` 3182, `ur` 3124, `hi` 2928, `it` 2920, `pt` 2787, `bg` 2640, `hr`
2505, `ru` 2464, `es` 2447, `nl` 2447, `ja` 2388, `fr` 2308, `ne` 2306, `tr` 2298, `mk` 2221, `bn`
2214. A language is written as a short code where the row's source names one this pool recognises,
and otherwise as the source's own label, which the `language_label` field always carries.

Script variants are folded into one code. A source that names a romanised or a traditional-script
rendering separately keeps that name in `language_label` while `language` carries the language:
`Arabic` under `ar`, `Azerbaijani` under `az`, `Bulgarian` under `bg`, `Bengali` under `bn`, and
so on for 46 codes in all. Filter on `language_label` rather than on `language` if you want one
script only.

## Options per row

Most rows offer four options, but not all of them do: 490 rows with 3, 311829 rows with 4, 16346
rows with 5. The options are lettered A upwards in the order the `options` list gives them, and
the `answer` field is the letter of the correct one in that order. The rows with five come almost
entirely from the commonsense set, whose own lettering runs A to E, and the rest are scattered
through the examination sets. Code that assumes four options will fail on the others rather than
skip them.

## Provenance and licences

Every row was written by people: examination and licensing questions written for human tests,
crowd-written reading-comprehension questions rendered by professional translators, and
commonsense questions translated by people. Nothing here was generated by a model. One directory
carries the class `collected` rather than `human` because its rows were passed through a fixed
template after translation, and every row names its class in the `provenance_class` field.

The pool as a whole is offered under `cc-by-sa-4.0`, which is the most restrictive term its
sources compose to. Commercial use is permitted: no source carries a NonCommercial term. The per-
source terms are apache-2.0 for the local examination set, for the commonsense set and for the
medical set, cc-by-sa-4.0 for the reading-comprehension set, the state examination set and the
English science set, and mit for the English development and validation splits. Each rewritten row
carries its own in the `licence` field and each directory under `sources/` is one source, so a
subset under a single licence can be selected. Attribution for the share-alike sources goes to
their authors, and questions taken from national examinations remain the property of the boards
that wrote them.

## Filtering

Rows whose question duplicated a question in a held-out evaluation set were removed before
publication, from both layers alike, by an exact match on the normalised question (6 rows) and by
an n-gram overlap check (2650 rows), each comparing a row only with the held-out questions in its
own language. That evaluation set is not distributed here. Nothing else was filtered: no language,
no subject and no difficulty was selected for or against, so the pool still holds the history, law
and business questions its multi-subject sources carry alongside the sciences, and the subject
field is how to select what you want.
