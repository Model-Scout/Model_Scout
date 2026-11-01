---
language: [th, en, zh, ja, ko, ar, hi, ru]
multilinguality: multilingual
license: other
license_name: per-source
license_link: LICENSE.md
pretty_name: Laya Thai Typed Decisions
size_categories: [10K<n<100K]
task_categories: [text-classification, zero-shot-classification]
tags: [laya, rlcd, thai, typed-decisions, soft-labels, knowledge-distillation, synthetic, calibration]
source_datasets:
  - extended|AmazonScience/massive
  - extended|pythainlp/wisesight_sentiment
  - extended|Wongnai/wongnai_reviews
  - extended|pythainlp/thaisum
  - extended|iapp/iapp_wiki_qa_squad
  - extended|LocalLLaMA/typed-decisions
configs:
  - config_name: default
    data_files:
      - split: train
        path: data/train.parquet
      - split: calibration
        path: data/calibration.parquet
  - config_name: unfiltered
    data_files:
      - split: rows
        path: unfiltered/rows.parquet
  - config_name: eval
    data_files:
      - split: massive_intent_th
        path: eval/massive_intent_th.parquet
      - split: massive_intent_th_full
        path: eval/massive_intent_th_full.parquet
      - split: massive_intent_th_heldout_scenarios
        path: eval/massive_intent_th_heldout_scenarios.parquet
      - split: massive_intent_ar
        path: eval/massive_intent_ar.parquet
      - split: massive_intent_hi
        path: eval/massive_intent_hi.parquet
      - split: massive_intent_ja
        path: eval/massive_intent_ja.parquet
      - split: massive_intent_ko
        path: eval/massive_intent_ko.parquet
      - split: massive_intent_ru
        path: eval/massive_intent_ru.parquet
      - split: massive_intent_zh_CN
        path: eval/massive_intent_zh_CN.parquet
      - split: massive_th_sampler_eval
        path: eval/massive_th_sampler_eval.parquet
      - split: wisesight_sampler_eval
        path: eval/wisesight_sampler_eval.parquet
      - split: iapp_sampler_eval
        path: eval/iapp_sampler_eval.parquet
      - split: probe_noul_labels
        path: eval/probe_noul_labels.parquet
      - split: probe_noul_negation
        path: eval/probe_noul_negation.parquet
      - split: probe_option_count
        path: eval/probe_option_count.parquet
      - split: probe_score_orientation
        path: eval/probe_score_orientation.parquet
      - split: synth_eval_domains_th
        path: eval/synth_eval_domains_th.parquet
---

# Laya Thai Typed Decisions

A Thai dataset of **typed decision questions**. Each row is a piece of text (a chat message, product review, social
post, news article, Wikipedia passage, or support ticket) plus one or more questions about it. Every question has a
fixed type:

- `choice`: pick one option from a labelled set
- `score`: pick a level on an ordered scale
- `noul`: answer true or false

