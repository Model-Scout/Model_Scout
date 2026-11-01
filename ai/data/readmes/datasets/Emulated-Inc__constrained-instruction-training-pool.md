---
license: cc-by-sa-4.0
pretty_name: Constrained Instruction Training Pool
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

# Constrained instruction training pool

Public prompts for writing tasks, many of them carrying a constraint a program can check, from ten
datasets read at the pinned revisions named below and one layer built here from them. The pool is
laid out twice. Train on either layer or on both.

## `pool.jsonl`

Every source rewritten into one shape, 462652 rows, one JSON object per line, with these fields.

| Field | What it holds |
|---|---|
| `id` | a row identifier unique within this file |
| `prompt` | the request, as a model should receive it |
| `response` | an answer to it where the source ships one, `null` otherwise |
| `instruction_id_list` | the constraints the prompt carries, each named by the checker that decides it, empty when none were recovered |
| `instruction_vocabulary` | one entry per entry of that list, saying which checker family the id belongs to |
| `kwargs` | one object per entry of that list, holding that checker's arguments |
| `instruction_origin` | how the constraints came to be attached: `source`, `mined` or `built`, and empty for a row that carries no constraint |
| `instructions_complete` | true when the listed constraints are every constraint the prompt states |
| `source` | the name of the source directory the row came from |
| `source_repo`, `source_revision` | the dataset and the revision it was read at |
| `source_split`, `source_id` | where the row sits in that set |
| `provenance_class` | how the row came to exist |
| `licence` | the licence of the source it came from |

Of those rows 340408 carry a response and 151239 carry at least one constraint, 321083 constraints
in all. A row with constraints can be scored without a reference answer, by running the named
checker over a generated response with the arguments beside it, which is what the
`instruction_id_list`, `instruction_vocabulary` and `kwargs` fields are for. A row with a response
and no constraints is ordinary supervised data. Rows that carry both are the ones where a response
was available to prove the constraint holds.

The three origins differ in what they guarantee. `source` means the set published the constraint
itself, so it is exactly what the prompt asks. `mined` means the prompt states the constraint in
words that a narrow set of patterns recognised and the row's own response already satisfies the
checker, so the constraint is true of the response by construction, but the prompt may ask for
other things besides. `built` means the request is a human one and the constraints after it were
sampled and written at build time, so they are complete and exact but the wording is not human.
`instructions_complete` records that difference per row, and the seed for the sampling is recorded
in the manifest.

### The constraints

Every constraint in the file is named by one of two checker families. `ifbench` is the harder,
out-of-distribution family: constraints about the shape of the text itself, such as word lengths,
syllable parity, alliteration runs and nesting depth. `ifeval` is the classic family: titles,
bullet counts, forbidden words, casing and the like. A row may mix the two, and
`instruction_vocabulary` says which family each id belongs to, position by position. Both are
decided by reading the response alone, so either can be used as a training reward.

