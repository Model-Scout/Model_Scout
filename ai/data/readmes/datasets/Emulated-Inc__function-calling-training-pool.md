---
license: cc-by-4.0
pretty_name: Function Calling Training Pool
language:
- af
- am
- ar
- az
- bn
- ca
- cy
- da
- de
- el
- en
- es
- fa
- fi
- fr
- he
- hi
- hu
- hy
- id
- is
- it
- ja
- jv
- ka
- km
- kn
- ko
- lv
- ml
- mn
- ms
- my
- nb
- nl
- pl
- pt
- ro
- ru
- sl
- sq
- sv
- sw
- ta
- te
- th
- tl
- tr
- ur
- vi
- zh
task_categories:
- text-generation
size_categories:
- 100K<n<1M
---

# Function calling training pool

Public function-calling data from five datasets, read at the pinned revisions named below and laid
out twice. Train on either layer or on both.

## `pool.jsonl`

Every source rewritten into one shape, 195624 rows, one JSON object per line, with these fields.

| Field | What it holds |
|---|---|
| `id` | a row identifier unique within this file |
| `query` | the user's request, as its source publishes it |
| `functions` | the declarations offered with the request, as a list of objects |
| `calls` | the gold call or calls, each a `name` and an `arguments` object |
| `gold` | which kind of answer the row carries: `call`, `no_call` or `none` |
| `response` | the prose answer, on rows whose gold answer is not a call |
| `language` | the language of the request |
| `source` | the name of the source directory the row came from |
| `source_repo`, `source_revision` | the dataset and the revision it was read at |
| `source_file`, `source_row` | the raw file it came from and its row number there |
| `source_id` | the identifier its source gives the row, where it gives one |
| `provenance_class` | how the row came to exist |
| `licence` | the licence of the source it came from |

Which rows carry which. `gold` is `call` on 166268 rows, where `calls` holds one or more calls and
`response` is null. It is `no_call` on 29344 rows, where the right answer is to make no call,
`calls` is an empty list and `response` holds the prose answer the source gives instead, which is
usually a refusal or a request for a missing argument. It is `none` on 12 rows, where the source
carries no answer for the request or its answer could not be read, and `calls` is null: those rows
are a request and a catalogue with no key, which is enough to sample from and not enough to
imitate. Every row carries `query` and a non-empty `functions`.

The declarations are kept in the shape each source publishes them in rather than converted to one
schema, because the sources disagree about how to write a type and converting between them would
invent information. Rows are deduplicated across sources on the request together with the names of
the functions offered with it, keeping the first source that carries it in the order of the
sections below.

## `sources/`

The same data untouched, 297996 rows, one directory per source, holding the files at the paths, in
the format and with the fields its own repository publishes. Nothing here was renamed, reshaped,
reordered or deduplicated, and the later turns of the multi-turn conversations that the rewritten
layer cuts to their first exchange are all still here. Use this layer if you want a field the
rewritten one drops, such as the acceptable-value lists of the MASSIVE answer keys, the rejected
answers in the preference split, or the tool results that come back mid conversation.

## The sources

### `sources/massive_agents`

Voice-assistant requests written by crowdworkers, localised into 51 further languages by
professional human translators, with human intent and slot annotation, turned mechanically into
calls against 55 hand-written function declarations. From `AmazonScience/massive-agents` at
revision `b6156972182bdf34e68c5b5dfbfe6d30db82f104`, files
`massive-full-converted-all-langs-with-id/af-ZA/input.jsonl`,
`massive-full-converted-all-langs-with-id/af-ZA/golden.jsonl`,
`massive-full-converted-all-langs-with-id/am-ET/input.jsonl` and 101 more. 47015 rows here, of
which 46049 also appear in `pool.jsonl`. Provenance class `human`, licence `cc-by-4.0`. Its own
fields are question, function as the 55 declarations offered with every request, gt as the answer
key, id, language and test_category in every input.jsonl, and the same answer key on its own in
every golden.jsonl, one line per request.

