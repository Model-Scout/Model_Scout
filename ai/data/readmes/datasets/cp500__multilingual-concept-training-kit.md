---
license: apache-2.0
task_categories:
  - sentence-similarity
  - text-retrieval
  - text-classification
language:
  - en
  - ja
  - ko
size_categories:
  - 10K<n<100K
tags:
  - splade
  - sparse-retrieval
  - cross-lingual
  - multilingual
  - xlm-roberta
  - dempster-shafer
  - temporal-reasoning
  - concept-bottleneck
pretty_name: Multilingual Concept Training Kit
---

# Multilingual Concept Training Kit

A synthetic, cross-domain training kit for multilingual concept-bottleneck
retrieval and reasoning. English / Japanese / Korean across six domains:
automotive, energy, semiconductors, finance, geopolitics, pharma.

Five datasets under one roof, all anchored to a **shared 400-anchor schema**
with typed concepts (actor / relation / feature / location / market),
multilingual token lists, and per-persona valence.

## What's inside

| Dataset | Rows | Purpose |
|---------|-----:|---------|
| `retrieval/concepts.jsonl` | ~4,995 | (query, positive, 5 hard neg, 1 easy neg) triplets — trains cross-lingual SPLADE retrieval |
| `polarity/concepts.jsonl` | ~991 | Same facts with positive / negative / neutral framings — trains polarity head, contrary-view inversion, DS belief fusion |
| `chains/chains.jsonl` | ~366 | Timestamped 5–8 event sequences sharing anchors — trains NEXT edges, temporal graph, MCTS |
| `claims/claims.jsonl` | ~794 | Claims with 3 supporting / 3 refuting / 2 neutral evidence — trains NLI head, Dempster-Shafer verification |
| `persona/predicate_valence.json` | ~112 | Per-persona signed valence + rationale for every relation anchor |

## Shared anchor schema

**400 anchors total**

| Type | Count |
|------|------:|
| actor | 135 |
| relation | 112 |
| feature | 92 |
| location | 36 |
| market | 25 |

| Domain | Count |
|--------|------:|
| automotive_mobility | 68 |
| finance_capital_markets | 62 |
| semiconductors_hardware | 62 |
| energy_commodities | 61 |
| geopolitics_defense | 59 |
| pharma_biotech | 58 |
| universal | 30 |

Each anchor has multilingual tokens:

```json
{{
  "toyota": {{
    "type": "actor",
    "parent": "japanese_oem",
    "tokens_en": ["toyota"],
    "tokens_ja": ["トヨタ"],
    "tokens_ko": ["토요타"],
    "description": "Japanese automotive OEM"
  }},
  "invest": {{
    "type": "relation",
    "tokens_en": ["invest", "investment", "investing"],
    "tokens_ja": ["投資", "投じる"],
    "tokens_ko": ["투자", "투자하다"],
    "valence": {{
      "investor":  1, "engineer":  0, "executive":  1,
      "regulator": 0, "analyst":   0
    }}
  }}
}}
```

## Retrieval triplets

Each concept carries an explicit `(subject, predicate, object)` anchor triple
drawn from the shared schema. The positive passage is guaranteed to contain
the anchor tokens verbatim in all three languages. Hard negatives are
deliberately varied across 5 types — same-subject-different-action,
similar-action-different-entity, same-region-different-sector, opposite-polarity,
and adjacent-domain.

## Polarity pairs

Each record has a single factual event rendered four ways: neutral claim,
positive-framing passage, negative-framing passage, and neutral evidence.
Same facts, same anchor tokens, different rhetorical thesis. This is what
trains contrary-view inversion and supports Dempster-Shafer belief fusion.

## Temporal chains

A chain is 5–8 events united by a shared "thread anchor" (usually an actor
or relation). Each event has a timestamp, a triple, and a trilingual
sentence description. Timestamps span 1–6 months. Chains exercise
NEXT-edge construction and MCTS traversal.

## Claim verification

Each claim has three supporting passages (direct confirmation, corroborating
side-data, consistent analyst opinion) and three refuting passages
(direct contradiction, inconsistent external data, contrary analyst opinion),
plus two neutral in-domain passages. Each piece of evidence carries a
`confidence` score and an `angle` label describing what kind of support or
refutation it represents.

## Persona valence

Every relation anchor has a per-persona valence record:

```json
{{
  "recall": {{
    "investor":  {{"valence": -1, "rationale": "Recalls hit margins and brand value."}},
    "engineer":  {{"valence": -1, "rationale": "Recalls reveal quality-control failures."}},
    "executive": {{"valence": -1, "rationale": "..."}},
    "regulator": {{"valence":  1, "rationale": "Recalls protect consumer safety."}},
    "analyst":   {{"valence":  0, "rationale": "Newsworthy but valence-neutral observationally."}}
  }}
}}
```

## Usage

```python
from datasets import load_dataset
import json

kit = "cp500/multilingual-concept-training-kit"

# Retrieval triplets
retrieval = load_dataset(kit, data_files="retrieval/concepts.jsonl")

# Polarity pairs
polarity = load_dataset(kit, data_files="polarity/concepts.jsonl")

# Temporal chains
chains = load_dataset(kit, data_files="chains/chains.jsonl")

# Claim verification
claims = load_dataset(kit, data_files="claims/claims.jsonl")

# Anchor schema + persona lookup (files, not datasets)
from huggingface_hub import hf_hub_download
schema = json.load(open(hf_hub_download(kit, "anchor_schema.json", repo_type="dataset")))
persona = json.load(open(hf_hub_download(kit, "persona/predicate_valence.json", repo_type="dataset")))
```

## Generation method

All records were synthesized via AWS Bedrock:
- **Shared schema** (one file, 400 anchors): **Claude Sonnet 4.6**
- **Persona valence**: **Claude Sonnet 4.6**
- **Bulk datasets** (retrieval, polarity, chains, claims): **Claude Haiku 4.5**

Each generator lives under `generation/` and is directly runnable — see
`generation/*.py` for prompts, validation, and parallelism. Total cost for
full kit generation: approximately **$53** in Bedrock charges.

## Intended uses

- Fine-tuning multilingual SPLADE / sparse retrieval models
- Training Dempster-Shafer belief heads over contrastive evidence
- Training polarity / contrary-view classifiers
- Training temporal reasoning modules (NEXT edges, MCTS)
- Cross-domain generalization research on typed concept bottlenecks

## Limitations

- All passages are synthetic — plausible but fictional. Not a factual QA source.
- JA/KO are machine-generated; native-speaker review has not been performed.
- Domain coverage is broad but not deep for any one industry.
- Anchor schema is curated, not exhaustive — a real production schema for
  any of the six domains would be 2–5× larger.

## License

Apache 2.0. Generated with Anthropic Claude — review Anthropic's
[Acceptable Use Policy](https://www.anthropic.com/legal/aup) for downstream
applications.

## Related models

- [`cp500/opensearch-neural-sparse-en-jp-ko`](https://huggingface.co/cp500/opensearch-neural-sparse-en-jp-ko) — a multilingual sparse retrieval model fine-tuned on the `retrieval/` subset of this kit
