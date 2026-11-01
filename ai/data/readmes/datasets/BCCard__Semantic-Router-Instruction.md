---
license: apache-2.0
language:
- ko
- en
- zh
- ja
- vi
---

# Semantic Router Instruction Dataset — Multilingual

A multilingual instruction dataset for training and evaluating the
semantic-turn router: a model that classifies one utterance along 14 axes
simultaneously. A single JSONL file of five languages × 600,000 rows =
**3,000,000 rows total**. Every row's `instruction` actually contains the
content signal its axis/value label depends on.

- **Scale**: 600,000 rows per language (14 axes × 150 values fully covered,
  fixed per-value counts — identical in every language)
- **Languages**: Korean · English · Chinese · Japanese · Vietnamese
- **Parallelism**: label-parallel, **not** text-parallel — each language block
  is authored natively in that language; no row is a translation of another
  language's row. Translation-parallel training data invites the router to key
  on translation artifacts, so it is deliberately excluded.
- **Character**: every row is a long-form composed turn (context + request +
  constraints/branches). en/zh/ja/vi are built with six distinct structural
  authoring engines so the corpus is not a single assembly pattern.

## Dataset overview

| Item | Value |
|---|---|
| Total rows | 3,000,000 (exactly 600,000 × 5 languages) |
| Size | 1,027,674,919 bytes (≈ 0.96 GiB), uncompressed |
| Encoding | UTF-8, one JSON object per line, no header |
| Block order | ko → en → zh → ja → vi (contiguous per-language blocks, no shuffle) |

Block boundaries: rows 1–600,000 = ko, 600,001–1,200,000 = en,
1,200,001–1,800,000 = zh, 1,800,001–2,400,000 = ja, 2,400,001–3,000,000 = vi.
Row order inside each block is fixed and reproduces identically on rebuild.

## Schema

Each row is a JSON object with four fields (`lang` always first):

```json
{"lang":"en","instruction":"I'm putting together the quarterly ops review and my notes are a mess, so pull the numbers from the attached workbook and build the review deck. Keep it under ten slides, lead with the churn story, and if the March figures are missing, use February and say on the slide.","category":"service","value":"presentation"}
```

| Field | Type | Description |
|---|---|---|
| `lang` | string | One of `ko` / `en` / `zh` / `ja` / `vi` |
| `instruction` | string | User utterance. Unique within each language block (all 600k verified) |
| `category` | string | One of the 14 axes |
| `value` | string | One of that axis's values (150 values total) |

Label strings (`category`, `value`) are English snake_case in **all** blocks,
including the non-English ones — they are the router's target vocabulary and
are deliberately kept language-independent.

## Axes, values, allocation

The table below applies **identically to every language block** (file-wide,
each axis's total is 5× the table figure — e.g. `service` is 96,000 rows per
language → 480,000 rows in the whole file):

| Axis | Values | Rows (per language) | Values |
|---|---:|---:|---|
| `service` | 16 | 96,000 | general, presentation, image, data_analysis, place_search, web_search, knowledge_search, calendar, memo, works, connector, artifact, coding, translation, skill, reasoning |
| `presentationSkillId` | 56 | 112,000 | executive-strategy, board-update, quarterly-business-review, sales-proposal, investor-pitch, training-explainer, technical-architecture, research-report, marketing-campaign, product-launch, product-roadmap, consulting-diagnosis, all-hands-update, thesis-research, crisis-communication, demo-day-pitch, compliance-training, lesson-lecture, customer-qbr, analyst-briefing, okr-review, esg-report, incident-postmortem, thesis-defense, grant-proposal, workshop-facilitation, competitive-analysis, investor-update, annual-report, pricing-proposal, analytics-readout, customer-onboarding, vendor-selection, market-entry, company-onboarding, case-study-analysis, model-un-position, lab-meeting, self-review, conference-talk, resume-portfolio, nonprofit-pitch, policy-briefing, earnings-brief, m-a-proposal, org-redesign, regulatory-response, course-syllabus, exam-prep, hobby-explainer, travel-itinerary, deck-redesign, deck-exec-polish, deck-board-upgrade, deck-content-cleanup, none |
| `contentDomain` | 15 | 60,000 | social, play, self_capability, affective_state, creative, support, explore, personal_scope, opinion, code_work, formal_reasoning, supplied_material, explicit_lookup, multi_step_research, unresolved |
| `action` | 14 | 56,000 | respond, create, revise, import, analyze, search, export, delete, translate, summarize, explain, compare, execute, none |
| `dialogueAct` | 10 | 40,000 | clarification_answer, option_selection, confirm, decline, correction, continue_output, preference_directive, meta_conversation, undo_action, none |
| `sourcePolicies` | 7 | 42,000 | web, internal, memory, attachments, conversation_only, auto, none |
| `memoryIntent` | 7 | 28,000 | informational, transactional, conversational, analytical, personal, navigational, none |
| `requestedOutputs` | 5 | 34,000 | chat, docx, xlsx, pptx, image |
| `diagramKind` | 4 | 24,000 | structure, visualization, plan, none |
| `presentationMode` | 4 | 24,000 | fast, professional, creative, none |
| `complexity` | 4 | 32,000 | simple, standard, complex, hard |
| `artifactKind` | 3 | 18,000 | diagram, interactive, none |
| `analysisMode` | 3 | 18,000 | focused, comprehensive, none |
| `artifactComplexity` | 2 | 16,000 | simple, complex |

