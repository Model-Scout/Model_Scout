---
license: apache-2.0
language: [en, ko, ja, zh]
task_categories: [text-classification]
pretty_name: Jev decision distillation data (Claude-labelled)
size_categories: [10K<n<100K]
tags: [decision-model, jev, clef, distillation, soft-labels, calibration, multilingual]
configs:
- config_name: train
  data_files: train.jsonl
- config_name: validation
  data_files: validation.jsonl
- config_name: language_pool
  data_files: language_pool.jsonl
---

# Jev decision distillation data (Claude-labelled)

The training and validation data behind
**[`jaeyong2/clef-flash-jev-claude-distill`](https://huggingface.co/jaeyong2/clef-flash-jev-claude-distill)**, a fine-tune
of [Cloudflare/clef-flash](https://huggingface.co/Cloudflare/clef-flash) (9B) that raises the Decision Index public suite
from 52.55 to **54.96** on the same 123,049 rows (paired McNemar: +2,227 net rows, p ≈ 1e-138) and, on the same 32
benchmarks, scores above TypeSafe Jev 1.13 (proxy index 59.33 vs 57.98).

Each record is a **decision state** (document, log, ticket, chat, JSON record, passage, review, trial report …) with one
or more **typed questions** about it; every question carries a **soft target distribution** over its options. The model
is trained to reproduce `soft`. Hard labels and every teacher's distribution are kept so targets can be rebuilt.

| file | states | questions | purpose |
|---|---|---|---|
| `train.jsonl` | 37,932 | 150,827 | training set |
| `validation.jsonl` | 1,645 | 7,349 | held-out (same generators and target rules; no language-judgement records) |
| `language_pool.jsonl` | 19,025 | – | every generated language-judgement record (before balancing and hard-example mining) with both teacher distributions and the Opus re-judge result; `train.jsonl` contains the 5,977 states selected from it |

## 1. Where the states come from

All text is synthetic and written to stratified plans (language × task family × length × option count, with per-cell
seed variables to avoid near-duplicates). `id` encodes language, family and plan sequence number
(`synth-ko-fmt_action_approval-304817`). Char 10-gram MinHash (CJK aware, J ≥ 0.7) found no near-duplicate pairs in the
format, general or language batches.

| family | states (train) | questions | what a record looks like |
|---|---|---|---|
| **workflow** — 35 domains (invoice, support_ticket, security_incident, agent_trace, refund_request, loan_application, insurance_claim, expense_report, purchase_order, contract_review, it_access_request, bug_triage, shipping_exception, warranty_claim, subscription_cancellation, payroll_correction, vendor_onboarding, customs_declaration, job_application, rental_application, travel_booking_change, code_review, data_pipeline_incident, property_maintenance, grant_application, marketing_campaign_approval, inventory_reconciliation, student_grade_appeal, fleet_maintenance, utility_billing_dispute, tool_selection, tool_argument_filling, tool_call_validation, tool_result_grounding, intent_detection) | 16,757 | 122,750 | long JSON-like business record (median ≈ 3.5k tokens) with 8 questions: 2 noul, 3 choice, 3 score, one of them unanswerable from the state (`label = -1`) |
| **format** — 12 families (`fmt_*`: intent_classification, claim_verification, policy_decision, sentiment_rating, content_moderation, action_approval, tool_routing, reading_mcq, continuation_mcq, fill_blank, severity_triage, answer_check) | 7,598 | 12,914 | short state (prose, chat, email, JSON, table), 1–3 questions, short option ids with one-line `descriptions`, 40 % with worked `examples` per option |
| **general** — 6 families (`gen_*`: nli, reading_mcq, knowledge_mcq, paraphrase, commonsense, coreference) | 7,600 | 8,727 | general-ability items, 90 % ko/ja/zh |
| **language judgement** — 9 families (`lang_*`: sarcasm, stance, aspect_sentiment, nli_neutral, clinical_nli, oos_intent, appliance_command, caption_match, evidence_rank) | 5,977 | 6,436 | short English-heavy items (55 % en) targeting judgement types where the base model was weakest: sarcasm/irony, stance toward a named target, aspect-level sentiment, 3-way NLI with a genuine neutral class, clinical-trial NLI with numeric traps, intent classification with an out-of-scope option, appliance command grounding against a capability list, caption–scene matching, evidence passage ranking |

Language-judgement questions in train by family: clinical_nli 2,045 · nli_neutral 971 · stance 843 · caption_match 753 ·
oos_intent 682 · aspect_sentiment 518 · sarcasm 399 · evidence_rank 131 · appliance_command 94.

States per language (train): en 11,203 · ko 9,005 · ja 8,889 · zh 8,835. The state language is also the question and
option language (noul options are the language's fixed yes/no words).

**Generators.** Codex (GPT-5.6 Sol) wrote the first 1,654 workflow states; Claude Opus 5.5 wrote everything else
(through Claude Code, plus 4,998 language-judgement records through the Anthropic API). Every record passed a validator:
JSON schema, option rules (noul = fixed yes/no, score = ordered low → high, unique choice ids), `descriptions` aligned
with options, probabilities summing to 1, `label` = argmax of `soft`, unique ids.

## 2. Question types

| `type` | options | semantics | train |
|---|---|---|---|
| `noul` | exactly 2, language-fixed yes/no; `soft[0]` is the *yes* side | binary judgement | 38,871 |
| `choice` | 2–40 unordered ids (Clef's encoder sorts choice ids alphabetically; training code re-orders `soft` to match) | pick one option | 65,950 |
| `score` | 3–7 ordered ids, low → high | ordinal rating | 46,006 |

## 3. Teachers and the soft target

`teacher_probs` holds, in `options` order:

* `Cloudflare/clef` — **the 27B Clef model, the main teacher** (typed-decisions acc 0.725 vs 0.703 for clef-flash;
  on this data's own validation set acc 0.891 with ECE 0.046).
* `Cloudflare/clef-flash` — the 9B base model being fine-tuned; used as the **KL anchor** during training (keeps the
  student close to its original behaviour) and for hard-example mining.
* `Qwen/Qwen3.5-27B` (workflow records, earlier pipeline) and `claude-opus-5-5` (Opus verbalised probabilities on
  re-judged questions).

`label_generator` is the author label written with the record; `label` is the final label (`-1` = unanswerable).
`vote` says how `soft` was formed:

| `vote` | condition | `soft` | train |
|---|---|---|---|
| `t27_agree` | 27B argmax = label | 27B distribution (mean max-prob 0.88) | 118,289 |
| `t27_sharpen` | 27B argmax ≠ label | `0.7·onehot(label) + 0.3·p_27B` (0.5/0.5 for questions Opus marked hard) | 13,082 |
| `t27_opus` | the label was disputed earlier (clef-flash and Qwen both against the author) and Opus re-judged it | Opus verbalised probabilities | 2,647 |
| `unlabeled` | label −1 | 27B distribution, no label push | 16,809 |

Why sharpen instead of a minimal move: targets that only move enough mass to make the label win are flat and two-peaked;
a student trained on them becomes under-confident and flips near-tie answers. Label-centred mixtures fixed that.

## 4. How the language-judgement subset was built

Generating each record independently made Opus favour the "interesting" answer (e.g. 99 % `neutral` in the neutral-NLI
family, 100 % `out_of_scope` in the OOS family, 0 % `neutral_or_none` in stance, ~11 % sarcastic, caption answers piling
on option C). The subset was therefore built in four steps; `language_pool.jsonl` keeps the intermediate fields.

1. **Label-targeted top-up**: 3,900 extra records generated with the answer assigned per cell (NLI entailment/contradiction,
   in-scope intents, neutral stance, sarcastic posts, clinical entailment).
2. **Opus re-judge**: 1,262 questions where clef-flash and the 27B teacher agreed with each other against the author label
   (both ≥ 0.6 confident) were re-judged by Opus as an independent reader: 1,239 kept, 19 relabelled to the models'
   answer, 4 dropped (`rejudge`, `opus_note`).
3. **Balancing**: per family, each answer group capped at 1.5 × the mean of the other groups; letter-id options (A–E) had
   their contents shuffled with label and probabilities moved accordingly (`mined`, `ensemble`).
4. **Hard-example mining**: kept questions clef-flash gets wrong or answers with max-prob < 0.6, or where the 27B teacher
   disagrees with the label (4,102), plus a 15 % random replay of the rest (2,334). Targets follow the table above.

## 5. Record schema

```jsonc
{
  "id": "synth-ko-fmt_action_approval-304817",
  "source": "synthetic_fmt_action_approval",
  "lang": "ko",
  "state": "…",                                     // string, or a JSON object for some workflow records
  "questions": [{
    "type": "choice",                               // noul | choice | score
    "instruction": "승인 정책에 따라 AR-봇의 제안 조치를 어떻게 처리해야 하는가?",
    "options": ["approve", "require_human_review", "block"],
    "descriptions": ["…", "…", "…"],                 // format / general / language records
    "examples": {"approve": "…", "…": "…"},          // optional worked examples
    "label": 2, "label_generator": 2,
    "soft": [0.02, 0.11, 0.87],                     // TRAINING TARGET (options order, sums to 1)
    "teacher_probs": {"Cloudflare/clef": [...], "Cloudflare/clef-flash": [...], "Qwen/Qwen3.5-27B": [...]},
    "teacher_agrees": true,
    "vote": "t27_agree"
  }]
}
```

## 6. How it was used

LoRA r = 32 on all text-decoder Linear layers + full fp32 joint-schema head; loss = soft cross-entropy + Brier against
`soft`, plus 0.3 · KL(model ‖ clef-flash distribution); question-order shuffling and random question subsets; states
truncated to 6,000 tokens; **one epoch** (two or three epochs lowered the knowledge and tool areas in our ablation);
18 states per optimizer step, lr 1e-4 (head 5e-5).

## 7. Licensing and provenance

Synthetic text written by Codex (GPT-5.6 Sol) and Claude Opus 5.5 under the project's own prompts; no benchmark text was
copied and no public-benchmark test items are included. Teacher distributions from Cloudflare/clef and clef-flash
(Apache-2.0) and Qwen3.5-27B (Apache-2.0). Released under Apache-2.0. All people, organisations and figures are fictional.
