---
license: cc-by-4.0
language:
- en
- hi
- es
- ar
- zh
- ja
- fr
- de
- pt
- ru
- ko
- tr
- multilingual
pretty_name: NyayaBench v2
size_categories:
- 1K<n<10K
task_categories:
- text-classification
tags:
- intent-classification
- agent-caching
- w5h2
- few-shot
- multilingual
- agentic
- setfit
- contrastive-learning
- llm-cost-reduction
configs:
- config_name: default
  data_files:
  - split: full
    path: data/nyayabench_v2.jsonl
  - split: train
    path: data/train.jsonl
  - split: test_en
    path: data/test_en.jsonl
  - split: test_multilingual
    path: data/test_multilingual.jsonl
dataset_info:
  features:
  - name: query
    dtype: string
  - name: intent
    dtype: string
  - name: w5h2_class
    dtype: string
  - name: language
    dtype: string
  - name: source
    dtype: string
  - name: popularity
    dtype: int64
  - name: is_compound
    dtype: bool
  - name: discovered_intent
    dtype: bool
  - name: region
    dtype: string
  - name: dialect
    dtype: string
  - name: register
    dtype: string
  - name: has_params
    dtype: bool
  splits:
  - name: full
    num_examples: 8514
  - name: train
    num_examples: 160
  - name: test_en
    num_examples: 1193
  - name: test_multilingual
    num_examples: 7161
---

# NyayaBench v2

A real-world agentic intent classification benchmark sourced from production personal AI agent interactions. Unlike synthetic benchmarks, NyayaBench v2 captures the messy reality of how people actually talk to AI agents — compound queries, regional phrasing, and the long tail of 528 intents that existing caching methods can't handle.