Each question comes with a gold label, the probability distribution an LLM teacher assigned to its options, and a
soft target that blends the two. The format follows
[LocalLLaMA/typed-decisions](https://huggingface.co/datasets/LocalLLaMA/typed-decisions). Laya
([convaiinnovations/laya](https://huggingface.co/convaiinnovations/laya)) and other models that score options given a
state and an instruction can read it directly.

What the dataset provides:

- **Thai decision data from real and synthetic sources:**
  - intent and scenario (MASSIVE)
  - sentiment and question detection (wisesight)
  - review ratings (wongnai)
  - headline and topic (thaisum)
  - reading comprehension (iapp)
  - eight synthetic business workflows: support routing, urgency, frustration, churn, escalation, moderation
  - Thai NLI
- **Soft labels:** a teacher distribution for every Thai question in `train`. They are useful for distillation,
  label-noise analysis, and calibration studies.
- **Non-Thai rows in the same format:** English typed-decisions, and MASSIVE in zh-CN, ja, ko, ar, hi, and ru, for
  mixing with the Thai data.
- **A calibration set** of Thai gold questions, disjoint from `train`.
- **17 frozen eval suites** covering Thai accuracy, unseen instruction phrasings, unseen MASSIVE scenarios, other
  languages, and behavioural probes.
- **An unfiltered view** of every question before quality filtering, with the reason each one was kept or dropped.

Size: `train` has 41,776 questions on 27,250 rows (71% Thai), `calibration` has 2,448 questions, and the eval suites
have 9,161 cases.

This is a first release with known weaknesses. The [audit](#known-issues) lists them, and [TASKS.md](TASKS.md) turns
each one into a contributor-sized task.

## Quick start

```python
import json
from datasets import load_dataset

train = load_dataset("hagsmand1/laya-thai-decisions", split="train")
row = train[0]
state, questions = json.loads(row["state"]), json.loads(row["questions"])
target = json.loads(row["target"])          # {qid: {option_key: prob}}, gold blended with the teacher

calib = load_dataset("hagsmand1/laya-thai-decisions", split="calibration")
unfiltered = load_dataset("hagsmand1/laya-thai-decisions", "unfiltered", split="rows")
probe = load_dataset("hagsmand1/laya-thai-decisions", "eval", split="probe_noul_negation")
```

Nested fields are stored as JSON strings because their keys change from row to row (option keys are Thai words,
English words, or letters). Decode them with `json.loads`.

## Configs and splits

| Config | Split | Rows | Questions | What it is |
|---|---|---|---|---|
| `default` | `train` | 27,250 | 41,776 | Questions that passed the quality filters. Each has a gold label, a teacher distribution, and a soft target. 71% Thai; the rest are English and multilingual rows in the same format |
| `default` | `calibration` | 2,000 | 2,448 | Thai gold questions from the five public sources, disjoint from `train`, with one-hot targets. Use it to measure or fit confidence calibration |
| `unfiltered` | `rows` | 31,042 | 50,038 | Every question before filtering, with the filter outcome for each. Use it to audit or change the filters |
| `eval` | 17 splits | 9,161 cases | | Frozen test suites; see [Evaluation suites](#evaluation-suites) |

`unfiltered` rows have a `role`:

| Role | Rows | Questions | Meaning |
|---|---|---|---|
| `train` | 27,702 | 44,691 | Source rows of the `train` split before filtering. 452 rows lost every question, so `train` has 27,250 |
| `calibration` | 2,000 | 2,448 | The same rows as the `calibration` split |
| `reshuffle_check` | 1,040 | 1,999 | Copies of synthetic rows with the options reordered. A question was dropped when its teacher distribution changed with the order |
| `eval_only` | 300 | 900 | Source rows of `synth_eval_domains.th` (insurance claims, school admin) before filtering. **Do not train on these** |

## Data fields

### `default` and `unfiltered`

| Field | Type | Description |
|---|---|---|
| `id` | string | `<source>:<upstream id>`; unique |
| `source` | string | `massive_th`, `wisesight`, `wongnai`, `thaisum`, `iapp`, `synth_<domain>`, `synth_nli`, `typed_decisions`, `massive_<lang>` |
| `lang` | string | Language of the text (`th`, `en`, `zh-CN`, ...). Instructions can be Thai or English independently |
| `text` | string | The natural-language text the questions are about (for search, dedupe, and overlap checks) |
| `state` | JSON string | What the model reads: a plain string or an object such as `{"ticket_id": ..., "message": ...}`. Some states add realistic distractor fields |
| `questions` | JSON string | `{qid: question}`; see below |
| `gold` | JSON string | `{qid: {"type", "label", "probabilities"}}`. One-hot for public data; the generator's intended label for synthetic rows; upstream soft labels for `typed_decisions` |
| `teacher` | JSON string or null | Raw teacher distribution `{qid: {key: prob}}` before temperature. Null for the English and non-Thai MASSIVE rows |
| `target` | JSON string or null | Soft target `{qid: {key: prob}}`: gold blended with the teacher (see [Soft targets and filtering](#soft-targets-and-filtering)). In `calibration` it equals the gold one-hot |
| `role` | string | `unfiltered` only; see above |
| `decision` | JSON string or null | `unfiltered` only: `{qid: reason}`, the filter rule that applied (table below) |
| `teacher_adjudication` | JSON string or null | `unfiltered` only: second teacher pass at higher effort on hard MASSIVE disagreements |
| `teacher_reshuffle` | JSON string or null | `unfiltered` only: teacher distribution with the options in a different order (synthetic rows) |

### Question types

Instructions refer to state fields in backticks, for example ``How urgent is `message`?``.

```json
{"type": "choice", "instructions": "`message` ควรอยู่ในคิวใด",
 "criteria": {"A": "เปลี่ยนหรืออัปเกรดแพ็กเกจ", "B": "บิล ค่าบริการ เติมเงิน การชำระเงิน", "C": "มือถือ เราเตอร์ ซิมการ์ด"}}

{"type": "score", "instructions": "How urgent is `message`?",
 "criteria": ["urgent or blocking", "should be handled soon", "routine, handle in the normal queue", "no time pressure"]}

{"type": "noul", "instructions": "Does the writer of `message` threaten to cancel or leave?",
 "criteria": {"false": "ไม่ได้ขู่ยกเลิก", "true": "ขู่ว่าจะยกเลิกหรือเลิกใช้"}, "labels": {"false": "no", "true": "yes"}}
```

- `choice`: option keys are letters, English slugs, or Thai words, and options are shuffled. Some questions add a
  "none of the other options fit" option.
- `score`: an ordered list of levels. The label is the level index as a string (`"0"`, `"1"`, ...), and the direction
  varies: sometimes level 0 is the worst, sometimes the best.
- `noul`: keys are always `false` / `true`; the optional `labels` map changes how they are displayed.

`train` by question type: 19,916 `choice`, 13,712 `noul`, 8,148 `score`.

### `eval`

| Field | Type | Description |
|---|---|---|
| `suite` | string | Original suite name, e.g. `massive_intent.zh-CN` |
| `index` | int | Case position in the frozen file |
| `language` | string | Language of the text |
| `tags` | list of strings | e.g. `heldout-template`, `probe`, `regression` |
| `state`, `questions` | JSON string | As above. Probe cases put two paired questions on one state |
| `expected` | JSON string | `{qid: answer}`: option index for `choice` and `score`, boolean for `noul` |

`eval/manifest.json` records the sha256 of each original frozen file, so results stay comparable across versions.
Suites are never edited in place; a changed suite gets a new versioned name.

## How it was built

### Sources

| Source | Rows (train) | Questions (train) | Calibration rows | Tasks | License |
|---|---|---|---|---|---|
| [MASSIVE](https://huggingface.co/datasets/AmazonScience/massive) `th` | 3,455 | 4,852 | 513 | intent / scenario choice, "asks for X" noul | CC BY 4.0 |
| [wisesight_sentiment](https://huggingface.co/datasets/pythainlp/wisesight_sentiment) | 2,317 | 3,178 | 305 | sentiment choice and score, "is a question" noul | CC0 1.0 |
| [wongnai_reviews](https://huggingface.co/datasets/Wongnai/wongnai_reviews) | 2,550 | 3,408 | 338 | star score, sentiment score, "is positive" noul | LGPL-3.0 |
| [thaisum](https://huggingface.co/datasets/pythainlp/thaisum) | 3,976 | 3,976 | 524 | headline choice, headline match noul, topic choice | MIT (articles: publisher copyright) |
| [iapp_wiki_qa_squad](https://huggingface.co/datasets/iapp/iapp_wiki_qa_squad) | 2,630 | 2,630 | 320 | answer-span choice, answerable noul | MIT; passages CC BY-SA |
| Synthetic workflows (8 domains) | 2,934 | 7,819 | | department, urgency, frustration, churn, needs-human, severity, ... | CC BY 4.0 |
| Synthetic NLI | 3,932 | 3,932 | | premise / hypothesis relation choice, "implies" noul | CC BY 4.0 |
| [typed-decisions](https://huggingface.co/datasets/LocalLLaMA/typed-decisions) (`typed_decisions`, en) | 1,200 | 6,000 | | English workflow decisions: urgency, routing, risk, review flags | Apache-2.0 |
| MASSIVE other languages (`massive_<lang>`: zh-CN, ja, ko, ar, hi, ru) | 4,256 | 5,981 | | intent / scenario choice, "asks for X" noul | CC BY 4.0 |

Synthetic workflow domains: telco support, bank support, e-commerce support, content moderation, LINE chat, HR email,
government service, and code-mixed Thai-English reviews.

- Public rows come from the upstream **train** splits.
- Any row whose normalised text matches a case in any eval suite (including suites not published here) was dropped.
- Six MASSIVE scenarios (cooking, email, lists, music, news, social) are absent from `train` and `calibration`. They
  appear only in `massive_intent.th.heldout_scenarios`.
- One instruction template per task is reserved for the `*.sampler_eval` suites, so those suites use phrasings that
  never occur in `train`.

### Teacher labels

Every Thai public and synthetic question was labelled by an LLM teacher (`gpt-5.6-terra`). The teacher was asked
for a calibrated probability over the options, with `choice` options shown in shuffled order and the output
constrained by a JSON schema (low reasoning effort, four states per request). The same model generated the synthetic
workflow and NLI states, each with an intended label.

On a 300-row pilot, the teacher agreed with gold 81% of the time (MASSIVE 91%, iapp 98%, thaisum 93%,
wisesight 63%, wongnai 67%). Most of the low agreement on wisesight and wongnai traces back to noisy crowd labels.
For the soft targets, the teacher distribution is first softened with a single temperature T = 1.447, fitted on that
pilot. The `teacher` column holds the raw, unsoftened distribution.

### Soft targets and filtering

`target = floor(alpha * onehot(gold) + (1 - alpha) * teacher_T, 0.01)`, renormalised. The weight alpha on gold depends
on how well gold and teacher agree. A question is dropped when they conflict and the gold label is unreliable. The
`decision` column in `unfiltered` records which rule applied:

| `decision` | Applies to | alpha | Questions |
|---|---|---|---|
| `agree` | teacher argmax == gold | 0.5 | 15,694 |
| `soft_disagree` | teacher p(gold) >= 0.2, or for `score` >= 0.5 of the mass within ±1 of gold | 0.7 | 1,846 |
| `structural_gold` | hard disagreement on thaisum / iapp, where gold is a real headline or span | 0.9 | 272 |
| `adjudicated_keep` / `adjudicated_drop` | hard MASSIVE disagreement, re-asked at higher effort; kept if p_adj(gold) >= 0.1 | 0.85 / dropped | 232 / 200 |
| `noisy_drop` | hard disagreement on wisesight / wongnai | dropped | 516 |
| `kept` | synthetic, teacher argmax == intended label; target is the floored teacher distribution | teacher only | 11,751 |
| `generator_disagree` | synthetic, teacher argmax != intended label | dropped | 2,169 |
| `reshuffle_unstable` | synthetic, teacher distribution moved by total variation > 0.3 when options were reordered | dropped | 22 |
| `replay` | `typed_decisions`: upstream soft target, floored; `massive_<lang>`: gold smoothed by 0.05 | n/a | 11,981 |

The `calibration` split is 2,000 Thai public rows, chosen so that every (question type, option count) bucket has at
least 200 questions.

## Evaluation suites

All suites come from upstream **test** splits or from synthetic domains absent from `train`. None of their texts
appear in `train` or `calibration`.

| Split | Cases | Measures |
|---|---|---|
| `massive_intent_th`, `massive_intent_th_full` | 100, 2,974 | Thai intent, upstream 20-option protocol |
| `massive_intent_th_heldout_scenarios` | 796 | Thai intents from the six scenarios absent from `train` |
| `massive_intent_{ar,hi,ja,ko,ru,zh_CN}` | 100 each | Intent in six other languages, to check that non-Thai ability holds up |
| `massive_th_sampler_eval`, `wisesight_sampler_eval`, `iapp_sampler_eval` | 1,092, 1,052, 647 | Questions in the `train` format, phrased with instruction templates absent from `train` |
| `probe_noul_negation` | 400 pairs | A claim and its negation on one state; predictions must flip |
| `probe_noul_labels` | 400 pairs | Default `false`/`true` labels vs. relabelled A/B; predictions must agree |
| `probe_score_orientation` | 400 pairs | A 3-level scale in normal and reversed order; predictions must follow the scale |
| `probe_option_count` | 400 | MASSIVE intent with 3 / 6 / 12 / 20 options |
| `synth_eval_domains_th` | 300 | Synthetic domains absent from `train` (insurance claims, school admin); see the caveat in H4 |

Suites built from XNLI, Belebele, SIB-200, XCOPA, thai_toxicity_tweet, thai_exam, and the typed-decisions test split
are not included, because some are non-commercial or of unclear copyright. Build them from upstream if you need them.

### Baseline

To show how hard each suite is, the table gives the zero-shot scores of the public `multilingual` checkpoint of
convaiinnovations/laya, with no temperature scaling:

| Suite | Metric | Score |
|---|---|---|
| massive_intent.th.full | accuracy | 0.378 |
| massive_intent.th.heldout_scenarios | accuracy | 0.432 |
| massive_intent.{ar,hi,ja,ko,ru,zh-CN} | mean accuracy | 0.542 |
| massive_th.sampler_eval | accuracy | 0.584 |
| wisesight.sampler_eval | accuracy | 0.469 |
| iapp.sampler_eval | accuracy | 0.539 |
| probe.noul_negation | flip consistency | 0.118 |
| probe.noul_labels | default / relabelled agreement | 0.808 |
| probe.score_orientation | orientation consistency | 0.270 |
| probe.option_count | accuracy at k = 3 / 20 | 0.825 / 0.363 |
| synth_eval_domains.th | accuracy | 0.553 |

Read the probe numbers together with H4 below: a constant predictor can score well on some of them.

## Known issues

An audit of this release found the following. Severity reflects the expected effect on models trained with this
data. Each item maps to tasks in [TASKS.md](TASKS.md).

**High**

- **H1. The synthetic agreement filter skews class balance.** Synthetic questions are kept only when the teacher
  agrees with the generator, and the teacher rejects middle levels far more often than extremes. Moderation
  `severity` "medium" keeps 15%, telco `urgency` "no pressure" 27%, while "urgent" keeps 100%; after filtering,
  "urgent" makes up 52% of telco urgency (27% before). A model trained on `train` is pushed away from middle levels.
- **H2. thaisum `topic` is treated as structural gold.** Its gold is a keyword heuristic over the article category,
  not a real headline or span, yet 223 topic disagreements are forced onto it with alpha 0.9.
- **H3. Few instruction templates.** Most tasks have 2–3 instruction strings per language, and one is reserved
  for eval, so many tasks have only one or two phrasings in `train`.
- **H4. Some eval suites cannot detect what they target.**
  - `probe.noul_labels` is 97.8% `false`, so a constant predictor scores 100% agreement.
  - `probe.score_orientation` is 54% neutral, which reversal leaves unchanged.
  - The n = 100 non-Thai MASSIVE suites carry a ±9.8 pp 95% CI.
  - `synth_eval_domains.th` keeps only questions that the same teacher (the one that labelled `train`) agrees with,
    so it measures teacher agreement rather than correctness. Its 100-row human spot-check
    (`annotation/spot_check_synth_eval.csv`) has not been filled in yet.
- **H5. The calibration split leaks passages and uses noisy gold.** It splits by row, so 464 `train` iapp rows share a
  passage with a `calibration` row. It also includes wisesight and wongnai one-hot gold, which the teacher agrees with
  only 51–70% of the time.

**Medium**

- **M1.** The "none of the other options fit" option is always last (1,429 questions), so the last position is gold
  more often than chance.
- **M2.** Negatives are too easy. iapp unanswerable passages are random, and thaisum headline distractors are random;
  the teacher scores 98–99.5% on them.
- **M3.** Some synthetic questions are vaguely defined. Teacher and generator agree only 50–66% on `needs_human`,
  `urgency`, moderation `severity`, `frustration`, and LINE-chat `intent`.
- **M4.** Synthetic NLI has low diversity: a distinct 4-gram ratio of 0.117, and 11% near-duplicates.
- **M5.** Passages are clipped at 600–700 characters, and every thaisum state ends in "…".
- **M6.** A single teacher temperature is used for every question type.
- **M7.** No held-out suite exists for wongnai star scoring or thaisum topic / headline.
- **M8.** Non-Thai rows make up 28.7% of `train` questions, and no other share has been tested. Also, 994 non-Thai
  MASSIVE questions use Thai option keys.

**Low**

- **L1.** Overlap filtering strips Thai vowels and tone marks, so `เสือ` and `เสื่อ` normalise to the same string
  and some rows were dropped as false-positive overlaps.
- **L2.** Small bookkeeping gaps in the eval manifest: `massive_intent.th` has no `language` or `tags`.
- **L3.** `synth_gov_service` has 320 rows against 375 for the other domains, and 8 synthetic questions have no
  teacher label.
- **L4.** 217 wisesight and 204 massive_th rows have under 10 characters of content; some are noise (`555`, one emoji).

## Areas to improve

[TASKS.md](TASKS.md) has 30 tasks with a problem statement, what to do, and a measurable "done when" for each.
Most of the analysis and re-filtering tasks can be done with this repo alone, because `unfiltered` keeps the
teacher distribution, gold, and decision for every question.

Good places to start:

| Task | Effort | Needs |
|---|---|---|
| T02 Route thaisum `topic` disagreements away from structural gold | S | this repo |
| T07 Macro-F1, balanced accuracy, and majority baselines for every suite | S | this repo |
| T09 Keep synthetic `score` questions within ±1 of the intended level | S | this repo |
| T10 Per-class retention report for the synthetic filter | S | this repo |
| T16 Fill in the 100-row human spot-check | S | native Thai reader |
| T19 Group-level calibration split | S | this repo |
| T21 Per-question-type teacher temperature | M | this repo |
| T30 Reproducible audit script for every number in "Known issues" | M | this repo |

To contribute, open a Discussion to claim a task, then a pull request with the before/after numbers that the task's
**Done when** asks for. New sources need a license entry in [LICENSE.md](LICENSE.md), and nothing with a
non-commercial license may enter `train`.

## Licensing and attribution

There is no single license; each row follows its source. See [LICENSE.md](LICENSE.md) for the per-source table.

- Synthetic rows and all teacher distributions were generated for this project and are released under CC BY 4.0.
  They are model outputs, so the teacher model provider's usage terms may also apply to how you use them.
- **thaisum** articles are scraped Thai news. The dataset card says MIT, but copyright in the article text stays with
  the original publishers. Drop `source == "thaisum"` if that matters for your use.
- **iapp** passages come from Thai Wikipedia under CC BY-SA, so redistributed passages must stay share-alike.
- **wongnai** reviews carry LGPL-3.0, a code license applied to data by the upstream repo.
- Reviews and social-media posts (wisesight, wongnai) are user-generated text and may contain names or offensive
  language.

Please cite the upstream datasets when you use their rows: MASSIVE (FitzGerald et al., 2022), wisesight_sentiment
(Suriyawongkul et al., 2019), Wongnai reviews, ThaiSum (Chumpolsathien, 2020), iapp_wiki_qa_squad (iApp
Technology), and typed-decisions (LocalLLaMA).