Rewritten. In `pool.jsonl`, the request is question, the declarations are function, and the call
is gt read as one name with the first acceptable value of each argument, dropping any argument
whose first acceptable value is the empty string.

Worth knowing. Every answer key is a single call, so this source teaches one call at a time and
never several at once. The 55 declarations are repeated in full on every row, which is most of its
size on disk. Its answer key gives a list of acceptable values per argument rather than one value,
and an empty string in that list means the argument may be left out, which the rewritten layer
resolves by taking the first value.

### `sources/apigen`

Requests and calls written by large language models over real API documentation and over
synthesised Python functions, then filtered by a format check, by really executing the call and by
a semantic check. The half marked xLAM was written by DeepSeek-V2-Chat and Mixtral-8x22B-Instruct
over documentation collected from a public API marketplace, and the other half by
Qwen2.5-72B-Instruct and Llama-3.1-70B-Instruct over invented functions. From
`argilla/apigen-function-calling` at revision `170a8a7e0832101f2495a00c9ad9ba1821d3a9b0`, files
`data/train-00000-of-00001.parquet`. 106350 rows here, of which 103014 also appear in
`pool.jsonl`. Provenance class `model-generated`, licence `cc-by-4.0`. Its own fields are query,
tools, answers, id, func_name, func_desc, hash_id, model_name, origin.

Rewritten. In `pool.jsonl`, the request is query, the declarations are tools parsed out of its
JSON string, and the calls are answers parsed the same way, each already a name with an arguments
object. An answers column holding a sentence rather than a call list is read as no call, and the
sentence becomes the response.

Worth knowing. Tools and answers are JSON held inside strings rather than structured columns, and
the declarations use a compact argument shape with a description, a type name and a default rather
than a JSON schema. Roughly half the rows ask for more than one call, which is the only large
source in the pool that does. 6000 of its rows answer in a sentence rather than with a call,
saying that the request cannot be answered with what was offered or that an argument is missing,
and 2068 of those offer no declaration at all and are left out of the rewritten layer. The
published human check of the pipeline covered 600 of the 60000 rows it contributed.

### `sources/toolace`

Dialogues written by two language-model agents, one playing a user and one playing an assistant,
over a catalogue of 26507 interfaces that is partly collected and partly synthesised, checked
afterwards by rule-based and model-based verifiers. From `Team-ACE/ToolACE` at revision
`6bda777c88d21e5a204703c1ee45597a8fa4f734`, files `data.json`. 11009 rows here, of which 10227
also appear in `pool.jsonl`. Provenance class `model-generated`, licence `apache-2.0`. Its own
fields are system, holding the instruction and the declarations as a JSON list, and conversations,
a list of turns each with from and value.

Rewritten. In `pool.jsonl`, the declarations are the JSON list at the end of system, the request
is the first user turn, and the calls are the first assistant turn parsed as a bracketed list of
call expressions, with a turn that is prose rather than a call read as no call.

Worth knowing. The paper never names the model that wrote it, so its terms could not be checked
beyond the apache-2.0 tag on the repository. Its calls are written as a Python-like call string
rather than as JSON, and its function names contain spaces, which the rewritten layer parses.
10500 of its 11300 rows are a single exchange and the rest run on for several turns, of which the
rewritten layer keeps the first exchange only. 518 of its rows write their declarations in a
second system format under a different marker and with different field names, and 248 more offer
no declaration at all, and both are left out of the rewritten layer and kept here.

### `sources/when2call`

Requests rewritten by Mixtral 8x22B from an existing model-written function-calling set, paired
with the answer a careful assistant should give when the offered functions do not cover the
request or when an argument is missing. From `nvidia/When2Call` at revision
`0582f7749df63a96fdc3070932e83e72396ace53`, files `train/when2call_train_sft.jsonl`,
`train/when2call_train_pref.jsonl`. 23839 rows here, of which 14926 also appear in `pool.jsonl`.
Provenance class `model-generated`, licence `cc-by-4.0`. Its own fields are tools as a list of
JSON strings and messages as a user turn and an assistant turn in the supervised split, and tools,
a user turn, a chosen_response and a rejected_response in the preference split.

