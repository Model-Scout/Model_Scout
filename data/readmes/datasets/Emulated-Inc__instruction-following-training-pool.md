---
license: cc-by-sa-4.0
pretty_name: Instruction Following Training Pool
language:
- ar
- ca
- cs
- da
- de
- en
- eo
- es
- eu
- fi
- fr
- he
- hu
- id
- it
- ja
- ko
- nl
- pl
- pt
- ru
- th
- tr
- uk
- vi
- zh
task_categories:
- text-generation
size_categories:
- 100K<n<1M
---

# Instruction following training pool

Public prompts for writing tasks, many of them carrying a constraint a program can check, from
eight datasets read at the pinned revisions named below and one layer built here from them. The
pool is laid out twice. Train on either layer or on both.

## `pool.jsonl`

Every source rewritten into one shape, 310602 rows, one JSON object per line, with these fields.

| Field | What it holds |
|---|---|
| `id` | a row identifier unique within this file |
| `prompt` | the request, as a model should receive it |
| `response` | an answer to it where the source ships one, `null` otherwise |
| `instruction_id_list` | the constraints the prompt carries, each named by the checker that decides it, empty when none were recovered |
| `kwargs` | one object per entry of that list, holding that checker's arguments |
| `instruction_origin` | how the constraints came to be attached: `source`, `mined` or `built` |
| `instructions_complete` | true when the listed constraints are every constraint the prompt states |
| `source` | the name of the source directory the row came from |
| `source_repo`, `source_revision` | the dataset and the revision it was read at |
| `source_split`, `source_id` | where the row sits in that set |
| `provenance_class` | how the row came to exist |
| `licence` | the licence of the source it came from |

Of those rows 285170 carry a response and 27761 carry at least one constraint, 38821 constraints
in all. A row with constraints can be scored without a reference answer, by running the named
checker over a generated response with the arguments beside it, which is what the
`instruction_id_list` and `kwargs` fields are for. A row with a response and no constraints is
ordinary supervised data. Rows that carry both are the ones where a response was available to
prove the constraint holds.

The three origins differ in what they guarantee. `source` means the set published the constraint
itself, so it is exactly what the prompt asks. `mined` means the prompt states the constraint in
words that a narrow set of patterns recognised and the row's own response already satisfies the
checker, so the constraint is true of the response by construction, but the prompt may ask for
other things besides. `built` means the request is a human one and the constraints after it were
sampled and written at build time, so they are complete and exact but the wording is not human.
`instructions_complete` records that difference per row, and the seed for the sampling was
20260911.

### The constraints

Every constraint in the file is named by one of these checkers, with the arguments the name
implies. A checker decides its constraint by reading the response, so the same vocabulary can be
used as a training reward.

| Checker | Rows |
|---|---|
| `change_case:capital_word_frequency` | 1270 |
| `change_case:english_capital` | 1879 |
| `change_case:english_lowercase` | 1279 |
| `combination:repeat_prompt` | 896 |
| `combination:two_responses` | 986 |
| `detectable_content:number_placeholders` | 2070 |
| `detectable_content:postscript` | 1516 |
| `detectable_format:json_format` | 977 |
| `detectable_format:multiple_sections` | 1278 |
| `detectable_format:number_bullet_lists` | 1485 |
| `detectable_format:number_highlighted_sections` | 1280 |
| `detectable_format:title` | 1599 |
| `keywords:existence` | 2515 |
| `keywords:forbidden_words` | 2211 |
| `keywords:frequency` | 1279 |
| `keywords:letter_frequency` | 1412 |
| `language:response_language` | 1188 |
| `length_constraints:nth_paragraph_first_word` | 1303 |
| `length_constraints:number_paragraphs` | 1246 |
| `length_constraints:number_sentences` | 2746 |
| `length_constraints:number_words` | 3563 |
| `punctuation:no_comma` | 2072 |
| `startend:end_checker` | 1488 |
| `startend:quotation` | 1283 |

## `sources/`

The same data untouched, 546342 rows, one directory per source, holding the files at the paths, in
the formats and with the columns its own repository publishes. Nothing here was renamed, reshaped,
reordered or deduplicated. Use this layer if you want a field the rewritten one drops, such as the
later turns of a conversation, the reviewer rankings of the volunteer trees or the constraint
descriptions of the reinforcement set, or if you would rather pair prompts with constraints
yourself.

