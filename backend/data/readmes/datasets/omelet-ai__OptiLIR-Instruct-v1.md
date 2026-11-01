---
license: cc-by-4.0
language:
- ko
- en
pretty_name: OptiLIR-Instruct-v1
task_categories:
- text-generation
tags:
- semantic-parsing
- optimization
- operations-research
size_categories:
- 10K<n<100K
annotations_creators:
- machine-generated
language_creators:
- machine-generated
source_datasets:
- original
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train.jsonl
  - split: validation
    path: data/validation.jsonl
  - split: test
    path: data/test.jsonl
---

# OptiLIR-Instruct-v1

Each row pairs a user's optimization request with its IR in OptiLIR (Optimization-oriented Language
Intermediate Representation; see [Terms](#terms)), a short line-based text that states the objectives and
constraints of the request over a fixed domain vocabulary. Requests are in Korean, English, or a mix of the
two. Most are a single user turn; some are three turns, where the user answers a clarification question
that the system asked about the first turn.

A parser model reads the conversation and writes the IR. A deterministic grounder then maps the IR onto
the capabilities that the optimization server declares and returns one of three decisions:

- `execute`: the request maps onto declared objectives and constraints (refs with strengths, weights and
  values);
- `clarify`: the system must ask the user, because the IR has a hole, names a quantity without its
  aggregation, has no objective, does not determine what to optimize (`CLARIFY(intent)`), or names a way of
  combining objectives that the server does not offer;
- `unsupported`: the request is declined, because it has no optimization intent, needs a meaning the server
  does not declare, or needs a declared capability that cannot run here (input data the server does not
  supply, a configuration it does not realize, a strict priority order between objectives).

The model only writes what the user meant. Whether the request can be executed is decided by the grounder,
not by the model, so the IR must stay faithful even when the meaning is unsupported. The grounder is not
part of this dataset; `gold_decision` records its output for each row. Code (the IR parser and grammar,
the grounder, training and evaluation): [omelet-ai/OptiLIR](https://github.com/omelet-ai/OptiLIR).
Adapters trained on this dataset: [omelet-ai/OptiLIR-Qwen3-8B](https://huggingface.co/omelet-ai/OptiLIR-Qwen3-8B)
and [omelet-ai/OptiLIR-Gemma-4-12B](https://huggingface.co/omelet-ai/OptiLIR-Gemma-4-12B).

The dataset has 14,212 rows in three domains: vehicle routing (`routing`), nurse scheduling
(`nurse`) and retail inventory (`retail`).

## Task

- Input: the system prompt of the row's domain (`prompts/<domain>.txt`), followed by `messages`.
- Output: the `ir` string and nothing else.

The system prompt contains a summary of the IR grammar, the domain vocabulary (populations, measures,
accessors, units) and the capability forms, that is, how the server writes each declared objective and
constraint. The released adapters were trained and evaluated with these prompts, their vocabulary listing
shuffled per row and seeded by the row id (`system_prompt(domain, seed=id, forms=True)` in the code
repository); at inference, use the files unchanged.
`grammar/<domain>.ebnf` is an EBNF (xgrammar / GBNF style) for the domain's IR; it can be used for
grammar-constrained decoding.

`registry.json` is the registry that produced `gold_decision`, with `binding.projections` and
`binding.required_paths` left empty in every domain (neither grounding nor scoring reads them). With
`EXECUTION_LLM_REGISTRY` set to its path, `decide` in the code repository reproduces each row's
`gold_decision` from its gold IR and user turns, and `scripts/evaluate.py` also reports decision match:

```bash
export EXECUTION_LLM_REGISTRY="$(python -c 'from huggingface_hub import hf_hub_download
print(hf_hub_download("omelet-ai/OptiLIR-Instruct-v1", "registry.json", repo_type="dataset"))')"
```

## IR format

One item per line. Objective and constraint lines are frames; the `COMPOSE` line, `UNEXPRESSED` lines and
the whole-output answers are not:

- objective frames: `MINIMIZE( term )` or `MAXIMIZE( term )`. The term usually aggregates a measure over a
  population, for example `SUM(x0 in routes: travel_distance(x0))`; some objectives are a bare measure,
  for example the retail `MAXIMIZE( profit )`;
- constraint frames: `EACH(x in P): body`, `AND( ... )` over several comparisons, a bare comparison such as
  the vehicle count `COUNT(x1 in routes) <= 6`, or `HOLE(constraint, family)` (a rule named only loosely);
- marks: `[HARD]` (the user made it mandatory) or `[SOFT]` (the user made it preferential) at the start of
  a frame, and no mark when the user did not say. Marks are mostly on constraint frames, but in routing four
  capabilities that the server declares as constraints are written as `MINIMIZE` frames (priority-weighted
  arrival, the zone count and two region preferences), and those frames can take marks too;
- a `COMPOSE(...)` line (`weighted_sum`, `lexicographic` or `product`) when the user states how several
  objectives combine;
- holes for what the user left open: `HOLE(value)` (a bound without a number), `HOLE(measure, family, x)`
  (an unresolved quantity), `EACH(x in HOLE(scope))` (an unstated per-unit scope),
  `HOLE(constraint, family)` (see above) and `UNSPECIFIED(x in P: m(x))` (a quantity named without its
  aggregation). A family is a group of measures or rules listed in the prompt. Every row with a hole is
  `clarify`;
- `UNDECIDED` in place of a bound's value that the user has not decided yet. The prompt lists it with the
  holes, but it is not asked about: the grounder leaves the bound out and grounds the rest, with a notice
  (138 of the 139 such rows execute);
- `UNEXPRESSED(class, side)` in place of a stated requirement that the grammar cannot express (class
  `condition`, `relative`, `literal` for a clock time or date, or `other`; side `objective` or
  `constraint`);
- whole-output answers: `NO_INTENT` (no optimization request, for example a status question) and
  `CLARIFY(intent)` (an optimization request whose objective the conversation does not determine).

Bound variables are written `x0, x1, ...` in order of first binding across the frames.

## Terms

- **OptiLIR** (Optimization-oriented Language Intermediate Representation): the line-based language the
  parser model writes, used both for the capability forms in the prompt and for the model's output. The
  system prompt and the code (`execution_llm.tier2`) use its earlier name, Tier-2 IR; tier 1 was a flat
  record per capability (measure, aggregation, direction or comparator, unit) and is not part of this
  release. Below, "IR" means OptiLIR.
- **Frame**: one objective line (`MINIMIZE(...)`, `MAXIMIZE(...)`) or one constraint line (`EACH(...)`,
  `AND(...)`, a bare comparison such as a vehicle count, or `HOLE(constraint, family)`). `COMPOSE`,
  `UNEXPRESSED`, `NO_INTENT` and `CLARIFY(intent)` lines are not frames; the prompt's "one frame per line"
  means one item per line. The form a frame matches decides which capability it grounds to, not its first
  word: in routing, four capabilities the server declares as constraints are written as `MINIMIZE` frames.
- **Mark**: `[HARD]` (mandatory) or `[SOFT]` (preferential) at the start of a frame, written only when the
  user says so; otherwise the server's default applies. The code calls it `hardness`; decisions call it
  `strength`.
- **COMPOSE line**: how several objectives combine (`weighted_sum`, `lexicographic`, `product`). Without
  one, the server's default applies.
- **Hole**: a marker for something the user left unstated, so that the parser never guesses: `HOLE(value)`,
  `HOLE(measure, family, x)`, `HOLE(scope)`, `HOLE(constraint, family)`, and `UNSPECIFIED(...)` (a quantity
  named without its aggregation). A family is a group of measures or rules listed in the prompt. A hole
  leads to `clarify`. The prompt's "Holes" heading also lists `UNDECIDED`, which behaves differently.
- **UNDECIDED**: a bound the user wants but has not set a value for yet. The system does not ask: the bound
  is left out, the rest is grounded as usual, and a notice says so.
- **UNEXPRESSED(class, side)**: a clear requirement that the IR cannot express (class: what kind, such as a
  literal clock time or date). The request is `unsupported`, unless another line needs a clarification,
  which is asked first.
- **NO_INTENT** / **CLARIFY(intent)**: the whole output when there is no optimization request / when it
  does not determine what to optimize.
- **Vocabulary**: the domain names the prompt lists: populations (sets such as `routes`), measures
  (quantities such as `travel_distance`), accessors (per-item data such as `capacity`) and units. "Sort"
  there means value type. In code, a domain's vocabulary and capability forms together are its surface
  (`execution_llm.tier2.domains.SURFACES`).
- **Capability**: an objective or constraint the server declares. Its **capability form** is how it is
  written in IR, as listed in the prompt (class `Signature` in the code). Its **ref** is its id in
  decisions, such as `objective:distance_cost`. Refs never appear in the IR, and their names can differ from
  the IR's names.
- **Slot**: a value a capability takes, such as the 80 km of a distance limit; written `$name` in a capability
  form. The registry declares each slot's type, unit, default and bounds (its value policy).
- **Deferred**: a declared capability whose input data the server does not supply; a request for it is
  declined with `required_primitive_absent`.
- **Server**, **registry**: the optimization service of a domain, and the JSON file that lists what it
  declares. The registry behind `gold_decision` is `registry.json` in this repository; decisions follow
  whichever registry you supply.
- **Grounder**: the deterministic code (`execution_llm.grounding`) that turns an IR into one decision
  against a registry.
- **Decision**: `execute` (run with these refs and values), `clarify` (ask the user) or `unsupported`
  (decline). Clarify and unsupported decisions carry a reason code; together they are called abstentions.
- **Fleet**: a stated vehicle count is returned beside the decision (`fleet`), not in it.
- **Gold**: a row's reference label: the gold IR (`ir`) and the gold decision (`gold_decision`: what
  `decide` returns for the gold IR and the row's user turns).
- **Stratum**: the recipe that produced a row. It records where the row came from, not its outcome.
- **Held-out capability**: upper bounds on route duration. Its form is in the prompt, but no training row
  uses it; the held-out test subset does (928 rows; 822 of them name `constraint:max_duration` in
  `gold_decision`).
- **Capability forms in the prompt** (`forms=True`): `system_prompt(domain, forms=True)` includes the
  capability forms, and the adapters were trained with it (each training row with its own shuffled order,
  `seed=<row id>`). The default, `forms=False`, leaves the forms out.
- **Parse rate**, **IR match**, **decision match**: the output is accepted by the IR parser; it equals the
  gold IR once both are in normal form; its grounded decision equals the gold decision.
- **Normal form**: values in base units (80 km = 80000 m); the quantity on the left of a comparison; an
  upper bound on a MAX (or a lower bound on a MIN) written as the same bound under EACH; AND items flattened, sorted and deduplicated;
  TOGETHER/OVERLAPS arguments and EACH chains in a fixed order; binders renumbered. For an IR match, frames
  must come in the same order with the same marks; COMPOSE, NO_INTENT and CLARIFY(intent) lines must agree;
  UNEXPRESSED lines are compared regardless of order.

## Examples

Three rows from this release, one per decision kind.

**Example 1: `execute`** (routing, ko, stratum `v4/vehicle`)

```text
user: 총 운행시간 최소화 부탁드립니다. 차량은 반드시 6대 이하입니다
```

IR:

```text
MINIMIZE( SUM(x0 in routes: duration(x0)) )
[HARD] COUNT(x1 in routes) <= 6
```

Gold decision:

```json
{"constraints": [], "data_binding": {"overrides": [], "selections": []}, "kind": "execute", "objectives": {"method": "weighted_sum", "terms": [{"objective_ref": "objective:duration_cost", "weight": "1/1"}]}, "parameters": []}
```

**Example 2: `clarify`** (nurse, mixed, stratum `3.2/1`)

```text
user: Nurses’ preferences를 우선 반영하되, 근무시간에 대한 필수 규정은 꼭 맞춰 주세요.
```

IR:

```text
MAXIMIZE( SUM(x0 in assignments: preference_score(x0)) )
[HARD] HOLE(constraint, hours)
```

Gold decision:

```json
{"candidate_refs": ["constraint:max_hours_per_week", "constraint:min_rest_hours"], "kind": "clarify", "missing_field_refs": [], "reason_code": "ambiguous_capability", "required_inputs": []}
```

**Example 3: `unsupported`** (retail, en, stratum `v4/residual`)

```text
user: Reduce waste by 30% compared with last month
```

IR:

```text
UNEXPRESSED(relative, objective)
```

Gold decision:

```json
{"kind": "unsupported", "reason_code": "semantic_not_declared", "related_refs": []}
```

A stated vehicle count, as in Example 1, is returned beside the decision (`fleet`), not in it, so that
row's `constraints` list is empty.

## Data fields

| Field | Type | Description |
|---|---|---|
| `id` | string | Row id from the source corpus (`<stratum>:<domain>:<hash>`; the 66 hand-written `clarify-contrast` rows use `clarify-20260916:<group>:<case>`, a topic group and a case within it; the date is when they were written). |
| `domain` | string | `routing`, `nurse` or `retail`. |
| `language` | string | `ko`, `en` or `mixed`, computed from the user turns: `mixed` when they contain both Hangul words and Latin-script words (unit symbols such as `km` and `h` are ignored). |
| `messages` | list of `{role, content}` | The conversation, ending with a user turn. An assistant turn, when present, is the system's clarification question. The system prompt is not included. |
| `ir` | string | The target output: the gold IR. |
| `decision_kind` | string | `execute`, `clarify` or `unsupported` (equal to `gold_decision.kind`). |
| `gold_decision` | object | The decision that the grounder's `decide` returns for the gold IR and the row's user turns. `execute`: `objectives` (method and weighted terms), `constraints` (ref, strength, arguments), `parameters`, `data_binding`. `clarify`: `reason_code`, `candidate_refs`, `required_inputs`, `missing_field_refs`. `unsupported`: `reason_code`, `related_refs`. Constraints also carry declared defaults that the IR never states: `exp_factor`, a penalty parameter of routing constraints (11,895 arguments in 7,131 rows, on hard and soft constraints alike), and the weight of a soft constraint (1, except 100 for nurse `constraint:max_consecutive_days`). Refs are the server's ids and can differ from the IR's names: the objective over `travel_distance` is `objective:distance_cost`, a per-route bound on `sec_radius` is `constraint:enclosing_circle_radius`, `delivery_count(x) <= $max_size` is `constraint:delivery_length`, and the `MINIMIZE` frame over `priority_weighted_arrival` is the constraint `constraint:delivery_time_priority`. |
| `stratum` | string | The recipe that produced the row (see Rows by stratum). It records provenance, not the outcome: 183 of the 226 `v3/hole-measure` rows execute. |
| `episode_id` | string or null | Links the rows of one clarification episode: the first turn alone and the full three-turn conversation. 95 of the 110 ids have both rows; 15 have only one (14 a first turn, 1 a three-turn conversation). Null otherwise, also for the 30 hand-written three-turn `clarify-contrast` rows, which have no first-turn row. Keep rows with the same `episode_id` in the same split. |

To build a training example, put the domain prompt first and the IR last:

```python
from datasets import load_dataset
from huggingface_hub import hf_hub_download

REPO = "omelet-ai/OptiLIR-Instruct-v1"
ds = load_dataset(REPO)
prompts = {d: open(hf_hub_download(REPO, f"prompts/{d}.txt", repo_type="dataset"), encoding="utf-8").read()
           for d in ("routing", "nurse", "retail")}

def to_prompt_completion(row):
    return {"prompt": [{"role": "system", "content": prompts[row["domain"]]}] + row["messages"],
            "completion": [{"role": "assistant", "content": row["ir"]}]}

train = ds["train"].map(to_prompt_completion)
```

The snippet uses the prompts as published. The released adapters were trained with the vocabulary listing
shuffled per row; `scripts/train_lora.py` in the code repository does this with `SHUFFLE=1`.

## Splits

Source splits were mapped to release splits as follows:

| Source split | Release split | Rows |
| --- | --- | --- |
| `dev` | `validation` | 880 |
| held-out capability | `test` | 928 |
| `test` | `test` | 988 |
| `train` | `train` | 11416 |

- `validation`: distinct IRs shared with `train`: 0 of 256; refs in its gold decisions that never occur in `train`: none.
- `test`: distinct IRs shared with `train`: 3 of 557; refs in its gold decisions that never occur in `train`: `constraint:max_duration`.
- Clarification episodes split across splits: 0.

The 66 hand-written `clarify-contrast` rows were split by case, not by topic group. Three topic groups
(`routing_time`, `nurse_fairness` and `nurse_rule`) have rows in both train and test, and in each of them
one opening request occurs in both splits: alone or with a continuation in one split, with another
continuation in the other.

### Rows by domain

| Domain | train | validation | test | total |
| --- | --- | --- | --- | --- |
| `nurse` | 2045 | 131 | 269 | 2445 |
| `retail` | 1852 | 165 | 168 | 2185 |
| `routing` | 7519 | 584 | 1479 | 9582 |

### Rows by language

| Language | train | validation | test | total |
| --- | --- | --- | --- | --- |
| `en` | 2783 | 243 | 439 | 3465 |
| `ko` | 7085 | 529 | 1243 | 8857 |
| `mixed` | 1548 | 108 | 234 | 1890 |

### Rows by decision kind

| Decision kind | train | validation | test | total |
| --- | --- | --- | --- | --- |
| `clarify` | 810 | 69 | 182 | 1061 |
| `execute` | 9610 | 771 | 1558 | 11939 |
| `unsupported` | 996 | 40 | 176 | 1212 |

### Rows by reason code

| Reason code | train | validation | test | total |
| --- | --- | --- | --- | --- |
| `(execute)` | 9610 | 771 | 1558 | 11939 |
| `ambiguous_capability` | 379 | 45 | 118 | 542 |
| `composition_choice_required` | 50 | 0 | 0 | 50 |
| `missing_value` | 381 | 24 | 64 | 469 |
| `realization_absent` | 87 | 2 | 0 | 89 |
| `request_out_of_scope` | 53 | 0 | 3 | 56 |
| `required_primitive_absent` | 188 | 0 | 0 | 188 |
| `semantic_not_declared` | 648 | 38 | 173 | 859 |
| `unsupported_composition` | 20 | 0 | 0 | 20 |

- `(execute)`: execute rows, which have no reason code.
- `ambiguous_capability` (clarify): the IR leaves open which capability is meant: a measure, scope or
  constraint hole, `UNSPECIFIED`, or `CLARIFY(intent)`. `candidate_refs` lists the options, even when there
  is only one. It is empty for `CLARIFY(intent)` (4 rows) and for `UNSPECIFIED` over routing `duration`,
  for which the server declares no candidate (76 rows).
- `missing_value` (clarify): a needed value is missing: a `HOLE(value)` on a required slot (34 rows;
  `required_inputs` names the slot), or no objective at all (435 rows; `required_inputs` names the
  `objectives` field).
- `composition_choice_required` (clarify): the user named a way of combining objectives that the server
  does not offer (`COMPOSE(product)`).
- `semantic_not_declared` (unsupported): a meaning the server does not declare, including every
  `UNEXPRESSED` line (207 rows).
- `realization_absent` (unsupported): a related capability is declared (`related_refs`), but not this
  configuration, for example an upper bound on rest between shifts, where the server declares only a
  minimum.
- `required_primitive_absent` (unsupported): the capability is declared, but it needs input data that the
  server does not supply, such as cost tables or regions.
- `request_out_of_scope` (unsupported): `NO_INTENT`.
- `unsupported_composition` (unsupported): a strict priority order between objectives ("first A, then B,
  no trade-off").

The schema defines more clarify codes (`ambiguous_scope`, `missing_composition`, `unit_ambiguity`,
`data_shortage`, `hardness_ambiguity`, `form_choice_required`) that this grounder never emits.

### Rows by stratum

| Stratum | train | validation | test | total |
| --- | --- | --- | --- | --- |
| `2.4/activation` | 7 | 0 | 3 | 10 |
| `2.4/binding_intervention` | 1 | 0 | 0 | 1 |
| `2.4/half_selection` | 3 | 0 | 0 | 3 |
| `2.4/minimal_contrast` | 4 | 0 | 0 | 4 |
| `2.4/near_miss` | 6 | 0 | 1 | 7 |
| `3.1/4` | 27 | 0 | 0 | 27 |
| `3.1/6` | 31 | 10 | 0 | 41 |
| `3.2/1` | 182 | 33 | 0 | 215 |
| `3.3/1` | 100 | 0 | 0 | 100 |
| `clarify-contrast` | 17 | 0 | 49 | 66 |
| `v3/base` | 313 | 44 | 94 | 451 |
| `v3/deferred` | 72 | 0 | 0 | 72 |
| `v3/extra` | 60 | 0 | 0 | 60 |
| `v3/hole-measure` | 127 | 12 | 87 | 226 |
| `v3/hole-scope` | 55 | 12 | 16 | 83 |
| `v3/hole-value` | 0 | 0 | 11 | 11 |
| `v3/multi` | 294 | 42 | 28 | 364 |
| `v3/perturb` | 176 | 8 | 62 | 246 |
| `v4/base` | 393 | 61 | 96 | 550 |
| `v4/combo` | 5577 | 392 | 1001 | 6970 |
| `v4/deferred` | 115 | 0 | 0 | 115 |
| `v4/extra` | 73 | 0 | 10 | 83 |
| `v4/fragment` | 366 | 24 | 45 | 435 |
| `v4/hole-measure` | 6 | 0 | 0 | 6 |
| `v4/hole-scope` | 95 | 5 | 19 | 119 |
| `v4/hole-value` | 15 | 0 | 18 | 33 |
| `v4/multi` | 633 | 71 | 105 | 809 |
| `v4/perturb` | 325 | 25 | 83 | 433 |
| `v4/plain` | 23 | 6 | 18 | 47 |
| `v4/residual` | 176 | 18 | 13 | 207 |
| `v4/scenario` | 297 | 13 | 18 | 328 |
| `v4/short` | 853 | 48 | 54 | 955 |
| `v4/undecided` | 106 | 0 | 27 | 133 |
| `v4/vehicle` | 175 | 2 | 13 | 190 |
| `v4/wide` | 713 | 54 | 45 | 812 |

The `v3/...` and numeric strata are the earlier corpus (1,921 rows, built in September 2026; see "How the
rows were made"). `v3/base`: one declared capability with its values bound. `v3/multi`: one objective with two or three
constraints in one request. `v3/hole-measure`, `v3/hole-scope`, `v3/hole-value`: a measure, a scope or a
value left unstated. `v3/perturb`: one element of a declared form changed, so that the grounder decides
the outcome. `v3/extra`: meanings the vocabulary can express but the server does not declare.
`v3/deferred`: capabilities whose data primitive the server defers. Strata with numeric names
(`2.4/...`, `3.1/...`, `3.2/...`, `3.3/...`) are the 408 rows that the earlier corpus took over from its
first version. The numbers are cells of that version's coverage plan and mean nothing more: execute variants (`3.1`), both
turns of clarification episodes (`3.2`), requests meant to be out of scope or unsupported (`3.3`; 29 of
its 100 rows ended up `clarify`) and contrast probes (`2.4`). `clarify-contrast`: hand-written contrast
cases for clarification, grouped by topic (34 of the 66 rows execute, 17 clarify and 15 are unsupported).

`v4/...` strata come from the meaning-first generator of this release. The names shared with `v3/...`
mean the same recipes. The others: `v4/combo`, one or two objectives with up to three constraints, values
and strengths sampled; `v4/plain`, a quantity named without its aggregation; `v4/fragment`, constraints
stated without an objective; `v4/residual`, a clear requirement the grammar cannot express; `v4/vehicle`,
vehicle-count directives; `v4/undecided`, a bound whose value the user has not decided yet. Added for this
release: `v4/short`, `v4/wide` and `v4/scenario` (see "Revisions in this release").

### Distinct IRs

|  | train | validation | test | all |
| --- | --- | --- | --- | --- |
| Distinct IR strings | 3506 | 256 | 557 | 4316 |

## How the rows were made

The rows are synthetic. They were produced by a meaning-first pipeline:

1. Meanings. A sampler enumerates target meanings from each domain's vocabulary and capability forms, and
   writes each one as a gold IR (see the strata above). For 408 rows of the earlier corpus, the gold IR was derived from an existing gold decision.
2. Utterances. An LLM writes a user request that expresses the target meaning, following a style card
   (language, persona, written or spoken register). Generator models: claude-sonnet-5-5, gpt-6.1-sol for the `v4/...`
   strata. The earlier corpus was generated with gpt-5.6-terra and claude-sonnet-5 and cross-certified with
   claude-opus-5 and gpt-5.6-terra, each request by the other provider's model.
3. Certification. A model from a second provider parses the request with the same system prompt the
   parser is trained on, and a row is kept only when its IR equals the gold IR in normal form (see Terms),
   in any frame order when there is no `COMPOSE` line (the IR match metric always requires the same
   order). Rows of the earlier corpus were certified at the decision level instead (the
   certifier's decision had to equal the gold decision); the marks of their unsupported rows were later
   re-certified at the IR level (see "Revisions in this release"). For per-unit constraints, a
   second question checked whether the request states the unit; a constraint whose unit is not stated is
   labeled `EACH(x in HOLE(scope))`. Certifier models: claude-opus-5 and gpt-5.6-terra for the rows of the pre-release build; gpt-6.1-sol (checking Sonnet 5.5) and claude-opus-5-5 (checking gpt-6.1-sol) for the rows added for this release and for the re-certification of marks.
4. Clarification episodes. For some `clarify` rows, a second row continues the conversation with the
   system's clarification question and a generated user answer; its gold IR states the resolved meaning.
5. Gold decisions. `gold_decision` is what `decide` returns for the gold IR and the row's user turns.

People audited a sample of 55 rows of the earlier corpus, and the labeling conventions were revised from
that audit and from a later diagnosis. The rows generated since then were checked by the automated
certification and by the gates of the build (every IR parses, is admitted by the published grammar, and
grounds; no request carries two labels; no clarification episode spans two splits). The hand-written
contrast rows are split by case instead (see Splits).

The prompts and grammars were generated with grounder version `2026-10-24.1`. SHA-256 of the files:

| File | SHA-256 |
| --- | --- |
| `prompts/nurse.txt` | `96a9fb26233a0e234be00281b3a55194e7c9c36346b891bc226044d6db316bac` |
| `grammar/nurse.ebnf` | `d3bf570cb32315212330252f6c2f77ee1e6f630311237c5b09ddc5e3d1a4876b` |
| `prompts/retail.txt` | `db5127ba8db344d54e105bad3787e3def4157b4bf9bd10f8801ef62c679e873b` |
| `grammar/retail.ebnf` | `a399c3130e1c6d55758872a93cbc35a5272fd7a327bcb7738229c439431ea36c` |
| `prompts/routing.txt` | `d0e05a63aaf448d55e168f6e76c43c717e2b94b821bf6263631a4acbc410085f` |
| `grammar/routing.ebnf` | `f1b510377624a63997b6ac8f446348735a3615eb5cc012c9eb94b77ddb57161d` |

## Revisions in this release

Compared with the pre-release build of this dataset, the release has these revisions:

- New rows. 2,095 rows were added in three new strata. Their briefs give the generator the user's situation
  and what the user wants, in work words, instead of the definitions of the measures.
  - `v4/short` (nurse and retail, 955 rows): chat requests typed in one line, with one or two objectives and
    at most one constraint.
  - `v4/wide` (nurse and retail, 812 rows): up to three objectives and four constraints, told from a ward's or a
    store's situation.
  - `v4/scenario` (routing, 328 rows): three to five constraints that occur together in one kind of operation,
    with values in working ranges. Example operations: a refrigerated-truck run, a parcel agency serving
    large apartment complexes, a motorbike delivery hub.

  Generators: claude-sonnet-5-5 and gpt-6.1-sol. Certifiers: gpt-6.1-sol for the rows Sonnet 5.5 wrote, and
  claude-opus-5-5 for the rows gpt-6.1-sol wrote. In the `v4/...` strata, a nurse or retail IR may now have
  up to ten paraphrases; routing keeps six. 33 generated rows had more than six frame or `UNEXPRESSED`
  lines, the most the published grammar admits besides one `COMPOSE` line; they were dropped.
- Rows let back in. The higher cap let 86 rows of the pre-release run back in, all nurse or retail rows in
  existing `v4/...` strata. With the two dropped contrast rows (see Splits), the release has
  12,033 + 2,095 + 86 - 2 = 14,212 rows.
- Marks. Some unsupported rows of the earlier corpus state how strict a constraint is ("if
  possible", "without exception") but had no `[SOFT]` or `[HARD]` mark. Both certifiers of the new rows
  re-parsed all 156 unsupported single-turn rows of that origin that have a constraint line. Where both read the
  same marks, and otherwise the gold frames, the marks were taken over: 107 rows changed. The other rows are
  unchanged.
- Splits.
  - `NO_INTENT` and `CLARIFY(intent)` no longer pull rows into one split by meaning: each is one label per
    domain, whatever the user said. Train now has 53 `NO_INTENT` rows and 1 `CLARIFY(intent)` row; in the
    pre-release build all of them were in test.
  - Seven stale `CLARIFY(intent)` labels were relabeled to the objective the request names, for example
    "minimize waste" became `MINIMIZE( waste_rate )`.
  - Two hand-written contrast rows were dropped, because relabeling them would have pulled train meanings
    into test.
  - 8 more rows left train: 6 `v4/extra` rows moved to test and 2 `v3/perturb` rows to validation.
- Clarification wording. After the adapters were trained, the system's clarification question was reworded
  in 96 rows (84 train, 6 validation, 6 test). Only that turn changed, and the IRs are the same. The released
  adapters were trained on the earlier wording.

## Intended use

- Training and evaluating parsers that turn optimization requests into IR that a downstream system can
  check before running a solver.
- Research on semantic parsing with abstention, where a model must keep ambiguous and unsupported
  meanings visible instead of mapping them to the nearest supported capability.

The dataset is not a sample of real user traffic, and it is not a general Korean or English instruction
dataset.

## Limitations

- Synthetic data. All requests were written by LLMs from sampled meanings. They cover the meanings that
  the sampler enumerates, not the distribution of real requests, and many rows paraphrase the same IR
  (14,212 rows, 4,316 distinct IRs).
- Realism. Many requests read more like a specification than like what a user would type, long routing
  requests most of all. The 2,095 rows added for this release were written from the user's situation, but
  they are 15% of the data. Korean and mixed-language requests were generated, not collected, and some read
  as translated or overly explicit. See Planned updates.
- Few human checks. Rows passed automated cross-certification and the build gates; people checked only a
  small sample. Some labels are likely wrong.
- Skewed decisions. About 84% of the rows execute; clarification and unsupported rows are fewer
  than real traffic may need.
- One capability held out. Every routing row whose IR bounds route duration from above, per route or per
  round (928 rows; 822 of them name `constraint:max_duration` in `gold_decision`), is in the test split
  only. Its capability form is in the prompt, but no training row uses it, so the test measures transfer to
  a form seen only in the prompt.
- Open conventions. Strict comparisons ("more than N") and bounds stated without a number follow the
  conventions at release time and may change.
- Behaviors without eval rows. Five behaviors have training rows but no validation or test rows, so the
  metrics reported on this dataset say nothing about them:
  - clarifying an unresolved measure (`HOLE(measure, ...)`, 23 rows, one IR);
  - clarifying a loosely named rule (`HOLE(constraint, ...)`, 32 rows);
  - asking for another way to combine objectives when the user names one the server does not offer
    (`COMPOSE(product)`, 50 rows);
  - declining a capability whose input data the server does not supply (188 rows, 19 of them objectives);
  - declining a strict priority order between objectives (20 rows).
- Unstated evenness (nurse). If a nurse request asks for an even workload without saying how evenness
  is measured, its label asks back (`UNSPECIFIED`). Train has 25 such rows (9 of them also leave the overtime aggregation open). Against them stand 479 rows whose
  requests state the gap between the busiest and the least busy nurse (`RANGE`), a few of them only loosely
  ("even out the shifts"). A model trained on `train` may fill in the gap instead of asking. The Qwen3-8B
  adapter trained on this release did so on 8 of the 19 such validation rows.
- Nurse scope. Nurse requests execute with four objectives (overtime, preference satisfaction, unmet
  demand, workload balance) and three constraints (consecutive working days, hours per week, rest between
  shifts). Other common rostering constraints, such as forbidden shift patterns, minimum staffing per shift
  and skills, are declined as unsupported: the prompt lists their forms, but they need input data or a
  configuration that the server does not provide here. The nurse rows therefore cover a narrow slice of
  real rostering.
- Domain ratio. Routing is 67% of the rows, nurse 17% and retail 15%. Routing has far more capabilities
  that execute: 4 objectives and 20 constraints, against 4 and 3 for nurse and 4 and 4 for retail. It
  therefore has far more distinct meanings.
- Unsupported meanings by design. Many rows are `clarify` or `unsupported`. The vocabulary, capability
  forms, refs (such as `objective:distance_cost`) and units belong to one optimization server's
  declarations at the time of release; a different server needs different prompts and decisions.
- Closed domains. Only the three domains above are covered.

## Planned updates

This dataset will be updated: the planned work brings its requests closer to the way real users phrase
optimization requests. All requests in this version were written by LLMs (see Limitations).

## License

The dataset is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Citation

```bibtex
@misc{omelet-ai-optilir-instruct-v1,
  title   = {OptiLIR-Instruct-v1},
  author  = {omelet-ai},
  year    = {2026},
  url     = {https://huggingface.co/datasets/omelet-ai/OptiLIR-Instruct-v1}
}
```
