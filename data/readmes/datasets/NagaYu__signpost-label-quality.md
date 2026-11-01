---
annotations_creators:
- machine-generated
language:
- de
- en
- es
- fr
- it
- ja
- ko
- pt
- ru
- zh
language_creators:
- machine-generated
license: mit
multilinguality: multilingual
pretty_name: "Signpost label quality"
size_categories:
- "1K<n<10K"
source_datasets:
- original
tags:
- accessibility
- a11y
- aria
- wcag
- label-quality
- multilingual
- synthetic
task_categories:
- text-classification
- text-generation
task_ids:
- multi-class-classification
configs:
- config_name: hard
  data_files:
  - split: test
    path: "hard/test-*"
  - split: train
    path: "hard/train-*"
- config_name: labels
  default: true
  data_files:
  - split: test
    path: "labels/test-*"
  - split: train
    path: "labels/train-*"
- config_name: rewrites
  data_files:
  - split: test
    path: "rewrites/test-*"
  - split: train
    path: "rewrites/train-*"
---

# Signpost label quality

Labels from accessibility trees, each one classed as good or as one of seven
ways a label can fail to mean anything. It is built for the question that is
left over after `axe-core` and Xcode's Accessibility Inspector have both
passed: there *is* a name, but does the name identify this control?

Repository: `NagaYu/signpost-label-quality`

| | |
|---|---|
| Code, evaluation, and the builder for this dataset | <https://github.com/NagaYu/signpost> |
| Model trained on it | <https://huggingface.co/NagaYu/signpost-classifier> |
| Try it in your browser | <https://huggingface.co/spaces/NagaYu/signpost> |

## Configs

| config | train | test | total | what a row is |
| --- | --- | --- | --- | --- |
| labels | 1648 | 827 | 2475 | one label, one class from the eight-way taxonomy |
| rewrites | 622 | 309 | 931 | a corrupted label and the original it replaced |
| hard | 205 | 96 | 301 | a defect that every syntactic check still passes |

`labels` is the default config.

## Data statement -- read this before quoting a number from it

**The corpus is synthetic.** Every screen in this build was composed by
`scripts/make_seed_corpus.py` from a per-language vocabulary written for the
project. No site was crawled and no app was decompiled, which is why the whole
pipeline runs offline on a laptop and why there is no redistribution question to
answer. Every row carries `synthetic: true`.

What that means for the numbers: a model evaluated on this data is being
evaluated against a *generator*, and its score is partly a measurement of how
learnable that generator is. Real screens are messier -- more abbreviations,
more house style, more labels that are bad in ways nobody thought to plant. Take
detection and accuracy figures computed here as an upper bound on a real
codebase, not as an estimate of one. `signpost/collect.py` is the path for real
pages, and it keeps the same redistribution discipline: label, role, minimal
context, never a page body.

**How the defects were planted.** The clean corpus goes through
`signpost/inject.py`, which corrupts a fixed share of labels (35% here) and
records, for each one, the position, the class, the original string, and the
strategy that produced it. Seven classes are planted: `generic`, `role_echo`,
`identifier`, `duplicate`, `verbose`, `missing` and `mismatch`. A corrupted
label is admitted to the **hard** set only if the corrupted string still passes
every syntactic criterion -- specific, role-free, not an identifier, short
enough -- so "syntactically valid but contextually wrong" is enforced by
re-running the checks rather than by assertion. `mismatch` is generated five
ways; one of them, `confusable_action`, draws from the same action lexicon a
rule-based checker could use, and it is flagged as `lexicon_derivable` so nobody
has to take a hard-set score at face value.

**What the splits guarantee.** The split is by **origin** -- site or app -- not
by screen and not by row. Naming conventions belong to a codebase, so a
per-screen split would let a model score well on a second page of a shop it had
already seen. Train and test share no origin: 40 origins on the train side, 20
on the test side, checked by `collect.assert_no_origin_leak` before this file
was written. The two sides are corrupted with different injection seeds, so a
test defect is not a training defect relocated. The split is stratified by
language, so no language lands entirely on one side.

