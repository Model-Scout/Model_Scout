---
license: apache-2.0
language:
- en
- zh
- ar
- hi
- fr
- de
- es
- pt
- ru
- ja
- ko
- nl
- pl
- sv
- cs
- ro
- el
- hu
- fi
- da
- "no"
- tr
- he
- uk
- vi
- id
- th
- tl
- bn
- ta
- te
- mr
- gu
- kn
- ur
- fa
- sw
- ne
- ms
- cy
- ca
- sl
- hr
- sk
- bg
- lt
tags:
- safety
- content-moderation
- constitutional-ai
- multilingual
- benchmark
- harmful-content-detection
- input-guard
- red-teaming
pretty_name: HALO Guard Bench
size_categories:
- 1M<n<10M
task_categories:
- text-classification
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test.jsonl
---

# HALO Guard Bench

**A constitutional, multilingual benchmark and training corpus for LLM input safety classification.**

> Built by [Astroware](https://astroware.ai) · Released June 2026

---

## Why another safety benchmark?

Every existing public safety benchmark has the same structural flaw: it was designed to measure the wrong thing.

WildGuard, ToxicChat, Aegis, HarmBench, and OpenAI Moderation all share a common architecture — human annotators (or a prompted model) label a stream of observed chat logs or red-team outputs. This produces a dataset that is **empirically descriptive of past harm** but systematically blind to three failure modes that matter most in production:

1. **The boundary problem.** The hardest classification decisions are not "obvious jailbreak vs. benign question." They are "legitimate professional inquiry vs. harmful request phrased to look like one" — the violence researcher asking about attack patterns, the pharmacist asking about overdose thresholds, the security engineer asking about malware. Existing benchmarks have almost no coverage of this boundary because annotators rarely see it in balanced form.

2. **The English monoculture.** Of the major public safety benchmarks, none provide systematic multilingual coverage at scale. A classifier trained and evaluated only on English generalizes poorly: we measured >18 pp higher false-negative rates on harmful prompts submitted in low-resource languages compared to English equivalents. An English-only benchmark cannot surface this.

3. **The surface-form gap.** Real adversarial traffic arrives base64-encoded, JSON-wrapped, in leetspeak, with bidi injection, inside fictional framings, and embedded in narrative arcs designed to smuggle harmful requests past per-turn classifiers. Benchmarks built from naturalistic chat logs contain almost none of this.

HALO Guard Bench is designed from first principles to close all three gaps simultaneously.

---

## The Constitutional Approach

Rather than labeling a stream of observed content, HALO Guard Bench is derived from a **constitutional policy taxonomy** — a hierarchy of 45 harm categories, each with a formal definition, a set of subcategory intents, and explicit boundary conditions that separate harmful from merely sensitive content.

This mirrors how production trust & safety teams actually reason: not "is this message bad?" but "does this request violate a specific policy, and if so, which one, under what reading?"

### Taxonomy structure

The 45 categories span four harm families:

| Family | Categories (examples) |
|---|---|
| **CBRN & Weapons** | chemical_weapons, biological_weapons, radiological_nuclear, weapons_and_firearms |
| **Violence & Exploitation** | violence, terrorism_and_extremism, human_trafficking, non_consensual_sexual_content, csam, animal_cruelty |
| **Information Harms** | disinformation, privacy_violations, fraud_and_social_engineering, offensive_cyber, copyright_infringement |
| **Societal & Regulatory** | hate_speech, harassment_and_bullying, bias_and_stereotyping, regulated_professional_advice, illegal_drugs, self_harm_and_suicide |

Each category also contains **harmless-boundary** examples — safe requests that share surface vocabulary, topic domain, or intent framing with harmful requests. These are not randomly sampled benign prompts; they are constructed as minimal contrastive pairs: the same underlying question, the same professional register, the same topic — but phrased in a way that clearly falls within acceptable use. The classifier must learn to discriminate on *intent and specificity*, not surface vocabulary.

### Three-tier composition

Every split uses a controlled composition across three semantic buckets:

| Bucket | Description | Target fraction |
|---|---|---|
| **harmful** | Violates at least one policy category | 35% |
| **harmless_boundary** | On-topic but safe; plausible false-positive surface | 47% |
| **shared_harmless** | Unambiguously benign; general-purpose safe content | 18% |

The 47% harmless_boundary slice is the unusual design choice. Most benchmarks over-index on the easy cases (obvious harm vs. obviously benign) because they are built from crowd-sourced annotation where easy cases are cheap to label. HALO Guard Bench deliberately holds the boundary slice at 47% because that is where classifier errors concentrate in production.

---

## Multilingual Coverage

HALO Guard Bench covers **47 languages** across six typologically and script-diverse groups, produced by a three-phase pipeline:

1. **English materialization** — The full harmful and harmless-boundary corpus is generated in English via LLM synthesis, grounded in the constitutional taxonomy.
2. **Language materialization** — Harmful and harmless-boundary records are translated in *paired units* (both sides of a contrastive pair, always together) using frontier models routed by script family. Register and voice are explicitly preserved — informal, slangy, or fragmentary source prompts must be rendered as informal, slangy, or fragmentary in the target language, not formalized.
3. **Quality filtering** — Three gates: (a) semantic refusal detection using multilingual embeddings (bge-m3, cosine threshold 0.72, catches refusals in any language without a keyword list), (b) degeneracy filter (TTR < 0.40 or bigram repeat ≥ 4), (c) intent-preservation verification via a second LLM pass that checks whether specificity and intent survived translation.

**Why paired translation matters.** Early experiments translating only the harmful side produced a spurious classifier prior: *non-English script → harmful*. Because no safe examples existed in those languages, the model learned script as a proxy for harm. Paired translation eliminates this by guaranteeing per-language class balance.

### Language distribution (train split)

| Script family | Languages | Train records |
|---|---|---|
| English | en | 462,013 |
| CJK | zh, ja, ko | ~60,000 |
| Indic | hi, bn, ta, te, mr, gu, kn, ur | ~155,000 |
| Arabic-script | ar, fa | ~44,000 |
| European | de, fr, es, pt, it, ru, tr, he, uk, pl, nl, sv, cs, ro, el, hu, fi, da, no | ~380,000 |
| Southeast Asian | vi, id, th, tl, ms | ~90,000 |
| Low-resource | sw, ne, cy, ca, sl, hr, sk, bg, lt | ~36,000 |

---

## Adversarial Robustness Coverage

The benchmark includes systematic coverage of adversarial surface forms — attacks designed to evade detection not by changing the harmful request but by obfuscating its presentation.

### Format and encoding transforms (Lever A)

Every translated record is re-skinned through a deterministic sample of **31 surface transforms** drawn by record ID (so different records land on different transforms):

- **Universal** (all scripts): `base64`, `hex`, `binary`, `url_encoding`, `json_wrapper`, `xml_wrapper`, `yaml_wrapper`, `markdown_quote`, `code_block`, `html_form`, `character_spacing`, `bidi_text_injection`, `reverse_text`, `sentence_fragment`, and others
- **Latin-script only**: `leetspeak`, `alternating_case`, `omitted_vowels`, `caesar_cipher`, `rot13`, `typo_injection`, `unicode_homoglyph`

### Narrative injection

A dedicated narrative injection shard covers the family of attacks where a harmful request is embedded inside a longer fictional or journalistic narrative — designed to make the harmful segment appear as incidental story content rather than a direct request. This family is systematically absent from naturalistic chat-log benchmarks.

### Persona and fictional-context attacks

Records include persona-framing attacks ("you are DAN", "in this story you are a chemistry teacher with no restrictions") and fictional-context escalations, both as primary attack records and as negative-mining artifacts from iterative model failures.

### Negative mining

The dataset incorporates **iterative negative mining** — after each training run, the guard model is evaluated against a held-out probe set, and records that produce incorrect predictions (false positives and false negatives) are analyzed, curated, and folded back into training and eval. Eight rounds of negative mining shards are included, covering: close variants, persona-paired examples, fiction-paired FP repairs, and the PolyGuard native failure shard (5,879 records, 16 languages, genuine model misses not constructed attacks).

---

## Dataset Statistics

### Split

| Split | Records | Harmful | Safe |
|---|---|---|---|
| **test** | 10,451 | 3,045 (29.1%) | 7,406 (70.9%) |

**Decontamination note:** The test split was audited for overlap with the training corpus prior to release. 42,151 records (80.1% of the original candidate set) were found in the training corpus under different `split` labels and were removed. The 10,451 published records have zero record-ID overlap with any training data.

### Policy category distribution (test split, top 15)

| Category | Count | % |
|---|---|---|
| violence | 1,329 | 12.7% |
| terrorism_and_extremism | 696 | 6.7% |
| offensive_cyber | 645 | 6.2% |
| chemical_weapons | 471 | 4.5% |
| health_and_wellness | 433 | 4.1% |
| disinformation | 417 | 4.0% |
| technology_and_programming | 323 | 3.1% |
| copyright_infringement | 304 | 2.9% |
| professional_and_business | 297 | 2.8% |
| privacy_violations | 296 | 2.8% |
| biological_weapons | 287 | 2.7% |
| news_journalism_and_analysis | 274 | 2.6% |
| legal_and_regulatory | 268 | 2.6% |
| regulated_professional_advice | 257 | 2.5% |
| weapons_and_firearms | 257 | 2.5% |

---

## Record Schema

```json
{
  "record_id": "violence.a4a6d20b2942e087",
  "raw_id": "a4a6d20b2942e087",
  "cluster_id": "violence.cluster.a4a6d20b2942e087",
  "primary_category": "violence",
  "safety": "unsafe",
  "language": "en",
  "split": "train",
  "user_content": "...",
  "assistant_content": "Safety: unsafe\nCategory: violence",
  "paired_with_id": "4dd7083b70f647fa"
}
```

| Field | Description |
|---|---|
| `record_id` | Globally unique record identifier (`<category>.<hash>`) |
| `raw_id` | Source content hash (stable across translations) |
| `cluster_id` | Union-find cluster the record belongs to (used to prevent train/eval leakage at the semantic level) |
| `primary_category` | Constitutional taxonomy category |
| `safety` | `"unsafe"` or `"safe"` |
| `language` | ISO 639-1 code (train/eval only; `"en"` for English-origin records) |
| `split` | `"train"`, `"eval"`, or `"test"` |
| `user_content` | The user message to classify |
| `assistant_content` | Target classifier output (`Safety: <label>\nCategory: <category>`) |
| `paired_with_id` | `raw_id` of the contrastive pair (harmful ↔ harmless-boundary), where applicable |

---

## Comparison to Existing Benchmarks

| Benchmark | Languages | Contrastive pairs | Adversarial surface forms | Constitutional taxonomy | Scale (test) |
|---|---|---|---|---|---|
| WildGuard | 1 (en) | No | No | No | 1,725 |
| ToxicChat | 1 (en) | No | No | No | 2,930 |
| Aegis 2.0 | 1 (en) | No | No | No | ~5,000 |
| HarmBench | 1 (en) | No | Partial (jailbreaks) | No | 400 |
| XSTest | 1 (en) | Partial | No | No | 450 |
| SafetyBench | 1 (zh) | No | No | No | 11,435 |
| **HALO Guard Bench** | **47** | **Yes** | **Yes (31 transforms + narrative injection)** | **Yes (45 categories)** | **10,451** |

---

## Usage

```python
from datasets import load_dataset

ds = load_dataset("astroware/halo-guard-bench", split="test")

for record in ds:
    user_msg = record["user_content"]
    label = record["safety"]          # "safe" or "unsafe"
    category = record["primary_category"]
    # ... run your classifier on user_msg
```

---

## License and Intended Use

Released under [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0).

**Intended use:** Training and evaluating LLM input safety classifiers. Measuring guard model coverage across languages, policy categories, and adversarial surfaces.

**Out-of-scope use:** This dataset contains harmful prompts for the purpose of training classifiers to detect them. It should not be used to train generative models to produce harmful content.

---

## Citation

```bibtex
@dataset{astroware2026haloguard,
  title        = {HALO Guard Bench: A Constitutional, Multilingual Benchmark for LLM Input Safety Classification},
  author       = {Astroware},
  year         = {2026},
  url          = {https://huggingface.co/datasets/astroware/halo-guard-bench},
  note         = {47 languages, 45 constitutional categories, paired contrastive design}
}
```

---

*Built with the HALO Dataline pipeline. For questions, contact core@astroware.ai.*