Per-value counts are the row count divided by the value count (e.g. 6,000 per
`service` value, 2,000 per `presentationSkillId` value — 30,000 / 10,000
respectively file-wide). Each `instruction` is labeled with exactly one
`(category, value)` pair — rows exist per axis, not as multi-label records.
Because per-value counts are identical across languages, any language block
you slice has the same label distribution (class priors) — this is what makes
cross-lingual evaluation compare like with like.

## Cross-lingual design

- **Label-parallel, not text-parallel.** The five blocks align on labels only.
  No instruction is a translation of another block's instruction.
- **Same class priors everywhere.** Identical per-value counts mean every
  per-language slice has the same label distribution.
- **Native authorship.** Each language block is written from scratch in that
  language: its own slot pools (topics, companies, cities, apps, document and
  file names, people, math/logic prompts), its own group mains, and its own
  engine banks (openers, scene sentences, constraints, email frames,
  conversational fillers, closers). Real-world anchors are localized — Chinese
  cities and platforms for zh, Vietnamese names and places for vi, and so on —
  the way native speakers actually write.
- **Technical terms stay in their original script** where that is the natural
  usage (`React`, `Kubernetes`, `x²−5x+6=0`, `ECONNREFUSED`) — matching how
  each language's technical community writes.

## Authoring architecture

The Korean block composes every row in a single shape: situational opener
(+background) + group request + constraint tails. The en/zh/ja/vi blocks route
each row through one of **six structural authoring engines**:

| Engine | Shape |
|---|---|
| `composed` | Situational opener (95%) + optional background (38%) + main request + 1–4 constraint tails; the last tail may fork conditionally (~35%) |
| `brief` | 2–3 flowing scene sentences + connector (55%) with the request woven in + optional softener (50%) — no bolted-on opener/tail skeleton |
| `numbered` | Lead-in + main request + enumerated constraints (`1) …; 2) …; 3) …`, 2–4 items) |
| `convo` | Conversational filler + request + self-correction (30%) + softener (70%) — dialogue-register turns |
| `email` | Inline email framing: greeting + context + ask + request + tail (60%) + closer |
| `forked` | Optional opener (60%) + request + 1–2 explicit if/then branch tails + an "either way" base line |

Rows are routed first to one of six **profiles** (by axis/value); each profile
fixes the engine mix and the register (work / casual / terse):

| Profile | Applied to | Engine mix (weights) |
|---|---|---|
| general | most `service`, `sourcePolicies`, `diagramKind`, `artifactKind`, `presentationMode`, `requestedOutputs`, … | composed 30, brief 22, numbered 16, email 12, forked 12, convo 8 |
| formal | `complexity::hard`, `contentDomain::formal_reasoning` | brief 28, numbered 24, composed 20, email 14, forked 14 |
| code | `contentDomain::code_work`, `service::coding` | numbered 32, composed 22, brief 18, forked 16, email 6, convo 6 |
| quick | `complexity::simple` | composed 42, brief 30, convo 20, numbered 8 |
| personal | `contentDomain::{social,support,opinion,explore,personal_scope}`, `memoryIntent::personal` | convo 36, brief 26, composed 22, email 6, forked 6, numbered 4 |
| micro | `dialogueAct` (all), `memoryIntent::{conversational,navigational,none}`, `contentDomain::{play,self_capability,affective_state,unresolved}`, `action::none` | convo 72, composed 20, brief 8 |