Rewritten. In `pool.jsonl`, the request is the user turn, the declarations are tools with each
JSON string parsed, and the answer is the assistant turn in the supervised split and
chosen_response in the preference split, read as calls when it carries a TOOLCALL block and as no
call otherwise.

Worth knowing. The whole supervised split answers in prose rather than with a call, on purpose,
and two thirds of the preference split does the same, so this source teaches restraint and
clarification and teaches almost no call syntax. Its two test splits are not in the pool.

### `sources/glaive`

Assistant dialogues produced by a commercial synthetic-data platform, each with a system message
offering one or two functions and a conversation that either calls one of them or explains that it
cannot help. From `glaiveai/glaive-function-calling-v2` at revision
`e7f4b6456019f5d8bcb991ef0dd67d8ff23221ac`, files `glaive-function-calling-v2.json`. 109783 rows
here, of which 21408 also appear in `pool.jsonl`. Provenance class `model-generated`, licence
`apache-2.0`. Its own fields are system, the instruction with the declarations appended, and chat,
the dialogue as one block of text.

Rewritten. In `pool.jsonl`, the declarations are the JSON objects appended to system, the request
is the first USER block of chat, and the calls are the ASSISTANT block that follows it, read as a
call when it opens with a functioncall marker and as no call otherwise.

Worth knowing. Its card carries no prose at all and the model that wrote it is not named anywhere,
so the apache-2.0 tag is the only statement of terms there is. 34598 of its rows offer no function
at all and are left out of the rewritten layer for that reason. Its calls are written as JSON
whose arguments field is itself a JSON string in single quotes, which the rewritten layer parses.

## Provenance and licences

One source was written by people and four were written by models, and every row says which in its
`provenance_class` field. The MASSIVE conversion is the human one: crowdworkers wrote the
requests, professional translators localised them, annotators labelled the intent and the slots,
and the authors hand-wrote the 55 declarations, so its answer keys are human throughout. The other
four are `model-generated`, and they differ in how real the interfaces behind them are: the APIGen
merge and When2Call are built over documentation collected from a real API marketplace, ToolACE
over a catalogue that is partly collected and partly synthesised, and Glaive over functions it
invented. There is no rule-generated data in the pool.

Say plainly what that means for the keys. On the four model-written sources the gold call was
itself written by a language model, so it is only as correct as that model was on the day the set
was built. The APIGen rows are the best of them, because that pipeline filtered its rows by really
executing the call. The MASSIVE keys are the only ones in the pool that a person wrote.

The pool as a whole is offered under `cc-by-4.0`, which is the most restrictive term its sources
compose to. The sources themselves are cc-by-4.0 for the MASSIVE conversion, for the APIGen merge
and for When2Call, and apache-2.0 for ToolACE and for Glaive. Nothing in the pool is
non-commercial and nothing in it is share-alike. Each rewritten row carries its own licence in the
`licence` field and each directory under `sources/` is one source, so a single-licence subset can
be selected. Attribution goes to Amazon Science for the MASSIVE conversion and through it to the
authors of MASSIVE and SLURP, to Argilla and Salesforce for the APIGen merge, to the ToolACE
authors, to NVIDIA for When2Call and to Glaive AI.

## Filtering

Near-duplicate rows were removed before publication, from both layers alike, measured against a
reserved list of requests that is not distributed here: a word 8-gram overlap check on the request
text removed 6682 rows and an exact-match check on the whole normalised request removed 4 more.
Nothing else was filtered: no language, no domain, no source's weaker half and no difficulty was
selected for or against, so the pool still holds the rows that answer in prose rather than with a
call, and the `gold` field is how to select what you want.
