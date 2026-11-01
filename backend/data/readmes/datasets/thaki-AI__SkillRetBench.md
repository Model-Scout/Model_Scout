---
license: apache-2.0
language:
  - en
  - ko
tags:
  - skill-retrieval
  - information-retrieval
  - agents
  - benchmark
  - retrieval
pretty_name: SkillRetBench
size_categories:
  - n<1K
---

# SkillRetBench

## Dataset summary

**SkillRetBench** is a benchmark for **query-to-skill retrieval**: given a natural-language user request, systems must rank or select the correct procedural skill document(s) from a fixed library. The corpus is derived from a real-world production-style agent skill library (**501** skills). The benchmark includes **1,250** queries with gold skill identifiers and optional distractors, spanning five evaluation settings (single skill, multi-skill composition, distractors, outdated/redundant, budget-constrained). Packaged **baseline experiment results** (BM25, dense, hybrid, LLM-style, and SADO-style runs) report standard IR metrics (Recall@k, nDCG@k, MRR, MAP) per setting.

SkillRetBench accompanies the **SEFO** framework (Self-Evolving Federated Orchestration) and targets research on skill-aware orchestration, large skill libraries, and retrieval under composition and noise.

## Dataset structure

The release consists of three JSON artifacts (also listed in `croissant.json`):

| File | Description |
|------|-------------|
| `skill_corpus.json` | Full skill index: metadata, corpus statistics, and the `skills` array (one object per skill). |
| `skillretbench_queries.json` | Benchmark definition: `meta` (counts, seed, generator) and `queries` array. |
| `baseline_results.json` | Aggregated baseline metrics: per-method, per-setting IR scores and a markdown summary table. |

### `skill_corpus.json`

- **`meta`**: `generated_at` (ISO 8601), `skills_root`, `output_path`, `skill_file_count`.
- **`statistics`**: `total_skills`, `skills_per_category`, description length stats, `token_count_distribution`, composition graph stats (`skills_with_composition_references`, `total_composition_edges`).
- **`skills`** (array, length 501): each element includes:
  - `skill_id` (string, canonical id)
  - `skill_name` (string)
  - `description` (string, short routing description)
  - `trigger_phrases` (string array)
  - `anti_triggers` (string array)
  - `korean_triggers` (string array; may be empty)
  - `category` (string)
  - `full_text` (string, full SKILL.md-derived body)
  - `token_count` (integer)
  - `composable_skills` (string array; referenced skill ids)
  - `parse_warnings` (string array)

### `skillretbench_queries.json`

- **`meta`**: `benchmark`, `generator`, `corpus_meta`, `total_queries` (1250), `counts_by_setting`, `rng_seed` (42).
- **`queries`** (array, length 1250): each element includes:
  - `query_id` (string, e.g. `SS-0001`)
  - `setting` (enum-like string): `single_skill` | `multi_skill_composition` | `distractor` | `outdated_redundant` | `budget_constrained`
  - `query` (string; English and/or Korean natural language)
  - `gold_skills` (string array; expected skill ids)
  - `distractor_skills` (string array)
  - `budget_tokens` (number or `null`)
  - `difficulty` (string, e.g. `easy`, `medium`)
  - `source` (string, e.g. `trigger_paraphrase`)

**Query counts by setting**

| Setting | Count |
|---------|------:|
| `single_skill` | 400 |
| `multi_skill_composition` | 200 |
| `distractor` | 300 |
| `outdated_redundant` | 150 |
| `budget_constrained` | 200 |

### `baseline_results.json`

- **`timestamp`**, **`meta`**: `corpus_skills`, `queries_total`, `queries_by_setting`, `dense_backend` (e.g. `jaccard_fallback`).
- **`baselines`**: nested object — top-level keys **`BM25`**, **`Dense`**, **`Hybrid`**, **`NaiveLLM`**, **`SADO`**. Under each method, keys match query `setting` names; each leaf holds metrics: `recall@1`, `recall@3`, `recall@5`, `recall@10`, `ndcg@1`, `ndcg@3`, `ndcg@5`, `ndcg@10`, `mrr`, `map` (floats).
- **`summary_table`**: pre-rendered markdown table (macro-style summary over settings).

> **Note:** As documented in the artifact, `NaiveLLM` and `SADO` entries may be **simulated** (no live API) for reproducible baselines; see project script `run_baselines.py`.

## Supported tasks

- **skill-retrieval** — Rank or classify skills given a query; evaluate with gold `gold_skills` and IR metrics.
- **information-retrieval** — Same retrieval formulation; comparable to passage/tool retrieval with long procedural documents.

## Languages

- **English** — Majority of skill text and many queries.
- **Korean** — Present in `korean_triggers`, many `query` strings, and mixed Korean/English skill descriptions.

## Dataset creation

### Sources

- Skills were built from **Cursor agent `SKILL.md` files** under a single repository’s `.cursor/skills` tree (501 files), parsed into structured records plus full markdown bodies.
- Queries were **programmatically generated** by `app.sefo.benchmark.query_generator` with fixed **`rng_seed`: 42** for reproducibility.

### Methodology (high level)

1. **Corpus build** — Parse frontmatter and body; extract triggers, categories, composition edges, and token counts.
2. **Query generation** — Instantiate templates and paraphrases aligned to skills and settings (single vs. multi-skill, distractors, outdated/redundant, token budget hints).
3. **Baselines** — Run packaged retrievers/rankers (lexical, dense with configured fallback, hybrid, simulated LLM/SADO-style) and aggregate metrics per setting.

## Considerations

### Biases

- **Corpus domain** — Skills reflect one organization’s automation stack (dev tooling, PM, trading, cloud, etc.); frequency and vocabulary are **not** uniformly representative of all industries or locales.
- **Authoring style** — Descriptions follow a consistent “when to use / do not use” pattern; models may exploit **format bias** rather than deep semantics.
- **Query generation** — Synthetic and template-driven queries may **over- or under-represent** realistic user phrasing compared to production logs.

### Limitations

- **Scale** — 501 skills is medium-scale vs. ecosystems with 10⁵+ tools; retrieval hardness may not transfer linearly.
- **Gold labels** — Defined by benchmark construction rules; edge cases and valid alternative skill sets may exist.
- **Static snapshot** — Skill text and ids are frozen for the benchmark revision tied to `meta.generated_at` in the JSON files.
- **Baseline simulation** — Some methods are noted as simulated in-code; compare only under the same harness and seeds.

## License

This dataset is released under the **Apache License 2.0**. See [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0).

## Citation

If you use SkillRetBench or this corpus, please cite:

```bibtex
@misc{han2026sefo,
  title        = {{SEFO}: Self-Evolving Federated Orchestration with Trusted Skill Governance and Skill Retrieval Benchmark for Recursive Agentic Systems},
  author       = {Han, Hyojung and {ThakiCloud AI Research}},
  year         = {2026},
  howpublished = {\url{https://github.com/hyojunguy/ai-model-event-stock-analytics}},
  note         = {Includes SkillRetBench: 501-skill corpus and 1,250-query retrieval benchmark}
}
```

Adjust `howpublished` / venue fields when a formal publication DOI is available.

## Dataset repository layout (recommended)

After upload to the Hugging Face Hub, a typical layout is:

```
skill_corpus.json
skillretbench_queries.json
baseline_results.json
croissant.json
README.md
```

## Additional documentation

- Croissant (ML Commons) metadata: **`croissant.json`** in this folder.
- Implementation and regeneration: `backend/app/sefo/benchmark/` in the source repository.
