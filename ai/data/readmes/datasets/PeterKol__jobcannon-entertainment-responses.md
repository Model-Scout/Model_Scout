---
license: cc-by-4.0
pretty_name: JobCannon Entertainment Quiz Response Dataset
size_categories:
  - 10K<n<100K
language:
  - en
  - ja
  - ar
  - es
  - de
  - fr
  - pt
  - uk
  - id
  - ru
  - ko
  - it
  - he
  - tr
  - zh
  - pl
  - th
  - nl
  - sv
  - vi
  - nb
  - fa
  - uz
  - hi
tags:
  - entertainment
  - quiz
  - multilingual
  - cross-lingual
  - forced-choice
  - response-time
  - not-validated
configs:
  - config_name: jungian_archetype
    data_files: jungian_archetype.csv
  - config_name: spirit_animal
    data_files: spirit_animal.csv
  - config_name: mental_age
    data_files: mental_age.csv
  - config_name: aura_color
    data_files: aura_color.csv
  - config_name: past_life
    data_files: past_life.csv
  - config_name: coverage
    data_files: coverage.csv
  - config_name: result_distribution_by_locale
    data_files: result_distribution_by_locale.csv
  - config_name: dimension_means_by_locale
    data_files: dimension_means_by_locale.csv
---
# JobCannon Entertainment Quiz Response Dataset

**v1. 77,284 item-level responses to five for-fun quizzes, in 24 languages.**