## The sources

### `sources/dolly`

Instruction and response pairs written by several thousand employees of one company across seven
task categories, with reference passages copied from Wikipedia for the categories that need them.
From `databricks/databricks-dolly-15k` at revision `bdd27f4d94b9c1f951818a7da7fd7aeea5dbff1a`,
files `databricks-dolly-15k.jsonl`. 14993 rows here, of which 14776 also appear in `pool.jsonl`, 2
of them with constraints. Provenance class `human`, licence `cc-by-sa-3.0`. Its own fields are
instruction, context, response, category.

Worth knowing. The contributors were told not to use a language model for either side, so both
sides are human, but the writing is question answering and summarising rather than constrained
writing, so almost no row states a constraint a checker can decide.

### `sources/oasst1`

Message trees from a volunteer effort to build an assistant corpus by hand, in thirty-five
languages, each message reviewed and ranked by other volunteers. From `OpenAssistant/oasst1` at
revision `fdf72ae0827c1cda404aff25b6603abec9e3399b`, files
`data/train-00000-of-00001-b42a775f407cee45.parquet`,
`data/validation-00000-of-00001-134b8fd0c89408b6.parquet`. 88810 rows here, of which 10226 also
appear in `pool.jsonl`, 4 of them with constraints. Provenance class `human`, licence
`apache-2.0`. Its own fields are message_id, parent_id, user_id, created_date, text, role, lang,
review_count, review_result, deleted, rank, synthetic, model_name, detoxify, message_tree_id,
tree_state, emojis, labels.

Worth knowing. The schema carries a synthetic flag and a model name, so a subset is model-written
and is dropped from the rewritten rows. The rewritten rows take the first message of a tree and
the reply the volunteers ranked first, so later turns live in this directory only.

### `sources/oasst2`

The later release of the same volunteer message trees, with more languages. From
`OpenAssistant/oasst2` at revision `179dd21fc55192153d94adb0e0ce8f69e222bf75`, files
`data/train-00000-of-00001-88ba0162028a73fc.parquet`,
`data/validation-00000-of-00001-1deeef95c3248fe0.parquet`. 135121 rows here, of which 3431 also
appear in `pool.jsonl`, 1 of them with constraints. Provenance class `human`, licence
`apache-2.0`. Its own fields are the same columns as the earlier release.

Worth knowing. It contains the earlier release, so the rewritten rows of the two overlap heavily
and the duplicates are dropped in favour of the earlier one.

### `sources/rlvr_ifeval`

Prompts drawn from an earlier supervised mixture with one machine-checkable constraint appended to
each, shipped with the constraint's checker name and arguments and with no response. From
`allenai/RLVR-IFeval` at revision `47c03c73621c4aab2b824b7818681117d662770e`, files
`data/train-00000-of-00001.parquet`. 5366 rows here, of which 5365 also appear in `pool.jsonl`,
2857 of them with constraints. Provenance class `rule-generated`, licence `odc-by`. Its own fields
are messages, ground_truth, dataset, constraint_type, constraint.

Worth knowing. Its constraints are drawn from the same public registry that most of the sets here
draw on, so its constraint sentences collide with the held-out prompts and two thirds of its rows
were removed by the overlap rule. Four of its constraint kinds cannot be stated exactly in this
vocabulary, and those rows keep the prompt with no constraints beside it.

### `sources/conifer`

Conversations built by reframing collected user queries into instructions with layered constraints
and answering them with a large proprietary model. From `ConiferLM/Conifer` at revision
`8f085348895f8b794bbc8e1ccae705473625e156`, files `data/train_sft-00000-of-00001.parquet`. 13606
rows here, of which 13576 also appear in `pool.jsonl`, 89 of them with constraints. Provenance
class `model-generated`, licence `apache-2.0`. Its own fields are prompt, messages, type.

Worth knowing. Both sides are model-written, and only the seed queries trace to people. The
constraints are stated in free prose rather than drawn from a registry, so what is recovered here
is only what the mining patterns recognise.

### `sources/autoif`