| Family | Checker | Constraints |
|---|---|---|
| `ifbench` | `count:conjunctions` | 703 |
| `ifbench` | `count:keywords_multiple` | 691 |
| `ifbench` | `count:numbers` | 717 |
| `ifbench` | `count:person_names` | 644 |
| `ifbench` | `count:pronouns` | 687 |
| `ifbench` | `count:punctuation` | 740 |
| `ifbench` | `count:unique_word_count` | 683 |
| `ifbench` | `count:word_count_range` | 778 |
| `ifbench` | `count:words_japanese` | 472 |
| `ifbench` | `format:emoji` | 522 |
| `ifbench` | `format:line_indent` | 536 |
| `ifbench` | `format:list` | 495 |
| `ifbench` | `format:newline` | 477 |
| `ifbench` | `format:no_bullets_bullets` | 497 |
| `ifbench` | `format:no_whitespace` | 465 |
| `ifbench` | `format:options` | 443 |
| `ifbench` | `format:output_template` | 676 |
| `ifbench` | `format:parentheses` | 645 |
| `ifbench` | `format:quote_unquote` | 647 |
| `ifbench` | `format:quotes` | 667 |
| `ifbench` | `format:sub-bullets` | 516 |
| `ifbench` | `format:thesis` | 658 |
| `ifbench` | `format:title_case` | 504 |
| `ifbench` | `ratio:overlap` | 446 |
| `ifbench` | `ratio:sentence_balance` | 513 |
| `ifbench` | `ratio:sentence_type` | 523 |
| `ifbench` | `ratio:sentence_words` | 513 |
| `ifbench` | `ratio:stop_words` | 519 |
| `ifbench` | `repeat:repeat_change` | 471 |
| `ifbench` | `repeat:repeat_span` | 444 |
| `ifbench` | `sentence:alliteration_increment` | 514 |
| `ifbench` | `sentence:increment` | 554 |
| `ifbench` | `sentence:keyword` | 674 |
| `ifbench` | `words:alphabet` | 548 |
| `ifbench` | `words:consonants` | 498 |
| `ifbench` | `words:keywords_specific_position` | 5436 |
| `ifbench` | `words:last_first` | 507 |
| `ifbench` | `words:no_consecutive` | 524 |
| `ifbench` | `words:odd_even_syllables` | 566 |
| `ifbench` | `words:palindrome` | 555 |
| `ifbench` | `words:paragraph_last_first` | 514 |
| `ifbench` | `words:prime_lengths` | 537 |
| `ifbench` | `words:repeats` | 646 |
| `ifbench` | `words:start_verb` | 682 |
| `ifbench` | `words:vowel` | 489 |
| `ifbench` | `words:words_position` | 707 |
| `ifeval` | `change_case:capital_word_frequency` | 5194 |
| `ifeval` | `change_case:english_capital` | 5680 |
| `ifeval` | `change_case:english_lowercase` | 13141 |
| `ifeval` | `combination:two_responses` | 2576 |
| `ifeval` | `detectable_content:number_placeholders` | 19441 |
| `ifeval` | `detectable_content:postscript` | 19498 |
| `ifeval` | `detectable_format:constrained_response` | 1775 |
| `ifeval` | `detectable_format:json_format` | 2407 |
| `ifeval` | `detectable_format:multiple_sections` | 8438 |
| `ifeval` | `detectable_format:number_bullet_lists` | 19395 |
| `ifeval` | `detectable_format:number_highlighted_sections` | 25655 |
| `ifeval` | `detectable_format:title` | 16677 |
| `ifeval` | `keywords:existence` | 24666 |
| `ifeval` | `keywords:forbidden_words` | 7607 |
| `ifeval` | `keywords:frequency` | 22221 |
| `ifeval` | `keywords:letter_frequency` | 5849 |
| `ifeval` | `language:response_language` | 4134 |
| `ifeval` | `length_constraints:nth_paragraph_first_word` | 5444 |
| `ifeval` | `length_constraints:number_paragraphs` | 9222 |
| `ifeval` | `length_constraints:number_sentences` | 33676 |
| `ifeval` | `length_constraints:number_words` | 14614 |
| `ifeval` | `punctuation:no_comma` | 5701 |
| `ifeval` | `startend:end_checker` | 11382 |
| `ifeval` | `startend:quotation` | 5447 |

## `sources/`

The same data untouched, 703711 rows, one directory per source, holding the files at the paths, in
the formats and with the columns its own repository publishes. Nothing here was renamed, reshaped,
reordered or deduplicated. Use this layer if you want a field the rewritten one drops, such as the
later turns of a conversation, the reviewer rankings of the volunteer trees, the raw constraint
sentences of the reinforcement sets or the per-constraint scores of the generated sets, or if you
would rather pair prompts with constraints yourself.

## The sources

### `sources/dolly`

Instruction and response pairs written by several thousand employees of one company across seven
task categories, with reference passages copied from Wikipedia for the categories that need them.
From `databricks/databricks-dolly-15k` at revision `bdd27f4d94b9c1f951818a7da7fd7aeea5dbff1a`,
files `databricks-dolly-15k.jsonl`. 15011 rows here, of which 14793 also appear in `pool.jsonl`, 0
of them with constraints. Provenance class `human`, licence `cc-by-sa-3.0`. Its own fields are
instruction, context, response, category.

Worth knowing. The contributors were told not to use a language model for either side, so both
sides are human, but the writing is question answering and summarising rather than constrained
writing, so almost no row states a constraint a checker can decide. Its value here is as a seed
for the built layer.

### `sources/oasst1`