Anonymized, item-level answers to five entertainment quizzes taken by real
visitors on [JobCannon](https://jobcannon.io) between March and August 2026.
One row is one completed quiz: the raw per-item answers, the category totals the
site computed from them, and the result the taker was shown.

We collected all of it on our own traffic. It is not a repackaging of somebody
else's file.

## Read this part before you use it

These five quizzes are **not psychometric instruments**. Nobody validated them.
There is no norm sample behind them and no reliability coefficient, and they
were never built to measure any particular construct. "Spirit animal" is not a
trait. The result a taker sees is the largest of a handful of hand-authored
category counters, and those categories were picked because they make a fun
result page.

So please don't read a mean here as a population estimate. And there is no
published norm for any of the five, so there is nothing to compare these
numbers against.

The useful thing in the file is the behaviour around the answers: how people
respond to forced-choice items in twenty-four languages, how long they take,
and how answer patterns and result shares move between language audiences
looking at identical items. The sample is big enough and clean enough for that
kind of question.

If you want scored instruments with published norms behind them, that is a
separate release: the [JobCannon Psychometric Response
Dataset](https://doi.org/10.5281/zenodo.20686669), nine instruments, no overlap
with this one. Both come out of the same generator, under the same privacy rules
and the same suppression thresholds, and we kept the two test lists apart on
purpose, so any given row appears in exactly one of them.

## Files

### Item-level, one row per completed quiz

| config | quiz | items | result categories | median time | responses |
| --- | --- | --- | --- | --- | --- |
| `jungian_archetype` | Jungian archetype | 24 | 12 | 5m 17s | 31,081 |
| `spirit_animal` | Spirit animal | 12 | 8 | 2m 09s | 17,520 |
| `mental_age` | Mental age | 12 | 5 | 2m 02s | 10,985 |
| `aura_color` | Aura colour | 10 | 7 | 1m 52s | 10,929 |
| `past_life` | Past life era | 12 | 8 | 2m 27s | 6,769 |
| | | | | | **77,284** |

Columns: `response_id`, `locale`, `year_month`, `duration_seconds`,
`top_result`, `score_<category>` ..., `q1` ... `qN`.

Item wording is not distributed. The `q` columns hold answer values only.

The score columns work one way for four of the quizzes and a different way for
`mental_age`. The four carry one `score_<category>` per possible result, and
`top_result` is whichever of them came out largest. `mental_age` instead has a
single `score_percentage`, and its `top_result` is a band (`teen`,
`young_adult`, `mature`, `wise`, `elder`) rather than an age in years.

### Aggregates, by quiz × language

| config | rows | what it holds |
| --- | --- | --- |
| `coverage` | 126 | n, item count, distinct results and median duration for every quiz × locale cell, plus a `publishable` flag (n ≥ 100) |
| `result_distribution_by_locale` | 233 | share of each result category, per quiz per language |
| `dimension_means_by_locale` | 290 | mean of each category score, per quiz per language |

Small cells are suppressed. A language cell needs n ≥ 100 to appear at all, and
inside a cell any result category with n < 30 gets folded into `other_below_30`.
37 of the 121 quiz × language cells clear that floor. The other 84 are in the
file with `publishable=false` and no distribution rows, so you can see they
exist without anyone computing a share off eleven people.

Every table also carries an `ALL` pseudo-locale row, which is the same statistic
over the whole quiz with every language pooled.

`_manifest.json` is not a config. It records, per quiz, how many raw rows were
pulled, how many survived the item-count filter, and the resulting column count,
so you can check the numbers quoted on this page against the build that produced
the files.

## Language coverage

Responses per language, all five quizzes combined:

| | | | | | |
| --- | --- | --- | --- | --- | --- |
| en 35,541 | ja 26,769 | ar 5,885 | es 2,541 | de 927 | fr 769 |
| pt 717 | ua 543 | id 343 | ru 305 | ko 201 | it 197 |
| he 171 | tr 129 | zh 126 | pl 114 | th 107 | nl 92 |
| sv 92 | vi 68 | nb 40 | fa 39 | uz 31 | hi 30 |

A further 1,507 rows arrived without a locale and are labelled `unknown`. Treat
those as missing values. We kept them in a bucket of their own so that nobody
quietly counts them as English.

English is 46.0% of the rows, so most of this file is in some other language:
41,743 rows, of which 40,236 carry a named language. For a lot of uses that half
is the reason to download it at all. Japanese alone is 26,769 rows, around eight
times the Japanese sample in our psychometric release.

The Japanese mass is bunched into one quiz, which limits what you can do with
it. 22,223 of the 26,769 Japanese rows sit in the Jungian archetype quiz, where
Japanese takers are 71.5% of everyone who finished. Arabic behaves differently:
3,098 of its 5,885 rows are `mental_age`, and there Arabic, Japanese and English
land within four points of each other at 28.2%, 29.7% and 26.6%. `past_life` and
`aura_color` go the other way, at 86% and 78% English. Check the `coverage`
table for the cell you care about before you assume a language is represented in
the quiz you are looking at.

Twelve labels reach n ≥ 100 somewhere, so those are the ones that show up in the
aggregate tables: `ar de en es fr id ja ko pt ru ua` and the `unknown` bucket.

## Privacy

No personal data is in these files, and none is read in the first place. The
build selects exactly six columns (`locale`, `answers`, `scores`, `top_result`,
`duration_seconds`, `created_at`). Everything identifying on the source table is
therefore out of reach of the output even if somebody later changes the writer:
user id, anonymous id, participant name and email, referrer, entry host and
path, UTM parameters, cohort id and organization id.

Two more reductions on top of that. `response_id` is a per-file sequential
integer instead of the database id, and the timestamp is cut back to
`year_month`, so no row can be joined to a session by its time.

## Method

- Rows are filtered to each quiz's current item count. A response whose answer
  array is any other length is either a legacy version of the quiz or an
  incomplete one, and it gets dropped: 2,649 of 79,933 raw rows, 3.3%.
- `score_*` columns hold the category totals exactly as the live site computed
  them. Nothing was recomputed for the release.
- `duration_seconds` is blank where the recorded value was ≤ 0 or ≥ 7,200 s.
  Roughly 2% of rows are blank on that column.
- Nothing is weighted, balanced or down-sampled. Language shares are traffic
  shares, and traffic follows wherever the quiz got shared.

## Citation

```bibtex
@dataset{jobcannon_entertainment_2026,
  title  = {JobCannon Entertainment Quiz Response Dataset},
  author = {Kolomiets, Peter},
  year   = {2026},
  version = {1.0},
  publisher = {JobCannon},
  doi    = {10.5281/zenodo.21950814},
  url    = {https://doi.org/10.5281/zenodo.21950814}
}
```

## License

CC-BY-4.0. If you publish anything off it, cite the DOI above.
