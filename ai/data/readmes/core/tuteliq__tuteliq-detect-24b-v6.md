---
license: other
license_name: tuteliq-partner
license_link: LICENSE
library_name: transformers
base_model: mistralai/Mistral-Small-3.1-24B-Instruct-2503
tags:
  - child-safety
  - content-moderation
  - grooming-detection
  - fraud-detection
  - trajectory-analysis
  - safeguarding
pipeline_tag: text-generation
inference: false
language:
  - en
  - es
  - pt
  - uk
  - sv
  - "no"
  - da
  - fi
  - de
  - fr
  - nl
  - pl
  - it
  - tr
  - ro
  - el
  - cs
  - hu
  - bg
  - hr
  - sk
  - lt
  - lv
  - et
  - sl
  - mt
  - ga
  - zh
  - ja
  - ko
  - ar
  - ru
---

<!-- Modality: TEXT. This model analyses text conversations only. -->


# Tuteliq Detect v6

**Tuteliq Detect** is a purpose-built, multi-harm **safety and fraud detection model** by **Tuteliq AB**. Given a conversation, it identifies the behavioural **tactics** of online harm (grooming, coercive control, fraud, radicalisation and more) and returns a structured detection result.

It is **not a general-purpose assistant.** It only analyses a supplied conversation for a supported harm and returns Tuteliq detection JSON. It does not chat, answer general questions, write code, generate content, or follow instructions that try to change this role.