Message trees from a volunteer effort to build an assistant corpus by hand, in thirty-five
languages, each message reviewed and ranked by other volunteers. From `OpenAssistant/oasst1` at
revision `fdf72ae0827c1cda404aff25b6603abec9e3399b`, files
`data/train-00000-of-00001-b42a775f407cee45.parquet`,
`data/validation-00000-of-00001-134b8fd0c89408b6.parquet`. 88830 rows here, of which 10225 also
appear in `pool.jsonl`, 1 of them with constraints. Provenance class `human`, licence
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
`data/validation-00000-of-00001-1deeef95c3248fe0.parquet`. 135166 rows here, of which 3433 also
appear in `pool.jsonl`, 0 of them with constraints. Provenance class `human`, licence
`apache-2.0`. Its own fields are the same columns as the earlier release.

Worth knowing. It contains the earlier release, so the rewritten rows of the two overlap heavily
and the duplicates are dropped in favour of the earlier one.

### `sources/if_multi`

Prompts drawn from an earlier supervised mixture with up to five machine-checkable constraints
appended to each, shipped with the constraints' checker names and arguments and with no response.
From `allenai/IF_multi_constraints_upto5` at revision `2e3a77407b7fce69f95b248d64a884e3ae1c2423`,
files `data/train-00000-of-00001.parquet`. 87591 rows here, of which 87588 also appear in
`pool.jsonl`, 67421 of them with constraints. Provenance class `rule-generated`, licence `odc-by`.
Its own fields are key, messages, ground_truth, dataset, constraint_type, constraint.

Worth knowing. Its fifty-four constraint kinds are the twenty-five classic ones and twenty-nine
newer ones, and the newer twenty-nine are a different family from the fifty-eight this package
checks: exactly one of them, the keyword at a given word of a given sentence, is the same
constraint under a different name and is the only id here that translates into this package's own
vocabulary. The rest of what it publishes enters as classic ids, and twenty-eight kinds translate
into neither vocabulary and are dropped with the reason recorded.

### `sources/rlvr_ifeval`

Prompts drawn from an earlier supervised mixture with one machine-checkable constraint appended to
each, shipped with the constraint's checker name and arguments and with no response. From
`allenai/RLVR-IFeval` at revision `47c03c73621c4aab2b824b7818681117d662770e`, files
`data/train-00000-of-00001.parquet`. 13754 rows here, of which 13751 also appear in `pool.jsonl`,
11256 of them with constraints. Provenance class `rule-generated`, licence `odc-by`. Its own
fields are messages, ground_truth, dataset, constraint_type, constraint.

Worth knowing. Its constraints are the classic twenty-five, so its rows enter under classic ids.
Four of its constraint kinds cannot be stated exactly in either vocabulary, and those rows keep
the prompt with no constraints beside it. Its prompts come from the same upstream mixture as the
larger set above, so the two overlap and the deduplication drops the later copy.

### `sources/ifeval_like`

Prompts generated by a 72B instruct model in the style of the classic constraint registry, kept
only where the model's own response passed every checker, shipped with the constraint ids and the
checker arguments. From `argilla/ifeval-like-data` at revision
`56505d1771e36fa5aa07aa9a1b39008fe60a8487`, files `filtered/train-00000-of-00001.parquet`. 56325
rows here, of which 51584 also appear in `pool.jsonl`, 51581 of them with constraints. Provenance
class `model-generated`, licence `other`. Its own fields are key, prompt, response,
instruction_id_list, kwargs, prompt_level_strict_acc, inst_level_strict_acc,
prompt_level_loose_acc, inst_level_loose_acc.

Worth knowing. Its licence tag is the word other, and the tag's name points at the generating
model's own licence rather than at a data licence, so its rows carry that model's terms as well as
this pool's. The filtered configuration keeps only what a 72B model already got right, which
bounds what it can teach.

### `sources/personas_if`

Prompts written by expanding a persona description into a request with two to four constraints
attached, answered by a large model. From `allenai/tulu-3-sft-personas-instruction-following` at
revision `fe0c7d350c9b4542b8d829a6f1daa1c259f0ba0e`, files `data/train-00000-of-00001.parquet`.
29980 rows here, of which 29962 also appear in `pool.jsonl`, 47 of them with constraints.
Provenance class `model-generated`, licence `odc-by`. Its own fields are id, prompt, messages,
constraints.

Worth knowing. The constraint taxonomy is deliberately copied from the classic registry, and the
constraints ship as free-text lines rather than as checker arguments, so they are recovered here
only by mining.

### `sources/conifer`