The micro profile keeps short dialogue turns ("맞아", "嗯嗯", "そうだね"-style utterances) intact while padding them with surrounding context clauses, so the label's meaning survives inside a long-form distribution.

### Per-language contracts

The engine is language-agnostic; every string and orthographic rule lives in a
language pack (`dataset/generator/i18n/{en,zh,ja,vi}-*.mjs`):

| Lang | Joining | Terminal | Enumerated list | Per-language notes |
|---|---|---|---|---|
| en | space-joined | `.` | `1)` + `;` | email engine lowercases the joined ask; non-Latin leak scan with a math-glyph allowlist (`√ ≡ → ∞ — …`) |
| zh | no inter-word spaces | `。` | `1）` + `；` | fullwidth punctuation, 「」 quotation marks, spacing-normalizing post-pass, doubled-CJK-run scan |
| ja | no inter-word spaces | `。` | `1）` + `；` | same CJK contract as zh; polite/plain register mix |
| vi | space-joined | `.` | `1)` + `;` | full diacritics; doubled-word scan covers `À-ỹ` |

## Quality gates and integrity

**Data generation** (when each language's 600,000 rows are produced):

- **Deterministic**: mulberry32 seeded with FNV-1a over
  `` `${lang}::${category}::${value}` `` plus per-pass offsets; no
  `Math.random`, no timestamps. Identical inputs rebuild byte-identical
  output. The final shuffle uses a fixed global seed plus a per-language
  offset. Writes are atomic (`.tmp` + rename).
- **Generation**: 14 passes per group, ~1.2× attempts, local + global dedupe
  across all 150 groups — each language's 600,000 instructions are unique.
- **Build-time validation** (a build is OK only when all of these hold):
  exactly 600,000 lines; every line valid JSON with exactly
  `instruction/category/value`; zero unresolved `{slot}` leaks; 100% unique
  instructions; and the language-specific scans at zero — doubled-word rows
  for en/vi, doubled 2-char CJK runs for zh/ja, non-Latin leaks for en.

**File integrity** — `dataset.all.jsonl` only exists if every gate below
passes (`generator/merge.mjs` enforces them at write time; on failure no file
is left behind):

1. Fixed language order: ko → en → zh → ja → vi contiguous blocks
2. Every row JSON-parsed + 4 field type checks + `lang` code consistency
3. Exactly 600,000 rows per language · 3,000,000 total
4. Written to `.tmp` and renamed only on success (atomic) — a partial file
   that failed validation cannot exist

## Length profile

All five blocks share the long-form design goal, but absolute character counts
are script-dependent (a Han character carries far more than a Latin letter) —
**compare within a script, not across**:

| Lang | Avg chars | ≥80 | ≥120 | Min | Max |
|---|---:|---:|---:|---:|---:|
| ko | 140.2 | 92.8% | 69.5% | 25 | 273 |
| en | 204.4 | 95.0% | 85.6% | 17 | 483 |
| zh | 72.8 | 39.4% | 3.0% | 5 | 165 |
| ja | 98.4 | 73.1% | 26.6% | 6 | 226 |
| vi | 205.9 | 94.9% | 86.7% | 12 | 470 |

## Caveats

- This is template-combination generated data. Individual sentences are
  grammatical, but rare semantic mismatches between slot combinations (a work
  topic meeting a casual opener, etc.) can occur. Labels are unaffected;
  account for it in naturalness evaluations.
- The same topic may appear under different axes, and near-identical strings
  may exist across different axes within one language block. Instructions are
  unique **within each language block** (verified exhaustively); blocks are
  not deduped against each other (by design).
- Cultural/regional anchors differ per language on purpose. The invariant is
  the label, not the surface content.