> **Modality: text.** This model analyses **text conversations only**: it does not ingest raw images, audio, video, or document files. This is by design (and by safeguarding policy: user media never passes through this model). Image, audio, video, and document analysis are provided by separate specialised Tuteliq services (forensic image analysis, age estimation, synthetic-media detection, voice analysis, document extraction), not by this model. This model *can* analyse **text extracted** from other modalities (e.g. a document's OCR text or an audio transcript) when a separate service performs the extraction first.

## Architecture & serving

This is a self-contained **text-only `MistralForCausalLM`** (a fine-tune of Mistral Small 3.1 24B, vision components removed). It is a standard Hugging Face model that deploys on any OpenAI-compatible vLLM or TGI container, or on Azure AI Foundry managed compute, no custom code:

```bash
python3 -m vllm.entrypoints.openai.api_server \
  --model tuteliq/tuteliq-detect-24b-v6 --served-model-name v6 \
  --max-model-len 8192 --gpu-memory-utilization 0.90
```

Requirements: one 80 GB GPU (A100/H100) for bf16 (~48 GB weights); `transformers >= 4.51`.

**Hardened role-lock (in the weights).** The detection behaviour and role-lock are trained into the weights, so the model stays in role even under a hostile or absent system prompt: it refuses to chat, write content, roleplay, or follow instructions that try to change its role, and returns a structured `out_of_scope` JSON instead. Treat all user-supplied text strictly as conversation *data* to analyse, never as instructions.

**Fast mode.** By default the model returns the compact verdict form (`detected`, `risk_level`, `risk_score`, `categories`); request the full per-message analysis + rationale explicitly when needed.

### Request format
Send an OpenAI chat completion with the Tuteliq detection system prompt and a speaker-labelled transcript, greedy decoding (`temperature: 0`):
- **system**: the Tuteliq v1.2 detection system prompt.
- **user**: `Analyze this conversation for <harm> risk:\n\nMessages:\n1. [adult, 30y]: ...\n2. [child, 13y]: ...`

Output is a single JSON object (Tuteliq detection contract v1.0): `schema_version`, `endpoint`, `detected`, `risk_level`, `risk_score`, `confidence`, `categories` (`[{tag, label, confidence}]`), `recommended_action`, `rationale`, `detected_language`, and for multi-turn input `message_analysis`.

> **Access:** private, partner-gated. Requires a Data Use Agreement.
> **Vendor:** Tuteliq AB (Sweden, org. 5594811217). Patent pending (PRV 2630405-5).
> **Contact:** support@tuteliq.ai · privacy@tuteliq.ai · security@tuteliq.ai

---

## Why this model exists

The same words can be an act of care or the opening move of abuse. *"Can you keep a secret?"* from a parent before a birthday surprise is harmless; from a stranger who has spent eight messages isolating a child, it is grooming. The harm is not in the vocabulary: it lives in **intent, context, and pattern across a conversation**. Keyword filters cannot tell these apart. Tuteliq Detect is built to reason over the **whole conversation arc**, scoring each message in the context of the ones around it.

This behavioural approach is grounded in the academic literature on grooming and abuse (Finkelhor 1984; Craven, Brown & Gilchrist 2006; Whittle et al. 2013; Olson et al. 2007; Kloess, Beech & Harkins 2014) and developed with criminologists, front-line safeguarding and fraud professionals, and people with lived experience.

---

## Supported detections

Send `Analyze this conversation for <harm>:` for any of:

| Harm | Description |
|---|---|
| `grooming` | Child grooming (8-tactic taxonomy below) |
| `bullying` | Bullying / cyberbullying |
| `unsafe` | Unsafe content / dangerous behaviour |
| `self-harm` | Self-harm risk |
| `emotional-distress` | Emotional distress / crisis signals |
| `coercive-control` | Coercive control |
| `vulnerability-exploitation` | Exploitation of a vulnerable person |
| `radicalisation` | Radicalisation / extremism |
| `tfgbv` | Technology-facilitated gender-based violence |
| `image-based-abuse` | Image-based sexual abuse / sextortion |
| `social-engineering` | Social engineering |
| `romance-scam` | Romance scam |
| `mule-recruitment` | Money-mule recruitment |
| `app-fraud` | Authorised push-payment / app fraud |
| `gambling-harm` | Gambling harm |

A single **tactic architecture** (secrecy, isolation, boundary-pushing, and others) recurs across these harms; the model shares that architecture rather than treating each harm as a separate keyword problem.

---

## Detection modes

1. **Directed**: `Analyze this conversation for grooming:` → one harm, best accuracy.
2. **Multi-detection**: `Analyze this conversation for harm:` (no harm named) → screens for **all** relevant harms in a single pass and returns a `mode: "multi"` result with one detection object per harm found.
3. **Trajectory / per-message**: for multi-turn input, every response includes `message_analysis[]` with a per-message risk score and the tactics present on that turn, so you can see *how* the risk escalates across the arc.

---

## Input format

```
Analyze this conversation for grooming risk:

Messages:
1. [adult, 30y]: you're so much more mature than other kids your age
2. [child, 13y]: haha thanks
3. [adult, 30y]: let's keep this just between us, your parents wouldn't get it
```

- One numbered line per message; `[role, age]` prefix is recommended (roles e.g. `adult`/`child`; age optional).
- Multi-turn conversations are analysed as a unit (trajectory-aware). Single messages are also supported.

## Output format (detection contract v1.0)

```json
{
  "schema_version": "1.0",
  "endpoint": "grooming",
  "detected": true,
  "risk_level": "high",
  "risk_score": 0.78,
  "confidence": 0.9,
  "categories": [
    {"tag": "SECRECY_REQUEST", "label": "Secrecy Request", "confidence": 0.9},
    {"tag": "FLATTERY", "label": "Flattery", "confidence": 0.85}
  ],
  "recommended_action": "flag_for_review",
  "rationale": "The adult builds a privileged bond through flattery, then presses for concealment of the contact from the child's guardians.",
  "detected_language": "en",
  "message_analysis": [
    {"message_index": 1, "risk_score": 0.6, "categories": ["FLATTERY"], "summary": "Targeted praise to build a special bond."},
    {"message_index": 2, "risk_score": 0.05, "categories": [], "summary": "Ordinary reply."},
    {"message_index": 3, "risk_score": 0.75, "categories": ["SECRECY_REQUEST"], "summary": "Push to conceal the contact from guardians."}
  ]
}
```

**Field reference**

| Field | Type | Notes |
|---|---|---|
| `schema_version` | string | `"1.0"` |
| `endpoint` | string | the harm analysed, or `"meta"` |
| `detected` | bool | whether the harm is present |
| `risk_level` | enum | `none` \| `low` \| `medium` \| `high` \| `critical` |
| `risk_score` | 0 to 1 | age-adjusted severity |
| `confidence` | 0 to 1 | model confidence |
| `categories` | array | `{tag (SCREAMING_SNAKE_CASE), label, confidence}`, the tactics present |
| `recommended_action` | enum | `none` \| `monitor` \| `flag_for_review` \| `guardian_notify` \| `transaction_hold` \| `immediate_intervention` |
| `rationale` | string | describes the tactics; never quotes the participants |
| `detected_language` | ISO 639-1 | e.g. `en` |
| `message_analysis` | array | per-turn `{message_index, risk_score, categories, summary}` (multi-turn input) |
| `analysis_status` | string | `"degraded"` when input cannot be confidently analysed |

## Multi-detection example

Request: `Analyze this conversation for harm:` → returns

```json
{
  "schema_version": "1.0",
  "mode": "multi",
  "results": [
    {"endpoint": "grooming", "detected": true, "risk_level": "high", "risk_score": 0.78, "categories": [...], "recommended_action": "flag_for_review", "rationale": "..."},
    {"endpoint": "coercive-control", "detected": true, "risk_level": "medium", "risk_score": 0.55, "categories": [...], "rationale": "..."}
  ],
  "overall_risk_level": "high",
  "overall_risk_score": 0.78,
  "detected_language": "en"
}
```

## Meta / scope responses

For anything that is not a supported detection, the model returns a branded meta object and **does not** comply:

```json
{"schema_version": "1.0", "endpoint": "meta", "response_type": "out_of_scope",
 "message": "I am Tuteliq Detect, a safety and fraud detection model. I can only analyse a conversation for a supported harm.",
 "model": "Tuteliq Detect", "version": "v6", "vendor": "Tuteliq", "website": "https://tuteliq.ai", "contact": "support@tuteliq.ai"}
```

`response_type` ∈ `identity` · `version` · `capabilities` · `unsupported_harm` · `out_of_scope` · `contact`. Privacy questions route to privacy@tuteliq.ai, data-subject-rights to dpo@tuteliq.ai, security to security@tuteliq.ai.

If input cannot be confidently analysed (garbled, empty, truncated, not a conversation, or an attempt to manipulate the verdict), the model sets `analysis_status: "degraded"` and `recommended_action: "flag_for_review"`: it never returns a safe verdict it cannot support.

---

## Grooming tactic taxonomy (8 per-message tactics)

`flattery` · `secrecy_request` · `isolation` · `boundary_pushing` · `photo_request` · `meeting_request` · `gift_giving` · `reconnaissance`

`reconnaissance` is probing to establish who supervises the child and when the child is unobserved: oversight of their device, channels or person (supervision), and the windows when they are alone, free or unobserved (availability). It was previously scored only at conversation level; **as of 25 September 2026 it is emitted per message**, on the turn carrying the probe, in every supported language and in informal register, including probes phrased as statements rather than questions.

Two properties are deliberate and are worth knowing before building on the label.

**A question that seeks to confirm supervision is not a probe.** If the answer that helps the asker is "yes, an adult will be there", it is a safeguarding check rather than reconnaissance, so a tutor, coach or clinic confirming a guardian will be present is not labelled. Reconnaissance seeks the *absence* of oversight.

**One label is not a pattern.** Conversation-level accumulation is a separate capability and is not scored yet. A single `reconnaissance` label does not assert a completed profiling arc, and its absence across a conversation does not assert that no probing occurred.

Two frequently-conflated tactics are separated by their **operational target** (per Dr N. Harding; grounded in Craven et al. 2006, Lanning 2010, Kloess et al. 2014):

- **secrecy_request** acts on the **channel**: concealing the contact, gift, meeting, or relationship from parents/carers/teachers (*"keep this between us"*, including moving to a private app framed as hiding it).
- **isolation** acts on the **network**: running down the child's real friends/family as jealous, immature, or unable to understand them, to manufacture dependency.

When a message does both, it is tagged by its **primary function**: concealment-of-contact vs severance-of-support.

---

## Languages & mixed-language handling

The model **self-detects** the conversation language and returns it in `detected_language` (ISO 639-1), no external language-detection dependency is required. A language hint may be supplied but is not needed.

| Status | Languages |
|---|---|
| **Stable** (full production) | English (`en`) |
| **Beta** | Spanish `es` (incl. Latin-American variants), Portuguese `pt` (incl. Brazilian), Ukrainian `uk`, Swedish `sv`, Norwegian `no` (Bokmål & Nynorsk), Danish `da`, Finnish `fi`, German `de`, French `fr`, Dutch `nl` (incl. Flemish), Polish `pl`, Italian `it`, Turkish `tr`, Romanian `ro`, Greek `el` (Greeklish also recognised), Czech `cs`, Hungarian `hu`, Bulgarian `bg` (Cyrillic & Latin), Croatian `hr` (also Serbian/Bosnian), Slovak `sk`, Lithuanian `lt`, Latvian `lv`, Estonian `et`, Slovenian `sl`, Maltese `mt` (heavy code-switching supported), Irish `ga`, Chinese `zh` (Simplified & Traditional; mainland, Taiwan, Hong Kong and Singapore usage, including written Cantonese), Japanese `ja`, Korean `ko`, Arabic `ar` (Modern Standard plus Egyptian, Levantine, Gulf and Maghrebi dialects; Arabizi recognised), Russian `ru` (translit recognised) |

**32 languages are supported: English stable, 31 beta.** That is the size of the `LANGUAGE_GUIDELINES` registry, which gates support. 26 carry the 728-case matrix; the remaining six are measured directly below, so every supported language now carries a figure.

**Mixed languages / code-switching.** The behavioural tactics are language-agnostic, so the model is trained to detect them across **code-switched** conversations (e.g. English↔Spanish within a sentence, or two non-English languages mixed). Mixed input returns `detected_language: "mul"`. Deliberate language-mixing to evade monolingual filters is treated as content to analyse, not a reason to under-fire.

### Languages outside the 728-case matrix

Six supported languages (`ga`, `zh`, `ja`, `ko`, `ar`, `ru`) sat outside the
multilingual matrix. They were measured on 2026-10-01 against the hosted Tuteliq
API, alongside `mt` as a matrix control. **The hosted API does not run this
model**, so this table is evidence about Tuteliq's platform, not about these
weights; it is kept here only because it is the sole figure for these six
languages. A measurement of this model on them is still to be done.

Four canonical tactics (secrecy request, meeting request, photo request,
isolation) and two benign controls per language:

| language | tactic recall | benign false positives |
|---|---|---|
| Maltese `mt` *(matrix control)* | 4/4 | 0/2 |
| Irish `ga` | 4/4 | 0/2 |
| Chinese `zh` | 4/4 | 0/2 |
| Japanese `ja` | 4/4 | 0/2 |
| Korean `ko` | 4/4 | 0/2 |
| Arabic `ar` | 4/4 | 0/2 |
| Russian `ru` | 4/4 | 0/2 |

**Read this as a capability signal, not a per-language performance figure.** Six
cases per language is far too small for a rate, and the cases are translated
from validated English anchors **without native review**. Native review is the
gate before any of these appear as a headline number. What it does establish is
that the tactic signal survives into each of these languages rather than being
an untested assumption.

---

## Stateful trajectory continuation

For high-volume streaming, the hosted Tuteliq API supports a **continuation token**: a signed, client-carried trajectory state (per-category counts, severity history, trajectory label, **no raw message text**). A caller can send only the *new* message plus the token, and the service reconstructs the trajectory without re-sending the history and without storing it server-side. This preserves arc-level awareness at constant request size, privacy-preserving by design.

---

## Evaluation

Evaluated across nine benchmark suites, 2,400+ held-out cases. **Two things to
read before the table, because they change what the numbers mean.**

**Most of these suites are in-distribution.** The expert-trajectory, TUT-100,
multilingual-matrix, coded-language and duality sets were authored under the
same direction as the training data, by a **single expert annotator, with no
inter-annotator agreement study**. They demonstrate that the model learned what
it was taught. They are not evidence of field performance, and an earlier
version of this card described all nine as "independent", which was wrong.

**The externally sourced sets are the ones to weigh:** PAN12 (public, 2012) and
COVA-X (Lochstampfor, C., & Roy, A. (2026). COVA-X. arXiv:2606.06879. https://arxiv.org/abs/2606.06879; terms of use at https://scamlingua.org/). The gap
between 0.987 on our held-out expert set and 0.806 on TUT-100 (0.886 after the
label corrections described under Tactic adjudication) is the honest measure of
how much same-direction authoring is worth.

Each row below is marked accordingly.

| source | meaning |
|---|---|
| **in-distribution** | authored under the same direction as training; single annotator; no IAA |
| **external** | third-party dataset, not authored by Tuteliq |

| Benchmark | Macro-F1 | Precision | Notes |
|---|---|---|---|
| *in-distribution* · **Expert trajectories** (500 held-out, criminologist-authored multi-turn) | **0.987** | **1.00** | tactic-disambiguation rules now weight-native; recall 0.976; flattery, photo_request and gift_giving at 1.00, secrecy 0.994, boundary_pushing 0.955; covers grooming, sextortion, financial grooming, coercive control, image-based abuse, TFGBV |
| *in-distribution* · Benign specificity (legitimate parent / teacher / coach / sex-ed conversations) |, | 1.00 | zero false positives on 450 benign turns. **450 turns cannot establish a deployment false-positive rate; see Benign specificity below.** |
| *in-distribution* · **26-language held-out matrix** (728 expert-pattern cases, 7 tactics per language) |, |, | 96.4% exact-tactic identification; 10 languages at 100%; zero missed detections in 728 (all residual errors are adjacent-tactic labels with the harm still flagged); in-language analysis, not translation |
| *in-distribution* · **Adversarial red-team** (86 attacks: jailbreaks, prompt swaps, injection, romantic/roleplay lures) |, |, | **86 attacks is a starting point, not a robustness claim.** 97.7% hold rate; 100% on jailbreaks, injections, and system-prompt overrides; residual cases flagged the attack as grooming rather than complying |
| **external** · **Real-world predator chats** (PAN12, author-labelled sample, measured on this model) |, |, | predator recall **0.78** at risk ≥ 0.6, conversation level; 102 of 120 predator conversations flagged as detected. The non-predator side is adult IRC chat, not child-safe conversation: 74 of 120 were flagged, so it cannot stand in for a false-positive rate (see below). Tuteliq's curated benign sets remain at zero false positives |
| *in-distribution* · Coded language / emoji evasion (proprietary lexicon, 60 cases) |, |, | 39/39 coded-positive detections, 0 false positives on 21 benign look-alikes |
| *in-distribution* · Trajectory duality ("Can you keep a secret?") |, |, | same phrase: benign context risk ≈ 0.02, grooming context risk ≈ 0.75 |
| **external** · **Cross-domain fraud, COVA-X benchmark** (150 scam conversations: romance, government impersonation, bank; Lochstampfor, C., & Roy, A. (2026). COVA-X. arXiv:2606.06879. https://arxiv.org/abs/2606.06879) |, |, | conversation-level detection: **bank 100%** (50/50), **government impersonation 100%** (50/50), **romance 94%** (47/50) with the v1.3 serving prompt, 92% with v1.2; the residual romance cases contain no observable scam behaviour within the evaluated window (pure rapport-building before any ask), trajectory continuation catches the eventual ask in streaming deployment |

The model reasons over the whole conversation; individual messages that look benign in isolation are correctly surfaced when the **arc** reveals harm.

Coded-language comparisons against general-purpose moderation services were run through the hosted Tuteliq API, where a separate coded-term layer sits around the detection, so they are not figures for this model and are not listed here.

*Benchmark data: COVA-X, Lochstampfor, C., & Roy, A. (2026). COVA-X. arXiv:2606.06879. https://arxiv.org/abs/2606.06879. Terms of use: https://scamlingua.org/. Used with the authorization of its authors, who have granted Tuteliq permission to evaluate against it and to reference these results in public materials.*

---

## Benign specificity is unquantified

Grooming base rates are very low, so deployment precision is governed by the
false-positive rate over **large volumes of ordinary conversation**, not by the
450 benign turns above. That figure is real but far too small to stand in for
it, and it should not be cited as a deployment precision claim.

For calibration, on PAN12's non-predator class (adult-to-adult IRC chat, 120
conversations) this model flagged **74 of 120 (0.62)**. That class is not
child-safe conversation, so it does not measure what a false positive means in
deployment either. It is reported because withholding it would leave the
impression that 1.00 precision generalises.

A large-scale benign corpus is in progress. **Until it exists, treat deployment
precision as unquantified.**

## Metrics we do not publish for PAN12, and why

PAN12 accuracy and precision are governed by how participant roles and ages are
framed in the request and by the adult-chat negative class described above, so a
single figure would not be meaningful. Measured on this model, AUC was **0.63**
on a 100-conversation sample.

**Recall is the defensible figure on this dataset**, and PAN12 is 2012 data.

The figures above come from the author-labelled construct, where a conversation
counts as positive because a predator is in it, even when that conversation is
ordinary chat. Tuteliq's benchmark has since moved to the corpus's own
line-level annotation of predatory messages, which measures what the corpus
actually marks. This model has not yet been measured on that construct; the
figures here will be replaced when it is.

## Fairness

**Under evaluation. Not yet publishable, and stated here rather than omitted.**

Text moderation models have documented bias against dialects such as AAVE and
against LGBTQ+ young people discussing their own identity. The previous version
of this card said nothing about either, which an external reviewer correctly
identified as a gap.

We have begun measuring both. An early internal probe found **no dialect effect**
on the cases tested, and **did identify a defect affecting young people
discussing their identity**. That defect is being fixed, and the mechanism is
deliberately not described here: publishing the specific shape of a detection
gap hands an evasion route to the people this model exists to detect.

We will publish per-group figures once the corpus is large enough for a rate to
mean something. A number from a set this small, for a defect already identified
and being worked on, would be worse than this paragraph.

## Reproducibility

Results come from a separate evaluation repository, not from ad-hoc runs:

- datasets pinned by **manifest SHA-256**
- **pre-registered floors**, set before the run and recorded with the
  measurement that set them
- for the hosted API, gates executed **in CI against the live API**; figures on this card were measured on the model itself, served with vLLM
- per-run reports retained, including runs that moved numbers the wrong way

Available to evaluators alongside the Data Use Agreement. If you are assessing
this model and want the harness, ask.

## Independent evaluation

None of the above is a third-party evaluation of this model. Independent
evaluations of text detection are under way, and they test the hosted Tuteliq
API, which runs a different detection system; their results will not describe
this model. The existing IWF relationship covers image work only. **Until an external
evaluation exists, every in-distribution figure on this card should be read as
self-reported.**

---

## Tactic adjudication: boundary_pushing and reconnaissance

Expert re-adjudication by Dr Nicola Harding (criminologist, Chief Scientific Officer), 13 August 2026. **Identical model predictions, no retraining.**

All sixteen `boundary_pushing` anchor turns in TUT-100 v1 were found to be mislabelled, and were re-adjudicated as follows.

**Four turns · concealment framing → `secrecy_request`.** *"just between us"*, *"no need to make it a big family announcement"*. These act on the **channel**: an instruction to withhold the conversation from parents. There is no access-advance in the utterance, so `boundary_pushing` does not apply.

**Eleven turns · supervision and availability probes → `reconnaissance`.** *"are your parents checking your messages?"*, *"do your parents sit near you?"*, *"how late are you allowed out on your own?"*. This is information-gathering. `reconnaissance` was already carried in the taxonomy but was scored only at conversation level at the time, so it was absent from the per-message benchmark and that benchmark defaulted to `boundary_pushing` as the least-wrong bucket. It became a per-message tactic on 25 September 2026, which does not change any label in this section.

The sixteenth turn is an age question wrapped in praise. `reconnaissance` is scoped to supervision, availability and unobserved access, so an age question is not a probe; that reading was confirmed by Dr Nicola Harding, who authored the taxonomy. So **one anchor did remain that is not a probe**, and an earlier version of this card said twelve probes with no genuine anchors left. Both were wrong, and the correction runs against us: the tactic was less cleanly *untested* by that benchmark than claimed. The model's behaviour was correct on both groups: it labelled the concealment turns `secrecy_request`, and declined to call the reconnaissance probes `boundary_pushing`. The per-item reasoning for all sixteen turns is published at https://docs.tuteliq.ai/boundary-pushing-readjudication.

**Corrected per-message result:** macro F1 **0.886** at precision **1.00** across the six per-message tactics, from the same predictions with corrected labels.

Any earlier citation of **0.316** for `boundary_pushing` is **withdrawn**. It measured label quality, not model quality.

### Purpose-built follow-up sets

| Set | Result | Note |
|---|---|---|
| `boundary_pushing`, 10 genuine anchors + 4 benign controls | F1 **0.750**, recall 0.60, precision 1.00 | Catches explicit and repeated pushes; misses softer first-move normalisation |
| `reconnaissance`, 5 probe + 5 benign conversations | recall **1.00** | Conversation-level result, measured before the tactic moved to per-message scoring |

### Known refinement

Severity is not yet conditioned on the **speaker relationship**. *"Is anyone home with you tonight?"* carries a different operative function from a stranger on a gaming platform than from a foster carer checking in, and the risk is carried by direction and role rather than by the words. The per-message discriminator addresses part of this at the utterance level, by separating a probe seeking the absence of oversight from a check seeking to confirm it, but it does not condition severity on who is speaking. This is a calibration item, not a capability gap.

A deliberate consequence of that same discriminator: an adult who phrases a probe as a supervision check (*"will your mum be home when I come round? just want to make sure it's ok"*) is seeking presence by the wording and is not labelled reconnaissance. Separating that from a genuine safeguarding check requires the conversation arc, not the single utterance.

---

## Response envelope: model output vs SDK

This model returns **only the detection**. Production responses also include an *envelope* added by the Tuteliq SDK/API, never by the model. On Foundry, the envelope is provided by the companion Tuteliq SDK (or a bundled server-side wrapper).

| From the **model** | From the **SDK/API envelope** |
|---|---|
| `detected`, `risk_level`, `risk_score`, `confidence`, `categories`, `rationale`, `message_analysis`, `detected_language`, `recommended_action` | `support` (helplines, emergency number, response guide, a **curated per-country/per-harm database**, never model-generated) · `continuation_token` / `continuation_expires_at` / `state_source` · `normalized` · `language_status` · `credits_used` · echoed `external_id` / `customer_id` / `metadata` / `country` |

**Context inputs** (`country`, `childAge`, `external_id`, `customer_id`, `metadata`, `continuation_token`) are supplied by the caller to the SDK/API and are **stripped before the model**: the model only ever sees `content` + the harm to analyse. In particular, **`country` is a caller input** used to select helplines; it is never inferred by the model (language ≠ country), and helplines/emergency numbers are never model-generated (a safety requirement).

## Deployment

- Format: **merged, self-contained `MistralForCausalLM`** (safetensors, 10 shards). The LoRA adapter it was merged from is kept under `adapter/` for reference.
- System prompt: the Tuteliq detection prompt (supplied separately to partners); the model is trained to run on a compact prompt. **Serving prompt v1.2** (`docs/serving-prompt-v1.2.txt`) remains the recommended deployment prompt. Its two tactic-disambiguation rules (flattery-vs-isolation; push-vs-wrapper) are **now also trained into the weights**, making detection quality robust to minor prompt drift.
- Greedy decoding recommended for stable, schema-valid JSON.
- **Fast mode (verdict-only):** appending the verdict-only directive (see SDK `verdict_only`) suppresses the per-message `message_analysis` array, validated at 99% compliance with **100% verdict agreement** vs full mode on held-out trajectories, cutting output length (and latency) roughly 3 to 4× for real-time screening.
- **The hosted Tuteliq API does not currently run this model.** It runs Tuteliq's deployed detection system, which is versioned separately (`GET https://api.tuteliq.ai/health` reports it as `detector_version`). Figures measured through the API describe that system, not this model, and are reported in our disclosure rather than here.

## Intended use & limitations

- **Intended:** assistive safety triage for platforms, guardians, and safeguarding/fraud teams, surfacing conversations for **human review**, not autonomous action.
- **Out of scope:** general chat, content generation, or any use outside the supported detections. The model refuses these.
- **Language:** English is fully validated (Stable); 31 additional languages are Beta (see Languages).
- **Not a determination of guilt.** Outputs are risk signals for human judgement. High-stakes actions (e.g. guardian notification) should involve a human.
- **Known items being addressed** in the next revision: branded-refusal formatting on some direct off-topic prompts under a bare prompt; the `detected` flag on a small number of cross-harm endpoints.

## Data, privacy & governance

- Tuteliq stores **no user content**: no messages, images, or derived artefacts.
- The continuation token carries only aggregate state and hashed evidence pointers, never raw text.
- **Training data contains no real cases and no personal data.** The corpus is fully synthetic conversational material authored and validated under the direction of Dr Nicola Harding (Co-Founder & Chief Scientific Officer, criminologist): expert-designed offender-behaviour scenarios grounded in the published tactic taxonomy, never real victim conversations, real identities, or personally identifiable information of any kind. No CSAM or real abuse material is used at any stage of training or evaluation.
- **"Synthetic" means fabricated, not collected.** The conversations were written rather than gathered from real people; expansion was AI-assisted under expert direction, with expert validation of the output. Fabrication was a deliberate data-protection decision by the authoring experts, who declined to work from real case material so that no victim's data could enter the corpus, be retained, or leak through the model.
- **Who did what.** External consultants in criminology, child psychology and linguistics supplied the material and ran validation tests in their own domains, with their findings acted on. Dr Harding led the programme and labelled and validated the corpus. The consultants did not apply labels, so Dr Harding is the sole annotator and **no inter-annotator agreement statistic exists**. The panel evidences expertise, not independence: the consultants were engaged and paid by Tuteliq, and Dr Harding is a co-founder and shareholder.
- **Ground truth is not independently produced.** Every in-distribution figure in this card rests on labels we produced ourselves. Independent evaluations now under way test the hosted Tuteliq API, not this model.
- The expert-authored material is the English backbone. Multilingual coverage is derived from it by translation and in-language generation with native-speaker review.
- Held-out evaluation sets are isolated from training data by an 8-word shingle leak-guard.

**Transparency disclosure.** Tuteliq publishes a completed disclosure for this model against [TUT-CSDT-001](https://tuteliq.ai/standard), the Child Safety Detection Transparency Framework, covering what is measured, what is not, and where we fall short. Full provenance is recorded there at clause P2.8.3, and it is the authoritative source where this card and that document differ:

- Framework: <https://tuteliq.ai/standard>
- Our disclosure: <https://docs.tuteliq.ai/vendor-reference-disclosure>
- Machine-readable: <https://docs.tuteliq.ai/csdt-disclosure.json>

## Team & authors

**Dr Gabriel Sabadin**: Founder, Chief Executive Officer & Chief Technology Officer, Tuteliq.
Dr Sabadin is a computer scientist with over 25 years of experience in software engineering and machine learning. He designed and built the entire Tuteliq platform, from research data to production API, and leads the company's technical architecture, AI model development, and product strategy. PhD in Computer Science; 21+ years in ML engineering; has built ML systems for Citibank, MasterCard, Adobe, and Apple; inventor of Tuteliq's patent-pending Multi-Signal Forensic Pipeline (PRV 2630405-5).

**Dr Nicola Harding**: Co-Founder & Chief Scientific Officer, Tuteliq.
Dr Harding is a criminologist whose research focuses on child exploitation, coercive control, and the psychology of online harm. Her work underpins Tuteliq's approach to detecting grooming and manipulation as behavioural patterns rather than keywords, and informs how the platform's models are trained, validated, and reviewed. She advises law enforcement and safeguarding bodies, and guides Tuteliq's detection science and clinical review.

**Prof Sarah Kingston**: Advisor, Tuteliq.
Professor Kingston is a leading criminologist specialising in criminal justice, policing, and sexual offences. As Research Lead for the UK National Centre for Violence Against Women and Girls, she bridges academic research with operational policing, and advises Tuteliq on detection methodology, research ethics, and the intersection of technology with criminal justice practice. Professor of Criminal Justice & Policing at the University of Central Lancashire; expert witness to UK parliamentary committees including the Home Affairs Select Committee; cited 990+ times and published in leading criminology journals.

## Acknowledgements & references

Developed with criminologist **Dr Nicola Harding** and safeguarding, law-enforcement, financial-crime, and lived-experience contributors.

Craven, Brown & Gilchrist (2006); Finkelhor (1984); Whittle et al. (2013); Olson et al. (2007); Kloess, Beech & Harkins (2014); Lanning (2010); Quayle & Taylor (2011); Wortley & Smallbone (2006); Stark (2007); Home Office (2015); FATF (2019); Levi & Handley (2016).

## Citation

```
@software{tuteliq_detect_v6,
  title  = {Tuteliq Detect v6},
  author = {Tuteliq AB},
  year   = {2026},
  note   = {Multi-harm safety and fraud detection model. Patent pending (PRV 2630405-5).},
  url    = {https://tuteliq.ai}
}
```

© Tuteliq AB. Partner-gated; use governed by the Tuteliq Data Use Agreement.