**What is not in the denominator.** Before injection, every label passes the
strict quality gate in `signpost/quality.py`; 0 of 2592 nodes (0.0%) were
dropped as not demonstrably good. A node that was never corrupted but does not
pass that gate is dropped rather than published as `ok`. This matters because
the `ok` rows are the denominator of any over-flagging rate computed from this
dataset, and a doubtful label counted as a good one would make every such rate
-- ours included -- look better than it is.

**What is not published.** The label, the role, and clipped context. Page
bodies, DOM, screenshots and full visible text stay local. The caps are enforced
by `collect.assert_no_bulk_text`, which raises rather than truncates, and this
build fails rather than shipping an oversized row.

## Classes

| class | train | test |
| --- | --- | --- |
| ok | 1026 | 518 |
| generic | 120 | 55 |
| role_echo | 89 | 48 |
| identifier | 83 | 54 |
| duplicate | 77 | 36 |
| verbose | 65 | 36 |
| missing | 69 | 27 |
| mismatch | 119 | 53 |

## Languages

| language | train rows | test rows |
| --- | --- | --- |
| de | 160 | 79 |
| en | 169 | 84 |
| es | 170 | 83 |
| fr | 163 | 86 |
| it | 164 | 85 |
| ja | 166 | 79 |
| ko | 167 | 83 |
| pt | 161 | 82 |
| ru | 164 | 86 |
| zh | 164 | 80 |

## Mismatch strategies

| mismatch strategy | train | test | a fixed lexicon can solve it |
| --- | --- | --- | --- |
| asset_export | 21 | 12 | no |
| asset_file | 24 | 18 | no |
| asset_name | 10 | 3 | no |
| blank_empty | 49 | 20 | no |
| blank_space | 12 | 6 | no |
| blank_zwsp | 8 | 1 | no |
| camelCase | 7 | 3 | no |
| confusable_action | 38 | 13 | yes |
| copy_sibling_name | 77 | 36 | no |
| design_tool | 10 | 12 | no |
| entity_swap | 33 | 16 | no |
| expand_to_sentence | 65 | 36 | no |
| generic_term | 120 | 55 | no |
| role_prefix | 11 | 8 | no |
| role_suffix | 55 | 34 | no |
| role_suffix_title | 23 | 6 | no |
| sibling_swap | 25 | 10 | no |
| snake_case | 11 | 6 | no |
| state_flip | 0 | 1 | no |
| topic_drift | 23 | 13 | no |

## Fields

| field | what it holds |
| --- | --- |
| `name` | the accessible label -- the string under judgement |
| `role` | the normalised role: button, link, image, textfield, ... |
| `value`, `description`, `visible_text` | clipped to 80-120 characters |
| `nearby_text`, `sibling_labels` | at most 3 items of at most 80 characters |
| `screen_title`, `asset_name`, `action_hint` | the icon and the handler |
| `lang`, `platform` | language tag; web / ios / android |
| `origin`, `url`, `license`, `license_url`, `attribution` | provenance, per row |
| `label` | one of `ok`, `generic`, `role_echo`, `identifier`, `duplicate`, `verbose`, `missing`, `mismatch` |
| `hard`, `strategy`, `rule_detectable` | how the defect was planted |
| `target` (rewrites only) | the held-out original label |
| `lexicon_derivable` (hard only) | true for the `confusable_action` slice |

## Limitations

- Synthetic throughout. See the data statement.
- The per-row `license` and `attribution` fields are real fields carrying
  synthetic values: the generator assigns each origin a licence so that the
  provenance machinery is exercised end to end. For a corpus collected with
  `signpost/collect.py` they carry what the source actually said.
- The class balance is a choice, not an observation. Most real screens have far
  fewer defects than 35% of labels.
- `duplicate` is only definable within a screen, so a row taken out of its
  screen cannot be re-judged for that class.
- Nothing here says what any person will experience. The classes point at
  documented guidelines (WCAG 2.2, Apple's and Google's own guidance) and the
  citations live in `signpost/cite.py`. Signpost is not a replacement for
  `axe-core`, for Xcode's Accessibility Inspector, or for review by people who
  use assistive technology; it narrows what a human has to look at.

## Reproducing this build

```bash
python scripts/make_seed_corpus.py
python scripts/build_dataset.py --seed 0 --test-frac 0.30 --inject-rate 0.35
```

Both are deterministic: same seed, same bytes.

## Licence

The data is released under `mit`. Per-row licence, origin and attribution travel
with each row.