Conversations built by reframing collected user queries into instructions with layered constraints
and answering them with a large proprietary model. From `ConiferLM/Conifer` at revision
`8f085348895f8b794bbc8e1ccae705473625e156`, files `data/train_sft-00000-of-00001.parquet`. 13606
rows here, of which 13576 also appear in `pool.jsonl`, 1 of them with constraints. Provenance
class `model-generated`, licence `apache-2.0`. Its own fields are prompt, messages, type.

Worth knowing. Both sides are model-written, and only the seed queries trace to people. The
constraints are stated in free prose rather than drawn from a registry, so what is recovered here
is only what the mining patterns recognise.

### `sources/autoif`

Conversations whose instructions were generated from hand-written seed instructions and collected
queries, kept only when a generated checker function and its unit tests accepted the generated
response. From `Post-training-Data-Flywheel/AutoIF-instruct-61k` at revision
`0705aa867cce36d595123cb34f4a35281e6acc7c`, files `data/train-00000-of-00001.parquet`. 61477 rows
here, of which 38515 also appear in `pool.jsonl`, 22 of them with constraints. Provenance class
`model-generated`, licence `apache-2.0`. Its own fields are system, tools, messages,
conversation_id.

Worth knowing. The generated checkers are not shipped, so the constraints here are recovered by
mining like any other prose set. The publishing account is not the laboratory that wrote the
method.

### `sources/ultraif`

Instructions composed by a constraint-composing model over collected seed queries, answered by an
open 8B instruct model. From `kkk-an/UltraIF-sft-175k` at revision
`1c14ef537756de2a41ee75a61c34711719f18d74`, files `UltraIF_llama31_8B_generated_sft_175k.jsonl`.
181067 rows here, of which 178321 also appear in `pool.jsonl`, 6 of them with constraints.
Provenance class `model-generated`, licence `cc-by-4.0`. Its own fields are instruction, output,
history.

Worth knowing. Both sides are model-written. Rows carry a prior conversation in history, which the
rewritten rows drop in favour of the final instruction and its answer, and a noticeable minority
of the seed queries are not in English.

### `sources/built`

A prompt of one of the human sets with one or two checkable constraints of the out-of-distribution
vocabulary sampled and stated in words written for this pool, shipped with the constraint ids and
the checker arguments and no response. Built here from the rows of the human sources above. 20904
rows here, of which 20904 also appear in `pool.jsonl`, 20904 of them with constraints. Provenance
class `rule-generated`, licence `the licence of the request's source, carried on each row`. Its
own fields are prompt, seed_prompt, instruction_sentences, instruction_id_list,
instruction_vocabulary, kwargs, source, source_repo, source_revision, source_id, licence.

Worth knowing. The request is human and the constraint sentences are not: they were written here
and sampled at build time, which is why the class is rule-generated. Every row carries the licence
of the set its request came from. Constraints that fix the whole surface of a response are never
paired with one another and constraints that refer to the request itself are never paired with
anything, but no response was written to prove an item answerable: the checkers of this vocabulary
are not constructively satisfiable in general.

## Provenance and licences

Every row carries the class of the way it came to exist, and the rewritten layer holds 28451
human, 311958 model-generated, 122243 rule-generated. Human means a person wrote the text. Model-
generated means a language model wrote the prompt, the response or both, which is true of most
published instruction-following data. Rule-generated means a program attached constraints to text
it did not write. Nothing has been filtered out on its class: the field is there so that you can.

The pool as a whole is offered under `cc-by-sa-4.0`, which is the most restrictive term its
sources compose to, since one human set is share-alike. Each rewritten row carries its own licence
in the `licence` field and each directory under `sources/` is one source, so a subset under a
single licence can be selected. Attribution goes to the volunteers of the open assistant effort,
to the employees who wrote the human instruction set, and to the authors of the generated and
reinforcement sets, each named by its repository above. One source carries a language model's own
licence rather than a data licence, which is noted in its section.

## Filtering

Rows in which the user repeated a prompt of a reserved set, or shared an eight-word run with one,
were removed before publication, from both layers alike, and every user turn of a conversation was
read for this and not only the last one: 0 rows on the first rule, 9114 on the second and 12 more
as the rest of a message tree one of them came from. That reserved set is not distributed here.
The second rule is blunt on data of this kind, because a constraint stated in a standard sentence
is an eight-word run in its own right, so any set that draws its constraint sentences from the
same registry loses rows to it. Nothing else was filtered: no subject, no language and no
difficulty was selected for or against.