**Paper:** [Why Agent Caching Fails and How to Fix It: Structured Intent Canonicalization with Few-Shot Learning](https://arxiv.org/abs/2602.18922) (arXiv:2602.18922)

**Code:** [nabaos/w5h2-intent-cache](https://github.com/nabaos/w5h2-intent-cache) — W5H2 taxonomy, SetFit evaluation, ablation studies, ONNX export

## Why This Dataset

Most intent classification benchmarks (MASSIVE, CLINC150, BANKING77) are collected in controlled settings with clean, single-intent utterances. Real agent traffic looks different:

- **Compound queries** — "check my email and set a reminder for the meeting at 3"
- **Extreme class imbalance** — `check_info` has 1,528 entries, `add_list` has 50
- **63 languages** — not just translated templates, but region-specific intents (Japanese transit queries, Latin American fintech, South Asian agriculture)
- **528 fine-grained intents** that must be compressed to 20 actionable cache keys

This makes NyayaBench v2 substantially harder than established benchmarks and a better proxy for production agent systems.

## The Problem It Tests

GPTCache and similar embedding-similarity caches achieve only 3–38% hit rate on personal agent tasks. The paper shows this happens because they optimize for the wrong property: semantic similarity instead of *key consistency*. W5H2 decomposes intents into **action × target** pairs (e.g., `check` × `weather` → `check_info`) and uses few-shot contrastive learning to classify them in ~2ms — achieving 91.1% accuracy with just 8 examples per class.

This approach is used in production by [NabaOS](https://github.com/nabaos/nabaos), an open-source autonomous agent runtime, where the W5H2 cache tier handles 85% of interactions locally at near-zero cost as part of a five-tier cascade architecture.

## Overview

| Property | Value |
|----------|-------|
| Total entries | 8,514 |
| Fine-grained intents | 528 |
| W5H2 super-classes | 20 |
| Languages | 63 |
| Sources | Voice assistants, smart home, IoT, productivity agents, regional deployments |
| Compound queries | Yes (flagged) |

## Quick Start

```python
from datasets import load_dataset

ds = load_dataset("biztiger/nyayabench-v2", data_files={
    "full": "data/nyayabench_v2.jsonl",
    "train": "data/train.jsonl",
    "test_en": "data/test_en.jsonl",
    "test_multilingual": "data/test_multilingual.jsonl",
})

# 8-shot train split (160 examples, 8 per W5H2 class)
print(ds["train"][0])
# {'query': '...', 'intent': '...', 'w5h2_class': 'check_info', 'language': 'en', ...}
```

## W5H2 Taxonomy (20 Classes)

The W5H2 framework decomposes intents into **action** × **target** pairs:

| Class | Description | Count | Examples |
|-------|-------------|-------|----------|
| `check_info` | Query information | 1,528 | Weather, news, prices, sports, traffic |
| `order_commerce` | Commerce & booking | 1,084 | Food, rides, hotels, tickets |
| `analyze_data` | Analyze data | 992 | Financial, sentiment, data analysis |
| `search_web` | Search & discover | 841 | Web search, directions, recipes |
| `create_content` | Generate content | 623 | Write code, documents, presentations |
| `control_home` | Control smart home | 603 | Lights, thermostat, locks, vacuum |
| `manage_tasks` | Manage tasks/files | 505 | Files, notes, expenses, fitness |
| `send_comms` | Send communications | 309 | Message, email, call |
| `play_media` | Play media | 304 | Music, radio, ambient sounds |
| `convert_data` | Convert/calculate | 262 | Translate, units, currency |
| `research_info` | Research & analysis | 245 | Market research, competitor analysis |
| `check_home` | Check home status | 202 | Camera, door, battery, temperature |
| `control_media` | Control media | 199 | Volume, TV, podcast controls |
| `set_schedule` | Set time-based | 199 | Alarm, reminder, timer |
| `check_comms` | Check communications | 139 | Read email, email queries |
| `run_routine` | Execute routines | 137 | Morning routine, smart home scenes |
| `check_schedule` | Check calendar | 128 | Calendar events, reminders |
| `manage_comms` | Manage communications | 103 | Email triage, classification |
| `schedule_meeting` | Schedule meetings | 61 | Meeting scheduling |
| `add_list` | Add to lists | 50 | Shopping list, todo list |

## Splits

| Split | Size | Description |
|-------|------|-------------|
| `full` | 8,514 | Complete dataset, all languages |
| `train` | 160 | 8-shot stratified (8 per class, seed=42) — matches paper setup |
| `test_en` | 1,193 | English test set |
| `test_multilingual` | 7,161 | 30 translated + 32 source languages |

## Schema

```json
{
  "query": "research the top 5 competitor products and summarize their pricing",
  "intent": "research_competitors",
  "w5h2_class": "research_info",
  "language": "en",
  "source": "auto_gpt_examples",
  "popularity": 8,
  "is_compound": true,
  "discovered_intent": true,
  "region": "north_america",
  "dialect": null,
  "register": "informal",
  "has_params": true
}
```

| Field | Description |
|-------|-------------|
| `query` | Natural language user utterance |
| `intent` | Fine-grained intent label (528 unique) |
| `w5h2_class` | W5H2 super-class (20 unique) |
| `language` | ISO 639-1 language code |
| `source` | Collection source |
| `popularity` | Usage frequency score (1–8) |
| `is_compound` | Whether query contains multiple intents |
| `discovered_intent` | Whether intent was discovered during collection (vs. predefined) |
| `region` | Geographic region (e.g., `east_asia`, `south_asia`, `latin_america`) — multilingual entries only |
| `dialect` | Language dialect or variant where applicable |
| `register` | Formality register (`formal`, `informal`, `colloquial`) |
| `has_params` | Whether query contains extractable parameters (times, names, quantities) |

## Benchmark Results

From the paper, evaluated on the English test split (1,193 examples, 20 classes):

| Method | Accuracy | V-measure | Latency |
|--------|----------|-----------|---------|
| GPTCache (cosine threshold) | 37.9% | — | ~50ms |
| GPTCache (KMeans k=20) | 49.1% | 0.397 | ~50ms |
| LLM baseline (20B) | 68.8% | — | 3,447ms |
| **SetFit 8-shot (22M params)** | **55.3% ± 1.0%** | **0.504** | **2.4ms** |
| SetFit 16-shot | 62.6% | 0.558 | 2.4ms |
| BERT fine-tuned (full data) | 97.3% | 0.926 | ~5ms |

NyayaBench v2 is intentionally harder than MASSIVE (where SetFit gets 91.1%) — the 528→20 compression means each class absorbs dozens of semantically diverse phrasings. This reflects the real difficulty of agent caching.

Cross-lingual zero-shot transfer (trained on English only): mean 37.7% across 30 languages, with 5 languages above 50%.

## Citation

```bibtex
@article{basu2026w5h2,
  title={Why Agent Caching Fails and How to Fix It: Structured Intent Canonicalization with Few-Shot Learning},
  author={Basu, Abhinaba},
  journal={arXiv preprint arXiv:2602.18922},
  year={2026}
}
```

## License

CC BY 4.0