Conversations whose instructions were generated from hand-written seed instructions and collected
queries, kept only when a generated checker function and its unit tests accepted the generated
response. From `Post-training-Data-Flywheel/AutoIF-instruct-61k` at revision
`0705aa867cce36d595123cb34f4a35281e6acc7c`, files `data/train-00000-of-00001.parquet`. 59819 rows
here, of which 37386 also appear in `pool.jsonl`, 600 of them with constraints. Provenance class
`model-generated`, licence `apache-2.0`. Its own fields are system, tools, messages,
conversation_id.

Worth knowing. The generated checkers are not shipped, so the constraints here are recovered by
mining like any other prose set. The publishing account is not the laboratory that wrote the
method.

### `sources/ultraif`

Instructions composed by a constraint-composing model over collected seed queries, answered by an
open 8B instruct model. From `kkk-an/UltraIF-sft-175k` at revision
`1c14ef537756de2a41ee75a61c34711719f18d74`, files `UltraIF_llama31_8B_generated_sft_175k.jsonl`.
181082 rows here, of which 178315 also appear in `pool.jsonl`, 875 of them with constraints.
Provenance class `model-generated`, licence `cc-by-4.0`. Its own fields are instruction, output,
history.

Worth knowing. Both sides are model-written. Rows carry a prior conversation in history, which the
rewritten rows drop in favour of the final instruction and its answer, and a noticeable minority
of the seed queries are not in English.

### `sources/personas_if`

Prompts written by expanding a persona description into a request with two to four constraints
attached, answered by a large model. From `allenai/tulu-3-sft-personas-instruction-following` at
revision `fe0c7d350c9b4542b8d829a6f1daa1c259f0ba0e`, files `data/train-00000-of-00001.parquet`.
27479 rows here, of which 27461 also appear in `pool.jsonl`, 3267 of them with constraints.
Provenance class `model-generated`, licence `odc-by`. Its own fields are id, prompt, messages,
constraints.

Worth knowing. The constraint taxonomy is deliberately copied from the public registry, and the
constraints ship as free-text lines rather than as checker arguments, so they are recovered here
only by mining.

### `sources/built`

A prompt of one of the human sets with one to three checkable instructions sampled from the
registry and stated in words written for this pool, shipped with the instruction ids and the
checker arguments and no response. Built here from the rows of the human sources above. 20066 rows
here, of which 20066 also appear in `pool.jsonl`, 20066 of them with constraints. Provenance class
`rule-generated`, licence `inherited`. Its own fields are prompt, seed_prompt,
instruction_sentences, instruction_id_list, kwargs, source, source_repo, source_revision,
source_id, licence.

Worth knowing. The request is human and the constraint sentences are not: they were written here
and sampled at build time, which is why the class is rule-generated. Every row carries the licence
of the set its request came from. Combinations the registry calls contradictory are never sampled
together, but no response was written to prove an item answerable.

## Provenance and licences

Every row carries the class of the way it came to exist, and the rewritten layer holds 28433
human, 256738 model-generated, 25431 rule-generated. Human means a person wrote the text. Model-
generated means a language model wrote the prompt, the response or both, which is true of most
published instruction-following data. Rule-generated means a program attached constraints to text
it did not write. Nothing has been filtered out on its class: the field is there so that you can.

The pool as a whole is offered under `cc-by-sa-4.0`, which is the most restrictive term its
sources compose to, since one human set is share-alike. Each rewritten row carries its own licence
in the `licence` field and each directory under `sources/` is one source, so a subset under a
single licence can be selected. Attribution goes to the volunteers of the open assistant effort,
to the employees who wrote the human instruction set, and to the authors of the generated and
reinforcement sets, each named by its repository above.

## Filtering

Rows whose prompt repeated a prompt of a held-out set, or shared an eight-word run with one, were
removed before publication, from both layers alike: 0 rows on the first rule and 14774 on the
second. That held-out set is not distributed here. The second rule is blunt on data of this kind,
because a constraint stated in a standard sentence is an eight-word run in its own right, so the
reinforcement set, whose constraints come from the same public registry, lost the greater part of
its rows and the sets of ordinary human requests lost almost none. Nothing else was filtered: no
subject, no language and no difficulty was selected for or against.
